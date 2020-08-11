### go-admin的部署：

[项目地址](https://github.com/wenjianzhang/go-admin)



##### 前后台启动前准备

`请注意 Go version >= 1.11，并且 GO111MODULE=on (Go MOdule 模式)；`

1. 下载源码

    ```shell
    mkdir e_world
    cd e_world
    git clone https://github.com/wenjianzhang/go-admin.git
    git clone https://github.com/wenjianzhang/go-admin-ui.git
    cd ./go-admin
    go build
    ```

2. mysql新建"go_admin"数据库：

    ```
    create database if not exists go_admin 
    >default character set utf8;
    ```

3. 配置源:

    首先找到配置文件，`config/settings.yml`， 同时也可创建开发环境配置，只需将默认配置文件 `config/settings.yml` 复制到 `config/settings.dev.yml` 就好了

    `vim config/settings.dev.yml`

    ```
    settings:
      application:
        # dev开发环境 test测试环境 prod线上环境
        mode: dev
        # 服务器ip，默认使用 0.0.0.0
        host: 0.0.0.0
        # 服务名称
        name: e_world
        # 端口号
        port: 8927 # 服务端口号
        readtimeout: 1
        writertimeout: 2
        # 数据权限功能开关
        enabledp: false
      logger:
        # 日志存放路径
        path: temp/logs
        # 控制台日志
        stdout: true
        # 日志等级
        level: all
        # 业务日志开关
        enabledbus: true
        # 请求日志开关
        enabledreq: false
        # 数据库日志开关 dev模式，将自动开启
        enableddb: false
      jwt:
        # token 密钥，生产环境时及的修改
        secret: go-admin
        # token 过期时间 单位：秒
        timeout: 3600
      database:
        # 数据库类型 mysql，sqlite3， postgres
        driver: mysql
        # 数据库连接字符串 mysql 缺省信息 charset=utf8&parseTime=True&loc=Local&timeout=1000ms
        source: root:root123456@tcp(127.0.0.1:3306)/go_admin?charset=utf8&parseTime=True&loc=Local&timeout=1000ms
        # source: sqlite3.db
        # source: host=myhost port=myport user=gorm dbname=gorm password=mypassword
      gen:
        # 代码生成读取的数据库名称
        dbname: go_admin
        # 代码生成是使用前端代码存放位置，需要指定到src文件夹，相对路径
        frontpath: ../go-admin-ui/src
    ```
    
4. 初始化数据库：`./go-admin init -c config/settings.yml -m dev`

5. 修改go-admin/cmd/api/server.go:

    ```go
    //在if mode != ""{...} 那一块代码，换成：
    if mode == "" {
    	config.SetConfig(configYml, "settings.application.mode", mode)
    }
    
    if port == "" {
    	config.SetConfig(configYml, "settings.application.port", port)
    }
    ```

    

6. 配置前端：

    ```
    cd ../go-admin-ui
    npm install --registry=https://registry.npm.taobao.org  // 国内原，如果翻墙了，也可以直接用npm install
    ```

<br><br>

##### 服务器nginx配置反向代理go服务

1. 安装nginx：`sudo apt-get install nginx`;

2. 新建/etc/nginx/conf.d/e_world.com.conf文件：

   ```
   server {
     listen 80;
     server_name e_world.com;
     # 配置前端静态文件目录
     location / {
         index index.html index.htm;
         root /home/zhilong/Documents/my_projects/e_world_admin/go-admin-ui/dist;
        }
     # 配置后台go服务api接口服务 代理到8877端口  
     #注意这里的goadminapi，是之后前端的.env.production文件里面的go接口地址后缀
     location ~ ^/goadminapi/ {  
     
         proxy_set_header   Host             $http_host;
         proxy_set_header   X-Real-IP        $remote_addr;
         proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
         proxy_set_header   X-Forwarded-Proto  $scheme;
         rewrite ^/goadminapi/(.*)$ /$1 break;
         proxy_pass  http://127.0.0.1:8927;   
         }
   }
   ```

   测试配置是否可以生效：

   ```
   nginx -t //测试nginx配置是否正确
   nginx -s reload //重启nginx服务
   ```

   

3. 修改前端的go-admin-ui/.env.production文件：

   ```
   VUE_APP_BASE_API = 'http://e_world.com/goadminapi'
   ```

4. build前端：`npm run build:prod`，会在go-admin-ui目录下生成dist文件夹；

5. 运行go后端，cd到go-admin文件夹，执行`./go-admin server -c=config/settings.dev.yml`即可；

