环境信息
操作系统：Ubuntu 18.04.3
MongoDB：4.0.14
安装MongoDB
MongoDB 4.0.14官网

1. 下载MongoDB，并解压重命名

```
$sudo wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1804-4.0.14.tgz
$sudo tar -zxvf mongodb-linux-x86_64-ubuntu1804-4.0.14.tgz
$sudo cp -r mongodb-linux-x86_64-ubuntu1804-4.0.14 /usr/local/mongodb
$cd /usr/local/mongodb
```

2. 配置环境变量
`$ sudo vim .zshrc`
添加如下内容
```
export MONGODB_HOME=/usr/local/mongodb
PATH=${MONGODB_HOME}/bin
```

保存后更新配置使生效
`$ source .zshrc`

3. 创建用于存放数据和日志文件的文件夹，并修改其权限增加读写权限
```
$ sudo mkdir /data/mongo
$ sudo chmod 777 /data/mongo
$ sudo mkdir /var/log/mongo
$ sudo chmod 777 /var/log/mongo
```

4. 添加启动配置文件
```
cd /usr/local/mongodb/bin
sudo vim mongodb.conf
```
添加以下内容并保存
```
dbpath=/data/mongo #数据文件存放目录
logpath=/var/log/mongo/mongodb.log #日志文件存放目录
port=27017  #端口
fork=true  #以守护程序的方式启用，即在后台运行
logappend=true #使用追加方式写日志
directoryperdb=true #设置每个数据库保存在一个单独的目录
bind_ip=0.0.0.0 #将mongodb绑定到任意IP上，来支持远程访问
auth=false #不开启认证功能
```

5. 以配置文件的方式启动mongod数据库服务
`$ sudo ./mongod -f mongodb.conf`

6. 连接mongo，关闭mongo
```
./mongo
MongoDB shell version v4.0.14
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("fe50928a-6322-4ba4-a4ee-5e34fbad4eea") }
MongoDB server version: 4.0.14

> use admin;
 switched to db admin
> db.shutdownServer();
```

以上无用户权限的mongo安装配置完成，但是没有用户的mongo是非常不安全的，下面来对MongoDB添加用户并设置权限。

7. 设置用户权限
MongoDB是基于角色的访问控制，所以创建用户需要指定用户的角色，在创建用户之前需要满足：

- 先在admin数据库中创建角色为userAdmin或userAdminAnyDatabase的用户作为管理用户的用户；
- 启用访问控制，进行登录用户验证，这样创建用户才有意义。
```
// 创建超级管理员，可以做任何操作。用户用户名为root，密码roothuang139
> use admin;
> db.createUser({user:'root',pwd:'roothuang139',roles:['root']})
 Successfully added user: { "user" : "root", "roles" : [ "root" ] }
 // 创建管理用户用户名为user_admin，密码admin123
> db.createUser({user: "user_admin",pwd: "admin123",roles: [{ role: "userAdminAnyDatabase", db: "admin" }]})
 Successfully added user: {
 "user" : "user_admin",
 "roles" : [
 	{
 		"role" : "userAdminAnyDatabase",
 		"db" : "admin"
 	}
 ]
 }
```
开启访问控制，在启动配置文件加入选项auth=true，并重启mongodb实例。

8. 登录mongo，使用刚刚创建的user_admin登录
```
$ sudo ./mongo
MongoDB shell version v4.0.14
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("5dbc035a-699b-40d7-8ca3-94e8404515aa") }
MongoDB server version: 4.0.14
> use admin
switched to db admin
> db.auth('user_admin','admin123')
1
```

9. 为业务数据库创建单独账号stock，并赋予stock库的读写权限
```
> use admin
switched to db admin
> db.auth('user_admin','admin123')
 1
> use stock
 switched to db stock
> db.createUser({user:'stock',pwd:'stock123',roles:[{role:'dbOwner',db:'stock'},{role:'readWrite',db:'stock'}]})
 Successfully added user: {
 "user" : "stock",
 "roles" : [
 	{
 		"role" : "dbOwner",
 		"db" : "stock"
 	},
 	{
 		"role" : "readWrite",
 		"db" : "stock"
 	}
 ]
 }
> db.auth('stock','stock123')
1
```
 至此，超级管理员，用户管理员，业务库用户创建完毕。
