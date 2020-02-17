1. 
   
2. 禁用鼠标中键：
   命令行直接输入echo "pointer = 1 25 3 4 5 6 7 2" > ~/.Xmodmap，然后重新登录；<br><br> 

3. 设置开机启动项：
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


   ```
   
3. 修改默认python版本:

   - 直接执行下面命令:

   - ```shell
     echo alias python=python3 >> ~/.bashrc
     source ~/.bashrc
   ```

   - 或者：

   - ```shell
     sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
     sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
     ```

     其实就是设置运行python命令时，启动python2和python3的优先值，最后三位数是优先值

4. 设置开机挂载硬盘：

5. ```shell
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

6. 文件名乱码问题: 不一致所以导致了文件名乱码的问题，解决这个问题需要对文件名进行转码。文件名转码工具convmv没安装的话用下面的命令安装：`sudo apt-get install convmv `
   复制代码 
   convmv 使用方法：convmv -f 源编码 -t 新编码 [选项] 文件名常用参数：-r 递归处理子文件夹–notest 真正进行操作，默认情况下是不对文件进行真实操作–list 显示所有支持的编码–unescap 可以做一下转义，比如把%20变成空格
   主要方法:
   `convmv -f GBK -t UTF-8 --notest -r *`     把当前文件夹下所有乱码文件名改过来;

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

13. 
