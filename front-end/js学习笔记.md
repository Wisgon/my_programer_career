1. JavaScript函数允许接收任意个参数，可以用rest获取剩余参数：

   ```javascript
   function foo(a, b, ...rest) {
       console.log('a = ' + a);
       console.log('b = ' + b);
       console.log(rest);
   }
   
   foo(1, 2, 3, 4, 5);
   // 结果:
   // a = 1
   // b = 2
   // Array [ 3, 4, 5 ]
   
   foo(1);
   // 结果:
   // a = 1
   // b = undefined
   // Array []
   ```

   <br><br> 

2. var的本质:

   var a=3：声明一个变量a并给它赋值3;

   a=3：并没有声明一个新的变量，只是往它的外层寻找变量名为a的变量，并给它赋值3。（假设外层都没有声明a，那么会找到window上的变量a）；<br><br> 

3. JavaScript默认有一个全局对象`window`，全局作用域的变量实际上被绑定到`window`的一个属性；<br><br>

4.  有些时候，如果变量已经被声明了，再次赋值的时候，正确的写法也会报语法错误：

   ```javascript
   // 声明变量:
   var x, y;
   // 解构赋值:
   {x, y} = { name: '小明', x: 100, y: 200};
   // 语法错误: Uncaught SyntaxError: Unexpected token =
   ```

   这是因为JavaScript引擎把"`{`"开头的语句当作了块处理，于是`=`不再合法。解决方法是用小括号括起来：

   ```
   ({x, y} = { name: '小明', x: 100, y: 200});
   ```

   <br><br> 

5. 如下面的代码所示：如果以对象的方法形式调用，比如`xiaoming.age()`，该函数的`this`指向被调用的对象，也就是`xiaoming`，这是符合我们预期的。

   如果单独调用函数，比如`getAge()`，此时，该函数的`this`指向全局对象，也就是`window`。

   ```javascript
   function getAge() {
       var y = new Date().getFullYear();
       return y - this.birth;
   }
   
   var xiaoming = {
       name: '小明',
       birth: 1990,
       age: getAge
   };
   
   xiaoming.age(); // 25, 正常结果
   getAge(); // NaN
   ```

   <br><br> 

6. `Array`的`sort()`方法默认把所有元素先转换为String再排序；<br><br> 

7. 谷歌浏览器查看js耗时，首先，调出开发者工具，然后选择“performance”，按下左边第二排第二个带箭头的圆形按钮，开始记录，然后就可以在“Sources”里点开js文件查看各个函数的耗时了；<br><br> 

8. `$('.xxx div')`选择的是class='xxx'的元素内部的所有div，并不只是子div，子div应该是`$('.xxx>div')`;<br><br> 

9. JavaScript中，父元素包含子元素：
   　　当父级设置onmouseover及onmouseout时，鼠标从父级移入子级，则触发父级的onmouseout后又触发onmouseover；从子级移入父级后再次触发父级的oumouseout后又触发onmouseover。而如果onmouseover内又应用了计时器便会存在较大的问题。下面针对此问题给出解决方案。

   ```javascript
   var parent_div = $('.tbh-service').parent()[0];
   parent_div.onmouseout = function (ev) {
       var reg = this.compareDocumentPosition(ev.relatedTarget);
       if (!(reg == 20 || reg == 0)) {
           //这里执行onmouseout的逻辑代码，这样就不会被子元素干扰；
       }
   };
   ```

   上面代码中，ev.relatedTarget会记录触发事件的元素是什么，然后与本元素进行比较，标准浏览器下a.compareDocumentPosition(b)有5个值，若为0表示为同一节点，若为2表示a位于b后面，若为4表示a位于b前面，若为10表示a为b的后代，若为20表示a为b的祖级；

10. 