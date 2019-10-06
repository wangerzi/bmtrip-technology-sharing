## 分享内容顺序

Git、Nginx、Redis、MySQL、Docker

## 分享模式

每个内容可以有多个分享，一次分享周期为两周，参与人员分为：主讲人、参与人

第一周：主讲人整理并输出分享纲要以及相关材料文档

第二周：主讲人、参与人根据纲要商讨各自分享的部分，共同完成『分享文档』，所有参与的人需要在分享准备过程中了解整个分享内容，分享过程中进行讨论

## 分享文档编写

所有文档使用 gitbook 编写，以便于目录索引以及日后查阅

### 初次分享的准备工作

#### 安装 npm

首先安装 npm，请前往 [https://nodejs.org/#download ](https://nodejs.org/#download ) 下载最新版本，然后设置镜像源

```shell
npm config set registry https://registry.npm.taobao.org
```

#### 安装gitbook

使用 -g 表示全局安装，安装完毕后全局区出现可执行脚本 `gitbook`，使用 `gitbook -V` 查看版本信息

```shell
$ npm install gitbook-cli -g
$ gitbook -V
CLI version: 2.3.2
GitBook version: 3.2.3
```

PS:第一次执行 gitbook -V 会安装GitBook ，如果没有梯子等待时间超长

更多 GitBook 上手请见博客：[https://blog.csdn.net/lu_embedded/article/details/81100704](https://blog.csdn.net/lu_embedded/article/details/81100704)

### 每次分享准备工作

#### 初始化分享目录

首先建立一个分享目录，规则如下：创建时间月份-分享内容描述（如：2019-10 GIT相关知识）

执行如下命令，初始化 gitbook 信息

```shell
$ gitbook init
warn: no summary file in this book
info: create README.md
info: create SUMMARY.md
info: initialization is finished
```

维护 README.md(分享简介) 以及 SUMMARY.md(目录结构信息)，先维护目录信息，然后执行 `gitbook init` 即可自动生成对应文件

```shell
$ gitbook.cmd init
info: create Git基础/README.md    
info: create Git基础/Git对象概念整理.md 
info: create Git基础/基础操作.md      
info: create Git分支/README.md    
......      
info: create SUMMARY.md         
info: initialization is finished
```

#### 准备大纲，确定讲解内容

生成文件后，首先将大纲发给参与者共同讨论增加/删除，确认分享内容后主讲人为每个大标题补上简介及参考链接

#### 大纲结构

目录大纲的内容分为前言、介绍章节、扩展三个部分，前言仅做分享内容概要、分享人等记录，介绍章节为具体分享内容，扩展是平时工作中用得少，但是看完可以加深了解的知识，比如：实现原理、面试题、冷门用法等

#### 补全文档

根据参考链接，补全demo以及概念知识点，全部完成后开始讨论

#### 讨论结束

讨论结束后，主讲人根据讨论，维护文档即可，主讲人按顺序轮替

#### 分享内容模板

每个分享内容遵循[示例模板](分享内容模板.md)
