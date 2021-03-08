docker默认不能安装在win10的Home版本，此时，可以通过安装Hyper-V和修改注册表来达到目的。



- 安装hyper-v：
  把下面语句复制下来，保存在一个bat文件里，然后以管理员身份执行：

  ```
  pushd "%~dp0"
  dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
  for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
  del hyper-v.txt
  Dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL
  ```

  安装好后，会提示重新启动，此时打开windows的“启用或关闭Windows功能”窗口，会看到Hyper-V的选项，就表示安装成功；

- 修改注册表：
  运行->输入regedit->打开注册表->看到计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion->双击CurrentVersion->找到EditionID->将原本为“Core”的值修改为“Professional”，确定即可；

- 下载docker-desktop，即可进行安装；

- 更好的方法是直接淘宝买个秘钥然后升级到pro;