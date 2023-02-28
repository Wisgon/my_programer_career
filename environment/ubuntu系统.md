1. 禁用鼠标中键：
   命令行直接输入echo "pointer = 1 25 3 4 5 6 7 2" > ~/.Xmodmap，然后重新登录；<br><br> 

2. 设置开机启动项：
   直接把命令写入 /etc/rc.local这个文件里，记住要写在exit 0 之前，这个脚本会在开机时执行脚本里的内容，如:

   ```shell
   $echo “123456”| sudo -S /etc/init.d/php-fpm start
   ```

   这里的echo "123456" | sudo xxxx 其实就是shell命令输入密码的做法，然后开机后会自动执行这个脚本命令；

   如果没有rc.local，则自己写一个，内容如下：

   ```shell
   #!/bin/sh -e
   #
   # rc.local
   #
   # This script is executed at the end of each multiuser runlevel.
   # Make sure that the script will "exit 0" on success or any other
   # value on error.
   #
   # In order to enable or disable this script just change the execution
   # bits.
   #
   # By default this script does nothing.
   
   echo “123456”| sudo -S /etc/init.d/php7.0-fpm start
   exit 0
   
   ```

   <br><br>
   
3. 修改默认python版本:

   - 直接执行下面命令:

   	```shell
     echo alias python=python3 >> ~/.bashrc
     source ~/.bashrc
     ```

   - 或者：

     ```shell
     sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
     sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
     ```
   ```
   
     其实就是设置运行python命令时，启动python2和python3的优先值，最后三位数是优先值
   ```

4. 设置开机挂载硬盘：

    ```shell
        sudo ls -l /dev/disk/by-uuid
        # 来获得待挂载硬盘的uuid，然后打开/etc/fstab文件，然后，添加开机挂载硬盘，如：

        # /dev/sdb1

        UUID=2b0b3a6c-fe07-4e18-b5a2-0d11b3d85ede	/         	ext4      	rw,relatime,data=ordered	0 1

        # /dev/sdb1

        UUID=2b0b3a6c-fe07-4e18-b5a2-0d11b3d85ede	/boot     	ext4      	rw,relatime,data=ordered	0 2

        # /dev/sdb5

        UUID=bb33495f-19a8-4c27-a837-670b3b47578d      /home/zhilong/disk  ext4
        rw,relatime,data=ordered	0 2

        #重启系统就ok了，#后面的都是注释，无关紧要；
    ```


6. 文件名乱码问题: 
   方法1：不一致所以导致了文件名乱码的问题，解决这个问题需要对文件名进行转码。文件名转码工具convmv没安装的话用下面的命令安装：`sudo apt-get install convmv `
   复制代码 
   convmv 使用方法：convmv -f 源编码 -t 新编码 [选项] 文件名常用参数：-r 递归处理子文件夹–notest 真正进行操作，默认情况下是不对文件进行真实操作–list 显示所有支持的编码–unescap 可以做一下转义，比如把%20变成空格
   主要方法:
`convmv -f GBK -t UTF-8 --notest -r *`     把当前文件夹下所有乱码文件名改过来;
   
   方法2：
   
   ```
   1. 通过unzip行命令解压，指定字符集
   unzip -O CP936 xxx.zip (用GBK, GB18030也可以)
   有趣的是unzip的manual中并无这个选项的说明, unzip --help对这个参数有一行简单的说明。
   
   2. 在环境变量中，指定unzip参数，总是以指定的字符集显示和解压文件
   /etc/environment中加入2行
   UNZIP="-O CP936"
   ZIPINFO="-O CP936"
   ```
   
   <br><br>
   
7. 命令不输出信息到屏幕: 如何让有大量屏幕无用输出的命令（比如解压超多文件时的unzip命令，会输出大量解压文件到屏幕）不输出信息在屏幕，又不会浪费磁盘IO，答案是（unzip xxx.zip >> /dev/null)，这样，信息全部被指向不存在的设备，等于抛弃这些信息;

8. ubuntu查找包含某关键字的文件:

   - Ubuntu 查找文件夹中内容包含关键字的文件,路径为当前文件夹:
     `grep -rl "keyword" ./`
   - `find / -name '*' | xargs grep 'route'`
     在根文件夹下查找含有关键字route的文件，列出文件名和route所在行。
   - `find / -name '*.txt' | xargs grep 'route'`
     在根文件夹下查找后缀名为txt且含有关键字route的文件，列出文件名和route所在行。

9. ubuntu下查看文件夹大小：`$du -sh`；<br><br>


10. 换源：先备份原先的，然后`$vim /etc/apt/sources.list`:

    ```shell
    # 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
    
    # 预发布软件源，不建议启用
    # deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
    ```


    Debian源请参考：<https://mirror.tuna.tsinghua.edu.cn/help/debian/>
    
    <br><br>

11. 联想拯救者手提电脑重装ubuntu后wifi没用，可用以下步骤：

 ```
       sudo gedit /etc/modprobe.d/blacklist.conf
       最后加入一行：
       blacklist ideapad_laptop
 ```

       <br><br>

12. 当要将自己的库添加到编译器能搜索到的路径的时候，比如`/home/jhd/Documents/jhd_projects/zhps_jcpt/listener/linux64/lib`，此时，可以` sudo vim /etc/ld.so.conf`，在ld.so.conf最后加上一行：`/home/jhd/Documents/jhd_projects/zhps_jcpt/listener/linux64/lib`，然后保存退出，执行：`sudo ldconfig`即可；<br><br>


13.  设置代理：

  ```
  $export http_proxy=http://yourproxyaddress:proxyport  //http
  $export https_proxy=http://yourproxyaddress:proxyport  // https
  ```

  <br><br>

14. ubuntu端口转发：

    ```shell
    #sudo apt-get install rinetd
    #sudo vim /etc/rinetd.conf
    
    // 在最后添加以下配置
    0.0.0.0 27018 127.0.0.1 27017   // 将本机27018端口转发到27017
    
    #rinetd -c /etc/rinetd.conf 
    ```

    <br><br>

15. ubuntu点击图标最小化，执行命令：

    ```shell
     $gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'
    ```

    <br><br>

16. apt-get install 使用代理：`sudo apt-get install xxx -o Acquire::http::proxy="http://127.0.0.1:9001"`;<br><br>

17. ubuntu安装gcc-4:

    ```shell
    sudo add-apt-repository 'deb http://archive.ubuntu.com/ubuntu/ trusty main'
    sudo add-apt-repository 'deb http://archive.ubuntu.com/ubuntu/ trusty universe'
    sudo apt install gcc-4.4
    ```
    <br><br>
18. vmware启动虚拟机，出现“Could not open /dev/vmmon: No such file or directory“错误，修复命令如下：

    ```shell
    wget https://raw.githubusercontent.com/rune1979/ubuntu-vmmon-vmware-bash/master/wm_autoupdate_key.sh
    sudo chmod +x wm_autoupdate_key.sh
    ./wm_autoupdate_key.sh  // 这一步要输入密码，记住密码
    ```

    执行完重新启动，蓝屏出现时按选择`Enroll MOK`->`continue`->`Yes`->输入密码->`REBOOT`，重启完搞定；<br><br>
    
19. 解決Linux開啟VMWare Workstation時出現「Unable to start services」的問題:

    ```shell
    #git clone https://github.com/mkubecek/vmware-host-modules.git
    #cd vmware-host-modules/
    //假設現在要安裝VMWare Workstation Pro 15.1的Linux Kernel模組，那麼就要使用remotes/origin/workstation-15.1.0分支；假設現在要安裝VMWare Workstation Player 15.1的Linux Kernel模組，那麼就要使用remotes/origin/player-15.1.0分支。
    #git checkout remotes/origin/workstation-15.1.0
    #git fetch
    #make
    #sudo make install
    #sudo systemctl restart vmware
    ```

    搞定；<br><br>
    
20. 查找命令的可执行文件所在路径，用whereis，如：`$whereis php`，得到/usr/bin/php，知道php这个命令的路径在/usr/bin；<br><br>

21. 查看端口占用：`netstat -ap | grep 8080`；<br><br>

22. 服务器刚装好的ubuntu18.04，默认是防火墙封住所有端口的，除了阿里云安全组解放端口外，还需要下载firewall来解封端口：

    ```shell
    $apt-get install firewall
    $firewall-cmd --permanent --zone=public --add-port=80/tcp  // 这里是开放80端口
    $firewall-cmd --reload
    ```

    <br><br>

23. 自动登录服务器的脚本：

    - 首先要安装expect: `$sudo apt-get install expect`

    - //然后，编写shell脚本：load.sh

      ```
      #! /usr/bin/expect
      set timeout 300
      spawn ssh root@47.113.100.222
      expect "*password:"
      send "mzdykj0208hakka*#\r"
      interact
      ```

    - 执行：`./load.sh`，注意，不要用`bash load.sh`这样会默认用bash执行，而spawn这些命令会找不到，因为这些命令都是expect下的；

    <br><br>

24. 点击图标最小化：

    - 安装：`$sudo apt install dconf-editor`;
    - 打开： `$dconf-editor`;
    - 打开后在搜索栏搜索：`dash-to-dock`;
    - 进入搜索到的文件夹，拉下去，看到"click-action"字样，再点进去，把"Use default value"关掉，然后Custom Value选择`minimize-or-previews`，至此完成；<br><br>

25. ubuntu下好用的截图工具是flameshot，安装：`sudo apt-get install flameshot`<br><br>

26. ubuntu's useful gesture tool:
    ```
    sudo apt install gnome-shell-extension-manager
    ```
    open the tool just installed, then press "Browse" tab, search "Gesture Improvements" and install it.Then, in the "Installed" tab the extension will be there and press the gear to config it.<br><br>

27. disable mouse middle button in vscode,just add `"editor.selectionClipboard": false` in setting json.<br><br>
28. ubuntu install wechat: just cd ./packages and right click wechat.deb, then choose "open with other application",use "software install" to open it, then click "install", that's all.<br><br>
29. Ubuntu22.04 use wayland in some window.So the package Xlib can't work in some wayland base window.Then, use `sudo gedit /etc/gdm3/custom.conf `,if you can't find gdm3, find something like "gdm".Then, change the line like "# WaylandEnable=false",delete "#" to uncomment it.And then restart your computer.After restarted, if you have something wrong with your system, please recover the "custom.conf".Because ubuntu22.04 use wayland in some window,so if wayland is active status, there is some window that this app can't communicate.

    

    

  