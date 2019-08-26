1. 设置代理：可以在~/.bashrc(linux)或~/.zshrc(mac)文件中添加以下代理命令：

   ```shell
   alias proxy='export all_proxy=host:port'
   alias unproxy='unset all_proxy'
   ```

   然后，执行\$source ~/.bashrc，即可生效，在命令行中输入\$proxy，即可将命令行的请求都设置代理，输入\$unproxy即可取消；

2. mac查看端口占用并kill：注意，netstat没啥卵用
   `$lsof -nP -i:8000`  查看8000端口占用

   `$lsof -nP -i | grep QQ`   查看QQ程序的pid
   `$kill -9 pid`  杀pid

3. 