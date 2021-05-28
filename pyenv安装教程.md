## pyenv安装教程

### 1.安装git

1. 安装git  sudo apt install git

### 2.克隆项目，放在家目录下的隐藏文件夹中：.pyenv

1. git clone https://github.com/pyenv/pyenv.git ~/.pyenv

### 3.将一下内容放到 .bashrc的最后

1. echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
2. echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
3. echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

### 4.激活pyenv

1. source .bashrc

### 5.安装Python依赖包

1. sudo apt-get install make build-essential libssl-dev zlib1g-dev
2. sudo apt-get install libbz2-dev libreadline-dev libsqlite3-dev wget curl
3. sudo apt-get install llvm libncurses5-dev libncursesw5-dev
4. sudo apt-get update

### 6.查看可以安装的python版本

1. pyenv install --list

### 7.安装python3.6.13(示例)

1. pyenv install 3.6.13

### 8.查看安装的python版本

1. pyenv versions

### 9.更新数据库

1. pyenv rehash

### 10.切换python版本

pyenv local xxx

### 10.卸载python3.6.13版本（示例）

1. pyenv uninstall 3.6.13

### 11.卸载pyenv

1. rm -rf ~/.pyenv



