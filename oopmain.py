from collections import defaultdict

"""cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
"""

def tuple_text_book(text_book, cook_book):
  for string in text_book:
    if string.rstrip():
        dish_ingredients = []
        dish = string.rstrip()
        for _ in range(int(text_book.readline().rstrip())):
          dish_ingredients.append(dict(zip(('ingredient_name', 'quantity', 'measure'), text_book.readline().rstrip().split(' | '))))
          cook_book[dish] = dish_ingredients                


with open("oop.txt", "r", encoding="utf-8") as text_book:
    cook_book = {}
    print(tuple_text_book(text_book, cook_book))
    

for key in cook_book.keys():
    print(f"{key}:")
    for value in cook_book[key]:
        print(value)
print()
            
    



        
    