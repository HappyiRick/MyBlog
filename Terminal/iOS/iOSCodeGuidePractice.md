# Clang-format结合Xcode File-template、Code Snippet探索iOS代码规范实践

> 代码规范是每一个开发小组在实践中的一个痛点，如何让队伍中尽可能多的人遵循同一套代码风格，产出高质量的代码，同时能够尊重每位开发者的编程习惯，不增加冗余环节，是值得每个工程师思考的问题

在本文中，将利用Clang-format工具结合Xcode自带文件模版、Code Snippet探索iOS代码规范实践

<!-- toc -->

## Clang-format

> ClangFormat describes a set of tools that are built on top of LibFormat. It can support your workflow in a variety of ways including a standalone tool and editor integrations.

Clang-format 是一个代码格式化工具，能够为C/C++/Java/JavaScript/JSON/Objective-C/Protobuf/C#提供格式化规则

### 安装clang-format
--------
#####通过homebrew下载

```
brew install clang-format
```

#####查看是否安装成功

```
clang-format --version
```

### 添加clang-format服务
--------
在 __启动台__ >> __其他__ >> __自动操作__ 中选择 __快速操作__

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628663.png">

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628664.png">

##### 脚本代码

```
export PATH=/usr/local/bin:$PATH
clang-format
```
保存服务并命名，例如保存为 __Xcode-clang-format__  （很重要,后面还要用）

### clang-format使用

在当前用户根目录`～` 放入	`.clang-format` 文件

```
touch ~/.clang-format
```
下载链接 [.clang-format](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fhuipengo%2Fclang-format)

具体参数意义详见 [clang-format参数详解](https://www.cnblogs.com/PaulpauL/p/5929753.html)

### 添加clang-format快捷键

__系统设置__ >> __键盘__ >> __快捷键__ >> __APP快捷键__ >> __Xcode.app__ 添加服务 __Xcode-clang-format__ （之前保存的服务名）设置快捷键  __Control__ + __I__ 

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628666.png">

快去工程里试试吧

__参考资料__

1. [clang-format](https://www.jianshu.com/p/97ac40a78300)
2. [clang-format官方自定义参数介绍](https://www.cnblogs.com/PaulpauL/p/5929753.html)

## Xcode File-template

__Xcode的文件模板路径一般在下面这个目录__

`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/Xcode/Templates`

__所有的模板文件即存在File Template/iOS/Source中__

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628673.png">


复制 __source__ 文件夹，重命名为 __CustomTemplate__ ，即为自定义的文件模板分区

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628671.png">

其中，又分为 __Swift__ 和 __OC__ 以及带XIB文件的文件夹，其中的 __.h__ 和 __.m__ 文件即为模板文件

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628670.png">

以 __OC__ 的 __ViewController__ 为例

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628672.png">

新建 __CustomTemplate__ 下的 __ViewController__ 文件

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628669.png">

建立好的.m文件

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628668.png">

通过模板，即可实现代码分区和一部分固定方法的重写实现

__参考资料__

1. [Apple宏参数文档](https://help.apple.com/xcode/mac/9.0/index.html?localePath=en.lproj#/dev7fe737ce0)
2. [Xcode模板和Code Snippet](https://www.jianshu.com/p/376f372497b5)

## Code Snippet

新建 __Code Snippet__

<img src="https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203171628667.png">

通知、Observer、懒加载、创建单例、贝塞尔曲线等格式化代码，均可通过上述方式存储起来

<!-- endtoc -->









