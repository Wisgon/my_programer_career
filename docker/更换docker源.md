### win10下

启动docker_desktop，然后右键点击右下角的docker图标，选择settings，弹出的对话框中，选择

Daemon，将

```cpp
https://docker.mirrors.ustc.edu.cn
https://hub-mirror.c.163.com
```

黏贴进"Registry mirrors"中，apply即可；

 <br><br>

linux下：

修改或新增 /etc/docker/daemon.json

```
# vi /etc/docker/daemon.json

{

"registry-mirrors": ["http://hub-mirror.c.163.com"]

}

```



Docker国内源说明：

Docker 官方中国区

https://registry.docker-cn.com

网易

http://hub-mirror.c.163.com

中国科技大学

https://docker.mirrors.ustc.edu.cn

阿里云

https://pee6w651.mirror.aliyuncs.com




 