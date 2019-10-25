###无线网卡无法找到wifi

1) 创建/etc/modprobe.d/black_ideapad_laptop.conf文件：

```
sudo touch /etc/modprobe.d/black_ideapad_laptop.conf
```

2）编辑ideapad.conf文件： 

```
sudo gedit /etc/modprobe.d/black_ideapad_laptop.conf
```

3) 在ideapad.conf文件中添加：

```
blacklist ideapad_laptop
```

 4) 关闭并保存ideapad.conf文件，移除ideapad_laptop设备：

```
sudo modprobe -r ideapad_laptop  
```

5) 注销重启Ubuntu系统，可以看到无线设备能够被打开，并能搜索到WiFi信号。

<br><br>

###无法正常关机问题

有集成显卡和NVIDIA独立显卡，刚开始安装Deepin的时候，关机或者重启总是卡死，只能长按电源键断电，非常不方便。 后来在网上查了很多资料才知道是显卡驱动的问题，但是Deepin自带的显卡驱动切换软件总是切换失败，可以用下面的方法解决：  

先重启，或者说是先断电再开机，等进入开机引导界面，   按E键进入编辑模式，找到"splash quiet"，在它后面一个空格之后添加"acpi=off"，这个代码可以禁用高级配置，强制使用默认的英特尔集成显卡驱动， 

修改完成之后按F10键开机，进入系统，打开终端，输入：  `sudo -s`  回车，输入密码，进入root模式，输入以下命令安装NVIDIA显卡驱动：  `apt-get install -y nvidia-driver`  如果有提示让你卸载原有驱动，按回车确定即可，

安装完成后，重启电脑，或者说是先断电再开机，重复刚才在引导界面添加"acpi=off"的步骤，然后开机。 开机后打开Deepin的显卡切换软件，切换显卡为NVIDIA闭源驱动，这个时候应该可以切换成功了，如果提示失败，则可以打开Deepin的显卡切换软件，切换为大黄蜂方案，切换完成重启一下电脑就OK了，重启后出现茶壶图案，点击“应用”即可，不用再添加"acpi=off"。 现在应该可以正常关机和重启了，其它显卡我没有试过，但是安装驱动的命令在Deepin维基里面有，可以自己去看看。