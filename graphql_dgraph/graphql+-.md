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