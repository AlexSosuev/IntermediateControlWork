from datetime import date, datetime
import sys

file_path = 'notes.csv'

def file_read(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return  [line.rstrip().split(';') for line in file]
    except FileNotFoundError:
        print('Файл {} не найден!'.format(file_path))
        return []

def note_print():
    notes = file_read(file_path)
    if len(notes)!=0:
        for id, title, text, timestamp in notes:
            print('Заметка под номером {}\n\tзаголовок - {}\n\tтекст заметки: {}\n\tнаписана: {}'.format(id, title, text, timestamp))
    else:
        print('Список заметок пуст')

def note_print_by_date():
    notes = file_read(file_path)
    data = input('Введите дату для фильтрации в заметках в формате дд.мм.гггг: ')
    if len(data.split('.')) == 3 and datetime.strptime(data, '%d.%m.%Y'):
        filter_note = [note for note in notes if datetime.strptime(data, '%d.%m.%Y') == datetime.strptime(note[3], '%d.%m.%Y')]
        if filter_note:
            print('Заметки на данную дату: \n')
            for id, title, text, timestamp in filter_note:
                print('Заметка под номером {}\n\tзаголовок - {}\n\tтекст заметки: {}\n\tнаписана: {}'.format(id, title, text, timestamp))
        else:
            print('Заметок на данную дату - нет!')
    else:
        print('Введен неправильный формат даты')


def note_new_id(notes):
    if not notes:
        return 1
    return max(int(note[0]) for note in notes) + 1

def note_add():
    notes = file_read(file_path) or []
    note_id = note_new_id(notes)
    note_title = input('Введите заголовок заметки: ')
    note_text = input('Введите тело заметки: ')
    note_timestamp = datetime.now().strftime('%d.%m.%Y')
    notes.append([note_id, note_title, note_text, note_timestamp])
    print('Заметка сохранена.')
    note_save(notes)

def note_edit():
    notes = file_read(file_path) or []
    search_id = int(input('Введите ID заметки для изменения:'))
    found_note = False
    for note in notes:
        if int(note[0]) == search_id:
            note_title = input('Введите новое имя заметки: ')
            note_text = input('Введите новое описание заметки: ')
            note_timestamp = datetime.now().strftime('%d.%m.%Y')
            note[:] = [search_id, note_title, note_text, note_timestamp]
            found_note = True         
    if found_note:
        print('Заметка изменена.')
        note_save(notes)
    else:
        print('Заметки с таким ID нет!')

def note_delete():
    notes = file_read(file_path) or []
    search_id = int(input('Введите ID заметки для удаления:'))
    notes_del = [sublist for sublist in notes if int(sublist[0]) != search_id] 
    if len(notes_del) != 0:
        note_save(notes_del)
        print('Удаление прошло успешно!.')
    else:    
        print('Заметки с таким ID нет!')


def note_save(notes):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(';'.join(map(str, note)) + '\n' for note in notes)            
    except IOError as io_err:
        print('Ошибка записи: {}'.format(io_err))

def interface():
    while True:        
        mode = input("\nВыберет режим, в котором хотите работать: \n\n"+
                        "\tAdd, если хотите добавить новую заметку. \n" + 
                        "\tList, если хотите увидеть все заметки. \n" +
                        "\tFilter, если хотите увидеть отфильтрованные заметки. \n" +
                        "\tEdit, если хотите отредактировать заметку. \n" + 
                        "\tDelete, если хотите удалить заметку. \n" +
                        "\tExit, если хотите выйти из программы. \n\n" +
                        "Введите Ваш выбор: ")
        match mode.lower():
            case "add":
                note_add()
                input('Для продолжения нажмите клавишу Enter...')
            case "list":
                note_print()
                input('Для продолжения нажмите клавишу Enter...')
            case "edit":
                note_edit()
                input('Для продолжения нажмите клавишу Enter...')
            case "delete":
                note_delete()
                input('Для продолжения нажмите клавишу Enter...')
            case "filter":
                note_print_by_date()
                input('Для продолжения нажмите клавишу Enter...')
            case "exit":
                print("До встречи!")
                sys.exit()
            case _:
                print("Не верно, попробуй еще разок \n")


interface()