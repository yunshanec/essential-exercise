from pathlib import Path

def get_tree(path,n=0):
    global tree_str
    #创建对象
    
    if path.is_file():
        tree_str += '    |' * n + '—' * 4 + path.name + '\n'
    elif path.is_dir():
        tree_str += '    |' * n + '—' * 4 + str(path.relative_to(path.parent)) +'\n'
        for i in path.iterdir():
            get_tree(i,n+1)

if __name__ == "__main__":
    tree_str = ''
    p = Path("D:/learnRR")
    get_tree(p)
    print(tree_str)
    
    




