## v-for中的key

使用`v-for`更新已渲染的元素列表时,默认用`就地复用`策略;列表数据修改的时候,他会根据key值去判断某个值是否修改,如果修改,则重新渲染这一项,否则复用之前的元素; 我们在使用的使用经常会使用`index`(即数组的下标)来作为`key`,但其实这是不推荐的一种使用方法;

举个🌰

```
const list = [
    {
        id: 1,
        name: 'test1',
    },
    {
        id: 2,
        name: 'test2',
    },
    {
        id: 3,
        name: 'test3',
    },
]

<div v-for="(item, index) in list" :key="index" >{{item.name}}</div>
```

上面这种是我们做项目中常用到的一种场景,因为不加key,vue现在直接报错,所以我使用index作为key;下面列举两种常见的数据更新情况

### 1.在最后一条数据后再加一条数据

```
const list = [
    {
        id: 1,
        name: 'test1',
    },
    {
        id: 2,
        name: 'test2',
    },
    {
        id: 3,
        name: 'test3',
    },
    {
        id: 4,
        name: '我是在最后添加的一条数据',
    },
]
```

此时前三条数据直接复用之前的,新渲染最后一条数据,此时用`index`作为`key`,没有任何问题;

### 2.在中间插入一条数据

```
const list = [
    {
        id: 1,
        name: 'test1',
    },
    {
        id: 4,
        name: '我是插队的那条数据',
    }
    {
        id: 2,
        name: 'test2',
    },
    {
        id: 3,
        name: 'test3',
    },
]
```

此时更新渲染数据,通过`index`定义的`key`去进行前后数据的对比,发现

```
之前的数据                         之后的数据

key: 0  index: 0 name: test1     key: 0  index: 0 name: test1
key: 1  index: 1 name: test2     key: 1  index: 1 name: 我是插队的那条数据
key: 2  index: 2 name: test3     key: 2  index: 2 name: test2
                                                 key: 3  index: 3 name: test3

```

通过上面清晰的对比,发现除了第一个数据可以复用之前的之外,另外三条数据都需要重新渲染;

是不是很惊奇,我明明只是插入了一条数据,怎么三条数据都要重新渲染?而我想要的只是新增的那一条数据新渲染出来就行了

最好的办法是使用数组中不会变化的那一项作为`key`值,对应到项目中,即每条数据都有一个唯一的`id`,来标识这条数据的唯一性;使用`id`作为`key`值,我们再来对比一下向中间插入一条数据,此时会怎么去渲染

```
之前的数据                         之后的数据

key: 1  id: 1 index: 0 name: test1     key: 1  id: 1 index: 0  name: test1
key: 2  id: 2 index: 1 name: test2     key: 4  id: 4 index: 1  name: 我是插队的那条数据
key: 3  id: 3 index: 2 name: test3     key: 2  id: 2 index: 2  name: test2
                                                         key: 3  id: 3 index: 3  name: test3

```

现在对比发现只有一条数据变化了,就是`id`为4的那条数据,因此只要新渲染这一条数据就可以了,其他都是就复用之前的;

同理在react中使用map渲染列表时,也是必须加key,且推荐做法也是使用`id`,也是这个原因;

其实,真正的原因并不是vue和react怎么怎么,而是因为Virtual DOM 使用Diff算法实现的原因,

> 下面大致从虚拟DOM的Diff算法实现的角度去解释一下

vue和react的虚拟DOM的Diff算法大致相同，其核心是基于两个简单的假设：

1. 两个相同的组件产生类似的DOM结构，不同的组件产生不同的DOM结构。
2. 同一层级的一组节点，他们可以通过唯一的id进行区分。基于以上这两点假设，使得虚拟DOM的Diff算法的复杂度从O(n^3)降到了O(n)。