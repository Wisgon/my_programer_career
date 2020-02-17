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

5. vue组件中，用$refs来获取当前组件的dom：

   ```vue
   <template>
   	<p ref="ppp">
           this is p dom
       </p>
   </template>
   <script>
       module.exports = {
           data () {
               return {
                   msg: "success",
               }
           },
           mounted () {
               console.log(this.$refs.ppp) // 这个就是p这个dom，这个组件就算被复用，也不会变成其他克隆体的ppp
           }
       }
   </script>
   ```

   <br><br>

6. 要让js模块那些在项目所有文件夹下面都能找到，就要设置jsconfig.json，将其放在项目根目录：

   ```json
   {
       "compilerOptions": {
           "target": "es6"
       },
       "include": [
           "www/**/**/*"
       ]
   }
   ```

   解释：include的`www/**/**/*`是指，www文件夹下的所有文件，都可以引用该文件夹下的所有js模块；<br><br>

7. axios的普通post，在后台如果用form的形式来取的话，会取到空值，如果要form的形式来post，则：

   ```javascript
   let post_data = new FormData()
   post_data.append("keyName", "value")
   axios.post("http://xx.xx.xx", post_data).then(res => {
   	console.log(res)
   })
   ```

   <br><br>

8. 代码提示中，插件的snippet有时会妨碍真正需要的代码提示放到最上面，所以，在setting中，设置：

   ```
   "editor.snippetSuggestions": "inline", // 值可以是bottom, top, inline的意思是按字母顺序排
   ```

   ​	<br><br>

9. 