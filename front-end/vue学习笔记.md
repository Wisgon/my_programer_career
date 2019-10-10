1. 计算属性与方法的区别是，计算属性可以缓存，而方法每当触发重新渲染时，总会再次执行函数；<br><br> 

2. 在异步请求flask的接口时，出现cors报错，这时需要加上flask_cors:

   ```python
   from flask_cors import CORS
   todo_app = Flask(__name__)
   CORS(todo_app)
   ```

   这样就能正常请求了；<br><br> 

3. 使用v-for必须添加唯一的key：`<li v-for="(data, index) in user_help_data" :key="data.help_name">`，这个data.help_name必须是各条数据唯一的;<br><br> 

4. 当某个变量发生变化时，可用watch来监听，但是有某些样式会随着这个变量变化，用watch会太早执行动作，所以加上`this.$nextTick`就行：

   ```javascript
   challenge: function () {
         this.$nextTick(function () {
           console.log("###", this.$refs.challenge.offsetHeight)
         })
       }
   ```

   上例子中，challenge是一个变量，当challenge发生变化，`this.$refs.challenge`对应的元素的高会重新渲染，如果不用`​this.$nextTick`的话，会在高度变化之前就打印出原来的高度，达不到想要的效果；<br><br> 

5. 