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

3. Lorca库我修改的文件是：
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
   
4. 打开chrome，可以设置chrome在后台继续运行，这样打开快一点；<br><br>

5. 