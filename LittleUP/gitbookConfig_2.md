# Gitbook配置，开启写作之路 (下)

在本文中，将使用Gitbook + Github pages搭建属于自己的Blog，终端环境为zsh，设备为Macbook. 

> 上一篇中，我们讲了Gitbook的安装、构建及启动服务，这样只是完成了gitbook的本地化工作，如果我们想让更多人看到我们的电子书，就需要将其部署在公共服务器上了。对于个人博客来说，还有一条更方便的路径，便是利用Github提供的pages功能及公开仓库来完成网络电子书的部署。

<!-- toc -->

## 1.Github pages搭建

### 1.1 建立github pages仓库

仓库名称必须为 <你的github名称>.github.io

![image-20220303155540913](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203031729720.png)

### 1.2 设置主页

进入```<your name>.github.io```仓库，点击```Settings``` > ```Pages``` >> ```Theme chooser``` 

然后就可以选择一个jeklly提供的模板主题，同时，github会默认建立名为```gh-pages``` 的部署分支，其即为我们个人主页静态资源的部署分支. 当然，也可以选择fork其他自定义主题的仓库. 

![image-20220303160813268](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203031729414.png)

稍等两分钟之后，访问[https://<your github name>.github.io](https://happyirick.github.io/) 即可访问你的个人github主页.

## 2.建立Gitbook博客仓库

这部分无需赘言，即在github上建立一个存放gitbook内容的公共仓库，然后在本地gitbook目录中绑定该仓库，新建gh-pages分支用作静态资源部署分支，实现gitbook的版本管理和网络部署，其主要流程如下

1. 新建github仓库
2. 进入本地gitbook目录下, 并执行以下命令
   1. <code>git init </code>
   2. <code>git remote add origin xxx.git </code>
   3. <code>git checkout -b gh-pages</code> # 新建本地分支
   4. <code>git push --set-upstream origin gh-pages</code> # 绑定远端分支，若没有则新建
3. 在该仓库github中进入```Setting``` > ```Pages``` >```Source``` , 选择gh-pages作为部署分支

## 3.通过Github Actions实现自动部署

Actions是Github提供的一款CI工具，可以很便利地在我们提交代码后进行一些脚本操作，对于gitbook来说，我们在写完文档之后，还需要进行生成目录、构建、将生成的静态网页提交到部署分支上，这些工作都可以通过脚本来自动化完成。以前主流方法是通过Travis来做，随着Actions的发布，基于github pages的博客自动部署都可以更加便利地使用它来完成。

### 3.1 新建token

首先从 ```Setting``` > ```Developer Settings```>```Personal access tokens```

 生成用于仓库访问的token，仅选择repo读的权限即可 （记得保存，仅会出现一次）

![image-20220303170547919](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203031729415.png)

### 3.2 新建Actions脚本

1. 首先进入gitbook部署仓库```Settings``` > ```Security``` > ```Actions``` 新建secret，命名为TOKEN, 值为第二步中的personal access token生成的字符串

   ![image-20220303171104060](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203031729416.png)

2. 进入Actions, 新建脚本

   ![image-20220303171216302](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203031729418.png)

3. 部署脚本代码如下

   ```yaml
   name: auto-generate-gitbook
   on:                                 #在master分支上进行push时触发  
     push:
       branches:
   
      - master
   
   jobs:
     main-to-gh-pages:
       runs-on: ubuntu-latest
   steps:                          
   - name: checkout master
     uses: actions/checkout@v2
     with:
       ref: master
           
   - name: install nodejs
     uses: actions/setup-node@v1
     
   - name: configue gitbook
     run: |
       npm install -g gitbook-cli          
       gitbook install
               
   - name: generate _book folder
     run: |
       gitbook build
               
   - name: push _book to branch gh-pages 
     env:
       TOKEN: ${{ secrets.TOKEN }}
       REF: github.com/${{github.repository}}
       MYEMAIL: xxx@xx.com                  # ！！记得修改为自己github设置的邮箱
       MYNAME: ${{github.repository_owner}}          
     run: |
       cd _book
       git config --global user.email "${MYEMAIL}"
       git config --global user.name "${MYNAME}"
       git init
       git remote add origin https://${REF}
       git add . 
       git commit -m "Updated By Github Actions With Build ${{github.run_number}} of ${{github.workflow}} For Github Pages ${REF}"
       git branch -M master
       git push --force --quiet "https://${TOKEN}@${REF}" master:gh-pages
   ```

这样每次push之后，Actions上便会自动执行该脚本，失败则会给所填写的邮箱发送邮件提醒，整体来说还是非常高效的

## 总结

通过两篇文章阐述了利用Gitbook+Github pages搭建博客的过程，做一下记录，也希望能够帮到有需要的人

> 有些事情还是要试一试才知道，其实并没有那么难，只是我们一直在被自己对于未知的恐惧所支配

## 参考链接

[github actions 简易入门及自动部署博客实践](https://zhuanlan.zhihu.com/p/93829286)

<!-- endtoc -->
