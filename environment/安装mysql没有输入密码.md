**在Ubuntu 18.04 下安装mysql**

​        不知道是由于mysql更新为新版还是.Ubuntu18.04中的特性，安装过程中没有设置密码的环节，在网络上找了半天，总算解决了！特此记录下来，以便以后查看！

​    1、在终端下输入 sudo apt-get install mysql-server mysql-client 进行安装，如果安装过程中弹出密码输入提示，则正常安装即可！

​    2、由于没有出现密码设置项，所以不知道怎么进入数据操作命令行，在网络上找到了解决办法，链接：[ubuntu18.04 首次登录mysql未设置密码或忘记密码解决方法](https://blog.csdn.net/qq_38737992/article/details/81090373)

​            2.1、找到安装时默认生成的默认账户在终端上输入  sudo cat /etc/mysql/debian.cnf  如下图显示的账号和密码

2.1

​            2.2、用得到的账户和密码登录mysql，这里一定要提一嘴，这里的密码一定要用你自己查到的那个密码，因为那是随机生成的

2.2

​            2.3、然后就是修改密码了，跟原来的也有一点区别，注意看别眨眼 O(∩_∩)O~

> 1)、use mysql;                   #连接到mysql数据库
>
> 2)、update mysql.user set authentication_string=password('**123456**') where user='root' and Host ='localhost';    #修改密码**123456**是密码
>
> 3)、update user set  plugin="mysql_native_password";     
>
> 4)、flush privileges;
>
> 5)、quit; 
>
> 详情见下图！

2.3 其中第二条命令有点长，注意别打错了！记得后面的分号

2.4 重启mysql服务器后，直接可以用root账户进行登录了



------

​    3、顺便补充一点mysql服务的启动和关闭命令

> 启动mysql：
>
> 方式一：sudo /etc/init.d/mysql start
>
>  方式二：sudo service mysql start
>
>  停止mysql：
>
> 方式一：sudo /etc/init.d/mysql stop
>
>  方式二：sudo service mysql stop
>
>  重启mysql：
>
> 方式一：sudo/etc/init.d/mysql restart
>
> 方式二：sudo service mysql restart

注：参考资料

 

 

 

 

 