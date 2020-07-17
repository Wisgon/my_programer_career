1. python3 无法安装xadmin==2.0.1的问题：首先我们先去github上下载xadmin==2.0.1的zip文件。（源码包）。地址：<https://github.com/sshwsfc/xadmin/tree/django2>

   cd 到.zip文件所在文件夹，

   ```
   pip install django==2.0
   pip install xadmin-django2.zip
   ```
   即可；<br><br>

2. 要在80端口run server，需要sudo权限：`sudo ~/anaconda3/envs/zhps/bin/python3 manage.py runserver --noreload  0.0.0.0:80`；<br><br>

3. 报错信息：
    Invalid HTTP_HOST header: 'xxxx_xxxx.com'. The domain name provided is not valid according to RFC 1034/1035.

   - 方法1、修改域名，去掉域名中的下划线
   - 方法2、修改Django源代码（django/http/request.py文件，我的django版本是1.11.8）

   ```python
   host_validation_re = re.compile(r"^([a-z0-9.-]+|\[[a-f0-9]*:[a-f0-9:]+\])(:\d+)?$")
   加个"._"，改成
   host_validation_re = re.compile(r"^([a-z0-9._.-]+|\[[a-f0-9]*:[a-f0-9:]+\])(:\d+)?$")
   ```

   域名最好不带下划线，如果要分词，那么用减号代替；<br><br>

4. 数据库model中，DateTimeField类型的字段，default写成datetime.now比较好，如果是auto_add，则会在docker中与服务器时间有冲突！应该改成如：`models.DateTimeField(default=datetime.now, verbose_name=u'更新时间')`这样；<br><br>

5. 