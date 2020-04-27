# csc1001 CART

#### 介绍
This is for the csc1001 group project.


#### git教程

1.  安装git   https://www.liaoxuefeng.com/wiki/896043488029600/896067074338496

2.  使用 git clone 拷贝一个 Git 仓库到本地，让自己能够查看该项目，或者进行修改。
如果你需要与他人合作一个项目，或者想要复制一个项目，看看代码，你就可以克隆那个项目。
如何打开Git Bash：Windows键 输入Git 选择Git Bash打开
打开Git Bash输入：
```
cd /d/                                       #切换到d盘根目录（为保证环境一致请不要切换成不同的目录）
git clone https://gitee.com/fourdim/CART.git #从云上克隆并初始化仓库
```
输入用户名密码
如果输入错了 请打开\控制面板\用户帐户\凭据管理器\Windows凭据修改
克隆完成后，在d盘下会生成一个CART目录

3.  打开Git Bash输入
```
cd /d/CART/ # 切换到csc1001目录
code .         # 自动打开VSCODE，没有VSCODE的请下载一个 注意有一个空格有一个点
```

4.  如何同步云上内容（建议每次修改代码前同步一次）打开Git bash或者vscode里面的Terminal输入
```
git pull origin master
```

5.  如何把代码送到云上
```
git add
# 加入到暂存区 与左侧第三栏的叉子形状图标中的加号作用相同
git commit -m 'Fix a bug.'
# 提交到本地库 与左侧第三栏的叉子形状图标中的挑号作用相同 在提交时请添加本次修改的注释（引号内内容）。
# 或者在vscode中挑下面的黑框添加注释再点挑号
git push
# 发送给远程库 与左侧第三栏的叉子形状图标中的···号里的push作用相同
```

6.  更多不会的内容怎么办
- 先查教程
  - Kinely的[Git教程](https://bb.cuhk.edu.cn/webapps/blackboard/execute/content/file?cmd=view&content_id=_74890_1&course_id=_2602_1)  (需要登陆后获取)
  - 码云官方提供的 [使用手册](https://gitee.com/help)
  - [廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/896043488029600)
  - [Runoob的git教程](https://www.runoob.com/git/git-tutorial.html)
  - vscode 与 gitee 联合使用 [教程](https://blog.csdn.net/watfe/article/details/79761741)
- 为什么不问问万能的搜索引擎呢
- 再来问我

