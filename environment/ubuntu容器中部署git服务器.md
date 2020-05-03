创建并进入容器后，步骤如下：

```shell
#注意，docker创建容器时，要映射容器的22端口
apt-get install git
apt-get install openssh-client
apt-get install openssh-server
/etc/init.d/ssh start
#若要ssh能登录，则修改/etc/ssh/sshd_config文件
vim /etc/ssh/sshd_config
#文件末尾加上一行：PermitRootLogin yes
service ssh restart
```

其他步骤和真正的ubuntu上差不多

之后每次开机都记得要加上命令：`/etc/init.d/ssh start`

如果clone的时候出现` RSA host key for mysharebook.cn has changed and you have requested strict checking `的错误，则在客户端 删除/$HOME/.ssh/known_hosts文件中对应ip的那一行就行。

