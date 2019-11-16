手把手教你如何在mysql 中使用中文编码
1.首先在docker中拉取好一个最新的mysql镜像以后，创建一个容器：


docker run  -d -p 13306:3306 -e MYSQL_ROOT_PASSWORD=xxxxxx--name MYDB mysql

参数的解释：
-d 设置detach为true
-p port 映射端口 13306
-e environment 设置密码 xxxxx
2. docker ps 查看mysql容器是否启动，进去容器


docker exec -ti xxx(容器id) /bin/bash

理论上应该启动正常 进去容器内部

3.查看mysql密码 是否正常
mysql -u root -p

在提示下输入密码 xxxxx 正常情况下，应该出现以下提示符mysql>



！！重点来了！！
1.前期工作 查看当前mysql字符集情况
mysql>SHOW VARIABLES LIKE 'character_set_%';//查看数据库字符集

基本上都如下图所示：默认就是瑞典latin1 


 SHOW VARIABLES LIKE 'collation_%';


图上的第一个 connection 就是我们通过workbench等客户端连接的时候指定的编码。 
外部访问数据乱码的问题就出在这个connection连接层上

1.先解决外部访问数据乱码的问题
SET NAMES 'utf8';

它相当于下面的三句指令：

SET character_set_client = utf8;
SET character_set_results = utf8;
SET character_set_connection = utf8;

2.创建数据库，创建表的时候，包括设置字段的时候也要加上字符集设置：
例如

create database MYDB character set utf8;

use JSPDB;
create table  t_product(
pid     varchar(20),
pname    varchar(20),
price    double,
address   varchar(30)
) DEFAULT CHARSET=utf8;

3.如果你应经有建立了数据库，也可以通过以下语句修改字符集
当然 如果是刚刚建容器的时候 我想你肯定是没有数据库的，所有此步跳过

alter database name character set utf8;#修改数据库成utf8的.
alter table type character set utf8;#修改表用utf8.
alter table type modify type_name varchar(50) CHARACTER SET utf8;#修改字段用utf8


