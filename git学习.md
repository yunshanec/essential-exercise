## g i t学习

### Git的工作流程：

1. 克隆 Git 资源作为工作目录。
2. 在克隆的资源上添加或修改文件。 
3. 如果其他人修改了，你可以更新资源。
4. 在提交前查看修改。
5. 提交修改。
6. 在修改完成后，如果发现错误，可以撤回提交并再次修改并提交。

<img src="/home/lpf/Desktop/NoteBooks/git-process.png" style="zoom:80%;" />

### Git 工作区、暂存区（索引index）和版本库

![](/home/lpf/Desktop/NoteBooks/git.jpg)

- 工作区：在电脑里能看到的目录
- 暂存区（stage / index）：一般存放在.git目录下的index文件(.git/index)中，所以我们把缓存区有时也叫索引。
- 版本库：工作区有一个隐藏目录 .git,这个不算工作区,而是Git的版本库。



### Git基本操作

Git 的工作就是创建和保存你项目的快照及与之后的快照进行对比。

![git-command](/home/lpf/Desktop/NoteBooks/git-command.jpg)

- workspace: 工作区
- staging area：暂存区
- local repository：版本库/本地仓库
- remote repository ：远程仓库

#### 创建仓库命令

- git init 命令用于在目录中创建新的Git仓库
- git clone [url]  拷贝一个Git仓库到本地

#### 提交与修改

git add  可将文件添加到暂存区

- git add [file1] [file2]...   添加一个或多个文件到暂存区
- git add [dir]  添加指定目录到暂存区
- git add . 添加当前目录下的所有文件到暂存区

git status  用于查看仓库的状态，显示变更的文件

- ​	git statuas -s 来获取简短的输出结果

git diff 比较文件的不同，即比较文件在暂存区和工作区的差异

- 尚未缓存的改动：git diff  [文件]
- 查看已缓存的改动： git diff --cached 【文件】
- 查看已缓存的与未缓存的所有改动：git diff HEAD
- 显示摘要而非整个 diff：git diff --stat

​	

git commit 提交暂存区内容到本地仓库中

- git commit -m [message] 提交暂存区内容到本地仓库，其中【message】可以是一些备注信息。
- git commit  [file1] [file2]... -m [message]  用于提交指定文件到本地仓库区

git reset 用于回退版本，可以指定退回某一次提交的版本。

```
git reset [--soft | --mixed | --hard] [HEAD]
```

- git reset HEAD^    回退所有内容到上一个版本
- git reset HEAD^ [filename] 回退filename文件到上一个版本
- git reset 052e 回退到052e版本（会退到指定版本）

​    

git rm 删除工作区文件

- git rm [file] 将文件从暂存区和工作区中删除
- git rm -f [file] 强行删除(如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 )
- git rm --cached [file] 移动或重命名工作区文件(文件从暂存区移除，但工作区保留)

git mv 用于移动或重命名一个文件、目录或软连接

- git mv [file] [newfile]

#### 提交日志

- git log 查看历史提交记录
- git log [file] 查看指定文件的历史提交记录
- git blame [file]  以列表形式查看指定文件的历史修改记录





#### 远程操作

git remote 用于远程仓库操作

- git remote -v 显示所有远程仓库
- git remote show 【https://github.com/yunshanec/Git-】 显示某个远程仓库的信息
- git remote add [shortname] [url]  添加远程版本库
- git remote rm name 删除远程仓库



git fetch 从远程获取代码库

- 当版本库做更改后，怎么同步到本地
- ​	git fetch origin 在本地更新
- ​	git merge origin/main   用于将更新同步到本地

git pull 用于从远程获取代码并合并到本地的版本

- git  pull [远程主机名] [远程分支名]：[本地分支名]
- git pull origin main : git_learning  将远程主机 origin 的  main 分支拉取过来，与本地的git_learning 分支合并。
- git pull origin main 远程分支是与当前分之合并，冒号后面的部分可以省略

git push 用于将本地的分之版本上传的远程并合并

- git push [远程主机名] [本地分支名] ： [远程分支名]
- 如果本地分支名与远程分支名相同，则可以省略 ：git push [远程主机名] [本地分支名] 



​	



























