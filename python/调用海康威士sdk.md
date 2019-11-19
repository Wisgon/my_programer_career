###ctype数据类型映射：

[`ctypes`](https://docs.python.org/zh-cn/3/library/ctypes.html#module-ctypes) 定义了一些和C兼容的基本数据类型：

| ctypes 类型                                                  | C 类型                                     | Python 数据类型     |
| ------------------------------------------------------------ | ------------------------------------------ | ------------------- |
| [`c_bool`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_bool) | `_Bool`                                    | bool (1)            |
| [`c_char`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_char) | `char`                                     | 单字符字节对象      |
| [`c_wchar`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_wchar) | `wchar_t`                                  | 单字符字符串        |
| [`c_byte`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_byte) | `char`                                     | int                 |
| [`c_ubyte`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_ubyte) | `unsigned char`                            | int                 |
| [`c_short`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_short) | `short`                                    | int                 |
| [`c_ushort`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_ushort) | `unsigned short`                           | int                 |
| [`c_int`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_int) | `int`                                      | int                 |
| [`c_uint`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_uint) | `unsigned int`                             | int                 |
| [`c_long`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_long) | `long`                                     | int                 |
| [`c_ulong`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_ulong) | `unsigned long`                            | int                 |
| [`c_longlong`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_longlong) | `__int64` 或 `long long`                   | int                 |
| [`c_ulonglong`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_ulonglong) | `unsigned __int64` 或 `unsigned long long` | int                 |
| [`c_size_t`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_size_t) | `size_t`                                   | int                 |
| [`c_ssize_t`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_ssize_t) | `ssize_t` 或 `Py_ssize_t`                  | int                 |
| [`c_float`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_float) | `float`                                    | float               |
| [`c_double`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_double) | `double`                                   | float               |
| [`c_longdouble`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_longdouble) | `long double`                              | float               |
| [`c_char_p`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_char_p) | `char *` (NUL terminated)                  | 字节串对象或 `None` |
| [`c_wchar_p`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_wchar_p) | `wchar_t *` (NUL terminated)               | 字符串或 `None`     |
| [`c_void_p`](https://docs.python.org/zh-cn/3/library/ctypes.html#ctypes.c_void_p) | `void *`                                   | int 或 `None`       |

<br><br>

###登录代码：

```python
import os
import ctypes
import datetime
import time

lib_path = "./"
hk_so_list = []


def add_so(path, so_list):
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(path+file):
            if file.endswith(".so"):
                so_list.append(path+file)
        else:
            add_so(path+file+"/", so_list)


def call_cpp(func_name, *args):
    for so_lib in hk_so_list:
        try:
            lib = ctypes.cdll.LoadLibrary(so_lib)
            try:
                value = eval("lib.%s" % func_name)(*args)
                print("调用的库：" + so_lib)
                print("执行成功,返回值：" + str(value))
                return value
            except:
                continue
        except Exception as e:
            print("库文件载入失败：" + str(e) + so_lib)
            continue
    print("没有找到接口！")
    return False


# 定义结构体
class LpnetDvrDeviceinfoV30(ctypes.Structure):
    _fields_ = [
        ("sSerialNumber", ctypes.c_byte * 48),
        ("byAlarmInPortNum", ctypes.c_byte),
        ("byAlarmOutPortNum", ctypes.c_byte),
        ("byDiskNum", ctypes.c_byte),
        ("byDVRType", ctypes.c_byte),
        ("byChanNum", ctypes.c_byte),
        ("byStartChan", ctypes.c_byte),
        ("byAudioChanNum", ctypes.c_byte),
        ("byIPChanNum", ctypes.c_byte),
        ("byZeroChanNum", ctypes.c_byte),
        ("byMainProto", ctypes.c_byte),
        ("bySubProto", ctypes.c_byte),
        ("bySupport", ctypes.c_byte),
        ("bySupport1", ctypes.c_byte),
        ("bySupport2", ctypes.c_byte),
        ("wDevType", ctypes.c_uint16),
        ("bySupport3", ctypes.c_byte),
        ("byMultiStreamProto", ctypes.c_byte),
        ("byStartDChan", ctypes.c_byte),
        ("byStartDTalkChan", ctypes.c_byte),
        ("byHighDChanNum", ctypes.c_byte),
        ("bySupport4", ctypes.c_byte),
        ("byLanguageType", ctypes.c_byte),
        ("byVoiceInChanNum", ctypes.c_byte),
        ("byStartVoiceInChanNo", ctypes.c_byte),
        ("byRes3", ctypes.c_byte * 2),
        ("byMirrorChanNum", ctypes.c_byte),
        ("wStartMirrorChanNo", ctypes.c_uint16),
        ("byRes2", ctypes.c_byte * 2)]


def net_dvr_login_v30(s_dvr_ip = "192.168.100.152", w_dvr_port = 8000,
                      s_user_name = "admin", s_password = "swzd123456"):
    global l_user_id
    init_res = call_cpp("NET_DVR_Init")  # SDK初始化
    if init_res:
        print("SDK初始化成功")
    else:
        error_info = call_cpp("NET_DVR_GetLastError")
        print("SDK初始化错误：" + str(error_info))
        return False

    set_overtime = call_cpp("NET_DVR_SetConnectTime", 5000, 4)  # 设置超时
    if set_overtime:
        print("设置超时时间成功")
    else:
        error_info = call_cpp("NET_DVR_GetLastError")
        print("设置超时错误信息：" + str(error_info))
        return False

    # 用户注册设备
    # c++传递进去的是byte型数据，需要转成byte型传进去，否则会乱码
    s_dvr_ip = bytes(s_dvr_ip, "ascii")
    s_user_name = bytes(s_user_name, "ascii")
    s_password = bytes(s_password, "ascii")
    device_info = LpnetDvrDeviceinfoV30()
    device_info_ref = ctypes.byref(device_info)
    l_user_id = call_cpp("NET_DVR_Login_V30", s_dvr_ip, w_dvr_port, s_user_name, s_password, device_info_ref)
    print("登录结果：" + str(l_user_id))
    if l_user_id == -1:
        error_info = call_cpp("NET_DVR_GetLastError")
        print("登录错误信息：" + str(error_info))
        return error_info
    else:
        return l_user_id


add_so(lib_path, hk_so_list)
l_user_id = 0
net_dvr_login_v30()

```

<br><br>

###登录时发生编号41的错误
这是由于执行的python文件没有和lib目录下的.so文件在同一个目录下的缘故，将python的执行文件与lib下的所有文件、文件夹放在同一个目录下就好；另一个解决方法是：cd到sdk的文件夹，然后命令行运行：`$python3 ../start.py`也可；<br><br>

###关于发生段错误的经验总结：
回调函数对象(即**ctypes.CFUNCTYPE(callback_func)**创建的对象)一定不要直接传递给call_cpp，如：

```python
l_listen_handle = call_cpp("NET_DVR_StartListen_V30", None, listen_port, call_func_class(alarm_callback) , None)  # 会一定概率发生段错误
```

因为Make sure you keep references to [`CFUNCTYPE()`](https://docs.python.org/3.7/library/ctypes.html#ctypes.CFUNCTYPE) objects as long as they are used from C code.[`ctypes`](https://docs.python.org/3.7/library/ctypes.html#module-ctypes) doesn’t, and if you don’t, they may be garbage collected, crashing your program when a callback is made

所以应该：

```python
call_func = call_func_class(alarm_callback)
l_listen_handle = call_cpp("NET_DVR_StartListen_V30", None, listen_port, call_func , None)
```

<br><br>



**(1)将py脚本编译成so动态库**：

```shell
#pip installl  cython
$cython  xxx.py  #或直接cython *.py可将文件夹下所有py文件转成xxx.c文件
$gcc -c  -fPIC -I/home/xxx/anaconda3/envs/env_name/include/python3.7m/  xxx.c
$gcc -shared xxx.o -o xxx.so
```

/home/xxx/anaconda3/envs/env_name/include/python3.7m/是python运行环境所在目录，这样，就在当前文件夹下生成了xxx.so了，可以像普通py文件一样导入函数等；

**(2)将c++编译成.so并给python调用：**

```c++
//c_demo.cpp
#include<stdio.h>

int write_picture_plate_num(const char *filename) {
    FILE *fSnapPicPlate=NULL;
    char b[]= "sgfsdf";
    fSnapPicPlate=fopen(filename,"wb");
    fwrite(&b, 1, 8, fSnapPicPlate);
}

extern "C"
void write_picture_plate_num_func(char *filename)
{
 write_picture_plate_num(filename);
}
```

接收一个文件名的char指针，然后保存char b[]这个字符串的内容，注意extern "C"是必须要的，且C要大写！

```
$ g++ -o c_demo.so -shared -fPIC c_demo.cpp
```

这会生成 c_demo.so文件，

```python
#c_demo.py
import ctypes
func = ctypes.cdll.LoadLibrary("./c_demo.so")
func.write_picture_plate_num_func(b"dest.txt")
```

这样就能调用c_demo.so了，注意传入的字符串要带“b”；

<br><br>

###使用c++中的enum：

```c++
//c_demo.cpp
typedef enum {
    ZERO,
    ONE,
    TWO
} MyEnum;

extern "C"
int getAnEnumValue(MyEnum anEnum) {
    return (int)anEnum;
}

extern "C"
    int sayhello(){
     using namespace std;
    cout << "HelloWorld\n";
    //cout << endl;
    return 0;
}
```

```
$ g++ -o c_demo.so -shared -fPIC c_demo.cpp  # 生成c_demo.so
```

```python
# c_demo.py
import ctypes as c
from enum import IntEnum


# Define the types we need.
class CtypesEnum(IntEnum):
    """A ctypes-compatible IntEnum superclass."""
    @classmethod
    def from_param(cls, obj):
        return int(obj)


class MyEnum(CtypesEnum):
    ZERO = 0
    ONE = 1
    TWO = 2


# Load the DLL and configure the function call.
my_dll = c.cdll.LoadLibrary('./c_demo.so')
get_an_enum_value = my_dll.getAnEnumValue
get_an_enum_value.argtypes = [MyEnum]
get_an_enum_value.restype = c.c_int

# Demonstrate that it works.
print(get_an_enum_value(MyEnum.TWO))  # 打印出2，成功
my_dll.sayhello()  # 打印出“HelloWorld"
```

<br><br>

###c++ 类型转换

其中，string转const char*，用`constc= str.c_str(); `即可，但：

```c++
string a = "fdsf";
string b = "fsdfs";
const char* constc = nullptr;
//如果直接 constc = (a+b).c_str(); 会变成乱码！应该：
string temp = a+b;
constc = temp.c_str();
```

<br><br>

