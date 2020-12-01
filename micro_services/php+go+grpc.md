### 环境配置：

##### 安装php的grpc环境

1. 安装好宝塔，然后安装php7.2，搞定之后，在宝塔面板，选择php，点进去，在禁用函数那一栏，选中函数名，点删除，就可解除禁用，要解除禁用的函数为：`popen()`, `putenv()`, `exec()`, `proc_open()`,`pcntl_signal()`，解禁这几个函数，就可以使用perl了，否则，使用perl时会出现`failed to run phpize`的错误；

2. 执行命令：`sudo pecl install grpc`；

3. 修改php.ini，加上：`extension=grpc.so`

4. Add the gRPC PHP library as a Composer dependency

   You need to add this to your project’s `composer.json` file.

   ```json
     "require": {
       "grpc/grpc": "v1.7.0",
       "google/protobuf": "^v3.3.0"
     }
   ```

5. #### Install Protobuf compiler

   ```shell
   $ git clone https://github.com/grpc/grpc.git
   $ cd grpc/
   $ git submodule update --init
   $ cd third_party/protobuf
   $ ./autogen.sh && ./configure && make
   $ sudo make install
   ```

6. Protobuf Runtime library: `$ sudo pecl install protobuf`;

7. 修改php.ini，加上：`extension=protobuf.so`

8. PHP Protoc Plugin: cd到根目录grpc，执行`$ make grpc_php_plugin`，会生成./bins/opt/grpc_php_plugin，可以把它复制到/usr/bin/目录下，供以后protoc方便使用;

9. 到此，就可以运行example了；<br><br>

##### 安装go的grpc环境

前面已经安装好了protoc，这里就不必再重新安装

1. `$ go get github.com/golang/protobuf/protoc-gen-go`;

2. `$ export PATH="$PATH:$(go env GOPATH)/bin"`;  这一步就算装好了环境了，以下只是测试实例

3. ```
   $ cd grpc-go/examples/helloworld
   $ go run greeter_server/main.go
   $ go run greeter_client/main.go
   // 要run以下example，才能在grpc-go/cmd/目录下生成对应的二进制文件
   ```

4. update了helloworld.proto后，

   ```shell
   $ ( cd ../../cmd/protoc-gen-go-grpc && go install . )
   $ protoc \
     --go_out=Mgrpc/service_config/service_config.proto=/internal/proto/grpc_service_config:. \
     --go-grpc_out=Mgrpc/service_config/service_config.proto=/internal/proto/grpc_service_config:. \
     --go_opt=paths=source_relative \
     --go-grpc_opt=paths=source_relative \
     helloworld/helloworld.proto
   ```

5. 修改greeter_server/main.go，greeter_client/main.go再次运行，就可以看到修改的结果了；



### 具体实例

##### go作为grpc服务端

- 编写hello_php.proto:

  ```protobuf
  syntax = "proto3";
  
  option objc_class_prefix = "HLW";
  
  package demoserver;
  
  // The greeting service definition.
  service Greeter {
    // Sends a greeting
    rpc SayHello (HelloRequest) returns (HelloReply) {}
    rpc SayHelloAgain (HelloRequest) returns (HelloReply) {}
  }
  
  // The request message containing the user's name.
  message HelloRequest {
    string name = 1;
  }
  
  // The response message containing the greetings
  message HelloReply {
    string message = 1;
  }
  
  ```

- 执行命令：`$protoc --go_out=plugins=grpc:./your_path_store_out_file ./your_path_to_protofile/hello_php.proto`，会在`./your_path_store_out_file`下生成“hello_php.pb.go“；

- `./your_path_store_out_file/demo_server.go`如下所示，然后，在main.go中，调用StartServer()即可：

  ```go
  package demoserver
  
  import (
  	"context"
  	"log"
  	"net"
  
  	"google.golang.org/grpc"
  )
  
  const (
  	port = ":9321"
  )
  
  // server is used to implement helloworld.GreeterServer.
  type server struct {
  	UnimplementedGreeterServer
  }
  
  // SayHello implements helloworld.GreeterServer
  func (s *server) SayHello(ctx context.Context, in *HelloRequest) (*HelloReply, error) {
  	log.Printf("Received: %v", in.GetName())
  	return &HelloReply{Message: "Hello " + in.GetName()}, nil
  }
  
  func (s *server) SayHelloAgain(ctx context.Context, in *HelloRequest) (*HelloReply, error) {
  	return &HelloReply{Message: "Hello again " + in.GetName()}, nil
  }
  
  func StartServer() {
  	lis, err := net.Listen("tcp", port)
  	if err != nil {
  		log.Fatalf("failed to listen: %v", err)
  	}
  	s := grpc.NewServer()
  	RegisterGreeterServer(s, &server{})
  	log.Println("serving port " + port)
  	if err := s.Serve(lis); err != nil {
  		log.Fatalf("failed to serve: %v", err)
  	}
  }
  
  ```

  <br>

#### php客户端

- 复制hello_php.proto，放到项目根目录的app/micro_client/目录下；

- cd到micro_client/proto_gen目录下，执行:

  ```shell
  protoc --proto_path=../proto_files/ --grpc_out=. --php_out=. --plugin=protoc-gen-grpc=/usr/bin/grpc_php_plugin ../proto_files/hello_php.proto
  ```

- composer.json中，"autoload"的"psr-4"修改如下：

  ```json
  "psr-4": {
              "app\\": "app",
              "crmeb\\": "crmeb",
              "Demoserver\\": "app/microclient/proto_gen/Demoserver/",
              "GPBMetadata\\": "app/microclient/proto_gen/GPBMetadata/"
          },
  ```

- 根目录下，执行：

  ```shell
  $composer install
  $composer require grpc/grpc
  ```

  记得如果路径或文件有更新，那要在composer.json里的"psr-4"字段那里改一下，改完再执行`composer install`即可；

- microclient/test_demo_server.php：

  ```php
  <?php
  
  require __DIR__ . '/../../vendor/autoload.php';
  
  
  function greet($hostname, $name)
  {
      $client = new \Demoserver\GreeterClient($hostname, [
          'credentials' => \Grpc\ChannelCredentials::createInsecure(),
      ]);
      $request = new \Demoserver\HelloRequest();
      $request->setName($name);
      list($reply, $status) = $client->SayHello($request)->wait();
      $message = $reply->getMessage();
      list($reply, $status) = $client->SayHelloAgain($request)->wait();
      $message = $reply->getMessage();
      if ($status->code !== \Grpc\STATUS_OK) {
          echo "ERROR: " . $status->code . ", " . $status->details . PHP_EOL;
          exit(1);
      }
      echo $reply->getMessage() . PHP_EOL;
  }
  
  $name = !empty($argv[1]) ? $argv[1] : 'world';
  $hostname = !empty($argv[2]) ? $argv[2] : 'localhost:9321';
  greet($hostname, $name);
  
  ```

  运行命令：`php test_demo_server.php，可看到输出：Hello again world；



