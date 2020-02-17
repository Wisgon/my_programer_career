1. 修改密码：

   ```mysql
   // 进入mysql：mysql -u root -p
   use mysql;
   update user set password=password('123456') where user=root;
   // 如果出现ERROR 1054 (42S22): Unknown column 'password' in 'field list'，说明mysql版本大于5.7，这时候要换成:
   update user set authentication_string=password('123456') where user='root';
   flush privileges;  // 刷新
   ```

   <br><br>

2. ` CREATE DATABASE 'mydb' CHARACTER SET utf8 COLLATE utf8_general_ci; `创建新数据库并设置编码为utf8；<br><br>

3. 

