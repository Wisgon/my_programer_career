1. .proto文件中，指定的package必须是该proto文件所在的package名字；<br><br>

2. 安装protoc：ubuntu下直接` apt install protobuf-compiler `;<br><br>

3. protoc3中的字段规则：

   - singular关键字，是默认的，只能重复0次或1次，不能加在字段前，否则报错，如：

     ```
     message XXX {
         singular int32 aaa = 1;  // 会报错，因为aaa已经就是默认singular了
     }
     ```

   - repeated关键字，可以重复一次或以上，也就是一定要有，有required的性质：

     ```
     message XXX {
     	repeated int32 bbb = 1;
     }
     ```

     使用的时候，一般会有个add_bbb的方法，然后调用就可以，就像数组一样用；

