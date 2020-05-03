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



# 远程库已删，用本地库来恢复远程库

- 首先，在git服务器中，执行：`git init --bare xxx.git`;
- 然后，回到已克隆下来的本地的xxx目录下，看看.git文件夹中的config文件中的url对不对得上新的xxx.git的url，如果对不上，则修改config中的url；
- 随后，在本地的xxx根目录下，打开git命令行，执行：` git push origin master --force `，具体是master还是其他分支，都可以改成对应的分支名，这样强制push上去之后，刚生成的xxx.git就是跟原来被删的一样了；


