1. ubuntu20.04，静态ip设置方法(不能和局域网内其他机器相连，有这个需求的话，请用第3点的ip设置）：

   - `sudo vim /etc/netplan/00-installer-config.yaml`,内容如下：

     ```
     network:
       ethernets:
         ens33:
           addresses: [192.168.31.63/24]
           dhcp4: no
           dhcp6: no
           gateway4: 192.168.31.2
       version: 2
     
     ```

     注意空格！，比如，addresses: 与 [192....]之间一定要有一个空格！！！

     192.168.31.63/24这样的写法，表示子网掩码是255.255.255.0，因为这个子网掩码弄成二进制就是：11111111.11111111.11111111.00000000，一共24个1，所以/24表示这样的子网掩码；

     这里还要注意gateway4!!!，不一定是192.168.31.2，具体的要查看虚拟机菜单栏-->编辑(E)-->虚拟网络编辑-->点击"VMnet8   NAT模式  ....."那一栏，然后弹出的窗口中，点击"NAT设置"，这里就能看到网关了；

   - `sudo vim /etc/systemd/resolved.conf`，设置DNS，在"[Resolve]"下一行添加DNS=202.96.134.133即可；<br><br>

2. ubuntu与win10(主机)共享文件夹：

   -  问题现状：/mnt下没有hgfs目录，需要重新安装VMtools工具 ；

   -  虚拟机设置中使用虚拟光驱（CD/DVD(SATA))加载linux.iso（在VMware/VMware WorkStation安装目录下可找到）文件，可在VM安装文件夹找到，其他光驱设置为**自动检测** ；

   -  启动Ubuntu，使用mount -t iso9660 /dev/cdrom /mnt/cdrom；若/mnt无此目录则新建 ；

   - 拷贝VMwaretools-10.3.2*.tar.gz到安装目录，使用tar xzvf解压，安装 

     ```shell
     cp VMwaretools-10.3.2*.tar.gz ~/your_install_path/
     cd ~/your_install_path
     cd vmware-tools-distrib
     sudo ./vmware-install.pl
     ```

   -  安装完成，重启可发现/mnt/hgfs已存在 ;

   -  在虚拟机设置中增加文件夹共享 ，在虚拟机--》设置--》右边选项标签卡--》共享文件夹，按步骤设置主机需要共享的文件夹即可；

3. ubuntu20.04，静态ip设置（桥接模式，可以和局域网内其他ip相连）:

   - vmware虚拟机菜单栏-->编辑-->虚拟网络编辑器-->右下角更改设置-->VMnet0，桥接模式，桥接到...下拉框弹出，选择IntelR-Dual Band Wireless -AC 3165，不同机器可能不太一样，但是用wifi连的网络的话，尽量选择跟这个相似的，如果是有线连接的，则看看下拉中有哪个像是有线连接的对应选项了；
   - 虚拟机设置-->网络适配器-->点选“桥接模式”，下面那个“复制物理网络。。。”**不要**选!!!；
   - 开机，设置静态ip，这里要注意的是，要将网段和网关设置成和主机一样，比如主机ip是192.168.9.5，网关是192.168.9.1，那么虚拟机的ip设置成192.168.9.xxx，网关一样就可；
   - 接下来，局域网的其他机器就可以ping通这个vmware虚拟机了；

4. ubuntu20.04下vmware启动虚拟机，出现“Could not open /dev/vmmon: No such file or directory“错误，修复命令如下：

   ```shell
   wget https://raw.githubusercontent.com/rune1979/ubuntu-vmmon-vmware-bash/master/wm_autoupdate_key.sh
   sudo chmod +x wm_autoupdate_key.sh
   ./wm_autoupdate_key.sh  // 这一步要输入密码，记住密码
   ```

   执行完重新启动，蓝屏出现时按选择`Enroll MOK`->`continue`->`Yes`->输入密码->`REBOOT`，重启完搞定；<br><br>

5. 解決Linux開啟VMWare Workstation時出現「Unable to start services」的問題:

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
   
6. ubuntu主机，win10虚拟机中无法安装vmware tools，可能是缺少某个库：

   ```
   // ubuntu主机中运行：
   sudo apt install libncursesw5
   ```

   <br><br>

7. 