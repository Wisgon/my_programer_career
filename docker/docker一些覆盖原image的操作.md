# 使用docker run的选项以覆盖Dockerfile中的设置详解

通常，我们首先定义Dockerfile文件，然后通过docker build命令构建得到镜像文件。然后，才能够基于镜像文件通过docker run启动一个容器的实例。

那么在启动一个容器的时候，就可以改变镜像文件中的一些参数，而镜像文件中的这些参数往往是通过Dockerfile文件定义的。

但并非Dockerfile文件中的所有定义都可以在启动容器的时候被重新定义。docker run不能覆盖的Dockerfile文件指令如下：
```shell
	- FROM
	- MAINTAINER
	- RUN
	- ADD
	- COPY
```
1. 覆盖ENTRYPOINT指令
  Dockerfile文件中的ENTRYPOINT指令，用以给出容器启动后默认入口。
  ENTRYPOINT指令给出容器启动后的默认行为，一般难以在启动容器时覆盖，但是可以追加命令参数。示例如下：
`docker run --entrypoint /bin/bash mysql:latest ...`

给出容器入口的后续命令参数
`docker run --entrypoint="/bin/bash" mysql:latest ...`

给出容器的新Shell
`docker run -it --entrypoint="" mysql:latest bash`
重置容器入口

2. 覆盖CMD指令
Dockerfile文件中的CMD指令，给出容器启动后默认执行的指令。

可以在启动容器的时候，为docker run设置新的命令选项，从而覆盖掉Dockerfile文件中的CMD指令（不会再咨询Dockerfile文件中的CMD指令）。示例如下：

- docker run ... <New_Command>，可以给出其他命令以覆盖Dockerfile文件中的默认指令
如果Dockerfile文件中还声明了ENTRYPOINT指令，则上述指令都将作为参数追加到ENTRYPOINT指令。

3. 覆盖EXPOSE指令
Dockerfile文件中的 EXPOSE指令，用以向容器所在主机保留端口。

显然这是运行时容器的一个特性，所以docker run可以方便地覆盖该指令。示例如下：
```shell
docker run --expose="port_number:port_number"
docker run -p port_number:port_number/tcp，打开指定范围的端口
docker run --link="another_container_id"，链接到其他容器
docker run -P，打开所有端口
```
4. 覆盖ENV指令
Dockerfile文件中的 ENV指令，用以设置容器中的环境变量。

启动容器时，自动为容器设置如下环境变量：

- HOME，基于USER设置用户主目录
- HOSTNAME，默认容器的主机名
- PATH，默认:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
- TERM，默认xterm，如果容器被分配了伪TTY

docker run可以方便地覆盖该指令。示例如下：
```shell
docker run -e "key=value" ...，设置新的环境变量key
docker run -h ...，覆盖HOSTNAME
docker run ubuntu:latest /bin/bash -c export
```

```shell
declare -x HOME="/"
declare -x HOSTNAME="85bc26a0e200"
declare -x OLDPWD
declare -x PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
declare -x PWD="/"
declare -x SHLVL="1"
declare -x deep="purple"
```
通过脚本，设置或覆盖环境变量

5. 覆盖VOLUME指令

Dockerfile文件中的 VOLUME指令，用以为容器设置的data volumes。

docker run可以方便地覆盖该指令。示例如下：
```shell
docker run -v ...
docker run -volumes-from ...
```
6. 覆盖USER指令

容器内部的默认用户是root(uid=0)。
Dockerfile文件中可以通过USER指定其他用户为容器的默认用户。

docker run可以方便地覆盖该指令。示例如下：
```shell
docker run -u="" ...
docker run --user="" ...
```
docker run支持-u如下形式：

- user
- user:group
- uid
- uid:gid
- user:gid
- uid:group


7. 覆盖WORKDIR指令

Dockerfile文件中的 WORKDIR指令，用以为Dockerfile文件中的后续指令设置工作目录。

如果设置的路径不存在，则创建该路径，即时在后续指令中根本未使用。

在一个Dockerfile文件中的，可以存在多个WORKDIR指令。对于相对路径，后续指令继承前续指令。

在WORKDIR指令中，可以引用前续已经定义的环境变量。

docker run可以方便地覆盖该指令。示例如下：

- docker run -w="" ...
- docker run --workdir="" ...
