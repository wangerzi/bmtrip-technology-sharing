# GIT内部原理

## 从 diff 说起，代码差异是如何被找出来的

Linux 下有一个命令 `diff` 可用于查找两个文件中的差异，命令描述如下：

> diff [选项] … [文件1或目录1][文件2或目录2]（四种组合方式）
> 说明：diff命令在最简单的情况下，比较两个文件的不同。如果使用”-”代替文件参数，则要比较的内容将来自标准输入。Diff命令是以逐行的方式比较文本文件的异同之处。如果指定比较的是目录的时候，diff命令会比较两个目录下名字相同的文本文件，但不会比较其中子目录。列出不同的二进制文件、公共子目录和只在一个目录出现的文件

### 举个栗子

比如现在有两个文件 `a.txt`, `b.txt` 内容如下：

`a.txt`

> 老人和牛渐渐远去，我听到老人粗哑的令人感动的嗓音在远处传来，他的歌声在空旷的傍晚像风一样飘扬
>
> 老人唱道：
> 少年去游荡，
> 中年去掘藏，
> 老年做和尚。

`b.txt`

> 老人和牛渐渐远去，我听到老人粗哑的令人感动的嗓音在远处传来，他的歌声在空旷的傍晚像风一样飘扬
>
> 老人说道：
> 少年做开发，
> 中年做产品，
> 老年做和尚。

`a.txt` 和 `b.txt` 有差异，使用 `diff -u a.txt b.txt` 可查看差异

## 什么是底层命令，什么是高层命令？

底层命令(plumbing)和高层命令(procelain)，底层命令主要是为工具和自定义脚本服务的，高层命令更为友好方便，是底层命令的封装。

## Git的文件结构是什么？.git 里边到底存放了什么？

我们在执行 `git init` 之后，对应路径会出现一个 `.git` 的隐藏文件夹，Git的隐藏的秘密就在里边。

#### Git初始化

首先，找一个文件夹执行一下 `git init`

```shell
$ git init gitTest
Initialized empty Git repository in D:/git/gitTest/.git/
```

#### 文件结构

```shell
HEAD
config
description
hooks/
index
info/
objects/
refs/
```

##### hooks 文件夹

GIT HOOK，用于在个GIT的各个过程节点执行脚本，比如提交前/推送前/更新前等节点，均可以自定义执行脚本，可以做到提交前本地自动检查代码，进行单元测试、推送后自动通知服务器更新代码等功能。

##### info 文件夹

包含一些配置信息，比如 `except` 可以用于存一些跳过跟踪的文件配置，并且这里的配置不在 `.gitignore` 中管理

```shell
$ cat .git\info\exclude
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```

##### objects 文件夹

存储了所有的数据，相当于一个小的文件系统，hash 值的前两位作为子文件夹名称，后38位作为文件名。

##### ref 文件夹

保存引用信息，比如本地/远程分支信息、stash信息、标签信息，比如本地 master 分支就会被保存为 `.git/refs/head/master`，远程 master 分支会被保存为 `.git/refs/origin/master`

##### HEAD 文件

保存当前被检出的分支路径

```shell
$ cat .git\HEAD
ref: refs/heads/master
```

##### index 文件

保存暂存区信息

##### config 文件

项目特有的配置文件信息

##### description 文件

仅供 GitWeb 程序使用，看文件内容是用来写Git包名字的

## Git是如何存文件的？Hash-Object 介绍

在 Git 数据库里，存储着纳入 Git 版本管理的所有文件的所有版本的完整镜像。Git 数据库是一个 `key-value` 模式的数据库，可以往里边插入任意类型的数据，然后把 **头部信息 + 文件内容** 做 `SHA-1` **得到一个 HASH值，称为key**，通过这个 `key` 可以查询到插入的数据。

Git数据库文件位于 `.git/objetcts/`，Key 的前两位作为文件夹名称，后38位作为文件名，存储内容即为文件内容。

### 底层命令：

#### hash-object

作用：用于将文件存放于 Git 数据库中，并返回索引

使用：

```shell
echo "Hello World" > temp
git hash-object -w temp
```

也可以简化一下，用管道 + 标准输入的方式

```shell
echo "Hello World" | git hash-object -w stdin
```

重复的文件只会记录一次，比如：

```shell
$ echo "Hello" | git hash-object -w --stdin
010b3da57a0903855537d02ddcc4d63396515190

$ echo "Hello" | git hash-object -w --stdin
010b3da57a0903855537d02ddcc4d63396515190
```

### cat-file

作用：用于通过索引查找文件，PS：HASH的值至少写四位

使用：

查看文件内容用 -p

```shell
$ git cat-file -p 7aca
"Hello World!"
```

查看文件类型用 -t，使用 hash-object 存入的文件对象是 blob 类型的

```shell
$ git cat-file -t 010b
blob
```

通过这两个命令就可以实现一个简单的版本控制了，比如我先改了，比如先写了一版 `论如何与产品相处.md` ，使用 `hash-object` 之后返回hash `x`，然后根据编辑意见做了一些改动，再使用 `hash-object` 保存变动后的文件，得到第二个版本的hash `x`，但是主编看了不满意，说要改回第一版，这时候使用 `cat-file` 将文件恢复即可。

具体指令如下：

```shell

```





## 附录

#### 讲述人

王杰

#### 参考链接

- [深入理解Git的实现原理](https://www.cnblogs.com/mamingqian/p/9711975.html)
- [Git工作原理、基本操作](https://www.jianshu.com/p/f23f1af55708)
- [Git详解之内部原理](https://www.cnblogs.com/guge-94/p/11288154.html)