1. jupyter notebook --ip 0.0.0.0  可生成一个token，复制这个token就可以远程访问这台主机的jupyter notebook

   当不想用token而用密码登录的话，就要配置config文件了
   首先，创建一个jupyter_config.py文件，内容如下：

   ```python
   c = get_config()
   c.NotebookApp.allow_remote_access = True
   c.IPKernelApp.pylab = 'inline'
   c.NotebookApp.ip = '*'
   c.NotebookApp.open_browser = False
   c.NotebookApp.password= 'sha1:11dc98ddb41e:cd0c5f4a4313a5b9a7e33cf1a1e8dca2d5cd4d14'
   c.NotebookApp.port = 6789
   c.NotebookApp.notebook_dir= '/home/jhd/sda1/Documents/teacher/student_exercise/'
   ```

   其中，password可以在命令行中输入jupyter notebook password，然后查看用户根目录下的.jupyter文件夹里面的jupyter_notebook_config.json看到，然后黏贴过去就好，而notebook_dir就是jupyter进入时的文件夹路径

   编辑完成后，
   运行jupyter note book --config ./jupyter_note_book_config.py &
   即可<br><br>

2. jupyter notebook效率插件安装：
   `pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install`

<br><br>

3. 在编辑模式，函数括号中，按下shift+tab键，可以看到这个函数的简要说明<br><br>

4. jupyter-lab安装命令：

   ```
   pip install jupyterlab
   conda install xeus-python -c conda-forge  # 这个装了才能debug
   ```

   <br><br>