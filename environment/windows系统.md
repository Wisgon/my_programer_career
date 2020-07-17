1. windows cmd使用代理：

   ```
   set HTTP_PROXY=http://user:password@proxy.domain.com:port  // 一次性有效
   ```

   powershell使用代理：

   ```
   $env:HTTPS_PROXY="http://192.168.8.211:9001"
   $env:HTTP_PROXY="http://192.168.8.211:9001"
   ```

   <br><br>

2. `netstat -aon|findstr "49157" ` 查询端口占用；<br><br>

3. win10设置http代理：

   ```
   set http_proxy=http://127.0.0.1:12495
   set https_proxy=http://127.0.0.1:12495
   // 可用于下载go包，亲测可用
   ```

   查看变量：

   ```
   set http_proxy
   // 输出http_proxy=http://127.0.0.1:12495
   ```

   <br><br>

4. win10端口映射：

   ```
   命令行输入：netsh interface portproxy add v4tov4 listenport=9001 listenaddress=0.0.0.0 connectport=12495 connectaddress=127.0.0.1
   ```

   这样，蓝灯只代理本地的端口12495，用这个命令，本机在局域网就变成了一个代理，别的机器访问本机的内网ip:9001就可以代理上网了；

   原文：

   1、添加端口转发
   netsh interface portproxy add v4tov4 listenport=4000 listenaddress=127.0.0.1 connectport=4000 connectaddress=172.31.217.198
   2、删除端口转发
   netsh interface portproxy del v4tov4 listenport=4000 listenaddress=127.0.0.1
   3、查看已存在的端口映射
   netsh interface portproxy show v4tov4
   可以通过命令 netstat -ano|find 4000 查看端口是否已在监听
   telnet 127.0.0.1 4000 测试端口是否连通

   <br><br>

5. 出现`Unable to round-trip http request to upstream: dial tcp [::1]:8033: connectex: No connection could be made because the target machine actively refused it.`这类的错误，可能是开了代理，然后localhost被代理了，可以在代理设置上勾选"请勿将代理服务器用于本地地址"<br><br>

6. 添加ftp服务：

   - 打开“计算机管理”界面
   - 点击“服务和应用程序”
   - 点击“Internet Information Services(IIS)管理器”
   - 点击右边的“DESKTOP-XXX”
   - 下拉中右键点击“网站”，选择“添加FTP站点”
   - 按照提示添加FTP站点即可，在局域网其他计算机的文件资源栏中，填写"ftp://192.168.9.40"，即可访问到共享文件夹<br><br>

7. 移动硬盘有驱动但是没显示的解决办法：

   -  在计算器管理中打开“设备管理器”，找到“通用串行总线控制器” 
   -  右键下方的USB大容量储存设备，对其进行卸载操作 
   -  再右键点击“通用串行总线控制器”，点击“扫描检测硬件改动”，稍等片刻就可以看见移动硬盘刷新出来了

   <br><br>

8. windows远程桌面默认端口是3389；<br><br>

9. 

