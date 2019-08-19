1. 有时候出现顶上或边上留白问题，可以试试：

   ```css
   * {
   		 margin:0;
   		 padding: 0;
   } /*加上这个，不然顶上会有留白，因为浏览器默认的body和html标签的margin和padding都不是0*/
   ```



2. 设置ul的display属性值为”inline-box“的时候，li会出现顶上留白的问题，解决方法：

   将ul的display属性改为”flex“，问题解决；

   

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

   然后将这个父元素容器的class设置成class=“clearfix”即可，这样子元素就能撑起父元素了；

   

5. 相对定位是该元素相对于其原本该出现的位置的偏移量，如：

   ```css
   .exampl {
       position:relative;
       top:35px;
       left:100px;
   }
   ```

   设置了该样式的元素会相对于其自然位置向下偏移35px，向右偏移100px，但会在该元素原先的位置留下空白;

   

6. 绝对定位如果没有说明，则是相对于body的绝对位置的，脱离了文档流，其他元素不知道它的存在，它也不知道其他元素的存在，如果要让该元素相对于其父元素进行绝对定位，则在父元素中要加入：”position: relative;”

    

7. background-color: transparent; 是将背景色设置为透明；

8. 创建自适应的css布局的诀窍是：

   父元素用max-width: xx em; 来确定最大的尺寸，要用em为单位换算，子元素用width: xx%; 来确定尺寸，用百分数就可以灵活地适应不同屏幕的大小了，记住任何有关尺寸的设置，比如内边距等，都要用百分比来表示；

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

   其中vertical-container是父元素的class，子元素不用设置css属性即可居中；

10. 