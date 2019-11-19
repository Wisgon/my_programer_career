# 将现有项目添加到git的方法

比如，现在有个xproject文件夹没有上git，将其用上git的方法如下：

- 首先，在git服务器中：

  ```shell
  mkdir /git
  cd /git
  git init --bare xproject.git
  ```

- 然后，在xproject所在机器上：

  ```shell
  cd xxx/xproject
  git init
  vim .gitignore
  git add *
  git commit -m "init"
  git remote add origin root@xxx.xxx.xxx.xxx:/git/xproject
  git push -u origin master
  ```

  注意：root是远程的创建了xproject.git的账户名称，xxx.xxx.xxx.xxx是远程ip；

- 这时，就可以`git clone root@xxx.xxx.xxx.xxx:/git/xproject`了；

