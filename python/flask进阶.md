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

4. 
