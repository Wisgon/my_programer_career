1. 点击setting的时候，出现的是json编辑界面，要点一下右上角的一页纸一样的图标来切换到视图界面；<br><br> 

2. 代码编辑界面中，如果代码超出界面框会自动换行，而不是出现滚动条，则按alt+z可以出现滚动条；<br><br> 

3. 用command+f查找后，按alt+enter可以全选查找内容；<br><br> 

4. 最好不要用一个插件叫indent rainbow，对于大文件会拖慢速度，对于大文件，还要在setting.json中加入：

   ```json
   "files.autoSave": "onWindowChange",
   ```

   不然老是会保存；<br><br> 

5. command+shift+p是执行命令，command+p是快速搜索并打开文件；<br><br> 

6. command+j 打开或关闭下方的命令行；<br><br> 

7. 设置重启快捷键：command+k，command+s调出快捷键设置，然后，搜索reloadWindow，出来的几个选项中，默认是command+r的那个，右键点击，选择“change when expression”，改变出发时间为：editorTextFocus；<br><br> 

8. setting中，如果用了eslint来format代码，就不要用vetur.format.defaultFormatter.js和vetur.format.defaultFormatter.html了，这两个都给设置成“none”；<br><br> 

9. vscode中，如果打一个字母，按tab键，却无故给变成html标签，这可能是emmet.triggerExpansionOnTab被设置成true了；<br><br> 

10. 