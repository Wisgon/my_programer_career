### graphql+-学习

1. 使用多个条件，每个条件间用空格就行：

   ```
   {
     michael_friends_and(func: allofterms(name@., "Michael")) {
       name
       age
       #比如下面的需要filter并且要排序orderasc，只要空格开就行
       friend @filter(ge(age, 27) AND le(age, 48)) (orderasc: age){
         name@.
         age
       }
     }
   }
   ```

   <br><br>

2. 使用@cascade来排除下一级中，没有全部满足字段的node：

   ```
   {
     michael_friends_with_pets(func: allofterms(name@., "Michael")) @cascade {
       name
       age
       friend {
         name@.
         owns_pet  #由于上面有@cascade，所以没有owns_pet字段的friend将会被排除，如果没有@cascade，则只要是friend就会搜出来，只是这个字段没有值而已
       }
     }
   }
   ```

   <br><br>
   
3. 使用`dgraph.type`可获得类型：

   ```
   {
     q(func: has(<name>)) {
         <name>
       dgraph.type
     }
   }
   ```

   <br><br>

4. upsert block 中，query只能有一个，但是可以有多个子query，mutation则可以有多个：

   ```
   upsert {
     query {
     # 第一个子query
       q(func: eq(email, "user@company1.io")) {
         v as uid
         name
       }
       
       #第二个子query
       q2(func: eq(email, "ddd@company.co")) {
          v2 as uid
       }
     }
   	
   	# 第一个mutation
     mutation {  
       set {
         uid(v) <name> "user" .
         uid(v) <email> "user@company2.io" .
       }
     }
     
     # 第二个mutation
     mutation {
       set {
         uid(v2) <name> "ddd" .
       }
     }
   }
   ```
   
   <br><br>

5. 在docker中自己自行安装，而非官方下载的docker镜像安装，有可能安装后，设置schema的时候出现`unauthorized ip address: 172.17.0.1`报错，也就是未将172.17.0.1这个docker主机ip认证成功，解决方法是，在启动alpha时添加--whitelist参数：`/usr/local/bin/dgraph alpha --whitelist 172.17.0.1 --lru_mb 2048`；<br><br>

6. ```
   <0x01> <age> "32"^^<xs:int> .
   <0x01> <birthdate> "1985-06-08"^^<xs:dateTime> .
   ```

   像这样声明类型的写法，只适合还没有创建这个age和birthdate字段的时候使用，如果已创建，说明已确定类型，则不能这么写，应该去掉"^^"及后面的类型；<br><br>

7. dgraph中，要用`delete{ <0x5465> * * . }` 的语法删除一个node，这个node必须要有一个type才行！！！<br><br>

8. 当删除一个node之后，这个node的id会被保留，不会有什么影响，不用管它；<br><br>

9. 