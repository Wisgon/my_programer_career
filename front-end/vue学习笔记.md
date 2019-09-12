1. 计算属性与方法的区别是，计算属性可以缓存，而方法每当触发重新渲染时，总会再次执行函数；<br><br> 

2. 在异步请求flask的接口时，出现cors报错，这时需要加上flask_cors:

   ```python
   from flask_cors import CORS
   todo_app = Flask(__name__)
   CORS(todo_app)
   ```

   这样就能正常请求了；<br><br> 

3. 