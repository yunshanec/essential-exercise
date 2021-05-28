## Linux 常用命令

### ls 命令 （用于列举目录下的文件）

1. sudo reboot 重启计算机
2. ls -a 列出目录所以文件，包含隐藏的文件
3. ls -l 将文件的权限、所以者、文件大小、可读可写等详细信息列出

### cd命令  （用于切换目录）

1. cd [目录名]     切换当前目录到所需要的目录下
2. cd /     进入根目录
3. cd -    进入上一次的工作路径

### pwd 命令  （用于查看当前的工作目录路径）

1. pwd  查看当前路径

### mkdir命令   (用于创建文件夹)

1. mkdir [文件夹名字]
2. mkdir -p [新建文件的路径]   在指定文件夹下创建文件

### rm命令 （用于删除一个或多个文件或目录）

1. rm -i *.log    删除所以.log文件，删除前逐一确认
2. rm -rf [文件路径]     删除路径下所有文件
3. re -rf [文件夹]   删除文件夹子目录以及子目录中所有的文档，不一一确认
4. re -- -f*   删除以-f开头的文件

### chmod 命令  （用于改变和控制Linux系统文件或目录的访问权限）

权限范围：

u ：目录或者文件的当前的用户
g ：目录或者文件的当前的群组
o ：除了目录或者文件的当前用户或群组之外的用户或者群组
a ：所有的用户及群组

权限代号：

r ：读权限，用数字4表示
w ：写权限，用数字2表示
x ：执行权限，用数字1表示

-：删除权限，用数字0表示
s ：特殊权限

*chmod 【权限范围】+【权限代号】 文件名*

1. 譬如：chmod a+x test.log 增加文件test.log 所有用户可执行权限





### mv 命令 （用于移动或修改文件名）

1. mv test.log test.txt  将文件test.log重命名为test.txt
2. mv log1.txt log2.txt /test  将文件log1.txt log2.txt 移动到test文件夹下



### dpkg (用于安装、删除、构建、管理Debian软件包）

1. sudo dpkg -i [.deb file name]      安装软件包

2. sudo dpkg -R [文件夹目录]   安装文件夹下的所有软件包

3. sudo dpkg -r [软件包]    删除软件包

4. sudo dpkg --list   查看已安装的软件

5. sudo apt-get --purge remove  [软件名]   删除安装的软件

   



### apt（软件包管理器）（需要root权限）（提供了查找、安装、升级、删除某一个、一组甚至全部软件包的命令）

1. sudo apt update 列出所有可更新的软件清单
2. sudo apt upgrade 升级软件包
3. sudo apt install [package_name]  安装指定的软件包
4. sudo apt install package1 package2...  安装多个软件包
5. sudo apt remove【package_name】 移除软件包
6. sudo apt autoremove   清除不再使用的依赖和库文件

### ln  (用于为文件在另一个位置建立一个同步的链接)

(如果文件重命名，链接文件里的内容会消失)

1. ln -sv source.log link.log   给文件创建软连接，并显示操作信息
2. ln -v source.log link.log    给文件创建硬链接，并显示操作信息
3. ln -sv [目录] 给目录创建软连接



【软连接】

- 1.软链接，以路径的形式存在。类似于Windows操作系统中的快捷方式
- 2.软链接可以 跨文件系统 ，硬链接不可以
- 3.软链接可以对一个不存在的文件名进行链接
- 4.软链接可以对目录进行链接

【硬链接】

- 1.硬链接，以文件副本的形式存在。但不占用实际空间。
- 2.不允许给目录创建硬链接
- 3.硬链接只有在同一个文件系统中才能创建

### touch (用于新建文件)

touch [newfile_name] 创建新的文件

gedit [file_name] 编辑文件

### scp (用于复制文件和目录)

### ssh (用于远程连接服务器)

