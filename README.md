# csc1001

#### 介绍
This is for the csc1001 group project.


#### git教程

1.  安装git   https://www.liaoxuefeng.com/wiki/896043488029600/896067074338496
2.  制作公私钥 
3.  公钥上传到自己的git账户

#### 制作公私钥

1.  安装好git后按windows键输入git bash打开
2.  输入ssh-keygen回车 位置使用默认位置 密码可填写可不填写（这个密码不会泄露到网上，所以如填写密码请使用自己记得住的密码）
3.  c盘->用户->自己的用户名->.ssh 如果找不到.ssh请参看[如何查看隐藏文件](https://jingyan.baidu.com/article/5552ef47a4424c518ffbc9fc.html)
在文件夹里找到id_rsa.pub复制其中的内容，按照[教程](https://gitee.com/help/articles/4191#article-header0)添加到个人账户里

#### 使用vscode直接推送代码到云上

1.  在vscode中新建一个文件夹作为工作目录
2.  在控制台（终端输入）
```
git remote add origin https://gitee.com/fourdim/csc1001.git
```
3.  如何拉取云上内容
```
git pull origin master
```
4.  如何把代码送到云上
```
git add     # 加入到暂存区
git commit  # 提交到本地库
git push    # 发送给远程库
```
5.  更多不会的内容怎么办
- 先查教程
  - vscode 与 gitee 联合使用 [教程](https://blog.csdn.net/watfe/article/details/79761741)
  - [廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/896043488029600)
  - [Runoob的git教程](https://www.runoob.com/git/git-tutorial.html)
- 为什么不问问万能的搜索引擎呢
- 再来问我

#### 码云特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5.  码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
