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

10. golang开发配置，在项目文件夹下新建".vscode"文件夹，并在里面新建"setting.json"文件，内容如下：

   ```json
   {
       "go.gopath": "D:\\GoPath;D:\\Documents\\my_projects\\go_web_view_demo",
   }
   ```

   <br><br>

11. 如果遇到go的一些依赖库安装失败的，可以手动build：

   ```
   go get -v -u github.com/mdempsky/gocode                    gocode
   go get -v -u github.com/uudashr/gopkgs/cmd/gopkgs    gopkgs
   go get -v -u github.com/ramya-rao-a/go-outline              go-outline
   go get -v -u github.com/acroca/go-symbols               go-symbols
   go get -v -u golang.org/x/tools/cmd/guru                guru
   go get -v -u golang.org/x/tools/cmd/gorename            gorename
   go get -v -u github.com/derekparker/delve/cmd/dlv       dlv
   go get -v -u github.com/stamblerre/gocod                      gocode-gomod
   go get -v -u github.com/rogpeppe/godef                      godef
   go get -v -u github.com/ianthehat/godef                     godef-gomod
   go get -v -u github.com/sqs/goreturns                       goreturns
   go get -v -u golang.org/x/lint/golint                       golint
   
   go build -o %GOPATH%\\bin\\gocode.exe github.com/mdempsky/gocode
   go build -o %GOPATH%\\bin\\gopkgs.exe github.com/uudashr/gopkgs/cmd/gopkgs%
   go build -o %GOPATH%\\bin\\go-outline.exe github.com/ramya-rao-a/go-outline%
   go build -o %GOPATH%\\bin\\go-symbols.exe github.com/acroca/go-symbols%
   go build -o %GOPATH%\\bin\\guru.exe golang.org/x/tools/cmd/guru%
   go build -o %GOPATH%\\bin\\gorename.exe golang.org/x/tools/cmd/gorename%
   go build -o %GOPATH%\\bin\\dlv.exe github.com/derekparker/delve/cmd/dlv%
   go build -o %GOPATH%\\bin\\gocode-gomod.exe github.com/stamblerre/gocode
   go build -o %GOPATH%\\bin\\godef.exe github.com/rogpeppe/godef
   go build -o %GOPATH%\\bin\\godef-gomod.exe github.com/ianthehat/godef
   go build -o %GOPATH%\\bin\\goreturns.exe github.com/sqs/goreturns%
   go build -o %GOPATH%\\bin\\golint.exe golang.org/x/lint/golint
   ```

    手动将所有的.exe文件放入%Goroot%\bin 文件夹下 ；<br><br>

12. 使用“setting sync”扩展插件来上传和下载配置文件；<br><br>

13. 