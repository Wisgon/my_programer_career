### 用到的库是[three.js]( https://github.com/mrdoob/three.js )和[Lorca](https://github.com/zserge/lorca )

1. 真正解决 Windows 中 Chromium “缺少 Google API 密钥” 的问题:

   ```
   打开 windows 的 CMD 命令提示符，依次输入以下命令： 
   setx GOOGLE_API_KEY "no" 
   setx GOOGLE_DEFAULT_CLIENT_ID "no" 
   setx GOOGLE_DEFAULT_CLIENT_SECRET "no"
   ```

   <br><br>

2. 谷歌浏览器各重要参数：

   ```shell
   --window-position=0,0  # 浏览器打开的坐标位置
   --start-maximized  # 启动时就最大化
   --disable-features=TranslateUI  # 禁止弹出翻译
   --start-fullscreen  # 一打开就全屏
   --enable-panels  # 始终置顶
   --new-window  # 新窗口打开
   --app=http://xxx/xxx  # 以app模式打开浏览器
   ```

   <br><br>

3. go源码我重写的文件是：

   （1）net/http/fs.go中，所有小写开头的serveFile改成了MyServeFile，然后net/http/export_test.go中的serveFile也改成了MyServeFile；
   <br><br>

4. Lorca库我修改的文件是：
   github.com\zserge\lorca\ui.go:74行：

   ```go
   args := append(defaultChromeArgs, fmt.Sprintf("--app=%s", url))
   args = append(args, fmt.Sprintf("--user-data-dir=%s", dir))
   if width != -1 && height != -1 {
   args = append(args, fmt.Sprintf("--window-size=%d,%d", width, height))
   }
   
   args = append(args, customArgs...)
   args = append(args, "--remote-debugging-port=0")
   ```

   github.com\zserge\lorca\fs.go 81行增加：

   ```go
   func (f *file) AddAssets(relativePath string, data []byte) {assets[relativePath]  = data}
   ```

    github.com\zserge\lorca\chrome.go  

   ```
   273行：log.Println()注释掉
   ```

   

   <br><br>

5. 打开chrome，可以设置chrome在后台继续运行，这样打开快一点；<br><br>

6. No 'Access-Control-Allow-Origin' header is present on the requested resource'， 跨域访问的解决方法:
   有可能是在socket服务器端，开的是0.0.0.0，而输入url访问的是localhost，然后客户端的js的socket连接的又是127.0.0.1，所以会造成跨域；<br><br>

7. go服务器要解决js不可以import的问题，首先，js在引入时要这样：`<script src="js/zhilong/test_import.js" type="module"></script>`，加个type="module"，然后，如果go的fileserver不改的话，就会产生mime的type不是javascript的报错，这时候就要修改go的fileserver的代码了，自己做过一个fileserver：

   ```go
   package mapUtils
   
   import (
   	"net/http"
   	"path"
   	"strings"
   )
   
   var requestFileCounter = 0
   
   type myFileHandler struct {
   	root http.FileSystem
   }
   
   func MyFileServer(root http.FileSystem) http.Handler {
   	return &myFileHandler{root}
   }
   
   func (f *myFileHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
   	upath := r.URL.Path
   	if !strings.HasPrefix(upath, "/") {
   		upath = "/" + upath
   		r.URL.Path = upath
   	}
   	requestFileCounter += 1
   	// fmt.Println(requestFileCounter)
   	// todo:在生产环境记得加上去
   	//if requestFileCounter > 20 {
   	//	log.Println("illegal~~~ " + upath)
   	//	os.Exit(23333)
   	//}
   	if strings.HasSuffix(upath, ".js") {
           // 这里加上设置content-type，前端js就可以用import了
   		w.Header().Set("Content-Type", "application/javascript")
   	}
   
   	http.MyServeFile(w, r, f.root, path.Clean(upath), true)
   }
   ```

   <br><br>

8. 