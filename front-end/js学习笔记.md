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

4. 