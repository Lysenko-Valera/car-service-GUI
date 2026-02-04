from tkinter import Toplevel, Label, Button, Entry
import control.db_button_control as bdb


def button_add_mechanic():
    """Создаем окно где заполняем поля для добавления администратора в бд"""
    window_butt_add_mechanic = Toplevel()
    window_butt_add_mechanic.title('Добавление механника')
    window_butt_add_mechanic.geometry('1100x500')
    window_butt_add_mechanic.resizable(width=False, height=False)

    label = Label(window_butt_add_mechanic, text='Для добавления механника заполните следующие поля',
                  font=('Arial', 20, 'bold'), bg='orange', fg='white').pack()
    label = Label(window_butt_add_mechanic, text='Введите id механника, важно, что бы id не повторялись:',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_id_mechanic = Entry(window_butt_add_mechanic, font=('Arial', 20, 'bold'))
    entry_id_mechanic.pack()
    label = Label(window_butt_add_mechanic, text='Введите ФИО в поле для ввода',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_name_mechanic = Entry(window_butt_add_mechanic, font=('Arial', 20, 'bold'))
    entry_name_mechanic.pack()
    label = Label(window_butt_add_mechanic, text='Введите специализацию механника',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_special_mechanic = Entry(window_butt_add_mechanic, font=('Arial', 20, 'bold'))
    entry_special_mechanic.pack()
    label = Label(window_butt_add_mechanic, text='Введите опыт работы',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_experience_mechanic = Entry(window_butt_add_mechanic, font=('Arial', 20, 'bold'))
    entry_experience_mechanic.pack()
    label = Label(window_butt_add_mechanic, text='Введите з/п механника',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_zp_mechanic = Entry(window_butt_add_mechanic, font=('Arial', 20, 'bold'))
    entry_zp_mechanic.pack()
    label = Label(window_butt_add_mechanic, text='Введите премию механника',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_prize_mechanic = Entry(window_butt_add_mechanic, font=('Arial', 20, 'bold'))
    entry_prize_mechanic.pack()
    label = Label(window_butt_add_mechanic, text='Проверьте введеные данные и затем нажмите на кнопку',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()

    def button_create_mechanic():
        id_mechanic = entry_id_mechanic.get()
        name_mechanic = entry_name_mechanic.get()
        special_mechanic = entry_special_mechanic.get()
        experience_mechanic = entry_experience_mechanic.get()
        zp_mechanic = entry_zp_mechanic.get()
        prize_mechanic = entry_prize_mechanic.get()

        bdb.bd_add_mechanic(int(id_mechanic), str(name_mechanic), str(special_mechanic), int(experience_mechanic), int(zp_mechanic), int(prize_mechanic))

    button_agree_admin_add = Button(window_butt_add_mechanic, text='Создать',
    command=button_create_mechanic, font=('Arial', 40, 'bold'), bg='lime', fg='black').pack()


def button_del_mechanic():
    """Удаляем администратора по id"""
    window_butt_del_mechanic = Toplevel()
    window_butt_del_mechanic.title('Удаление администратора')
    window_butt_del_mechanic.geometry('600x500')
    window_butt_del_mechanic.resizable(False, False)

    label = Label(window_butt_del_mechanic, text='Для удаления администратора заполните следующие поля',
                  font=('Arial', 20, 'bold'), bg='orange', fg='white').pack()
    label = Label(window_butt_del_mechanic, text='Введите id администратора для его удаления',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_del_id_admin = Entry(window_butt_del_mechanic, font=('Arial', 20, 'bold'))
    entry_del_id_admin.pack()

    def button_help_del_mechanic():
        del_id_mechanic = entry_del_id_admin.get()
        bdb.bd_del_mechanic(int(del_id_mechanic))

    button_del_mechanic = Button(window_butt_del_mechanic, text='Удалить', command=button_help_del_mechanic,
                              font=('Arial', 40, 'bold'), bg='red', fg='black').pack()