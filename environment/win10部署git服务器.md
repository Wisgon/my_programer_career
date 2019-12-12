**一. 搭建Git服务器环境前的必要准备**

1.Windows10

2.Java环境

3.GitBlit服务器

4.Git版本管理工具

 <br><br>

**二. 开始搭建**

**第一步**.安装JAVA运行环境

https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

1.勾选Accept License Agreement，2.选择Windows系统对应的版本下载

2.配置环境变量

CLASSPATH=C:\Program Files (x86)\Java\jdk1.8.0_201\lib

JAVA_HOME=C:\Program Files (x86)\Java\jdk1.8.0_201

Path 在最后新增 %JAVA_HOME%\bin;

在cmd测试安装效果：在cmd界面输入 javac -version看输出版本号<br><br>



**第二步**.安装Git

下载地址：https://git-scm.com/downloads

<br><br>

**第三步**.下载Gitblit

**1**.下载地址：http://www.gitblit.com/

下载后是压缩包，解压即可，不需要再安装

**2**.配置

找到安装目录中的Data文件夹中的defaults.properties，我的是E:\Git\gitblit-1.8.0\data\defaults.properties

Git文件目录：git.repositoriesFolder = F:/Git/GitPepository，会在gitblit安装目录下新建GitPepository文件夹

端口：server.httpPort = 10101

服务器IP：server.httpBindInterface =  空值，不要填这个，这样服务器就不会限死一个ip了（服务器IP，本地即本机的IP，查看本机IP，cmd=》ipconfig中IPv4地址）

server.httpsBindInterface = 也是空值<br><br>

**3**.运行

点击安装目录下的gitblit.cmd可直接运行。需要使用Windows服务运行配置如下：

1.点击安装目录下的installService.cmd，使用文本编辑器打开

SET ARCH=x86（修改为需要运行的版本）（x86（32位），amd64（64位））

SET CD=E:\Git\gitblit-1.8.0（新增）

StartParams="" ^ （配置为空）

2.配置好后右键，以管理员身份运行。在cmd=》services.msc中即可查看到gitblit服务

 