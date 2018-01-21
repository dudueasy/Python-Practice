class Product:
    def __init__(self, id: object, name: object, price: object) -> object:
        self.id = id
        self.name = name
        self.price = price

def get_money():
    salary = input("please input your salary: ")
    if salary.isdigit():
        return int(salary)
    else:
        print('请输入正确的格式\n')
        get_money()

def show_p_info():
    print("您可以购买以下商品:")
    for product in product_list:
        print(product.id + ": " + product.name + "  $" + str(product.price))

def purchase(product):
    global money
    if money >= product.price:
        money -= product.price
        cart.append(product.name)
        print('已经购买了'+product.name)
        print('消费了$' + str(product.price))
        print('剩余金额$'+ str(money))

    else:
        print('买不起, 差$'+str(product.price - money))


def search_or_quit():
    show_p_info()
    input_key = input("请输入您要购买的商品编号, 输入q退出商店: ")
    if input_key == 'q':
        print("")
        print('您总计购买了以下商品:')
        for p_name in cart:
            print(p_name)
        print('您还有余额$' + str(money))
        print("byebye")
    else:
        p_found = False
        for product in product_list:
            if product.id == input_key:
                p_found = product
        if p_found:
            purchase( p_found)
        else:
            print("没有找到这个商品编号!")
        search_or_quit()

#initialize
iphone = Product('1', 'iphone', 1000)
coffee = Product('2', 'coffee', 30)
book = Product('3', 'book', 50)
condom = Product('4', 'condom', 1)
product_list =[iphone, coffee, book, condom]
cart = []

money = get_money()
print("您有$" + str(money) +"可以使用")

search_or_quit()