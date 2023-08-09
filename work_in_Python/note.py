from datetime import datetime
import sys

file_path = 'notes.csv'
notes_list = []


def file_read(file_path):
    try:
        with open(file_path) as file:
            return  [line.rstrip().split(';') for line in file]
    except FileNotFoundError:
        print('Файл {} не найден!'.format(file_path))


def note_print():
    notes = file_read(file_path)
    if notes is not None and len(notes)!=0:
        for id, title, text, timestamp in notes:
            print('Заметка под номером {}\n\tзаголовок - {}\n\tтекст заметки: {}\n\tнаписана: {}'.format(id, title, text, timestamp))
    else:
        print('Список заметок пуст')


def note_new_id():
    if not notes_list:
        return 1
    return max(int(note[0]) for note in notes_list) + 1


def note_save(notes):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(';'.join(map(str, note)) + '\n' for note in notes)
            print('Заметка сохранена.')
    except IOError as io_err:
        print('Ошибка записи: {}'.format(io_err))

def note_add():
    notes = file_read(file_path) or []
    note_id = note_new_id()
    note_title = input('Введите заголовок заметки: ')
    note_text = input('Введите тело заметки: ')
    note_timestamp = datetime.now().strftime('%d.%m.%Y')
    notes.append([note_id, note_title, note_text, note_timestamp])
    note_save(notes)


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
            case "list":
                note_print()
            case "edit":
                edit_note()
            case "delete":
                delete_note()
            case "filter":
                filter_notes()
            case "exit":
                print("До встречи!")
                sys.exit()
            case _:
                print("Не верно, попробуй еще разок \n")


interface()