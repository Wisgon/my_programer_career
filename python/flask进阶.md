1. jinja2模板中，变量名和大括号要有空格，如：`{{var}}`不会起作用，`{{ var }}`才会起作用；<br><br> 

2. 用app.add_template_global来让模板获得全局变量：
   `app/__init__.py`

   ```python
   #设置全局判断用户登陆状态的函数
   def get_current_user():
       return current_user
   
   app.add_template_global(get_current_user, "get_current_user")
   ```

   `app/templates/base.html`

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>{% block title %}{% endblock %} - To do app</title>
       {% block head %}{% endblock %}
   </head>
   <body>
   <div style="height: 20px; background-color: gray">
   <p>
       <span style="float:left">Todo app</span>
       <span style="float: right">
         <!--这里拿到current_user全局变量-->
           {% set current_user=get_current_user() %}
       {% if current_user.is_authenticated %}
           Hello, {{ current_user.username }}
           <a href={{ url_for("todo_list.logout") }} >注销</a>
       {% else %}
           <a href={{ url_for("todo_list.login") }} >登陆</a>
           {% endif %}
       </span>
   </p>
       </div>
   {% block body %}{% endblock %}
   </body>
   </html>
   ```

   <br><br> 

3. `from bson import ObjectId`可生成mongodb的_id值，如：`ObjectId("5d75b9f5734b070384599f7a")`<br><br> 

4. postman调试flask接口：由于项目用的是https，所以要关掉SSL certificate verification，方法：点击主界面右上角扳手图案，点击“setting”，禁掉SSL certificate verification即可，用postman做flask-wtf的表单验证，也可以是自己做的普通表单提交，也会触发validate_on_submit()，如果没有，可能有一下两个问题：（1）csrf_token没有，这时，在配置文件里面：WTF_CSRF_ENABLED = False禁掉就好；（2）表单验证错误，可以用print(your_form.errors)调试；<br><br>

5. 当我们设计路由时，如果后面加了‘/’ ，当用户输入的url末尾没有”/“ ，Flask会自动响应一个重定向，转向路由末端带有‘/’的url，当我们设计路由时，如果后面没加‘/’ ，当用户输入的url末尾带有”/“ ，会报错 ；<br><br> 

6. get访问时，参数的问号前面有没有斜线都可以，如：`xxx/yyy?my_var=value` 和`xxx/yyy/?my_var=value`都可以;<br><br> 

7. 
