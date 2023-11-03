from collections import defaultdict

# функция для создания словаря cook_book с соответствующими ключами и значениями

def tuple_text_book(text_book, cook_book):
  for string in text_book:
    if string.rstrip():
        dish_ingredients = []
        dish = string.rstrip()
        for _ in range(int(text_book.readline().rstrip())):
          dish_ingredients.append(dict(zip(('ingredient_name', 'quantity', 'measure'), text_book.readline().rstrip().split(' | '))))
          cook_book[dish] = dish_ingredients          
  

# функция для определения количества ингридентов на указанное количество гостей

def get_shop_list_by_dishes(dishes, person_count):
   dishes_dict = defaultdict(dict)
   for dish in dishes:
      for product in cook_book[dish]:
         dishes_name = product['ingredient_name']
         if dishes_name in dishes_dict:
            dishes_dict[dishes_name]['quantity'] += int(product['quantity'])*person_count
         else:
            dishes_dict[dishes_name]['measure'] = product['measure']
            dishes_dict[dishes_name]['quantity'] = int(product['quantity'])*person_count
   return dishes_dict
      

# открываем файл для чтпения информации с кодировкой utf-8 и присваиваем ему переменную text_book

with open("oop.txt", "r", encoding="utf-8") as text_book:
    cook_book = {}
    dishes = {}
    person_count = 4
    print(tuple_text_book(text_book, cook_book))
    
   

# цикл для корректного отображения словаря cook_book

for key in cook_book.keys():
    print(f"{key}:")
    for value in cook_book[key]:
        print(value)
print()
            
# создадим лист блюд на указанное количество персон  
person = 4
dishes_list = get_shop_list_by_dishes(["Запеченный картофель", "Фахитос"], person)
#print(f'Список ингридиентов для блюд: Фахитос, Запеченный картофель на {person} человек:', end='\n\n')
for key, value in dishes_list.items():
    print(f"{key}: {value}")
    


        
    