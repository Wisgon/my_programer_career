1. git pull 失败 ,提示：`fatal: refusing to merge unrelated histories`, 其实这个问题是因为 两个 根本不相干的 git 库， 一个是本地库， 一个是远端库， 然后本地要去推送到远端， 远端觉得这个本地库跟自己不相干， 所以告知无法合并；
   解决方法：使用这个强制的方法

   `git pull origin master --allow-unrelated-histories`

   后面加上 `--allow-unrelated-histories` ， 把两段不相干的 分支进行强行合并

   后面再push就可以了 `git push gitlab master:init`

   gitlab是别名 ;<br><br>

2. 

