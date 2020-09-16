### 用宝塔配置PSI

项目地址:  [PSI](https://gitee.com/crm8000/PSI)

1. 点击“添加站点”， 设置好域名，mysql；

2. 进入数据库，用phpmyadmin，然后选中数据库，点击“导入(import)”，然后点击“选择文件”，从 [/doc/99 SQL](https://gitee.com/crm8000/PSI/tree/master/doc/99 SQL) 文件夹中，导入`01CreateTables.sql`，执行，然后再次导入`02InsertInitData.sql`，`99psi_demo_data.sql`；

3. 配置` /web/Application/Common/Conf/config.php`，将数据库名，用户名和密码名改成对应的；

4. 关键步骤：

   ```
   点击网站的配置页面，点击“配置文件”，在最后一个location后面添加：
   location / {
           if (!-e $request_filename){
                  rewrite ^/web/(.*)$ /web/index.php/$1 last;   #--关键的配置，支持ThinkPHP的rewrite支持
           }
           }
       
       location ~ .*\.php {  #--经测试，必须以去除?$结尾，去掉$是为了不匹配行末，即可以匹配.php/，以实现pathinfo
                   fastcgi_pass  127.0.0.1:9000;
                   fastcgi_index index.php;
                   include fastcgi.conf;
                   include pathinfo.conf;  #--关键的配置，支持ThinkPHP的pathinfo支持
           }
   ```

   搞定，重启nginx，php；

5. 对根目录执行`chmod -R 777 xxx/`，将根目录的权限全部开放，这样才能访问；

6. 搞定；

