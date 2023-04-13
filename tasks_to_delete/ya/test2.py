with open('C:/Users/lm137/IDE/tasks_to_delete/ya/input.txt') as my_file:
    data = my_file.read()
numbers_list = list(map(int, data.split()))
with open('C:/Users/lm137/IDE/tasks_to_delete/ya/output.txt', "w") as write_file: # Откроем файл new_recipes.json для записи
    write_file.write(str(sum(numbers_list)))