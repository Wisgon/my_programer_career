1. python3 无法安装xadmin==2.0.1的问题：首先我们先去github上下载xadmin==2.0.1的zip文件。（源码包）。地址：<https://github.com/sshwsfc/xadmin/tree/django2>

   cd 到.zip文件所在文件夹，

   ```
   pip install django==2.0
   pip install xadmin-django2.zip
   ```
   即可；<br><br>

2. 要在80端口run server，需要sudo权限：`sudo ~/anaconda3/envs/zhps/bin/python3 manage.py runserver  0.0.0.0:80`；<br><br>

3. 