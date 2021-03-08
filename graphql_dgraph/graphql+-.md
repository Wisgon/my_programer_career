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

9. 每个RDF N-QURD格式的数据格式如下：

   ```
   <subject> <predicate> <object> .
   ```

   其中，subject是这个对象的名字，predicate是对象的所属属性，object是具体的值，例如：

   ```
   <0x01> <name> "Alice" .
   _:u <age> 32 .
   ```

   name和age这两个predicate分别代表名字和年龄，在schema中定义；<br><br>

10. @filter不仅可以用在查询体中的对象筛选，而且可以一开始就在root下用：

    ```
    {
      bladerunner(func: anyofterms(name@en, "Blade Runner")) @filter(le(initial_release_date, "2000")) { # 这里直接在root下用
        uid
        name@en
        initial_release_date
        netflix_id
        
        director.film @filter(le(initial_release_date, "2000")) { # 这里在查询体里用 
          name@en
          initial_release_date
        }
      }
    }
    ```

    <br><br>

11. `eq`, `ge`, `gt`, `le`, `lt`  这几个函数在func中只能在index了的字段上使用，但是在@filter中，可以对未index的字段也可以用；<br><br>

12. 对整数，浮点数等做index，可以加快该字段的搜索速度，但是不像string那样，不同的index有不同的搜索方法；

    <br><br>
    
13. 设置type：

    ```
    {
      set{
       <0x4e23> <dgraph.type> "Role" .
      }
    }
    ```

    <br><br>

14. 一个node只有设置了type，才可以被`<0xxxx> * * .`这样的方式给delete掉！！！<br><br>

15. 如果删除一个node用`<0xyyy> * * .`，那么，连接这个node的另外一个node，仍然会保持连接，只是连接到了空node，如：我有一个User的type的node，名为x，x.roles 指向<0x1>，<0x2>这两个role的node，如果我执行`delete{<0x2> * * .}`，那么，<0x2>会变成空node，但读取x的时候，仍会读取到<0x2>，虽然已经是空node，这时候，删除就不是这样简单删除了，例子如下：

    ```
    upsert{
        query{
    		find_nodes(func: uid(0x4e22)){
    			~roles{
    				linked_uid as uid
    			}
    		}
    	}
    
    	mutation{
    		delete{
    			uid(linked_uid) <roles> <0x4e22> .
          		<0x4e22> * * .
    		}
    	}
    }
    ```

    要用upsert删除，先查到这个node连接的所有其他node的uid，然后将这些node的指向要删除的node的predicate删除，这样就ok了；<br><br>

16. 第15条是user下面有role，而要删除role的情况，如果要删除user，则直接删除，即使user的role有`@reverse`的directive，也直接删除就好，role的`~roles`查询也会查不到这个user了<br><br>

17. 当docker挂载/dgraph文件夹时，如：`-v /d/dgraph_data:/dgraph` 则在宿主机电脑的/d/dgraph_data下，存在4个文件夹：`p`, `w`,`zw`,`t`，其中，p文件夹是主要储存数据的，w文件夹是每一个dgraph实例都不同的，如果删除了一个container，再创建另外一个或者有时候重启container时，挂载的还是`-v /d/dgraph_data:/dgraph`文件夹，则新建的容器启动时或旧容器重启时会报错，所以想要重新创建的容器还拥有以前的数据，则要将w文件夹删掉，重新create容器时会自动创建新的w文件夹；<br><br>

18. The `/alter` endpoint is used to create or change the schema. Here, the predicate `name` is the name of an account. It’s indexed so that we can look up accounts based on their name.

    ```sh
    $ curl -X POST localhost:8080/alter -d \
    'name: string @index(term) .
    type Person {
       name
    }'
    ```
    

    If all goes well, the response should be `{"code":"Success","message":"Done"}`.

    Other operations can be performed via the `/alter` endpoint as well. A specific predicate or the entire database can be dropped.

    To drop the predicate `name`:
    
    ```sh
    $ curl -X POST localhost:8080/alter -d '{"drop_attr": "name"}'
    ```

    To drop the type `Film`:
    
    ```sh
    $ curl -X POST localhost:8080/alter -d '{"drop_op": "TYPE", "drop_value": "Film"}'
    ```
    
    To drop all data and schema:

	```sh
    $ curl -X POST localhost:8080/alter -d '{"drop_all": true}'
	```

    To drop all data only (keep schema):
    
    ```sh
	$ curl -X POST localhost:8080/alter -d '{"drop_op": "DATA"}'
    ```

    用curl来实现临时更改比较方便，直接docker exec -it dgraph_name /bin/bash 进去就可以用curl；
    
    <br><br>

19. variable的使用讲求level，只能在变量定义的下一级使用，如：

    ```
    {
    	q(func: type(xxx)) {
    		device {
    			warning{
    				ct as create_time
    			}
    			get_max: max(val(ct)) # 这里使用ct这个变量就不会报错，因为只能在ct的上一级使用，上两级就不行了
    		}
    		# get_max: max(val(ct))  这里使用会报错，level问题
    	}
    }
    ```

    <br><br>

20. condition upsert中，condition只能用len，而不能用val，如：

    ```
    upsert{
      query{
        q(func:uid(0xc352)){
          pd as password
        }
      }
      
      mutation @if(eq(val(pd), "123456")) {
        set{
          <0xc352> <password> "222222" .
        }
      }
    }
    ```

    是错的，虽然执行成功但不会有修改，要改成：

    ```
    upsert{
      query{
        v as var(func:uid(0xc352)) @filter(eq(password, "123456")) {
          password
        }
      }
      
      mutation @if(eq(len(v), 1) {
        set{
          <0xc352> <password> "222222" .
        }
      }
    }
    ```

    才行；<br><br>

21. 

