### 一些python环境配置心得

1. anaconda完整环境迁移：
   - 这里的方法是断网状态下的环境迁移，先将旧环境打包好（打包旧环境中的Anaconda3\envs\xxx文件夹，还有Anaconda3\pkg文件夹里面的所有压缩包复制下来）；
   - 将旧环境打包的压缩文件复制到新机器，解压到Anaconda3\envs\文件夹下，然后，将pkg的压缩包解压缩到新机器的pkg文件夹下，至此，迁移完成；<br><br>
   
2. ubuntu安装pypy：

   ```shell
   // 安装pypy3
   // 官网http://pypy.org/下载最新的pypy版本 tar -xf pypy3-v6.0.0-linux64.tar.bz2 解压
   // 解压到对应目录下并将文件夹中的bin/添加到环境变量即可
   // 安装pip：
   $wget https://bootstrap.pypa.io/get-pip.py
   $pypy3 get-pip.py
   
   // 接下来就可以用pypy3安装东西了
   $pypy3 -m pip install requests
   
   // jupyter notebook中使用pypy：
   $pypy3 -m pip install ipykernel
   $pypy3 -m ipykernel install --user --name pypy3 --display-name "Python (PyPy)" 
   
   // 至此，在随便一个地方打开jupyter notebook，New那里就有pypy这个选项了。
   ```

   <br><br>

3. pypy3安装falcon,并使用asgi

   ```
   $pypy3 -m pip install falcon uvicorn
   
   //这时候，会在pypy3的根目录的bin下，有uvicorn可执行文件，但是falcon不是最新的，执行asgi项目会报错，这时：
   $git clone https://github.com/falconry/falcon.git
   
   // 克隆下来最新的falcon，并在项目文件夹下找到同名的falcon文件夹，然后，删除pypy3根目录/site-packages下的falcon文件夹，将git克隆下来的复制到pypy3根目录/site-packages下
   //执行falcon的asgi项目：
   $unicorn main:app   // 这个命令是在main.py文件相同的目录下执行
   ```

   至此，安装完毕；<br><br>

4. uvicorn在docker容器内要用`--host '0.0.0.0' `来指定host，不然访问不了；<br><br>

5. 

