go-admin项目前端代码地址： https://github.com/wenjianzhang/go-admin-ui 

go-admin项目后端代码地址： https://github.com/wenjianzhang/go-admin 



共有三个容器，分别是mysql端，go-gin后端，node-vue前端



### 数据库端

- 首先，下载mysql：`docker pull mysql:5.7`，这里可能会遇到docker因为众所周知的网络原因而无法拉取的问题，这时可以换源，右击右下角的docker图标，点击setting-> Docker Engine，然后`"registry-mirrors":[]` 改成：

  ```
  "registry-mirrors": [
      "http://ovfftd6p.mirror.aliyuncs.com",
      "http://registry.docker-cn.com",
      "http://docker.mirrors.ustc.edu.cn",
      "http://hub-mirror.c.163.com"
    ],
  ```

  重启docker并拉取，应该可以成功；<br><br>

- 创建一个三端共享的network：`docker network create go_admin_demo`<br><br>

- ```
  docker run --name mysql5 --network go_admin_demo --network-alias database -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
  
  docker exec -it mysql5 /bin/bash
  
  进去后执行:
  #mysql -uroot -p然后回车，输入密码root回车
  进入mysql之后，创建数据库goadmindb:
  >CREATE DATABASE IF NOT EXISTS goadmindb
  -> DEFAULT CHARACTER SET utf8;
  
  
  ```

  数据库部分搞定；<br><br>



### go-gin后端

- `docker run --name go_admin -it -p 8000:8000  --network go_admin_demo -v /d/Documents/github_projects/go-admin:/root/projects/go-admin go_ubuntu /bi
  n/bash`，这里用到了已经做好的镜像go_ubuntu；<br><br>
- 进去后，cd到go-admin文件夹，执行：`go build`<br><br>
- 然后，`#vim ./config/settings.yml`，修改host名为“database”（即上面创建的mysql5容器的network-alias），密码为"root"，保存退出；<br><br>
- 执行`./go-admin init`初始化数据库（如果是第一次运行的话）；<br><br>
- 执行`./go-admin server`启动后端服务，至此，后端部分搞定；<br><br>



### node-vue前端

- `docker run --name go_admin_ui -it -p 9527:9527  --network go_admin_demo -v /d/Documents/github_projects/go-admin-ui:/root/projects/go-admin-ui node
  js_env /bin/bash`，这里用到了做好了的镜像nodejs_env；<br><br>
- `docker exec -it go_admin_ui /bin/bash`；<br><br>
- cd到go-admin-ui文件夹，执行`cnpm install`；<br><br>
- 下载完后，执行`npm install`，即可在浏览器访问了；<br><br>