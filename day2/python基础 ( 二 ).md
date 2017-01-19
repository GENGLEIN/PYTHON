# 一 变量拾遗
<pre>
name = "alex"
name2 = name
print(name,name2)
name = "Jack"
print(name,name2)
</pre>
# 二 格式化输出
### 2.1 格式化输出补充
<pre>
%s 字符串 
%d 数字 
%f 浮点数
%r 原生字符,非转义
msg = " my name is %s and age is %s" %("genglei",22)
print(msg)
my name is genglei and age is 22
</pre>

### 2.2 位运算
<pre>
# 128 64 32 16 8 4 2 
# 0 0 1 1 1 1 0 0
# 0 0 0 0 1 1 0 1
a = 60 # 0 0 1 1 1 1 0 0
b = 13 # 0 0 0 0 1 1 0 1

a & b =  0 0 0 0 1 1 0 0 = 12 #与运算就是俩个值的二进制比较，都为1那就为真
a | b = 0 0 1 1 1 1 0 1 = 61 #或运算就是俩个值有一个为真就为真
a ^ b = 49  不一样的都为1
</pre>

### 2.3 for 循环
<pre>
for i in range(5):print(i)
0
1
2
3
4
例:
AGE = 56
count = 0
for i in range(10):
    if i == 3:
        print("不能在猜了")
    guess_num = int(input("you guess num:"))
    if guess_num == AGE:
        print("恭喜您猜对了")
        break  #跳出当前循环
    elif guess_num > AGE:
        print("对不起猜大了")
    else:
        print("对不起猜小了")
-----------------------------------------
AGE = 56
count = 0
for i in range(10):
    if count == 3:
        user_confirm = input("是否继续输入?:").strip()
        if user_confirm == "y":
            count = 0
        else:
            break
            #pass  是什么都不做想当与占位符
    guess_num = int(input("you guess num:"))
    if guess_num == AGE:
        print("恭喜您猜对了")
        break
    elif guess_num > AGE:
        print("对不起猜大了")
    else:
        print("对不起猜小了")
    count += 1
-------------------------------------------
# for i in range(10):
#     if i == 5:
#         pass
#     else:
#         print(i)

for i in range(10):
    if i == 5:
        for j in range(10):
            print(j)
            if j == 6:
                break
        continue
    print(i)
-------------------------------------------
# break 跳出当前的整个循环
# continue 跳出本次循环，进入下一次循环
</pre>

### 2.4 while使用
<pre>
import time #导入时间模块
t_start = time.time()   #开始计时
count0 = 0
while True: #条件为真
    #print("你是风儿我是沙，缠缠绵绵到天涯",t_start,time.time())
    if count0 == 1000000:
        break
    count0 += 1
    print("count0:",time.time()-t_start,count0)
time.time()-t_start # 当前时间减去开始计时的时间

s_start = time.time()
count1 = 0
while count1 < 1000000:
    count1 += 1
    print("count1:",time.time()-s_start,count1)

</pre>

### 2.5 三元运算
<pre>
例:如果a大于b那么c就等于a+b，否则c就等于a-b
>>> a = 2
>>> b = 3
>>> if a>b:
...  c = a+b
... else:
...  c = a-b
...
>>> c
-1
>>> c = a+b if a>b else a-b
>>> c
-1

</pre>

### 2.6 元组 
<pre>
# 元组其实跟列表差不多，也是存一组数，只不是它一旦创建，便不能更改，所以又叫只读列表
name = ("alex","jack","eric")
它只有2个方法，一个是count，一个是index，
例:
name = ["genglei","jack","alex","genglei"]
print(name.count("genglei"))
print(name.index("genglei"))
</pre>

### 三 字典的操作
<pre>
names = {
    #  KEY       VALUE
------------------------------
    "stu1101" : "Alex",
    "stu1102" : "Jack",
    "stu1103" : "Genglei",
}
print(names)
------------------------------
例：
names = {
    "stu1101" : {
        "name" :"genglei",
        "age" :"22",
        "hobbie" :"girl",
    },
    "stu1102" : "jack",
    "stu1103" : "alex",
    "stu1104" : "rain",
}
#查询
print(names["stu1101"]["age"]) #查看年龄
print("stu1101" in names) #判断stu1101在names列表没有
print(names.get("stu1105")) #判断stu1105在names列表里没有，如果没有返回none
print(names.get("stu1105","hehe")) #判断stu1105在names列表里没有，如果没
#有返回none,如果值不存在也可以自定义返回值

#add
names["stu1105"] = ["yangjian",31,"DBA"]
print(names)

#update
names["stu1105"][0] = "杨建"
print(names)

#delete
names.pop("stu1105")
print(names)
print(names.pop("stu1107","ssss")) #删除一个不存在的值，并且自定义返回值
print(names)
del names["stu1102"]
print(names)
-----------------------------------
例循环字典：
for k in names:
    print(k,[k])
-----------------------------------
for k in names:
    print(k,names[k])
print(names.keys())
print(names.values())

字典的速度要比列表快，原因是因为字典是通过hash算法生成一个唯一的值
------------------------------------------------------------
小结：
#无序的，key天生去重，查询效率高
</pre>

### 3.1 copy
<pre>
names = {
    "stu1101" : {
      "name" :"genglei",
        "age" :"22",
        "hobbie" :"girl",
    },
    "stu1102" : "jack",
    "stu1103" : "alex",
    "stu1104" : "rain",
}
n2 = names.copy()
print(names)
print(n2)
-----------------------------
import copy #导入模块
credit_card = {"name":"yangjian","acc":{"id":23333,"balance":900}}
credit_card2 = credit_card.copy()
credit_card3 = copy.deepcopy(credit_card) #深copy就是完全复制,credit_card是源
credit_card2["name"] = "yangjianxifu"
print(credit_card)
print(credit_card2)
credit_card["acc"]["balance"] -= 300
credit_card2["acc"]["balance"] -= 500
print(credit_card)
print(credit_card2)
print(credit_card3)

</pre>