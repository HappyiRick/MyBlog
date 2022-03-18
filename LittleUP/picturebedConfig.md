# Github+PicGo+jsDelivr创建稳定图床

> 图床是用来存储图片资源用于blog或者其他应用的网络资源库，对于个人blog来说，稳定长期且经济适用的图床非常重要

主要涉及三个服务

* Github为我们提供稳定的站点
* PicGo用来作为图床配置，管理图床图片
* jsDelivr是开源的CDN服务，用来加速图片访问

<!-- toc -->

## 1.Github配置

### 1.1 申请图床仓库

![image-20220317210158594](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203172103031.png)

### 1.2 申请Personal Token

到 __Setting--Developer settings--Personal access tokens__申请新的token，申请完之后记得保存

![image-20220317210812787](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203172108137.png)

## 2.PicGo安装

[PicGo release 传送门](https://github.com/Molunerfinn/PicGo/releases)

前往PicGo的Github地址下载并安装PicGo

![image-20220317211132992](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203172111780.png)

## 3.PicGo配置

[JSDELIVR](https://www.jsdelivr.com/) 

### 我的配置

![image-20220317211627316](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203172116298.png)

__其中，指定存储路径之后需要带`/`以创建路径__

### 打开时间戳设置

__在图床上传时，可能会出现重名情况，因此打开时间戳重命名的话，能有效避免这一问题__

![image-20220317211840104](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203172118655.png)

### 从相册中获取图片链接

![image-20220317211840104](https://cdn.jsdelivr.net/gh/HappyiRick/Album/Blogimg/202203180929932.png)

## 总结

__以上，即为构建blog稳定图床的全过程.__

<!-- endtoc -->
