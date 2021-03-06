1. 有时候出现顶上或边上留白问题，可以试试：

   ```css
   * {
   		 margin:0;
   		 padding: 0;
   } /*加上这个，不然顶上会有留白，因为浏览器默认的body和html标签的margin和padding都不是0*/
   ```

<br><br>

2. 设置ul的display属性值为”inline-block“的时候，li会出现顶上留白的问题，解决方法：

   - 将ul的display属性改为”flex“，问题解决，但是必须有设置float属性；
   - 还有一种更好解决办法是margin设置为0；
   - 还有一种方法是所有inline-block的元素设置vertical-align: top;<br><br>

3. 我们经常使用浮动，但浮动并不是唯一的解决方案。有时候inline-block会更好，特别是你想排列一些图片，或者横向排列链接时。Inline-block元素带有一些行内元素的特征（横向排列），同时内部也拥有块级元素的属性。这个跟浮动很类似，只不过有些区别。这些区别决定了你该使用哪种方案。如果你很纠结垂直对齐问题或者横向排列元素，不妨使用inline-block。如果你需要对一个元素跟围绕他的一些元素进行更多控制，你需要浮动；<br><br>

4. 当某容器的子元素设置了float属性之后，会脱离文档流，该容器的高度就会变成0，这样会引发一系列问题，解决方案是让容器自身具有清除浮动的能力，可以黏贴以下代码：

   ```css
   .clearfix:before,
   .clearfix:after {
       content: " ";
       display: table;
   }
   
   .clearfix:after {
       clear: both;
   }
   
   .clearfix {
       *zoom: 1;
   }
   ```

   然后将这个父元素容器的class设置成class=“clearfix”即可，这样子元素就能撑起父元素了；<br><br>

5. 相对定位是该元素相对于其原本该出现的位置的偏移量，如：

   ```css
   .exampl {
       position:relative;
       top:35px;
       left:100px;
   }
   ```

   设置了该样式的元素会相对于其自然位置向下偏移35px，向右偏移100px，但会在该元素原先的位置留下空白;<br><br>

6. 绝对定位如果没有说明，则是相对于body的绝对位置的，脱离了文档流，其他元素不知道它的存在，它也不知道其他元素的存在，如果要让该元素相对于其父元素进行绝对定位，则在父元素中要加入：”position: relative;”<br><br>

7. background-color: transparent; 是将背景色设置为透明；<br><br>

8. 创建自适应的css布局的诀窍是：

   父元素用max-width: xx em; 来确定最大的尺寸，要用em为单位换算，子元素用width: xx%; 来确定尺寸，用百分数就可以灵活地适应不同屏幕的大小了，记住任何有关尺寸的设置，比如内边距等，都要用百分比来表示；<br><br>

9. 使用 Flexbox 的居中布局：

   ```css
   .vertical-container {
     height: 300px;
     display: -webkit-flex;
     display:         flex;
     -webkit-align-items: center;
             align-items: center;
     -webkit-justify-content: center;
             justify-content: center;
   }
   ```

   其中vertical-container是父元素的class，子元素不用设置css属性即可居中；<br><br>

10. *逻辑属性*  
   所谓CSS逻辑属性，指的是`*-start`，`*-end`以及`*-inline-start`，`*-inline-end`，`*-block-start`，`*-block-start`这类CSS属性，其最终渲染的方向是有逻辑性在里面的。 例如`margin-left`方向是固定的，就左侧间距，没有逻辑；但是，`margin-start`有可能是左间距，也有可能是右间距，例如，对于内联元素，如果`direction`属性值是`rtl`，则`margin-start`的表现等同于`margin-right`，如果属性值是`ltr`，则`margin-start`的表现等同于`margin-left`，就表现出了逻辑判断在里面，因此，成为CSS逻辑属性。<br><br>

11. *逻辑维度*  
  逻辑属性定义块和内联维度的开始和结束属性。对于高度和宽度属性，我们改为使用`block-size`和`inline-size`。我们还可以设置`max-block-size`、`min-block-size`、`max-inline-size`和`min-inline-size`。如果您使用的是英语，则从上到下的横向语言`block-size`是指`height`屏幕上块`inline-size`的物理特性`width`，即物品的物理特性。如果您使用的是垂直运行的语言，那么当您查看屏幕时，`block-size`将会出现控制`width`和`inline-size`高度的情况。<br><br>
  
12. 任何属性都有initial值，表示不进行任何设置，为元素保持最初的属性值，即使父元素有属性要继承，也不会继承；<br><br> 

13. 可以用css的transform属性做轮播图，transform属性中，有个translate3d的属性方法，接受3个参数，分别是x,y,z轴坐标，例子：
   html代码：

   ```html
   <div class="window-div">
           <div class="lunbo-div">
               <div class="image" style="width:100px;height: 100px; background-color: red"></div>
               <div class="image" style="width:100px;height: 100px; background-color: green"></div>
               <div class="image" style="width:100px;height: 100px; background-color: blue"></div>
           </div>
       </div>
   ```

   css代码：

   ```css
   .window-div {
       width: 100px;
       height: 100px;
       overflow: hidden;
       position: relative;
       left: 1000px;
     }
   
     .lunbo-div {
       position: absolute;
       overflow: hidden;
       width: 350px;
       transition-duration: 0.5s;
       transform: translate3d(-200px, 0px, 0px);
       backface-visibility: hidden;
       overflow: hidden;
     }
   
     .image {
       display: inline-block;
     }
   ```

   这样子的话，window-div是父div，负责显示窗口，lunbo-div是轮播图的div，有三个子元素是3个图片div，当transform的属性值translated3d的x坐标设置为-200px时，显示的是第三个图片，因为lunbo-div已经向父元素向左缩进了200px的位置，而父元素的overflow属性是hidden，所以现在window-div显示的是第三张图片，transition-duration是过渡效果时间，我们现在只需要用js代码定时地改变transform的translated3d的x轴坐标，就可以做到轮播效果了，而改变的过渡效果实践由transition-duration控制；
   
14. 浏览器请求资源时，都会先判断是否有缓存，若有缓存且未过期则会从缓存中读取，不会再次请求。先加载的图片会存储到浏览器缓存中，后面再次请求同路径图片时会直接读取缓存中的图片。

15. 两个css类都作用在同一个元素中，如`<a class="c1 c2">`，这时，如果c1和c2都定义了同一个属性，比如width，那么，a的width究竟是什么并不取决于标签中“class=”那里是先写c1还是c2，而是取决于css表哪个最后加载（如果c1和c2不在同一个css文件的话）或者在同一个css文件中，哪个更后定义；

16. 父元素为设置了宽高的inline-block，子元素的margin会和父元素的上沿对齐，而父元素若是block，子元素也是block，则子元素的padding和父元素的上沿对齐，子元素的margin会超过父元素；

17. 

