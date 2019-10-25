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
这是由于执行的python文件没有和lib目录下的.so文件在同一个目录下的缘故，将python的执行文件与lib下的所有文件、文件夹放在同一个目录下就好；<br><br>

