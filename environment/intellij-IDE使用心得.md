###我的一些快捷键的更改：
- 原先command+enter另起一行的改为enter，而原先enter改为command+enter；
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
4. CLion禁止rust写代码时左边的小灯泡：setting->Editor->Intentions->Rust，去掉“show XXX macro xxx”那三个，如果要完全去掉，则RUST的全部勾取消掉；<br><br> 
5. 

