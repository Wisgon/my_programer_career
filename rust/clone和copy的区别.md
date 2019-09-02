##Clone
Rust 语法上一个变量的值是转移给另一个变量, 但是有些情况下可能会想变量值转移之后, 自身还能继续使用. 可以使用 clone 函数

```rust
let a = String::from("test");
let b = a.clone();
println!("{}", a);
```

clone 这个函数是在标准库的 std::clone::Clone trait 里, 既然是个 trait, 也就意味着可以自己实现一套操作, 通常情况下用默认的定义就好了.
<br><br>

Rust 有些类型是实现了 std::clone::Clone trait 的. 实现了这个 trait 就可以有 clone 函数. 这个 trait 还有一个 clone_from 函数, 这个函数是有默认实现的.
```rust
#[stable(feature = "rust1", since = "1.0.0")]
#[lang = "clone"]
pub trait Clone : Sized {
    #[stable(feature = "rust1", since = "1.0.0")]
    #[must_use = "cloning is often expensive and is not expected to have side effects"]
    fn clone(&self) -> Self;

    #[inline]
    #[stable(feature = "rust1", since = "1.0.0")]
    fn clone_from(&mut self, source: &Self) {
        *self = source.clone()
    }
}
```
理论上, 我们可以按照自己的要求实现 clone, 对于有 Copy 约束的类型, 实现 Clone trait 需要保证跟 Copy 是相容的, 也就是我们自己实现的 Clone 不会导致 Copy 的行为不正确. 通常情况下我们使用 Rust 的 #[derive(Clone)] 自动实现 Clone 就好了, 主要是避免手动实现出错.<br><br>

##Copy
我们现在了解到每次绑定变量, 都会发生所有权转移, 但是你会发现写有些东西的时候好像行为跟目前的认知有点不一样.

```rust
let a: i32 = 10;
let b = a;
println!("a = {}", a); // a = 10
```

a 没有使用 clone 还能使用, 原因是 Rust 有部分类型默认实现了 std::marker::Copy trait. 像 structs 这类没有默认实现的类型, 想要这样就得实现一下 Copy.

```rust
fn main() {
    let p1 = Point { x: 1.0, y: 1.0 };
    let p2 = p1;
    println!("p1 = {:?}", p1);
}

#[derive(Debug)]
struct Point {
    x: f64,
    y: f64,
}

impl Copy for Point {}
```

但是其实这样还是没法用的, 编译后就报错了, 因为 struct Point 没有实现 Clone trait.

```rust
pub fn main_8_6() {
    let p1 = Point { x: 1.0, y: 1.0 };
    let p2: Point = p1;
    println!("p1 = {:?}", p1);
}

#[derive(Debug)]
struct Point {
    x: f64,
    y: f64,
}

impl Clone for Point {
    fn clone(&self) -> Self {
        Self { x: self.x, y: self.y }
    }
}

impl Copy for Point {}
```

现在终于好使了. 但是我们发觉做这些操作非常烦, 我们注意到 #[derive(Debug)] 这个东西, 刚好 Rust 提供了Clone, Copy 的属性.

```rust
pub fn main_8_6() {
    let p1 = Point { x: 1.0, y: 1.0 };
    let p2: Point = p1;
    println!("p1 = {:?}", p1);
}

#[derive(Debug, Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}
```

Rust 默认绑定变量是进行 move 行为, 想要保留 move 前的变量, 可以使用 clone 函数, 想要实现基本类型一样的 copy 行为, 我们可以添加 Clone, Copy 属性.<br><br> 

之前讲到 Rust 有部分类型是默认实现了 std::marker::Copy trait 的. Rust 有很多类型, 有 整型, 浮点型, 布尔型 和 字符型, 还有 元组, 数组, 此外还有结构体, 枚举类型, & 借用指针, &mut 可变借用指针, 还有标准库提供的类型...<br><br> 

#####默认实现了 Copy 的类型
像 整型, 浮点型, 布尔型, 字符型, 都是实现了 Copy trait 的, 元组类型, 如果某个元组内的值都实现了 Copy trait, 那这个元组也是 impl Copy 类型, 数组同理.<br><br> 

#####需要手动实现 Copy 的类型
Rust 的结构体, 枚举类型, 如果它们的内部都是 impl Copy 的, 那么它们也可以自己手动 impl Copy.<br><br> 

#####无法实现 Copy 的类型
Box 就是无法实现 Copy 的类型, 原因很简单, 如果 Box 可以实现 Copy, 那么就会有多次释放这类问题. 还有可变借用指针的类型 &mut T, 同样的理由.