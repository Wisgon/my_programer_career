1. 设置代理：可以在~/.bashrc(linux)或~/.zshrc(mac)文件中添加以下代理命令：

   ```shell
   alias proxy='export all_proxy=host:port'
   alias unproxy='unset all_proxy'
   ```

   然后，执行\$source ~/.bashrc，即可生效，在命令行中输入\$proxy，即可将命令行的请求都设置代理，输入\$unproxy即可取消；<br><br>

2. mac查看端口占用并kill：注意，netstat没啥卵用
   `$lsof -nP -i:8000`  查看8000端口占用

   `$lsof -nP -i | grep QQ`   查看QQ程序的pid
   `$kill -9 pid`  杀pid
   `$lsof -nP -i | grep 127.0.0.1:6942`  查看具体ip:port<br><br>

3. pip清华源安装：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package`<br><br>

4. 常用解包命令：

   ```
   .tar
   打包：tar cvf FileName.tar DirName
   解包： tar xvf FileName.tar
   
   .gz
   壓縮：gzip FileName
   解壓1：gunzip FileName.gz
   解壓2：gzip -d FileName.gz
   
   .tar.gz
   壓縮：tar zcvf FileName.tar.gz DirName
   解壓：tar zxvf FileName.tar.gz
   
    
   
   .bz2
   壓縮： bzip2 -z FileName
   解壓1：bzip2 -d FileName.bz2
   解壓2：bunzip2 FileName.bz2
   
   .tar.bz2
   壓縮：tar jcvf FileName.tar.bz2 DirName
   解壓：tar jxvf FileName.tar.bz2
   
   .tgz
   壓縮：unkown
   解壓：tar zxvf FileName.tgz
   
   .tar.tgz
   壓縮：tar zcvf FileName.tar.tgz FileName
   解壓：tar zxvf FileName.tar.tgz
   
   .zip
   壓縮：zip FileName.zip DirName
   解壓：unzip FileName.zip
   
   .rar
   壓縮：rar a FileName.rar
   解壓：rar e FileName.rar
   
   .lha
   壓縮：lha -a FileName.lha FileName
   解壓：lha -e FileName.lha
   ```

   <br><br>

5. 

