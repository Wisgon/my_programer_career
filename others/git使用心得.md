1. git pull 失败 ,提示：`fatal: refusing to merge unrelated histories`, 其实这个问题是因为 两个 根本不相干的 git 库， 一个是本地库， 一个是远端库， 然后本地要去推送到远端， 远端觉得这个本地库跟自己不相干， 所以告知无法合并；
   解决方法：使用这个强制的方法

   `git pull origin master --allow-unrelated-histories`

   后面加上 `--allow-unrelated-histories` ， 把两段不相干的 分支进行强行合并

   后面再push就可以了 `git push gitlab master:init`

   gitlab是别名 ;<br><br>

2. git要放弃对某个文件的修改，只要执行命令： `git checkout filename.txt`就好<br><br>

3. gitignore不生效解决办法：有时候在项目开发过程中，突然心血来潮想把某些目录或文件加入忽略规则，按照上述方法定义后发现并未生效，原因是.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。那么解决方法就是先把本地缓存删除（改变成未track状态），然后再提交：

   ```
   git rm -r --cached .
   git add .
   git commit -m 'update .gitignore'
   ```

   <br><br>

4. 

