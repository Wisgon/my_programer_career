1. 修改 httpd.conf
   Apache 从2.2升级到 Apache2.4.x 后配置文件 httpd.conf 的设置方法有了大变化：

   老版本是将 httpd.conf中查找Deny from all，注释掉Deny from all，下面添加Allow from all，整个配置文件有三处实现外网访问。（老版本的，你们看看其他教程）
   Apache2.4.x开始是将 Require all denied 以及 Require local 注释掉，在下面添加 Require all granted 。
   直接点击进入文件或者去Apache安装目录搜索然后进入文件。

![20180221144647919](D:\Documents\my_projects\my_programer_career\static\20180221144647919.png)

​		打开文件之后修改下面两处，找到 Require all denied和 Require local，你们可能Ctrl+F**直接搜索可能搜不		到**，因为我发现有的写得是Require all deny，截图就在下边，你们找找周围的句子搜一下，找到就好。
​		然后把原句注释掉，就是直接在这两句前面加上#。然后在原句的下面粘贴上Require all granted即可。

![20180221155135907](D:\Documents\my_projects\my_programer_career\static\20180221155135907.png)

![20180221155315976](D:\Documents\my_projects\my_programer_career\static\20180221155315976.png)



2. 修改httpd-vhosts.conf
   去Apache安装目录下边找httpd-vhosts.conf，能搜出来俩，你仔细辨认一下。那个文件内容长这样（看下图）。

![20180221153023896](D:\Documents\my_projects\my_programer_career\static\20180221153023896.png)

添加如下内容：

```
<VirtualHost *:80>
  ServerName my_project_name.com     //注意这行
  DocumentRoot "D:/my_project/xxx"    //注意这行，这里添加项目所在根目录
  <Directory "D:/my_project/xxx/">
    Options +Indexes +Includes +FollowSymLinks +MultiViews
    AllowOverride All
    Require local
  </Directory>
</VirtualHost>
```



修改C:\Windows\System32\drivers\etc\hosts，添加：`127.0.0.1  my_project_name.com` 就ok了；


