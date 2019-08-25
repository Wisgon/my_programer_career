解决办法如下：
tensorflow

​    使用tensorflow时可以使用如下代码来选着使用某块显卡

```python
# Creates a graph.

with tf.device('/gpu:0'):

# write your code here
```



​    限制显存使用，官网同样提供了两种解决方案

a.

```python
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config, ...)
```

在这种方案下，显存占用会随着epoch的增长而增长，也就是运行后面的eopch时，会去申请新的显存，前面已经完成的epoch所占用的显存并不会释放，原因也是为了防止碎片化。

b.

```python
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3
session = tf.Session(config=config, ...)
```

这种方法就比较给力了，告诉tensorflow，我这块显卡只给你30%的显存，其余的你给我放着不动。
keras

由于keras是使用的tensorflow后端，所以需要加上额外的语句。

```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3
set_session(tf.Session(config=config)) # 此处不同
```

上面的语句中设定使用那一块显卡和tensorflow有些不同(我没试验过keras是不是可以用tensorflow指定gpu的语句)，需要使用CUDA_VISIBLE_DEVICES这个值来设定，这个值就是让某几块(使用','分隔)显卡可以被cuda看见，那么程序也就只能调用那几块显卡了。