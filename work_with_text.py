import os


# Функция считывает файлы в словарь: ключи - названия файлов, значения - списки строк в файлах

def my_func(files_list, dict_text_files):
    for file in files_list:
        with open(file, "r", encoding="utf-8") as get_file:
            dict_text_files[file] = get_file.read()


# Функция записи полученной информации в конечный файл:
            
def output_func(list_key, dict_text_files):
    with open("result.txt", "w", encoding="utf-8") as final_result:
        for file_name in list_key:
            final_result.write(f'{file_name}\n')
            file_len = len(dict_text_files[file_name].split('\n'))
            final_result.write(f"{file_len}\n")
            final_result.write(f"{dict_text_files[file_name]}\n")


dict_text_files = {}
my_func(["1.txt", "2.txt", "3.txt"], dict_text_files)

# сортировка словаря

list_key = []
for key in sorted(dict_text_files, key=lambda key: len(dict_text_files[key].split('\n'))):
    list_key.append(key)

output_func(list_key, dict_text_files)
        









