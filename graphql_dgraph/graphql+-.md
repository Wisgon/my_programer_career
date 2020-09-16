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

5. 