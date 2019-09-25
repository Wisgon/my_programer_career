*rust 的核心思想是 由程序员，语法，编译器 共同 维护 程序内的变量生成，使用，复制，转移和销毁。*

**基本数据类型**

i8,i16,i32,i64,i128 //有符号整数

u8,u16,u32,u64,u128 //无符号整数

f32,f64 //浮点数，money估计也要用到此值

char //字符类型

bool:true,false // bool 类型

String //要引用std::string::String //字符串类型

silce //切片，这是个片段引用

type Name = String; //类型别名，只是个别名不是新类型

**类型转换**

as 转换符 ：

`‘c’ as u8`

`23 as char`

`i64 as i128; i32 as i64`

如：`let a = 'c' as u8 //此时a是99`

**常量变量**

```rust
const MAX_POINTS: u32 = 100_000; // 静态

let x = 5;//绑定变量

let x:u32 = 5;

let mut x = 5;//声明可变绑定

let mut x:u64 = 5;

let an_integer = 5i32; //通过数据来定义

let y = 3.0_f64; //后缀指定类型

let _noisy_unused_variable = 2u32; // 如果某个值绑定了未使用,会报编译警告.只要加个前下划线就不会编译警告了.

let spaces = " ";//字面值

let spaces = spaces.len();//这是重定义space，而不是设置

let mut spaces = " ";

spaces = ‘3’;//这是变更值内容

let guess: u32 = "42".parse().expect("Not a number!");//这个是转换+验证抛错
```



**下面是字面值**

Decimal 98_222;

Hex 0xff;

Octal 0o77;

Binary 0b1111_0000;

Byte (u8 only) b'A';

**运算符**

+-*/% 5大运算，加减乘除余 整数除 取整，%求余数，浮点数除就是浮点结果

+=, -=, *=, /=

**组合结构**

```rust
let x: (i32, f64, u8) = (500, 6.4, 1); //元组

let x1 = (500i32,"500",500.0f64);

let a = [1, 2, 3, 4, 5]; // 数组

let mut a:[i32;5]=[1,2,3,4,5]; // 可变数组绑定 &a[0]=2后[2,2,3,4,5]

let ys: [i32; 500] = [0; 500]; // i32类型500长度，用0初始化 500长度？

// 数组的定义写法 变量名:[类型;数组长度]

// 简化 (1..4) 1-4组合=[1,2,3,4] 但不一定是数组，也可能是vector
```



**打印print 格式化打印**

5个宏 ：format!、format_arg!、print!、println!、write！

两个 trait: Debug、Display。

print!、println!、就是将 format!的结果输出到控制台;

```rust
println!("{} days", 31);

println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");

println!("{subject} {verb} {object}",

object="the lazy dog",

subject="the quick brown fox",

verb="jumps over");

println!("{} of {:b} people know binary, the other half doesn't", 1, 2);

println!("{number:>width$}", number=1, width=6); // 打印1宽度6

println!("{number:>0width$}", number=1, width=6); //打印1，0宽度6

println!("My name is {0}, {1} {0}", "Bond"); // 没有{1}对应值，必须加入才能编译通过

\#[allow(dead_code)]

struct Structure(i32);//这个是元组类型结构，用.0 .1访问成员

fmt::Debug: Uses the {:?} marker. // 实现了Debug特性可用{:?}标记打印信息

fmt::Display: Uses the {} marker. // 实现了display特性可用{}打印信息

println!("This struct `{}` won't print...", Structure(3)); // 注意打印占位符{} 不是 {:?}，需要Structure实现Display trait

println!("{1:?} {0:?} is the {actor:?} name.", // {1:?} 打印第二个 数组标记法

"Slater",

"Christian",

actor="actor's"); // 打印名字标记法

println!("{:#?}", peter); // 漂亮打印：其实就是参数分行打印，一个参数一行，易读

impl Display for Structure{ // 这个实现了 Display

fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result { // 这行就是 Display trait的具体方法描述

write!(f, "--({})--", self.0) //这里是实现：一定不能直接用self，必须用self.0 不然会导致嵌套调用“overflowed its stack”

}

}
```



**函数-方法**

fn another_function() { ... } // 孤立的叫函数，impl的&self首个参数的叫方法（类似对象方法），impl内首个参数非&self的方法叫关联函数（类似静态方法）

fn another_function(x: i32, y: i32)->i32// 多参数单返回值

fn plus_one(x: i32, y: i32) -> (i32,i32)//多参数多返回值

包含语句和表达式的函数体: 语句（Statements）是执行一些操作但不返回值的指令(有分号结尾)。表达式（Expressions）计算并产生一个值（无分号结尾）。

函数调用是一个表达式。宏调用是一个表达式。

**控制结构**

```rust
if number < 5 { //单个if else

} else {

}

if number % 4 == 0 { // 一堆if else if

} else if number % 3 == 0 {

} else if number % 2 == 0 {

} else {

}

let number = if condition { // if赋值，有分号的叫语句，没分号的叫表达式-含有返回

5

} else {

6

};
```



**循环**

```rust
loop { // 玩命的循环

if true { break; } //还是能退出的

}

while number != 0 { //不玩命的循环

}

for element in a.iter() { // 挨着循环

}

for number in (1..4).rev() { //倒着循环

}

let v = vec![1;10];

for (index, e) in v.iter().enumerate() { //带索引循环

}

for (pos, e) in v.iter()
```



**函数参数-引用参数**

```rust
fn calculate_length(s: &String) -> usize // 引用参数

let len = calculate_length(&s1);

// 可变引用函数

fn change(some_string: &mut String) {

let mut s = String::from("hello");

change( &mut s);
```



**slice 切片**

```rust
let s = String::from("hello world");

&s[起点索引值..终点索引值] start..end 语法代表一个以 start 开头并一直持续到但不包含 end 的 range。

let hello = &s[0..5];// 注意 字符串 时 这里取的是字节，utf-8不能这样取！必死！

let world = &s[6..11];// 数组的话ok

let hello = &s[0..=4];// 如果需要包含 end，可以使用 ..= 不用等号就是不含4号，加等号含有4号

let slice = &s[0..2]; // 开头开始取

let slice = &s[..2]; // 开头开始取，省了0

let len = s.len();

let slice = &s[3..len]; //3到结尾

let slice = &s[3..]; //3到结尾

let slice = &s[0..len]; //全取

let slice = &s[..]; //全取

fn first_word(s: &String) -> &str {

&s[..] // 表达式，返回slice

}

fn first_word(s: &String) -> &str {//这里（不可变）借用s，返回slice引用，有借鉴 
  let bytes = s.as_bytes(); 
  for (i, &item) in bytes.iter().enumerate() { 
    if item == b' ' {
      return &s[0..i]; 
     } 
   } &s[..]//用表达式返回，有借鉴。某值的不可变引用时，就不能再获取一个可变引用。 
  }

let s = "Hello, world!";

//这里 s 的类型是 &str：它是一个指向二进制程序特定位置的 slice。这也就是为什么字符串字面值是不可变的； &str 是一个不可变引用。
```



**字符串接入，字符串+操作**

```rust
let mut s = String::from("lo");

s.push('l');//push接入

let s1 = String::from("Hello, ");

let s2 = String::from("world!");

let s3 = s1 + &s2; // +接入

// 多个字符串组合

let s1 = String::from("tic");

let s2 = String::from("tac");

let s3 = String::from("toe");

let s = s1 + "-" + &s2 + "-" + &s3; //行但笨

let s = format!("{}-{}-{}", s1, s2, s3); // 女子

// 异类字符 slice

let hello = "Здравствуйте";

let s = &hello[0..4];// 必须双数，取得字节！

for c in "Здравствуйте" .chars() { //取得字面字符

println!("{}", c);

}

for b in "Здравствуйте".bytes() { //取得字节

println!("{}", b);

}
```



**字符串相等性对比：**

str::eq(str1, str2) 对比两者必须是 String或者 str 类型

不排除还有其他对比方式

**引用和借用**

&s1 语法允许我们创建一个 指向 值 s1 的引用，但是并不拥有它。

fn calculate_length( **s: &String**) -> usize { // 借用 将获取引用作为函数参数称为 借用（borrowing）

尝试修改借用的变量，（默认）不允许修改引用的值。除了一些特别的情况，比如标准库基本类型字符类型char.encode_utf8()方法

*可变借用一个样例：*

```rust
pub fn unicode_utf8(ustr: &String) -> Vec<u8> { //借用来的参数

let mut utf8_str: Vec<u8> = Vec::new();

for c in ustr.chars() {

let len = c.len_utf8();

let mut cb:[u8; 4] = [0u8; 4];

{ // 这里构成一个作用域，用于隔离另一个（后面一个）引用借用

let cb_a = &mut cb[..len]; //从cb中创建一个可修改引用借用，

let r = c.encode_utf8(cb_a); //将可修改引用借用给encode_utf8函数，内部有不安全代码

println!("r = {:?}", r);

} //作用域后cb_a已经失效了，这个引用借用被释放了

let cb_b = &cb[..len]; //再来个引用借用，但是这里不需要修改了。

for b in cb_b {

utf8_str.push(b.clone()); //循环将encode_utf8修改的内容装到vec中。

}

}

return utf8_str;//返回将unicode转换utf8编码后的byte数组vec

}
```



多个不可变引用是没有问题。不能在拥有不可变引用的同时拥有可变引用。

在任意给定时间，只能 拥有如下中的一个：

一个可变引用。

任意数量的不可变引用。

引用必须总是有效的。

**所有权要点** **★★★★★**

栈上数据 拷贝，有两个值；

堆上数据，使用所有权 **移动（move）**，而不是浅拷贝。

```rust
let s1 = String::from("hello");

let s2 = s1;//解读为 s1 被 移动 到了 s2 中，这之后s1无法再使用，所有权转移到s2上了

let s1 = String::from("hello");

let s2 = s1.clone();//这里深拷贝了s1的数据。所以s1和s2都可以使用，出现两个所有权者

fn takes_ownership(some_string: String) //这种方法定义表示输入参数所有权转移到函数内部了

fn takes_ownership(some_string: &String) //这种方法定义表示输入参数所有权被借用进来了
fn makes_copy(some_integer: i32)//对于基本栈类型 , 这里参数是拷贝进来的，另外建立了所有权

fn gives_ownership(input: String) -> String { //这里接收一个所有权，再返回数据将函数内部所有权转移到外部

let (s2, len) = calculate_length(s1);//此方法传入s1所有权，处理后返回所有权到s2，还有其他返回(len)。元组返回处理所有权。但是有些罗嗦
```



**引用（references）借用** & 符号就是 引用，它们允许你使用值但不获取其所有权。

`fn calculate_length(s: &String) -> usize {` //输入参数借用外部数据，但是不获取其所有权。获取引用作为函数参数称为 **借用（borrowing）（**不允许修改引用/借用 **）**

与使用 & 引用相反的操作是 解引用（dereferencing），它使用解引用运算符，*。

```rust
fn change(some_string: &mut String) {...//可变借用

let mut s = String::from("hello");//定义可变绑定

change(&mut s);//可变借用到函数内部（ **一次只有一个可变借用（**可以使用大括号隔离多个可变借用 **）**）

{ let r1 = &mut s;} // r1 在这里离开了作用域，所以我们完全可以创建一个新的引用 let r2 = &mut s;
```



也 不能在拥有不可变引用的同时拥有可变引用。

**悬垂引用（Dangling References）**在函数内部创建，返回其指针，但是函数结束其所有者会被释放

`fn dangle() -> &String { // dangle 返回一个字符串的引用 离开作用域并被丢弃。其内存被释放。危险！`

解决方法是直接返回String。`fn no_dangle() -> String {...`

 

**总结常用方法：**

String 转移

&String 借用

-> String 转移出来

slice不可变借用

作用域隔离{}

 

**struct 结构体**

```rust
struct User { //定义

username: String,

email: String,

sign_in_count: u64,

active: bool,

}

let user1 = User { //初始化赋值

username: String::from("someusername123"),

};

let mut user1 = User { // 可变更的

username: String::from("someusername123"),

};

user1.username = String::from("another"); //赋值
```





**结构-方法语法**

```rust
#[derive(Debug)] //这个让结构体可被打印出来

struct Rectangle {

width: u32,

height: u32,

}

impl Rectangle { // 方法语法，在impl中叫方法，孤立的叫函数

fn area(&self) -> u32 { //注意self 和py类似

self.width * self.height

}

}

let rect1 = Rectangle { width: 30, height: 50 };

rect1.area() //用变量.成员调用
```





**关联函数（associated functions）**

不加&self 就是关联函数，类似静态函数。加&self类似对象函数

```rust
impl Rectangle {

fn square(size: u32) -> Rectangle {

        Rectangle { width: size, height: size }

    }
}

Rectangle::square(100) //关联函数访问
```





**枚举，每个值可不同类型**

```rust
enum Message {

Quit,

Move { x: i32, y: i32 }, // 匿名结构体

Write(String),

ChangeColor(i32, i32, i32), //元组

}

Message::ChangeColor //访问方法

enum Option<T> { //官方一个结构用于返回错误和正常结果

Some(T),

None,

}

\#[derive(Debug)] // So we can inspect the state in a minute

enum UsState {

Alabama,

// ... etc

}

enum Coin {

Dime,

Quarter(UsState),//这个枚举类型是另一个枚举

}

match coin { // match语法

Coin::Dime => 10, // 直接返回（表达式）

Coin::Quarter(state) => { // 含有函数体

println!("State quarter from {:?}!", state);

25

},

// _ => (), // 通配符匹配，匹配所有剩余项目

}

// 只匹配一个其他忽略

let some_u8_value = Some(0u8);

match some_u8_value {

Some(3) => println!("three"),

_ => (),

}

// 只匹配一个其他忽略 简化写法

if let Some(3) = some_u8_value {

println!("three");

} else { ... }

// 这是一组写法，值得学习

fn plus_one(x: Option<i32>) -> Option<i32> {

match x {

None => None, //空返回

Some(i) => Some(i + 1), //有结果返回

}

}

let five = Some(5);

let six = plus_one(five);

let none = plus_one(None);
```





**pub**

pub //控制可见 在 fn impl mod 前面

**模块引用（1.31后有变化）**

```rust
extern crate my_library; // 先进入模块名 同下文的 a

a::series::of::nested_modules(); //完整路径模块引用样例

use a::series::of;

of::nested_modules(); // use 简短 引用路径

use a::series::of::nested_modules;

nested_modules(); // 最深到函数

use TrafficLight::{Red, Yellow}; // 只引入两个

let red = Red;

let yellow = Yellow;

let green = TrafficLight::Green;//这种还是要完整引入

// * 语法，这称为 glob 运算符（glob operator）

use TrafficLight::*; // 全引入

::client::connect(); // 开头双冒表从根模块引用开始

super::client::connect(); // super表上一级模块开始引用，是上一级不是根！

\#[cfg(test)]

mod tests {

use super::client; //在mod内部 super上一级 引入，少些好多super

\#[test]

fn it_works() {

client::connect();

}

}

use mymod::mymod2::mymod3 as mm3; // use as 语法use别名 我就说肯定有类似的！
```



注意: 默认好象是不引用std的,有用到std的地方需要在开始 use std;<br><br> 

**集合 vcetor**

默认引入，无需use

```rust
let v: Vec<i32> = Vec::new();

let v = vec![1, 2, 3];

v.push(5); //push进去

v.push(6);

let third: &i32 = &v[2]; // 用索引访问

let third: Option<&i32> = v.get(2); // get加索引访问，注意返回类型 超界处理良好

let v = vec![100, 32, 57]; //遍历1

for i in &v {

println!("{}", i);

}

let mut v = vec![100, 32, 57]; // 可变更遍历

for i in &mut v {

*i += 50; // 使用 += 运算符之前必须使用解引用运算符（*）获取 i 中的值。

}

// 枚举 的 vector 感觉好复杂哦！！！

enum SpreadsheetCell {

Int(i32),

Float(f64),

Text(String),

}

let row = vec![

SpreadsheetCell::Int(3),

SpreadsheetCell::Text(String::from("blue")),

SpreadsheetCell::Float(10.12),

];
```



<br><br> 

**HashMap**

```rust
use std::collections::HashMap; // 要use

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);

scores.insert(String::from("Yellow"), 50);

// 这是个杂交组合法，要use std::collections::HashMap;

let teams = vec![String::from("Blue"), String::from("Yellow")];

let initial_scores = vec![10, 50];

let scores: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect(); //这里杂交组合两个vector

// 插入值 所有权转移

let field_name = String::from("Favorite color");

let field_value = String::from("Blue");

let mut map = HashMap::new();

map.insert(field_name, field_value); // 这里插入后两个值所有权被转移到map内部了

访问map

let score = scores.get(&team_name);

for (key, value) in &scores { //遍历

println!("{}: {}", key, value);

}

scores.insert(String::from("Blue"), 25); // 覆盖

scores.entry(String::from("Blue")).or_insert(50); //没有就插入，有跳过

// 找到一个键对应的值并根据旧的值更新它

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {

let count = map.entry(word).or_insert(0);

*count += 1; // 为了赋值必须首先使用星号（*）解引用 count

}
```



<br><br> 

**异常 抛错**

```rust
[profile] //cargo.toml 配置

panic = 'abort'

[profile.release] // 这是发布模式

panic = 'abort'

panic!("crash and burn");// 抛错语句
```



设置 RUST_BACKTRACE 环境变量来得到一个 backtrace backtrace 是一个执行到目前位置所有被调用的函数的列表。（怎么设置？还不晓得）

```rust
enum Result<T, E> { //可恢复的错误 的 枚举

Ok(T),

Err(E),

}

let f = File::open("hello.txt");

let f = match f { // 用match处理成功和失败

Ok(file) => file,

Err(error) => {

panic!("There was a problem opening the file: {:?}", error)

},

};

// 一个错误处理范例 这个范例嵌套了 match
let f = File::open("hello.txt").unwrap(); // unwrap帮调用panic! 宏 但是无法体现具体错误

let f = File::open("hello.txt").expect("Failed to open hello.txt"); // expect可以体现不同的错误，更好
```

<br><br> 



**传播错误**

```rust
fn read_username_from_file() -> Result<String, io::Error>{ // 返回参数是“标准库结果”

let f = File::open("hello.txt");

let mut f = match f {

Ok(file) => file,

Err(e) => return Err(e), // 返回错误

};

let mut s = String::new();

match f.read_to_string(&mut s) {

Ok(_) => Ok(s),

Err(e) => Err(e),

}
```





**简化的错误传播**

```rust
fn read_username_from_file() -> Result<String, io::Error> { // 注意 ? 关键

let mut f = File::open("hello.txt")?;

let mut s = String::new();

f.read_to_string(&mut s)?;

Ok(s)

}

let mut s = String::new();

File::open("hello.txt")?.read_to_string(&mut s)?; //链式方法调用

Ok(s)
```



? 只能被用于返回值类型为 Result 的函数<br><br> 

**泛型**

```rust
struct Point<T> { //单泛型

x: T,

y: T,

}

struct Point<T, U> { // 多泛型

x: T,

y: U,

}

enum Option<T> { //单泛型枚举

Some(T),

None,

}

enum Result<T, E> { //多枚举泛型

Ok(T),

Err(E),

}

impl<T> Point<T> { //泛型方法定义

fn x(&self) -> &T {

&self.x

}

}

impl Point<f32> { // 特定类型方法定义

fn distance_from_origin(&self) -> f32 {

(self.x.powi(2) + self.y.powi(2)).sqrt()

}

}

impl<T, U> Point<T, U> { // 双泛型 方法定义，方法中还有泛型

fn mixup<V, W>(self, other: Point<V, W>) -> Point<T, W> {

Point {

x: self.x,

y: other.y,

}

}

}
```

<br><br> 



**trait 类似接口 定义共享行为**

```rust
pub trait Summarizable { // 定义trait

fn summary(&self) -> String;

}

impl Summarizable for NewsArticle { // 为类型NewsArticle 实现这个trait

fn summary(&self) -> String {

format!("{}, by {} ({})", self.headline, self.author, self.location)

}

}

impl Summarizable for Tweet { // 为类型 Tweet实现 Summarizable trait

fn summary(&self) -> String {

format!("{}: {}", self.username, self.content)

}

}
```





限制是：只能在 trait 或对应类型位于我们 crate 本地的时候为其实现 trait。换句话说，不允许对外部类型实现外部 trait。例如，不能在 Vec 上实现 Display trait，因为 Display 和 Vec 都定义于标准库中。

```rust
pub trait Summarizable { // 默认实现

fn summary(&self) -> String {

String::from("(Read more...)")

}

}

impl Summarizable for NewsArticle {} // 空impl 块，直接使用默认trait行为

pub trait Summarizable { // 默认实现可以调用未实现的 方法

fn author_summary(&self) -> String; // 这个行为 由 实现trait者去定义

fn summary(&self) -> String {

format!("(Read more from {}...)", self.author_summary()) // 调用author_summary，然后再调用特定行为

}

}

Trait Bounds 应该就是约束，实现约束，泛型实现trait约束

pub fn notify<T: Summarizable>(item: T) {

println!("Breaking news! {}", item.summary());

}

fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 { //多个约束

fn some_function<T, U>(t: T, u: U) -> i32 // where方式多个约束

where T: Display + Clone,

U: Clone + Debug

{
```





**生命周期注解语法**

生命周期注解并不改变任何引用的生命周期的长短。只是个注解

&i32 // a reference

&'a i32 // a reference with an explicit lifetime

&'a mut i32 // a mutable reference with an explicit lifetime

它只是个变量生命周期的标注，通过标注来识别生命周期范围，实际不影响变量生命周期

`let s: &'static str = "I have a static lifetime."; // 静态生命周期，全程序周期，字符串字面值自带`

“ 生命周期也是泛型” - 这句话让我直接炸裂！我艸，我说呢！写在<>内！

问题：泛型的生命周期呢？是不是要直接定义在泛型类型定义中？

多个生命周期定义只能通过泛型类型，或者结构体类型来定义？

生命周期也存在约束（where）？

`fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &str { //这里实际上是永远都不能编译的？除非用方法语法？`

 

**测试**

cargo test // 项目目录内运行此命令 就提取测试来运行了

```rust
#[cfg(test)] //测试模块 属性注解。属性（attribute）是关于 Rust 代码片段的元数据

mod tests {

use super::*; // 引用要测试的模块 为哈是super ，要测试的模块同级别

\#[test] //测试方法 属性注解

fn it_works() {

assert_eq!(2 + 2, 4); // 测试 断言宏

}

}

assert! 宏由标准库提供，参数bool，false 时 assert! 调用 panic! 宏 抛错

assert_eq! 相等断言宏 和 assert_ne! 不相等断言宏

assert_eq! 和 assert_ne! 宏在底层分别使用了 == 和 !=。被比较的值必需实现了 PartialEq 和 Debug trait。

可以直接在结构体或枚举上添加 #[derive(PartialEq, Debug)] 注解。

let result = greeting("Carol");

assert!(result.contains("Carol")); // 断言结果中含有“Carol”

assert!(

result.contains("Carol"),

"Greeting did not contain name, value was `{}`", result // 这里类似重载函数，打印出明确信息

);

#[test]

#[should_panic] // 这里表示“应该抛错” 才是对的

#[should_panic(expected = "Guess value must be less than or equal to 100")] //出错信息包含expected的字符串就通过

#[ignore] // 忽略此测试

fn greater_than_100() {

Guess::new(200);

}


```



**运行测试**

cargo test -- --test-threads=1 // 单线程运行测试

cargo test -- --nocapture // 测试会输出函数中打印的内容，就是说不截获（并丢弃）屏幕输出

cargo test one_hundred // 运行 含有“one_hundred”的测试

cargo test -- --ignored // 只运行忽略的测试

Rust 社区倾向于根据测试的两个主要分类来考虑问题：单元测试（unit tests）与 集成测试（integration tests）

测试模块的 #[cfg(test)] 注解告诉 Rust 只在执行 cargo test 时才编译和运行测试代码，而在运行 cargo build 时不这么做。

非pub函数可以测试

集成测试

目录中创建tests目录下放测试代码文件。

extern crate adder; // 需要导入指定模块

```rust
#[test]

fn it_adds_two() {

assert_eq!(4, adder::add_two(2));

}

测试目录文件结构和模块一样，但子目录不被测试提取

tests/integration_test.rs // 文件中test 注解会被测试提取

tests/common/mod.rs // 文件中不会被测试提取，测试系统不考虑子模块的函数。但是上级测试方法可以调用子级
```

<br><br>

**编写一个命令行程序**

```rust
use std::env; // 环境变量功能

fn main() {

let args: Vec<String> = env::args().collect(); // 解析参数

let query = &args[1]; // 提取参数，为啥不是[0]，[0]是二进制文件路径"target/debug/exename"

let filename = &args[2];

println!("{:?}", args);

}

注意 std::env::args 在其任何参数包含无效 Unicode 字符时会 panic。如果你需要接受包含无效 Unicode 字符的参数，使用 std::env::args_os 代替。这个函数返回 OsString 值而不是 String 值。

use std::env;

use std::fs::File; // std::fs::File 来处理文件

use std::io::prelude::*; // 而 std::io::prelude::* 则包含许多对于 I/O（包括文件 I/O）有帮助的 trait

let mut f = File::open(filename).expect("file not found"); // 读取文件

let mut contents = String::new();

f.read_to_string(&mut contents) // 文件内容读取到字符串变量

.expect("something went wrong reading the file");

let query = args[1].clone(); // 简单无脑的clone有一定好处，可以不用管生命周期

impl Config {

fn new(args: &[String]) -> Result<Config, &'static str> { // 静态周期 字符串

if args.len() < 3 {

return Err("not enough arguments");

}

let query = args[1].clone(); // clone

let filename = args[2].clone();

Ok(Config { query, filename }) // 返回Config结构

}

}

use std::process;//进程

let config = Config::new(&args).unwrap_or_else(| err| { // 注意 |err| 和闭包有关 将Err内部值传给闭包err参数

println!("Problem parsing arguments: {}", err); // 这就是闭包参数err，看起来类似 委托参数类似c#的(err)=>{...}

process::exit(1); //退出进程

});

line.to_lowercase().contains(&query) // 转换小写并检查是否含有&query

env::var("CASE_INSENSITIVE").is_err(); // 获取环境变量 powershell中设置环境变量：$env.CASE_INSENSITIVE=1

eprintln!("{:?}", &str1) // 标准错误输出宏
```

<br><br> 

**闭包（closures）**

c#叫委托，c叫函数指针 ( 最好不要乱叫 免得被大神喷！)

```rust
use std::thread; // 线程

use std::time::Duration; // 时间差

fn simulated_expensive_calculation(intensity: u32) -> u32 {

thread::sleep(Duration::from_secs(2)); // 睡2秒 这个值得记住

0

}

let expensive_closure = |num, strx| { // 定义一个闭包 委托 函数指针（别瞎叫）

println!("calculating slowly..{}..", strx);

thread::sleep(Duration::from_secs(2));

num

};

let expensive_closure = |num: u32, strx:String| -> u32 {

println!("calculating slowly..{}..", strx);

thread::sleep(Duration::from_secs(2));

num

};

fn add_one_v1 (x: u32) -> u32 { x + 1 } // 这是一组对比，下面的和这个fn一致

let add_one_v2 = |x: u32| -> u32 { x + 1 }; // 指定参数类型返回类型

let add_one_v3 = |x| { x + 1 }; // 不指定类型只写函数体

let add_one_v4 = |x| x + 1 ; // 连大括号都去掉了

闭包无法同时进行两次类型推断

let example_closure = |x| x;

let s = example_closure(String::from("hello")); // 不抛错

let n = example_closure(5); // 抛错 类型不对，已经 被推断过了。

存放了闭包和一个 Option 结果值的 Cacher 结构体的定义

struct Cacher<T>

where T: Fn(u32) -> u32 // T就是个闭包，T 的 trait bound 指定了 T 是一个使用 Fn 的闭包。

{

calculation: T,

value: Option<u32>,

}

fn main() { // 内部函数

let x = 4;

fn equal_to_x(z: i32) -> bool { z == x } // 这里 报错 不能使用 x 函数不能上下文用外部值，闭包可以

let equal_to_x = |z| z == x; // 这就可以，捕获其环境并访问其被定义的作用域的变量

let y = 4;

assert!(equal_to_x(y));

}

fn main() {

let x = vec![1, 2, 3];

let equal_to_x = move |z| z == x; // x 被移动进了闭包，因为闭包使用 move 关键字定义。闭包获取了 x 的所有权，main 不再允许使用 x 。去掉 println! 即可。

println!("can't use x here: {:?}", x);

let y = vec![1, 2, 3];

assert!(equal_to_x(y));

}
```



<br><br> 

**迭代器（iterator）**

负责遍历序列中的每一项和决定序列何时结束的逻辑。

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1. iter();

for val in v1_iter {

println!("Got: {}", val);

}

trait Iterator { 迭代器都实现了这个trait特性

type Item;

fn next(&mut self) -> Option<Self::Item>; // methods with default implementations elided

}

let mut v1_iter = v1.iter(); // v1_iter 需要是可变的

assert_eq!(v1_iter.next(), Some(&1)); //next之后处理结果

如果我们需要一个获取 v1 所有权并返回拥有所有权的迭代器，则可以调用 into_iter 而不是 iter。

如果我们希望迭代可变引用，则可以调用 iter_mut 而不是 iter。

调用 next 方法的方法被称为 消费适配器（consuming adaptors）

let v1_iter = v1.iter();

let total: i32 = v1_iter.sum(); // 调用 sum 之后不再允许使用 v1_iter 因为调用 sum 时它会获取迭代器的所有权。

let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1.iter().map(|x| x + 1).collect(); // 闭包+1后返还给Vec<...> v2

// collect 方法。这个方法消费迭代器并将结果收集到一个数据结构中。
```





 

**宏--结构比较复杂较难理解**

两种宏：

声明式宏（ declarative macro ）来进行元编程（metaprogramming）；

过程式宏（ procedural macro ）来自定义 derive traits | 更像函数（一种过程类型）

 

导入

```rust
#[macro_use] // 告诉编译器读取所有模块下的宏，这里就能区分重名

extern crate serde;

一个宏定义（声明式宏）

#[macro_export] // 定义 宏 体

macro_rules! strfrom { // 定义宏名 strfrom ，这个宏是将 一个字符串数组 加空格 组合成一个String

( $( $x:expr ),* ) => { // 单边模式 ( $( $x:expr ),* ) 表示 要匹配 *（0个或多个）个$x:expr模式

{

let mut temp_str = String::from(""); //创建一个字符串变量

$( // 宏替换的块

temp_str.push_str($x); // 提前换的具体操作

temp_str.push(' ');

)* // 0个或者多个宏替换块

temp_str // 表达式返回

}

};

}
```

