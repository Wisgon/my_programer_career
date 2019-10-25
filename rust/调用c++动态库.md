###首先，做到可以成功加载sdk
1. 首先遇到的是sdk包里面的c++动态库的放置位置问题，出现：`/usr/bin/ld: 找不到 -lhcnetsdk`的提示，意思是找不到这个so文件，解决方法：用build.rs来限制搜索包的目录；<br><br>

2. 然后，没有上面的错误提示了，但是，提示target/debug找不到包，解决方法：将sdk里面的全部文件复制到target/debug下面；<br><br>

3. 下面是代码结构以及部分代码：

   ```
   .
   ├── build.rs
   ├── Cargo.lock
   ├── Cargo.toml
   ├── hk_sdk(海康的sdk包)
   │   ├── .
   │   ├── .
   │   ├── .
   ├── src
   │   ├── hai_kang
   │   │   ├── mod.rs
   │   │   └── register.rs
   │   ├── lib.rs
   │   └── main.rs
   ├── target
   │   └── debug（要将hk_sdk里面的全部东西都复制过去）
   └── tests
       └── register.rs
   
   ```

   <br><br>

   Cargo.toml：

   ```rust
   [package]
   name = "jcpt_rust"
   version = "0.1.0"
   authors = ["jhd"]
   edition = "2018"
   build = "build.rs"
   
   # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
   
   [dependencies]
   libc = "0.2.9"
   
   #[lib]
   #name = "jcpt_rustlib"
   #crate-type = ["dylib"]
   ```

   <br><br>

   build.rs:

   ```rust
   fn main() {
       println!("cargo:rustc-link-search=native=./hk_sdk");
       println!("cargo:rustc-link-lib=dylib=hcnetsdk");
       println!("cargo:root = /home/jhd/Documents/jhd_projects/jcpt_rust/");
   }
   ```

   <br><br>

###然后，将c++的数据结构和rust的互相转换，用到"rust-bindgen"库

1. 使用自定义的头文件 #include指示接受以下两种形式：
   ` #include<iostream>` 
   `#include"query.h"` 
   如果头文件名括在尖括号< >里，那么认为该头文件是标准头文件。编译器会在预定义的位置集查找该头文件，这些预定义的位置可以通过设置查找路径环境变量或者通过命令行选项来修改。如果头文件名括在一对引号里，那么认为它是非系统头文件，非系统头文件的查找通常开始于源文件所在的路径；<br><br>

2. 对目录进行重构，现在的结构如下：

   ```
   .
   ├── build.rs
   ├── Cargo.lock
   ├── Cargo.toml
   ├── hk_pkg
   │   ├── build.rs
   │   ├── Cargo.lock
   │   ├── Cargo.toml
   │   ├── HCNetSDK.h
   │   ├── hk_sdk
   │   │   ├── .
   │   │   ├── .
   │   │   ├── .
   │   ├── src
   │   │   ├── bindings.rs
   │   │   ├── lib.rs
   │   │   └── register.rs
   │   ├── target
   │   │   └── debug
   │   └── wrapper.hpp
   ├── src
   │   └── main.rs
   ├── target
   │   └── debug
   │       ├── .
   │       ├── .
   │       ├── .
   └── tests
       └── register.rs
   
   
   ```

   hk_pkg作为海康sdk的rust package，里面定义rust化的接口函数，被主程序main.rs及tests模块引用，HCNetSDK.h是海康提供的sdk的头文件，warpper.hpp（注意，不可以是warpper.h，因为是c++）则是将HCNetSDK.h引入进来，只有一行代码：`#include "HCNetSDK.h"`；<br><br>

3. hk_pkg/cargo.toml:

   ```rust
   [package]
   name = "hk_pkg"
   version = "0.1.0"
   authors = ["jhd <jhd@jhd.com>"]
   edition = "2018"
   build = "build.rs"
   
   # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
   
   [dependencies]
   libc = "0.2.9"
   
   [build-dependencies]
   bindgen = "0.51.0"
   
   ```

   <br><br>

   hk_pkg/build.rs:

   ```rust
   extern crate bindgen;
   
   use std::{env, path::PathBuf};
   
   fn main() {
   
       println!("cargo:rustc-link-search=native=./hk_sdk");
       println!("cargo:rustc-link-lib=dylib=hcnetsdk");
       println!("cargo:root = /home/jhd/Documents/jhd_projects/jcpt_rust/hk_pkg");
   
       // Tell cargo to invalidate the built crate whenever the wrapper changes
       println!("cargo:rerun-if-changed=wrapper.hpp");
   
       // The bindgen::Builder is the main entry point
       // to bindgen, and lets you build up options for
       // the resulting bindings.
       let bindings = bindgen::Builder::default()
           // The input header we would like to generate
           // bindings for.
           .header("wrapper.hpp")
           // Tell cargo to invalidate the built crate whenever any of the
           // included header files changed.
           //.parse_callbacks(Box::new(bindgen::CargoCallbacks))
           // Finish the builder and generate the bindings.
           .generate()
           // Unwrap the Result and panic on failure.
           .expect("Unable to generate bindings");
   
       // Write the bindings to the $OUT_DIR/bindings.rs file.
       let out_path = PathBuf::from(env::var("OUT_DIR").unwrap());
       bindings
           .write_to_file(out_path.join("bindings.rs"))
           .expect("Couldn't write bindings!");
   }
   ```

   <br><br>

   hk_pkg/src/lib.rs:只有一行：  `pub mod register;`<br><br>

4. 用"rust-bindgen"库依靠HCNetSDK.h生成“bindings.rs”，cd进hk_pkg所在文件夹，然后：`cargo build`，则bindngs.rs就在hk_pkg/target/debug/build/hk_pkg-xxxx/out/文件夹中，它就是sdk接口用到的rust对应于c++的函数，结构体等数据结构的代码；<br><br>

5. 

   