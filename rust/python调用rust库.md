1. demo:

   - `cargo new handle --lib`

   - 编辑handle/Cargo.toml：

     ```shell
     [package]
     name = "handle"
     version = "0.1.0"
     authors = ["Joseph <josephok@qq.com>"]
     edition = "2018"
     
     [lib]
     name = "handle"
     crate-type = ["cdylib"]
     
     [dependencies.cpython]
     version = "0.2"
     features = ["extension-module"]
     ```

   - 如果是在mac os，还要编辑~/.cargo/config，不然会编译不过：

     ```shell
     [target.x86_64-apple-darwin]
     rustflags = [
       "-C", "link-arg=-undefined",
       "-C", "link-arg=dynamic_lookup",
     ]
     ```

     

   - 然后是编辑handle/src/lib.rc:

     ```rust
     #[macro_use]
     extern crate cpython;
     
     use cpython::ObjectProtocol;
     use cpython::{PyObject, PyResult, Python};
     use std::collections::HashMap;
     
     fn ret_py_dict(py: Python, obj: PyObject) -> PyResult<HashMap<&'static str, String>> {
         let mut response = HashMap::new();
         response.insert("method", obj.getattr(py, "method")?.extract(py)?);
     
         Ok(response)
     }
     
     py_module_initializer!(handle, init_handle, PyInit_handle, |py, m| {
         m.add(py, "ret_py_dict", py_fn!(py, ret_py_dict(val: PyObject)))?;
     
         Ok(())
     });
     ```


   - `cd handle && cargo build --release`

   - mac系统：`cp handle/target/release/libhandle.dylib your/python/script/path/handle.so`；
     linux系统：`cp handle/target/release/libhandle.so your/python/script/path/handle.so`；

   - 使用方法：
这里的handle是模块名，ret_py_dict就是模块的方法，供Python调用，handle.so必须与python脚本在同一目录：
     
     ```python
     import handle
     handle.ret_py_dict(py_dict)
     ```

<br><br> 

2. 