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

9. vue项目中，可以用`npm run build`来生成项目所有html，js，css文件；<br><br>

10. App.vue中，

   ```
   <template>
       <div id="app">
           <Header />
           <router-view />
       </div>
   </template>
   ```

   这里的`<router-view />`是指路由访问的是哪个页面，那么这个就是那个页面的view，如：
   router.js定义如下

   ```
   routes: [
           {
               path: "/",
               name: "home",
               component: Home
           },
           {
               path: "/about",
               name: "about",
               // route level code-splitting
               // this generates a separate chunk (about.[hash].js) for this route
               // which is lazy-loaded when the route is visited.
               component: () =>
                   import(/* webpackChunkName: "about" */ "./views/About.vue")
           }
       ]
   ```

   那么当访问localhost:xxx/时，`<router-view />`就是Home..Vue组件下的template，而访问localhost:xxx/about时，就是About.Vue组件下的template；<br><br>

11. Vue3.0报错error: Unexpected console statement (no-console) 解决办法：
    修改package.json中的eslintConfig:{} 中的 “rules”:{}，增加一行代码: "no-console":"off" :

   ```json
   "eslintConfig": {
       "root": true,
       "env": {
         "node": true
       },
       "extends": [
         "plugin:vue/essential",
         "eslint:recommended"
       ],
       "rules": {
          "no-console":"off"
       },
       "parserOptions": {
         "parser": "babel-eslint"
       }
    },
   ```

   <br><br>

12. vue的axios解决跨域问题：
      (1)  vue-cli产生的项目，有config/index.js的：

   - 根目录main.js下，增加：

     ```js
     import  Axios from  'axios'
     
     Vue.prototype.$axios=Axios
     Vue.prototype.HOST="/douban_api"
     ```

   - config文件夹的index.js下，修改"dev"这个字段的proxyTable：

     ```js
     // config/index.js是vue-cli生成的配置文件
      proxyTable: {
           '/douban_api': {
             target: 'http://api.douban.com',  //目标接口域名
             pathRewrite: {
               '^/douban_api': ''   //重写接口
             },
             changeOrigin: true,  //在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
           },
     
         },
     ```

   - 然后就是普通js或vue文件中的axios的用法：

     ```vue
     <script>
     export default {
     
       name: 'HelloWorld',
       data () {
         return {
           msg: 'Welcome to Your Vue.js App'
         }
       },
       mounted() {
         const  url=this.HOST+"/v2/movie/top250"; //会自动变成http://api.douban.com/v2/movie/top250
         this.$axios.get(url)
           .then(function (response) {
             console.log(response);
           })
           .catch(function (error) {
             console.log(error);
           });
       }
     
     }
     </script>
     ```

     
     
     (2)  普通的vue项目，根目录下有vue.config.js的：
     
     ```vue
     devServer {
     	...
     	proxy: { // 设置代理
           '/graphql': {
             target: 'http://192.168.9.5:8033',
             changeOrigin: true,
             pathRewrite: {
               '^/graphql': '/graphql'
             }
           }
         }
     }
     ```
     
     如果出现：“vue Proxy error: Could not proxy request xxx” 的报错的时候，可能是target的那个url的后台服务关闭了，或者不存在！
     
     <br>
     
     <br>

13. vue 定义全局变量:
      Global.vue文件：

   ```js
   <script>
       const token='12345678';
   
       export default {
           methods: {
               getToken(){
                   ....
               }
           }
       }
   </script>
   ```

   在需要的地方引用进全局变量模块文件，然后通过文件里面的变量名字获取全局变量参数值。

   ```js
   <script>
   import global from '../../components/Global'//引用模块进来
   export default {
       data () {
           return {
               token:global.token
           }
       },
       created: function() {
           global.getToken();
       }
   }
   </script>
   ```

   <br><br>

14. 在vue项目中定义全局变量和函数：
      ./utils/graphqlCURD.vue:

   ```vue
   <script>
   var graphqlCURD = {}
   
   graphqlCURD.generateMutation = function (
       funcName,
       inputs,
       returnValue = "numUids"
   ) {
       return `
   mutation{
     ${funcName}(input:${inputs}) {
       ${returnValue}
     }
   }
   `
   }
   
   export default graphqlCURD
   </script>
   ```

   在子组件中，这样使用：
   components/aaa.vue:

   ```vue
   import graphqlCURD from "./utils/graphqlCURD"
   graphqlCURD.generateMutation(xxx,xxx,xxx)
   ```

   <br><br>

15. 在使用vue进行开发的时候我们会发现地址栏上的ip后面会跟着一个#号，如果想去掉这个井号，我们可以在路由上加上 mode: 'history', 即可去掉，是不是很简单呢

    

   ```javascript
   export default new Router({
     mode: 'history',
     routes: [
       {
         path: '/', 
         name: 'Home',
         component: Home
       }   
     ]
   })
   ```

------

   vue-router默认是hash模式，在hash模式下，是会有#号在URL上的，很丑有没有？

   切换到HTML5的history模式，只需要在mode选项中配置即可。在history模式下，URL就像正常的URL一样，但是该模式下需要后台正确的配置才可以。因为在路由中传参时，后台没有配置好的话，就会返回404。<br><br>

16. 在vue组件中，要disable eslint，template和script的格式不一样，如：

    ```
    <template>
    <!-- eslint-disable -->
    </template>
    
    <script>
    /* eslint-disable */
    </script>
    ```

    这样，template和script都不受eslint检查了；<br><br>

17. 子组件中，data不能用`data: ()=>{return {xxx:xxx}}`这样的形式，应该用：`data: function() {return {xxx:xxx}}`这样，或者`data() {return {xxx:xxx}}`这样的；<br><br>

18. elementui的el-checkbox在使用v-for循环时，父级的checkbox-group的v-model一定要绑定一个数组类型的变量，如果是字符串类型，则会出现点击一个框马上全选的bug；<br><br>

19. vue要在新标签打开页面，可以：

    ```javascript
    let routeData = this.$router.resolve({ path: '/reportpreview', query: { id: id } });
    window.open(routeData.href, '_blank');
    ```

    <br><br>

20. `this.$router.go(0)`可强制刷新当前页面，重新获取数据；<br><br>

21. vue中，直接更新对象的属性值是无效的，要更新整个对象，如：

    ```vue
    <template>
        <div>
        	<p>{{aaa.bb}}</p>
        </div>
    </template>
    <script>
    	export default{
    		data():{
    			return{
    				aaa:{bb:3}
    			}
    		},
    		mounted(){
    			// this.aaa.bb = 4 // 无用，不会更新
    			this.aaa = {bb:4} // 这样才会更新
    		}
    	}
    </script>
    ```

    <br><br>

22. 在vue的html中，template可作为模板占位符，可帮助我们包裹元素，但是又不会渲染到html里，相当于小程序的block了；<br><br>
