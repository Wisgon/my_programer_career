###Gin项目目录结构
```css
├── gin
│   ├──  Router
│          └── router.go
│   ├──  Middlewares
│          └── corsMiddleware.go
│   ├──  Controllers
│          └── testController.go
│   ├──  Services
│          └── testService.go
│   ├──  Models
│          └── testModel.go
│   ├──  Databases
│          └── mysql.go
│   ├──  Sessions
│          └── session.go
└── main.go
```

> - **使用gorm访问数据库**
> -  **gin** 为项目根目录
> -  **main.go** 为入口文件
> -  **Router** 为路由目录
> -  **Middlewares** 为中间件目录
> -  **Controllers** 为控制器目录（MVC）
> -  **Services** 为服务层目录，这里把DAO逻辑也写入其中，如果分开也可以
> -  **Models** 为模型目录
> -  **Databases** 为数据库初始化目录
> -  **Sessions** 为session初始化目录
> - 文件 **引用顺序** 大致如下：
>    main.go(在main中关闭数据库) - router(Middlewares) - Controllers - Services(sessions) - Models - Databases

- **Databases / mysql**



```go
package Mysql

import (
    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
    "fmt"
)

var DB *gorm.DB

func init()  {
    var err error
    DB, err = gorm.Open("mysql", "wuyu:MIDSUMMERfish0@/gin?charset=utf8&parseTime=True&loc=Local")
    if err != nil {
        fmt.Printf("mysql connect error %v", err)
    }
    if DB.Error != nil {
        fmt.Printf("database error %v", DB.Error)
    }
}
```

- **Models / testModel.go**



```go
package Models

import (
    "gin/Databases"
)

type Test struct {
    Id int
    Testcol string `gorm:"column:testcol"`
}

// 设置Test的表名为`test`
// func (Test) TableName() string {
//     return "test"
// }

func (this *Test) Insert() (id int, err error) {
    result := Mysql.DB.Create(&this)
    id = this.Id
    if result.Error != nil {
        err = result.Error
        return
    }
    return
}
```

- **Services / testService.go**



```go
package Services

import (
    "gin/Models"
)

type Test struct {
    Id int `json:"id"` 
    Testcol string `json:"testcol"`
}

func (this *Test) Insert() (id int, err error) {
    var testModel Models.Test
    testModel.Id = this.Id
    testModel.Testcol = this.Testcol
    id, err = testModel.Insert()
    return
}
```

- **Controllers / testController.go**



```swift
package Controllers

import (
    "github.com/gin-gonic/gin"
    "net/http"
    "strconv"
    "fmt"
    "gin/Services"
)

func TestInsert(c *gin.Context) {
    var testService Services.Test

    err := c.ShouldBindJSON(&testService)
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }

    id, err := testService.Insert()
    if err != nil {
        c.JSON(http.StatusOK, gin.H{
            "code": -1,
            "message": "Insert() error!",
        })
        return
    }
    c.JSON(http.StatusOK, gin.H{
        "code": 1,
        "message": "success",
        "data": id,
    })

}
```

- **Router / router.go**



```go
package Router

import (
    "github.com/gin-gonic/gin"
    "gin/Controllers"
    "gin/Middlewares"
    "gin/Sessions"
    "github.com/gin-contrib/sessions"
)

func InitRouter() {
    router := gin.Default()
    // 要在路由组之前全局使用「跨域中间件」, 否则OPTIONS会返回404
    router.Use(Middlewares.Cors())
    // 使用 session(cookie-based)
    router.Use(sessions.Sessions("myyyyysession", Sessions.Store))
    v1 := router.Group("v1")
    {
         v1.POST("/testinsert", Controllers.TestInsert)
    }
    
    router.Run(":8080")
}
```

- **Middlewares / corsMiddleware.go**



```swift
package Middlewares

import (
    "github.com/gin-gonic/gin"
    "net/http"
)
// 跨域中间件
func Cors() gin.HandlerFunc {
    return func(c *gin.Context) {
        method := c.Request.Method
        origin := c.Request.Header.Get("Origin")
        if origin != "" {
            c.Header("Access-Control-Allow-Origin", origin)
            c.Header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE, UPDATE")
            c.Header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Authorization")
            c.Header("Access-Control-Expose-Headers", "Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Cache-Control, Content-Language, Content-Type")
            c.Header("Access-Control-Allow-Credentials", "false")
            c.Set("content-type", "application/json")
        }
        if method == "OPTIONS" {
            c.AbortWithStatus(http.StatusNoContent)
        }
        c.Next()
    }
}
```

- **Sessions/session.go**



```go
package Sessions

import (
    "github.com/gin-contrib/sessions"
    "github.com/gin-contrib/sessions/cookie"
    "github.com/gin-gonic/gin"
    "time"
    "strconv"
)

var Store = cookie.NewStore([]byte("very-very-secret"))

func SetSession(c *gin.Context, username string) string {
    session := sessions.Default(c)
    sessionId := "sessionIdxxxxxxxok"
    session.Set(sessionId, username)
    session.Save()
    return sessionId
}

func GetSession(c *gin.Context, sessionId string) (username string) {
    session := sessions.Default(c)
    result := session.Get(sessionId)
    username = result.(string)
    return
}
```

- **main.go**



```go
package main

import (
    "gin/Router"
    "gin/Databases"
)

func main() {
    defer Mysql.DB.Close()
    Router.InitRouter()
}
```