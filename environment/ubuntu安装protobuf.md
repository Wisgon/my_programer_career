```
$git clone https://github.com/protocolbuffers/protobuf.git
$apt-get update
$apt-get install autoconf automake libtool curl make g++ unzip libffi-devc
$cd protobuf/
$./autogen.sh
$./configure
$make
$make install
$ldconfig
$ protoc -h // 如果有东西出来，那就表示安装成功
```

