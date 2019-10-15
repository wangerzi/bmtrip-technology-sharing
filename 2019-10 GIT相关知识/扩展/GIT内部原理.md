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

`a.txt` 和 `b.txt` 有差异，使用 

## Git的文件结构是什么？.git 里边到底存放了什么？

我们在执行 `git init` 之后，对应路径会出现一个 `.git` 的隐藏文件夹，Git的隐藏的秘密就在里边。

#### Git初始化

首先，找一个文件夹执行一下 `git init`

```shell
$ git init gitTest
Initialized empty Git repository in D:/git/gitTest/.git/
```

#### 文件结构

##### hooks 文件夹

GIT HOOK，用于在个GIT的各个过程节点执行脚本，比如提交前/推送前/更新前等节点，均可以自定义执行脚本，可以做到提交前本地自动检查代码，进行单元测试、推送后自动通知服务器更新代码等功能。

##### info 文件夹

包含一些配置信息，比如 `except` 可以用于存一些跳过跟踪的文件配置

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

存储了所有的数据，相当于一个小的文件系统

##### ref 文件夹

保存引用信息，即分支信息

##### HEAD 文件

保存当前被检出的分支路径

```shell
$ cat .git\HEAD
ref: refs/heads/master
```

##### index 文件

保存暂存区信息

##### config 文件

##### description 文件

## Git是如何存文件的？Hash-Object 介绍

在 Git 数据库里，存储着纳入 Git 版本管理的所有文件的所有版本的完整镜像。Git 数据库是一个 `key-value` 模式的数据库，可以往里边插入任意类型的数据，然后把 **头部信息 + 文件内容** 做 `SHA-1` **得到一个 HASH值，称为key**，通过这个 `key` 可以查询到插入的数据。

Git数据库文件位于 `.git/objetcts/`，Key 的前两位作为文件夹名称，后38位作为文件名，存储内容即为文件内容。

### 举个栗子

#### Git初始化

`git init` ，初始化Git仓库，很基础就不必介绍了

```shell
$ git init gitTest
Initialized empty Git repository in D:/git/gitTest/.git/
```

#### Git数据库写入

数据库写入有一条底层命令：`git hash-object -w '这里是内容XXXXXX'`

```shell

```

#### Git数据库的查询操作





概念介绍之后，可以结合实际写一些demo

### 第一步 XXX

首先进行，xxxxxx

```shell
echo "示例代码"
```

### 第二步 XXX

然后进行，xxxxxx

```shell
echo "示例代码"
```

### 第三步 XXX

然后进行，xxxxxx

```shell
echo "示例代码"
```

### 得到结果

最后，xxxxxx

```shell
echo "示例代码"
```

## 附录

#### 讲述人

XXX

#### 参考链接

- [深入理解Git的实现原理](https://www.cnblogs.com/mamingqian/p/9711975.html)

- [Git工作原理、基本操作](https://www.jianshu.com/p/f23f1af55708)