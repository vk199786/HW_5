documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

#p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def get_person_info():
  number_doc = input('Введите номер документа: ')
  for people_info in documents:
    #print(people_info)
    if number_doc == people_info["number"]:
      print(f'Документ номер {number_doc} принадлежит {people_info["name"]}')
      break
  else:
      print(f'Документ номер {number_doc} нет в базе данных')
  return

#s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def number_of_shelf():
    number = input('Введите номер документа: ')
    for directory_number, directory_content in directories.items():
        if number in directory_content:
            print(f'Документ номер {number} найден на полке номер {directory_number}')
            break
    else:
        print(f'Документ номер {number} не найден')
    return

#l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def print_each_doc():
  for people_info in documents:
    print(f'"{people_info["type"]}" "{people_info["number"]}" "{people_info["name"]}"')
  return

#a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_new_person():
  type_of_doc = input('Введите тип документа: ')
  new_number = input('Введите номер документа: ')
  new_name = input('Введите имя владельца: ')
  new_shelf = input('Введите номер полки: ')
  new_dict = {}
  new_dict["type"] = type_of_doc
  new_dict["number"] = new_number
  new_dict["name"] = new_name
  documents.append(new_dict)
  if new_shelf == directories.keys():
    print("Ошибка")
  else:
    new_dict_1 = {}
    new_dict_1[new_shelf] = new_dict
    directories.update(new_dict_1)


def main():
  print('People - поиск человека по номеру документа.')
  print('Shelf - поиск номера полки с документами.')
  print('List - вывод всех документов в базе данных.')
  print('Add - добавление нового человека в базу данных.')
  user_input = input('Введите необходимую функцию:')
  if user_input == 'People':
    print(get_person_info())
  elif user_input == 'Shelf':
    print(number_of_shelf())
  elif user_input == 'List':
    print(print_each_doc())
  elif user_input == 'Add':
    print(add_new_person())
    print(documents)
    print(directories)
  else:
    print(f'Функции {user_input} нет в программе')
main()
