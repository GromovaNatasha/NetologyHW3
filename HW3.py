import os
os.getcwd()

# Пример 2 - построение пути к файлу
def get_dishes():
    file_path = os.path.join(os.getcwd(), 'dishes.txt') 
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for dish in f:
            dish_name = dish.strip()
            dish_number = int(f.readline())
            list_ingredients = list()
            for i in range(dish_number):
                ingredients_description = {}
                ingredients_line = f.readline().strip()
                ingredients_description['ingredient_name'], ingredients_description['quantity'], ingredients_description['measure'] = ingredients_line.split('|')
                ingredients_description['quantity'] = int(ingredients_description['quantity'])
                list_ingredients.append(ingredients_description)
            f.readline()
            cook_book[dish_name] = list_ingredients
    return cook_book

result=get_dishes()
print(result)


def get_shop_list_by_dishes(dishes:list, person_count:int):
    shopping_list = {}
    cook_book=get_dishes()

    for dish in dishes:
      ingr_list = dict()
      for ingredients in cook_book[dish]:
          print()
          ingredient_name = ingredients['ingredient_name']
          measure = ingredients['measure']
          quantity=ingredients['quantity']*person_count
          if ingredient_name in shopping_list:
             shopping_list[ingredient_name]['quantity'] += quantity
          else:
             shopping_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shopping_list


result_2=get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result_2)

file_paths = ['1.txt', '2.txt', '3.txt']  # Replace with the paths to your text files

file_contents = []
len_content=[]
file_names = [] 
for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        file_contents.append(content)
        len_content.append(len(content))
        file_names.append(os.path.basename(file_path))

file_data = list(zip(file_names, file_contents, len_content))
sorted_file_data = sorted(file_data, key=lambda x: x[2])

for name, content, content_length in sorted_file_data:
    print(name)
    print(content_length)
    print(content)

                 
