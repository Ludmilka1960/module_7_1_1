

class Shop:


    __file_name = 'products.txt'

    def get_products(self):
        file1 = open(self.__file_name, 'r',encoding='utf-8')
        product = file1.read()
        file1.close()
        return product

    def add(self,*products):
        file = open(self.__file_name, 'r+',encoding='utf-8')
        for product in products:
            if str(product)  in self.get_products():
                print(f"Продукт {str(product)} уже есть в магазине")
            else:
                file.write(str(product) + '\n')
        file.close()


class Product(Shop):
        def __init__(self, name, weight, category):
            self.name = name
            self.weight = weight
            self.category = category

        def __str__(self):
            return f"Название:'{self.name}' ,Вес:{self.weight} ,Категория:'{self.category}'\n"


s1 = Shop()
p1 = Product('Яблоко', 30.4, 'Фрукты')
p2 = Product('Помидор', 5.4, 'Овощи')
p3 = Product('Банан', 15.1, 'Фрукты')
print(p2)

s1.add(p1, p2,p3)

print(s1.get_products())
p4 = Product('Помидор', 12.5, "Овощи")
s1.add(p4)
print(s1.get_products())
