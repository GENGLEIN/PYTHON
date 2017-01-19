
#商品列表
product_list = [
    ["Apple Iphone7",5199],
    ["Apple Macbook",5699],
    ["联想 ISK15.6英寸笔记本",7699],
    ["美利达 公爵600",2777],
    ["宝马 740",120000],
    ["路虎 发现神行",590000],
    ["现代 名图",170000],
    ["特斯拉 v1",800000],
    ["奥迪 Q5",420000],
]
#print(product_list)
salary = int(input("请输入您的年收入: "))
#购物车
shopping_cart = []

while True:
    for index,i in enumerate(product_list):
        print("%s.\t%s\t%s" %(index,i[0],i[1]))
    choice = input("请选择要购买的商品>>:")
    if len(choice.strip()) == 0:
        print("输入不合法")
        continue
    if choice.isdigit():   #isdigit 判断输入的是不是数字
        choice = int(choice) #把用户输入的转换成整数
        if choice < len(product_list) and choice >=0: #用户输入的商品编号必须小于商品列表
            product_item = product_list[choice]  #product_item=获取商品
            if salary >= product_item[1]: #买的起
                salary -= product_item[1] #扣钱
                shopping_cart.append(product_item)
                print("\033[32;1m%s\033[0m 商品已添加购物车,\
 您现在的余额: \033[31;1m%s\033[0m" %(product_item[0],salary))
            else:
                print("您的金额不足：还差",product_item[1]-salary)

        else:
            print("没有此商品")
    elif choice == "p":
        print("当前购物车列表：",shopping_cart)
        pass
    elif choice == "exit":
        total_cost = 0
        print("您已经购买商品列表:")
        for i in shopping_cart:
            print(i)
            total_cost += i[1]
        print("总计消费:",total_cost)
        print("您的余额: ",salary)
        break

