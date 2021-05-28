## python基础知识

### 列表

| list.index(obj)         | 从列表中找出某个值第一个匹配项的索引位置                     |
| ----------------------- | ------------------------------------------------------------ |
| list.insert(index, obj) | 将对象插入列表                                               |
| list.pop(obj=list[-1])  | 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| list.reverse()          | 反向列表中元素                                               |
| list.sort([func])       | 对原列表进行排序                                             |



### 循环控制语句

| 循环控制语句 | 描述                                                         |
| ------------ | :----------------------------------------------------------- |
| break        | 在语句块执行过程中终止循环，并且跳出循环                     |
| continue     | 在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环 |
| pass         | pass 是空语句，是为了保持程序结构的完整性                    |



### 函数的参数

不定长参数：

1. 有些时候，我们在设计函数的时候，我们有时候无法确定传入的参数个数。
2. 那么我们就可以使用不定长参数。
3. Python 提供了一种元组的方式来接受没有直接定义的参数。这种方式在参数前边加星号 * 。
4. 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。

```python
def print_user_info(name, age, sex = "man", *hobby):
    print("昵称：{}".format(name), end=' ')
    print("年龄：{}".format(age), end= " ")
    print("性别：{}".format(sex), end= " ")
    print("爱好：{}".format(hobby))
if __name__ == "__main__":
    print_user_info("木子李",18,"女","乒乓球","篮球","足球")

>>>昵称：木子李 年龄：18 性别：女 爱好：('乒乓球', '篮球', '足球')
```

python 函数调用是，实参表由左到右就是简单的两个部分

function_name(【位置实参】，【关键字实参】)

关键字参数：

1. 编写一个可以接受任意数量的位置参数的函数，可以使用以*开头的参数。
2. 编写一个可以接受任意数量的关键字参数的函数，可以使用以**开头的参数。
3. 在函数定义中，以*打头的参数只能作为最后一个位置参数出现，而以**打头的参数只能作为最后一个关键字参数出现。

```python
def a(x,*args,y,**kwargs):
    pass
```

[函数参数]: https://www.zhihu.com/question/57726430



### 匿名函数

- lambda 的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
- lambda 函数有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
- 基本语法   lambda [arg1 [，arg2，arg3.........]] : expresion

```python
sum = lambda num1,num2,num3 : num1 + num2 + num3
print(sum(1,2))
>>>>3
```



### 迭代器

- 迭代器，一个可以记住遍历的位置的对象

- 迭代器只能前进不会后退
- 迭代器的两种基本方法：iter（）和next（），且字符串、列表或元组对象都可用于创建迭代器，迭代器对象可以使用常规的for语句进行遍历，也可以使用next ()函数来遍历。

```python
#字符串创建迭代器
str1 = “云杉ec”
iter1 = iter(str1)
for i in iter1:
    print(i,end= " ")
#列表创建迭代器
list1 = [1,2,3,4]
iter2 = iter (list1)
for i in iter2:
    print(i,end= " ")

#用元组来创建迭代器
tuple1 = (1,2,3)
iter3 = iter(tuple1)
while True:
    try:
        print(next(iter3))
    except StopIteration:
        break

```

### 生成器

```python
#一直向前不回头
def odd():
    print ( 'step 1' )
    yield ( 1 )
    print ( 'step 2' )
    yield ( 3 )
    print ( 'step 3' )
    yield ( 5 )

o = odd()

print(next(o))
```



```python
#反向迭代 reversed 函数
ls1 = [1,2,3,4]
for i in reversed(ls1):
    print(i)
>>>>4 3 2 1

# 同时迭代多个序列
ls1 = [1,2,3,4,5]
ls2 = [1,4,9,16,25]
ls3 = [1,8,27,64,125]
for i,j,k in zip(ls1,ls2,ls3):
    print(i,j,k)
>>>>1 1 1
	2 4 8
	3 9 27
	4 16 64
	5 25 125
####zip() 是可以接受多于两个的序列的参数，不仅仅是两个。
```



### 面向对象

1. 类方法，想要调用类属性，需要以下步骤：

- 在方法上面，用 `@classmethod` 声明该方法是类方法。只有声明了是类方法，才能使用类属性
- 类方法想要使用类属性，在第一个参数中，需要写上 `cls` ,  cls 是 class 的缩写，其实意思就是把这个类作为参数，传给自己，这样就可以使用类属性了。
- 类属性的使用方式就是 `cls.变量名`

​    无论是 `@classmethod` 还是 `cls` ,都是不能省去的。



2. 类方法传参数跟普通的函数一样，直接增加参数就好了。

示例如下：

![a](/home/lpf/Desktop/a.png)



3. 修改和增加类属性

   

```python
#从内部修改和增加类属性---从类方法来修改
class ClassB():
    var1 = 'asd'
    @classmethod
    def fun1(cls):
        print("原来的var1值为： "+ cls.var1)
        cls.var1 = input("请输入修改var1的值： ")
        print("修改后的var1值为： "+cls.var1)

ClassB.fun1()
>>>>>>>>>
原来的var1值为： asd
请输入修改var1的值： dsa
修改后的var1值为： dsa
```



```python
#从外部修改和增加类属性
class ClassC():
    var1 = "asd"
    @classmethod
    def fun1(cls):
        print("var1 值为： "+cls.var1)

ClassC.fun1()
ClassC.var1 = input("请输入修改var1的值： ")
ClassC.fun1()
>>>>>>>>>>>
var1 值为： asd
请输入修改var1的值： dsa
var1 值为： dsa

```

4. 类和对象

​    类的实例化和直接使用类 格式不同之处

1. 类方法里面没有了 `@classmethod` 声明了，不用声明他是类方法
2. 类方法里面的参数 `cls` 改为  `self`
3. 类的使用，变成了先通过 `实例名 = 类()` 的方式实例化对象，为类创建一个实例，然后再使用 `实例名.函数()` 的方式调用对应的方法 ，使用 `实例名.变量名` 的方法调用类的属性

类的实例化，类属性的修改，类方法的重写

```python
# 类的实例化
class ClassA(object) :
    var1 = "asd"
    def fun1(self) :
        print("var1值为： {}".format(self.var1))

        
# 实例化
a = ClassA()
#实例化之后使用它里面的方法
a.fun1()
#实例化之后使用它里面的属性
print(a.var1)

#改变类的属性
ClassA.var1 = "dsa"
print(a.var1)

#重写类方法
def newfun1(self):
    print("重写类的方法： {}".format(self.var1))

#修改类方法 注意函数不带括号
ClassA.fun1 = newfun1
b = ClassA()
b.fun1()

>>>>>>>>>>>>
var1值为： asd
asd
dsa
重写类的方法： dsa
```

5. 初始化函数

   初始化函数的意思是，当你创建一个实例的时候，这个函数就会被调用。

```python
class ClassD(object):
    #构造函数
    def __init__(self):
        print("实例化成功")
    #析构函数
    def __del__(self):
        print("实例化销毁了")

#实例化
d = ClassD()
#del可以删处一个对象
del d

>>>>>>>>>>>>>>
实例化成功
实例化销毁了
```



- [ ] ​		练习practice



```python
class Text(object) :
    def __init__(self, name, sex, nation,age) :
        self.name = name
        self.sex = sex
        self.nation = nation
        self.age = age
        print("实例化成功")

    def other_resume(self, date_of_birth, height) :
        print(date_of_birth, height)


text = Text("asd", "man", "Chinese",12)
text.other_resume("1998-3-2", 178)
print(text.name, text.sex, text.nation,text.age)

>>>>>>
实例化成功
1998-3-2 178
asd man Chinese 12
```



### 类的继承

```python
#单继承的语法
class ClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
‘‘‘
在定义类的时候，可以在括号里写继承的类，如果不用继承类的时候，也要写继承 object 类，因为在 Python 中 object 类是一切类的父类。
’’’
    
#多继承的语法
class ClassName(Base1,Base2,Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
“
多继承有一点需要注意的：若是父类中有相同的方法名，而在子类使用时未指定，python 在圆括号中父类的顺序，从左至右搜索 ， 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
”
```

继承的子类的好处：

1. 会继承父类的属性和方法
2. 可以自己定义，覆盖父类的属性和方法

```python
# 调用父类的方法
class Userinfo(object) :
    
    def __init__(self, name, age, account) :
        self.name = name
        self.age = age
        self.__account = account

    def get_account(self) :
        return self.__account


class Userinfo1(Userinfo) :
    pass


if __name__ == "__main__" :
    userinfo1 = Userinfo1("阿萨德", 23, 123455)
    print(userinfo1.get_account())
    print(userinfo1.name, userinfo1.age)
    
>>>>>>
123455
阿萨德 23
```



父类方法的重写

```python 
# 父类方法的重写
class Userinfo(object) :
    name = "dsa"

    def __init__(self, name, age, account) :
        self.name = name
        self.age = age
        self.__account = account

    def get_account(self) :
        return self.__account

    @classmethod
    def get_name(cls) :
        return cls.name

    @property
    def get_age(self) :
        return self.age


class Userinfo2(Userinfo) :
    #子类调用父类的__init__方法 使用Python内置的函数	super()
    def __init__(self, name, age, account, sex) :
        super(Userinfo2, self).__init__(name, age, account)
        self.sex = sex


if __name__ == "__main__" :
    userinfo2 = Userinfo2("阿萨德", 23, 123455,"man")
    #打印所有属性
    #print(dir(userinfo2))
    #打印构造函数中的属性
    print(userinfo2.__dict__)
    print(userinfo2.get_name())
    
>>>>>
{'name': '阿萨德', 'age': 23, '_Userinfo__account': 123455, 'sex': 'man'}
dsa
```



子类的类型判断 isinstance()函数



```Python
class User(object):
    pass

class User1(User):
    pass

if __name__ == "__main__":
    user = User()
    user1 = User1()
    print(isinstance(user1,user))

>>>>>>
True
```



### 类的多态

是指对不同类型的变量进行相同的操作，它会根据对象（或类）类型的不同而表现出不同的行为。

```python
class User(object) :
    def __init__(self, name) :
        self.name = name

    def printuser(self) :
        print("Hello " + self.name, end=' ')


class UserVip(User) :
    def printuser(self) :
        print("Hello 尊敬的vip用户： " + self.name)


class UserGeneral(User) :
    def printuser(self) :
        print("Hello 尊敬的用户：" + self.name)


def printuser_ino(user) :
    user.printuser()


if __name__ == "__main__" :
    uservip = UserVip("asd")
    printuser_ino(uservip)
    
    usergeneral = UserGeneral("阿萨德")
    printuser_ino(usergeneral)
    
>>>>>>>>>>>
Hello 尊敬的vip用户： asd
Hello 尊敬的用户：阿萨德

```





### 异常处理

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        print(x)
        break
    except (ValueError, TypeError):
        print("try中一旦检测到异常，就执行这个位置的逻辑")
        print("要输入数字呀！")
    except RuntimeError:
        print("要输入数字呀！")
    else:
        print("一切正常！")
    finally:
        print("无论是否发生异常都会执行这段代码\n")

print("输入正确才会显示")

>>>>>>
Please enter a number: ls
try中一旦检测到异常，就执行这个位置的逻辑
要输入数字呀！
无论是否发生异常都会执行这段代码

Please enter a number: 24
24
无论是否发生异常都会执行这段代码

输入正确才会显示

```



```python
#try;except;else;finally练习
def hannoi(n, a, b, c) :
    if n == 1 :
        print(a, "------>", c)
    else :
        hannoi(n - 1, a, c, b)
        hannoi(1, a, b, c)
        hannoi(n - 1, b, a, c)


if __name__ == "__main__" :
    while True :
        try :
            n = int(input("请输入圆盘的数目： "))
            hannoi(n, "A", "B", "C")
        except ValueError:
            print("请输入整数！")
        except RuntimeError:
            print("输入圆盘数目太多,运行超时！")
        else :
            print("没有发生异常才会执行else这条语句")
        finally :
            print("无论有没有异常都会执行的finally语句")
            
>>>>>>>>
请输入圆盘的数目： e3
请输入整数！
无论有没有异常都会执行的finally语句

请输入圆盘的数目： 2345
输入圆盘数目太多,运行超时！
无论有没有异常都会执行的finally语句

请输入圆盘的数目： 3
A ------> C
A ------> B
C ------> B
A ------> C
B ------> A
B ------> C
A ------> C
没有发生异常才会执行else这条语句
无论有没有异常都会执行的finally语句
```

触发异常

```python
#触发异常语法
'''
raise [Exception [, args [, traceback]]]

其中Exception是异常的类型（如NameError、ValueError等）参数标准异常里的一种，args是自己提供的异常参数。最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。

try:
    raise TypeError('类型错误')
except Exception as e:
    print(e)
'''
# 触发异常
def hannoi(n, a, b, c) :
    if n == 1 :
        print(a, "------>", c)
    else :
        hannoi(n - 1, a, c, b)
        hannoi(1, a, b, c)
        hannoi(n - 1, b, a, c)


if __name__ == "__main__" :
    while True :
        n = int(input("请输入圆盘的数目： "))
        hannoi(n, "A", "B", "C")

        try :
            raise (ValueError,RuntimeError)
        except Exception as e:
            print(e)
    
>>>>>>

请输入圆盘的数目： e3
ValueError: invalid literal for int() with base 10: 'e3'
     
请输入圆盘的数目： 1234
RecursionError: maximum recursion depth exceeded in comparison

请输入圆盘的数目： 3
A ------> C
A ------> B
C ------> B
A ------> C
B ------> A
B ------> C
A ------> C
```



### 标准库简介





