# 一 函数使用指南

### 1.1 为什么要使用函数(不用函数的问题)
> 组织结构不清晰   
> 代码冗余   
> 无法统一管理且维护难度大     
### 1.2 什么是函数
<pre>
工具箱里面的某个工具就是一种功能的物件，就是程序中函数的概念
事先准备好工具的过程称为函数的定义
遇到特定的场景拿来就用称为函数的调用
</pre>

### 1.3 函数的分类

> 1.3.1 内置函数    
> 1.3.2 自定义函数

### 1.4 为什么要定义函数
> 函数即变量，变量必须先定义后使用，未定义而直接引用函数，就相当于在引用一个不存在的变量名

### 1.5 自定义函数语法:
<pre>
#函数的定义:
     先定义
     在调用(函数名字)
#函数的定义与变量的定义类似，没有事先定义变量，而直接引用变量，会报错
                          没有事先定义函数，而直接引用函数，会报错
def 函数名(参数.arg1,arg2,arg3):
	"""注释信息"""
	函数体
	return  返回值

#函数名一般是动词，要有特殊的意义
#注释信息一定要有
#参数.......
</pre>

### 1.6 定义函数的三种形式:
>无参：应用场景仅仅只是执行一些操作，比如与用户交互，打印      
<pre>
#定义函数
#例1
'''
****************
hello glei
*****************
'''
def print_star(): #括号里面可以加参数
    print('*'*10)
def print_msg():
    print('hello glei')

print_star()  #加括号代表执行函数里面的内容
print_msg()
print_star()

</pre>
>有参：需要根据外部传进来的参数，才能执行相应的逻辑，比如统计长度，求最大值最小值(通常情况下有参函数都要有一个返回值return,函数内部可以有多个return，但只能执行一次，函数就结束调用，并且会把return后的值作为函数执行的结果返回)        
<pre>
#有惨函数
def my_max(x,y):
    if x > y:
        #print(x)
        return x
    else:
        #print(y)
        return y
res=my_max(1,2)
print(res)

def fcc():
    print('******-----***')
    return 123
    print('******-----***')
    print('******-----***')
    print('******-----***')
fcc()
#return的返回值没有限制
#没有return，返回None 等同于return None
return -个值：返回该值,return后面没有限制
return  val1,val2,val3:返回(val1,val2,val3)
　　什么时候该有？
　　　　调用函数，经过一系列的操作，最后要拿到一个明确的结果，则必须要有返回值
　　　　通常有参函数需要有返回值，输入参数，经过计算，得到一个最终的结果
　　什么时候不需要有？
　　　　调用函数，仅仅只是执行一系列的操作，最后不需要得到什么结果，则无需有返回值
　　　　通常无参函数不需要有返回值
----------------------------------------------------
#函数里面调用函数
#定义阶段
def bar():
    print('from bar')

def foo():
    print('from foo')
    bar()

#调用阶段
foo()

</pre>
>空函数：设计代码结构
<pre>
def bar():
    pass   #空函数,定义业务逻辑
</pre>
### 1.7函数调用的三种方式
<pre>
def my_max(x,y):
    if x > y:
        return x
    else:
        return y
my_max(1,2) #调用函数的语句形式
res=my_max(1,2)*10 #调用函数的表达式形式
my_max((1,2),3)
res1 = my_max(1,2)
res2 = my_max(res1,3)#函数调用可以当做另外一个函数的参数
print(res2)
</pre>

# 二 函数的参数
>形参   
>实参
<pre>
#形参：在定义函数阶段，括号内的参数成为形参
#特点:就是变量名
def foo(x,y): #x=y,y=2
    print(x)
    print(y)
#实参:在调用函数的时候，括号内的参数成为实参
#特点:就是变量值
foo(1,2)
# 在调用阶段实参（变量值）,才会绑定到形参（变量名）
# 调用结束后，解除绑定
</pre>

### 2.1 参数的分类
<pre>
位置参数:安装从作到右的顺序依次定义的参数
   位置形参:必须被传值，多一个不行，少一个也不行
   位置实参:与形参安装位置一一对应
def foo(x,y):
    print(x)
    print(y) 
foo(1,2)
</pre>

### 2.2 关键字实参，指的是按照name=value的形式，指名道姓的给name传值
<pre>
def foo(name,agen):
    print(name)
    print(agen)
foo(agen=18,name='egon')
# 关键字实参需要注意的问题是：
def foo(name,agen,sex):
    print(name)
    print(agen)
    print(sex)
foo('genglei',18,'male')
foo(sex='male',age=18,name='genglei')
foo('genglei',sex='male',age=18)

#问题1：语法规定位置实参必须在关键字实参的前面
foo(sex='male',age=18,'genglei')
#问题2：一定不要对同一个形参传多长值
foo('genglei',sex='male',age=18,name='genglei')
</pre>

### 2.3 默认参数
<pre>
#默认形参:在定义阶段就已经为形参赋值，意味在调用阶段可以不用传值
def foo(x,y=111111):
    print(x)
    print(y)
foo(1)
foo(x=2,y=1)

def register(name,age,sex='male'):
    print(name,age,sex)
register('asb',18)
register('bsa',48)
register('sab',88)
register('yy',32,sex='female')

</pre>
### 2.4 默认参数需要注意的问题
>问题1：默认参数必须放在位置参数之后
<pre>
def foo(y=1,x)
    print(x,y)
</pre>
> 问题2:默认参数只在定义阶段赋值一次，而且仅一次
<pre>
x=100
def foo(a,b=x)
    print(a,b)
x=0
print('egon')
</pre>
> 问题3：默认参数的值应该定义成不可变的类型

# 三 可变长函数
### 3.1 概念
<pre>
可变长参数指的是实参的个数不固定个数多了
实参无非是位置实参和关键字实参俩中
形参必须要俩种机制来分别处理按照位置定义的实参溢出的情况：*
根按照关键字定义的实战溢出的情况: **
</pre>
### 3.2 练习
<pre>
def foo(x,y):
    print(x)
    print(y)
foo(1,2,3,4,5,6,7) # *
def foo(x,y,*args):
    print(x)
    print(y)
    print(args)
foo(1,2,3,4,5,6,7) # *

def foo(x,y,**kwargs):
    print(x)
    print(y)
    print(kwargs)
#foo(x=1,y=2,c=3,h=6) # **
</pre>

### 3.3 *args的扩展用法
<pre>
def foo(x,y,*args):
    print(x)
    print(y)
    print(args)
foo(1,2,*(3,4,5,6,7)) #*foo(1,2,3,4,5,6,7)
</pre>

### 3.4 **kwargs的扩展用法
<pre>
def foo(x,y,**kwargs):
    print(x)
    print(y)
    print(kwargs)
foo(1,2,**{'z':3,'b':2}) # ** foo(1,2,z=3,b=2)


def foo(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
foo(1,2,3,4,b=1,c=2)
</pre>

### 3.5 args|kwargs作用
<pre>
*args
**kwargs
def register(name,age,sex='male'):
    print(name)
    print(age)
    print(sex)
def wrapper(*args,**kwargs):
    print(args)  #*args=(1, 2, 3, 4)
    print(kwargs) #**kwargs={'x': 1, 'y': 2}
    register(*args,**kwargs) #调用阶段 register(1,2,3,x=1,y=2)
wrapper(1,2,3,x=1,y=2)

#正确(会用到装饰器里面)
def register(name,age,sex='male'):
    print(name)
    print(age)
    print(sex)
def wrapper(*args,**kwargs):
    register(*args,**kwargs)
wrapper('genglei',age=18)

# 命名关键字参数: 在*后面定义的形参称为命名关键字参数，必须是已关键字实参的形式来传值

def foo(name,age,*,sex='male',group):
    print(name)
    print(age)
    print(sex)
    print(group)
foo('genglei',18,sex='hal',group='groupx')

</pre>

# 四 函数的对象
### 4.1 函数是第一类的对象,指的是函数可以被当做数据传递
<pre>

1#被赋值
f=foo
2# 可以当做参数的传入
def wrapper(fun):
    print(fun)
wrapper(foo)

3# 可以当做函数的返回
def wrapper(func):
    return func
res=wrapper(foo)
print(res)
4# 可以当做容器类型的元素
cmd_dic={
    'fun':foo
}
print(cmd_dic)
cmd_dic['fun']()
</pre>