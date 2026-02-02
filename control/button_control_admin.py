from tkinter import Toplevel, Label, Button, Entry
import control.bd_button_control as bdb


def button_add_admin():
    """Создаем окно где заполняем поля для добавления администратора в бд"""
    window_butt_add_admin = Toplevel()
    window_butt_add_admin.title('Добавление администратора')
    window_butt_add_admin.geometry('1100x500')
    window_butt_add_admin.resizable(width=False, height=False)

    label = Label(window_butt_add_admin, text='Для добавления администратора заполните следующие поля',
                  font=('Arial', 20, 'bold'), bg='orange', fg='white').pack()
    label = Label(window_butt_add_admin, text='Введите id админа, важно, что бы id не повторялись:',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_id_admin = Entry(window_butt_add_admin, font=('Arial', 20, 'bold'))
    entry_id_admin.pack()
    label = Label(window_butt_add_admin, text='Введите ФИО в поле для ввода',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_name_admin = Entry(window_butt_add_admin, font=('Arial', 20, 'bold'))
    entry_name_admin.pack()
    label = Label(window_butt_add_admin, text='Введите логин админа, важно что бы логина такого не существовало:',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_login_admin = Entry(window_butt_add_admin, font=('Arial', 20, 'bold'))
    entry_login_admin.pack()
    label = Label(window_butt_add_admin, text='Введите пароль админа: \n Рекомендации по паролю тут -> https://habr.com/ru/companies/femida_search/articles/983948/',
                  font=( 'Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_password_admin = Entry(window_butt_add_admin, font=('Arial', 20, 'bold'))
    entry_password_admin.pack()
    label = Label(window_butt_add_admin, text='Введите з/п администратора',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_zp_admin = Entry(window_butt_add_admin, font=('Arial', 20, 'bold'))
    entry_zp_admin.pack()
    label = Label(window_butt_add_admin, text='Введите премию администратора',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_prize_admin = Entry(window_butt_add_admin, font=('Arial', 20, 'bold'))
    entry_prize_admin.pack()
    label = Label(window_butt_add_admin, text='Проверьте введеные данные и затем нажмите на кнопку',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()

    def button_create_admin():
        id_admin = entry_id_admin.get()
        name_admin = entry_name_admin.get()
        login_admin = entry_login_admin.get()
        password_admin = entry_password_admin.get()
        zp_admin = entry_zp_admin.get()
        prize_admin = entry_prize_admin.get()

        bdb.bd_add_admin(int(id_admin), str(name_admin), login_admin, password_admin, int(zp_admin), int(prize_admin))

    button_agree_admin_add = Button(window_butt_add_admin, text='Создать',
    command=button_create_admin, font=('Arial', 40, 'bold'), bg='lime', fg='white').pack()


def button_del_admin():
    """Удаляем администратора по id"""
    window_butt_del_admin = Toplevel()
    window_butt_del_admin.title('Удаление администратора')
    window_butt_del_admin.geometry('600x500')
    window_butt_del_admin.resizable(False, False)

    label = Label(window_butt_del_admin, text='Для удаления администратора заполните следующие поля',
                  font=('Arial', 20, 'bold'), bg='orange', fg='white').pack()
    label = Label(window_butt_del_admin, text='Введите id администратора для его удаления',
                  font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    entry_del_id_admin = Entry(window_butt_del_admin, font=('Arial', 20, 'bold'))
    entry_del_id_admin.pack()

    def button_help_del():
        del_id_admin = entry_del_id_admin.get()
        bdb.bd_del_admin(int(del_id_admin))

    button_del_admin = Button(window_butt_del_admin, text='Удалить', command=button_help_del,
                              font=('Arial', 40, 'bold'), bg='red', fg='white').pack()
