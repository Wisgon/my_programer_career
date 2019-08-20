1. 有关于使用inline-block来代替float的讨论也蛮多的，最常说的就是使用inline-block来代替float进行布局，或者使用 inline-block来实现元素的居中效果。但是inline-block水平呈现的元素间，换行显示或空格分隔的情况下会有间距。关于这个问题，原 来很多人不知道啊。呵呵~其实很简单，当原素被转换为inline-block显示的时候，那么该元素会具有inline的一些属性，所 以当你在标签之间换行的时候会产生空格，inline-block之间的间距就是一个空格的位置，你要算间隙是几个像素，其实依赖于你的字体设置大小，空 格是个字符啊，所以-margin补间距之类的方法不可取，所以大家每个人出来的负值都不一样（-_-!）。空格是由inline-block标签之间换 行产生的，那么解决方法简单了，不要在转换为inline-block的标签的代码之间换行就行了，开发人员一定要在精确布局的时候要注意一下。 inline-block具有inline的一些属性，那么inline标签代码之间换行本来就会有空格产生 的；IE倒是奇怪没有产生空格，但是也讲的通。

   **解决方法：**

   第一：去掉html标签中的空格和回车；例如：

   ```html
   <ul><li>web前端开发</li><li>前端开发</li><li>前端开发:http://www.css119.com</li></ul>
   ```

   第二：改变html标签的结构(下面只展示出了一种，还有其他的类似方法)；
   例如：

   ```html
   <ul>
     <li>WEB前端开发</li
     ><li>前端开发</li
     ><li>前端开发:http://www.css119.com</li>
   </ul>
   ```

   第三：利用负margin解决（不推荐，具体负margin多少取决于字体的大小）；

   第四：设置父元素font-size:0;子元素重新设置自己的font-size；
   例如：

   ```css
   ul{font-size:0}
   li{ display:inline-block;*display:inline;*zoom:1;background:green; padding:5px;font-size:12px}
   ```

   可以看到在 ie8，firefox，chrome 和 opera 浏览器下已经没有问题了，但是在 低版本safari 浏览器下还是有问题。
   关于 低版本safari 浏览器的兼容。
   可以利用letter-space:-N px或者word-spacing:-N px来解决。<br><br> 

2. 