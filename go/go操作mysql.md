# [Go语言之操作数据库CRUD](https://www.cnblogs.com/yh2924/p/12395941.html)

### 原生mysql driver

```go
  1 package main
  2 
  3 import (
  4     "database/sql"
  5     "fmt"
  6     _ "github.com/go-sql-driver/mysql"
  7 )
  8 
  9 // 定义一个全局对象db
 10 var db *sql.DB
 11 //定义结构体
 12 type User struct {
 13     Id   int
 14     Name string
 15     Age  int
 16 }
 17 
 18 //初始化数据库
 19 func InitDB() (err error) {
 20     //连接数据库
 21     dsn := "root:root@tcp(127.0.0.1:3306)/db3"
 22     db, err = sql.Open("mysql", dsn)
 23     //错误处理
 24     if err != nil {
 25         return err
 26     }
 27     //检验dsn是否正确
 28     err = db.Ping()
 29     if err != nil {
 30         return err
 31     }
 32     return nil
 33 }
 34 
 35 //数据库单行查询
 36 func queryRowDemo() {
 37     //创建User对象
 38     var u User
 39     //sql语句
 40     sqlStr := "select * from user where id=?"
 41     //调用QueryRow方法返回查询的一行，后边调用的scan方法是将查询出来的行放入指定的参数中
 42     err := db.QueryRow(sqlStr, 1).Scan(&u.Id, &u.Name, &u.Age)
 43     if err != nil {
 44         fmt.Println(err)
 45         return
 46     }
 47     fmt.Println(u.Id, u.Name, u.Age)
 48 }
 49 
 50 //查询多行
 51 /*
 52 查询多行和查询单行的不同之处是调用方法query并返回多行
 53 然后通过for循环调用scan方法吧每一行循环遍历出来
 54 */
 55 func queryDemo() {
 56     //sql语句
 57     sqlStr := "select * from user"
 58     //调用方法
 59     rows, err := db.Query(sqlStr)
 60     //错误处理
 61     if err != nil {
 62         fmt.Println(err)
 63     }
 64     //关闭rows释放持有的数据库链接
 65     defer rows.Close()
 66     //使用for循环进行结果的读取
 67     for rows.Next() {
 68         var u User
 69         err := rows.Scan(&u.Id, &u.Name, &u.Age)
 70         if err != nil {
 71             fmt.Println(err)
 72         }
 73         fmt.Printf("id:%d name:%s age:%d\n", u.Id, u.Name, u.Age)
 74     }
 75 }
 76 
 77 //插入数据
 78 func InsertDemo() {
 79     //sql语句
 80     sqlStr := "insert into user(name,age) value(?,?)"
 81     //Exec执行一次命令（包括查询、删除、更新、插入等），返回的Result是对已执行的SQL命令的总结。参数args表示query中的占位参数
 82     ret, err := db.Exec(sqlStr, "赵六", 30)
 83     if err != nil {
 84         fmt.Println(err)
 85         return
 86     }
 87     fmt.Println(ret)
 88     // 新插入数据的id是theID
 89     theID, err := ret.LastInsertId()
 90     if err != nil {
 91         fmt.Printf("get lastinsert ID failed, err:%v\n", err)
 92         return
 93     }
 94     fmt.Printf("insert success, the id is %d.\n", theID)
 95 }
 96 
 97 //更新数据
 98 func UpdateDemo() {
 99     sqlStr := "update user set age=? where id =?"
100     ret, err := db.Exec(sqlStr, 39, 3)
101     if err != nil {
102         fmt.Printf("update failed, err:%v\n", err)
103         return
104     }
105     n, err := ret.RowsAffected() // 操作影响的行数
106     if err != nil {
107         fmt.Printf("get RowsAffected failed, err:%v\n", err)
108         return
109     }
110     fmt.Printf("update success, affected rows:%d\n", n)
111 }
112 
113 //删除数据
114 func DeleteDemo() {
115     sqlStr := "delete from user where id=?"
116     ret, err := db.Exec(sqlStr, 4)
117     if err != nil {
118         fmt.Println(err)
119         return
120     }
121     n, err := ret.RowsAffected()
122     if err != nil {
123         fmt.Printf("get RowsAffected failed, err:%v\n", err)
124         return
125     }
126     fmt.Printf("delete success, affected rows:%d\n", n)
127 
128 }
129 func main() {
130     //调用初始化函数
131     err := InitDB()
132     if err != nil {
133         fmt.Println(err)
134     }
135     //调用函数
136     //queryRowDemo()
137     //queryDemo()
138     //InsertDemo()
139     //UpdateDemo()
140     //DeleteDemo()
141 }
```



 sql预处理：

优化MySQL服务器重复执行SQL的方法，可以提升服务器性能，提前让服务器编译，一次编译多次执行，节省后续编译的成本。

避免SQL注入问题。

查询的sql预处理代码：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```go
 1 //预处理
 2 func prepareSql() {
 3     var u User
 4     sqlStr := "select * from user"
 5     stmt, err := db.Prepare(sqlStr)
 6     if err != nil {
 7         fmt.Println(err)
 8         return
 9     }
10     defer stmt.Close()
11     rows, err := stmt.Query()
12     if err != nil {
13         fmt.Println(err)
14         return
15     }
16     defer rows.Close()
17     for rows.Next() {
18         err := rows.Scan(&u.Id, &u.Name, &u.Age)
19         if err != nil {
20             fmt.Println(err)
21             return
22         }
23         fmt.Println(u.Id, u.Name, u.Age)
24     }
25 }
```



事务：

　　比如，我们去银行转账，操作可以分为下面两个环节：(1)从第一个账户划出款项。 (2)将款项存入第二个账户。 

　　在这个过程中，两个环节是关联的。第一个账户划出款项必须保证正确的存入第二个账户，如果第二个环节没有完成，整个的过程都应该取消，否则就会发生丢失款项的问题。整个交易过程，可以看作是一个事物，成功则全部成功，失败则需要全部撤消，这样可以避免当操作的中间环节出现问题时，产生数据不一致的问题。

事务的特性：

| 原子性 | 一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。 |
| ------ | ------------------------------------------------------------ |
| 一致性 | 在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。 |
| 隔离性 | 数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。 |
| 持久性 | 事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。 |

举例：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```go
 1 func transactionDemo() {
 2     //事务分为 开始事务 提交事务和回滚事务
 3     //开始事务 当开始一个事务后需要用事务进行操作
 4     tx, err := db.Begin()
 5     //出错了 如果有错误就需要进行事务的回滚
 6     if err != nil {
 7         if tx != nil {
 8             tx.Rollback()
 9         }
10         return
11     }
12 
13     sqlStr := "update user set age=100 where id=?"
14     _, err = tx.Exec(sqlStr, 1)
15     if err != nil {
16         fmt.Println(err)
17         tx.Rollback()
18         return
19     }
20 
21     sqlStr1 := "update user set age=101 where id=?"
22     _, err = tx.Exec(sqlStr1, 2)
23     if err != nil {
24         fmt.Println(err)
25         tx.Rollback()
26         return
27     }
28     //事务提交
29     err=tx.Commit()
30     if err!=nil{
31         tx.Rollback()
32         return
33     }
34 
35 }
```

<br><br><br>

### 第三方库sqlx

```go
package main

// 数据库连接初始化
import (
	"fmt"

	_ "github.com/go-sql-driver/mysql" // mysql
	"github.com/jmoiron/sqlx"
)

// DB 数据库模型
var DB *sqlx.DB

const dsn = "go_mysql_demo:root123456@tcp(127.0.0.1:3306)/go_mysql_demo"

type user struct {
	ID   int    `json:"id" db:"id"`
	Name string `json:"name" db:"name"`
	Age  int    `json:"age" db:"age"`
}

// connect 1.连接数据库
func connect() (db *sqlx.DB, err error) {
	db, err = sqlx.Connect("mysql", dsn)
	db.SetMaxOpenConns(100) // 设置连接池最大连接数
	db.SetMaxIdleConns(20)  // 设置连接池最大空闲连接数
	DB = db
	if err != nil {
		fmt.Println("数据库连接失败==>", err)
	}
	fmt.Println("数据库已连接！")
	return
}

// 添加数据 Exec、MustExec
// MustExec遇到错误的时候直接抛出一个panic错误，程序就退出了；
// Exec是将错误和执行结果一起返回，由我们自己处理错误。 推荐使用！
func createUser() {
	// 创建表
	sql := `
        CREATE TABLE user  (
            id bigint(20) NOT NULL AUTO_INCREMENT,
            name varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
            age int(11) NULL DEFAULT 0,
            PRIMARY KEY (id) USING BTREE
        ) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact
    `
	_, err := DB.Exec(sql)
	fmt.Println(err)
}

// 添加数据
func insertUser() {
	sql := `insert into user (name, age) values ("lgx",18)`
	res := DB.MustExec(sql)
	fmt.Println(res.LastInsertId)
	fmt.Println(res.RowsAffected)
}

// 更新数据
func updateUser() {
	sql := `update user set name = ?, age = ? where id = ?`
	res, err := DB.Exec(sql, "LGX", 28, 20)
	fmt.Println(err, res)
}

// Get、QueryRowx: 查询一条数据
// QueryRowx可以指定到不同的数据类型中
func getNum() {
	var num int
	_ = DB.Get(&num, "select count(*) from user")
	fmt.Printf("数据库一共有：%d 个用户\n", num)
	var u user
	_ = DB.Get(&u, "select name, id, age from user where id = ?", 20)
	fmt.Printf("查找用户id==1的用户:%v \n", u)
}

// Select、Queryx：查询多条数据
// Queryx可以指定到不同的数据类型中
func getAll() {
	sql := `select id, name ,age from user where id > 1`
	var us []user
	err := DB.Select(&us, sql)
	fmt.Println(err, us)
}

// 删除
func deleteUser() {
	sql := `delete from user where id = 20`
	_, _ = DB.Exec(sql)
}

// 事务处理
func events() {
	tx, _ := DB.Beginx()
	_, err1 := tx.Exec("update user set age = 10 where id = 20")
	_, err2 := tx.Exec("update user set age = 10 where id = 21")
	fmt.Println(err1, err2)
	if err1 != nil || err2 != nil {
		tx.Rollback()
	}
	tx.Commit()
}

func main() {
	db, _ := connect()
	defer db.Close()
	// 建表
	createUser()
	// 添加数据
	insertUser()
	// 修改数据
	// updateUser()
	// 查数据-Get
	// getNum()
	// 查数据-Select
	// getAll()
	// 事务
	events()
}

```

