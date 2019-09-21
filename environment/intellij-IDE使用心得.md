###我的一些快捷键的更改：
- 删除一行的快捷键command+shift+k，改为alt+shift+k；
- 代码提示插入的快捷键tab禁掉，改用enter代替；
- 格式化代码改为ctrl+alt+L；
  <br><br> 

###心得笔记：
1. 禁止tab代码自动补全：
   - keymap里面，找到“choose lookup item replace”，把tab的绑定取消；
   - Editor->Live Templates  "by default expand with" 改成“Enter”；<br><br> 
2. 代码出现没有import进来的函数，会出现错误提示，在鼠标移动到函数上面，按alt+shift+Enter就会自动import；<br><br> 
3. 在代码中把光标置于标记符或者它的检查点上再按 Alt-F7 （右键菜单中的 Find Usages… ）会很快地查找到在整个工程中使用地某一个类、方法或者变量的位置。<br><br> 
4. intellij-IDE去掉烦人的小灯炮：Setting->Editor->General->Appearance把“show intention bulb”勾掉即可；<br><br> 
5. pycharm的setting->Languages & Frameworks->python template languages 处可设置jinja2模板语言；<br><br> 
6. Setting->Editor->Color Scheme->General->Code->identifier under caret 可改变选中的变量的后续使用的地方的背景色；<br><br> 
7. 要控制回车后空格数量，可在Setting->Editor->Code style->对应的语言，里面设置；<br><br> 
8. 

