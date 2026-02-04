from tkinter import Entry, Label, Tk, Button, Toplevel
from random import choice
from tkinter import messagebox
import sqlite3 as sql
from PIL import ImageTk, Image


window_entry = Tk() #создаем окно входа
window_entry.title('Вход в систему')
window_entry.geometry('750x700')
window_entry.resizable(width=False, height=False)

img = Image.open('img_and_gif/key_logo_entry_window.JPG')
img = img.resize((750, 700))
img_photo = ImageTk.PhotoImage(img)

img_lablel = Label(window_entry, image=img_photo)
img_lablel.place(x=0, y=0)

label = Label(window_entry, text='Доброго пожаловать в систему.',
                 font=('Arial', 35, 'bold'), bg='orange').pack()

label = Label(window_entry, text='Введите логин:',
                 font=('Arial', 20, 'bold'), bg='black', fg='white', anchor='w').pack(fill='x')

login_input = Entry(window_entry, font=('Arial', 20), width=25, justify='left')
login_input.pack()

label = Label(window_entry, text='Введите пароль:',
                 font=('Arial', 20, 'bold'), bg='black', fg='white', anchor='w').pack(fill='x')

password_input = Entry(window_entry, font=('Arial', 20), width=25, justify='left')
password_input.pack()


dict_capcha = {'68ㄥ9ᄅ': '98762', '6ㄥƐᄅ8': '97328', '9ㄥㄥƐᄅ': '67732', 'ᄅᄅ98Ɩ': '22681', 'ㄣ8ㄣᄅㄥ': '48427'} #Капча, цифры которые надо ввести в правильном порядке
list_capcha = ['68ㄥ9ᄅ', '6ㄥƐᄅ8', '9ㄥㄥƐᄅ', 'ᄅᄅ98Ɩ', 'ㄣ8ㄣᄅㄥ'] #список символов которые должен ввести правильно

def capcha():
    """Создаем окно капчи, где пользователь вводит цифры наоборот в правильном положении, а затем это проверяется после
    нажати на кнопку "отправить", где функция check_capcha проверяет все ли верно. возвращаем True если все хорошо
    и вызываем заново функцию если нет, оповещаем через messagerror
    """
    capcha_text = choice(list_capcha) #Выводим рандомное значение для капчи из списка

    capcha_window = Toplevel()
    capcha_window.title('Капча')
    capcha_window.geometry('650x200')
    capcha_window.resizable(width=False, height=False)

    label = Label(capcha_window, text='Вы ввели пароль неверное более 3-х раз и попали на проверку',
                     font=('Arial', 18, 'bold'), bg='red').pack()

    label = Label(capcha_window, text=f'Введите цифры показанные на экране ниже \n{capcha_text}',
                     font=('Arial', 18, 'bold'), bg='red').pack()

    entry_capcha = Entry(capcha_window, font=('Arial', 20), width=20, justify='left')
    entry_capcha.pack()

    def check_capcha():
        global count
        """Проверяем что ввел пользователь и возвращаем True если все хорошо и вызываем заново функцию если нет,
        оповещаем через messagerror
        """
        capcha_user = entry_capcha.get() #Выбираем текст какой ввел пользователь
        if dict_capcha.get(capcha_text) == capcha_user:
            capcha_window.destroy()
            messagebox.showinfo('Проверка пройдена', 'Вы прошли проверку введите пароль заново')
            count = 4
        else:
            messagebox.showerror('Ошибка', 'Вы не прошли капчу, попробуйте снова')

    button_capcha = Button(capcha_window, text='Отправить', command=check_capcha, font=('Arial', 20, 'bold'), bg='lime')
    button_capcha.pack()
#КАПЧА КОНЕЦ


with sql.connect('sql/admin_table.db') as con:
    cursor = con.cursor()

    cursor.execute('''SELECT login_admin FROM admin_table''')
    result_login = cursor.fetchall()
    cursor.execute('''SELECT password_admin FROM admin_table''')
    result_password = cursor.fetchall()

    login_dict = list(map(list, result_login))
    password_dict = list(map(list, result_password))
    dict_password_login = {''.join(login): ''.join(password) for login, password in zip(login_dict, password_dict)}

count = 4

def check_password():
    global count
    login = login_input.get()
    password = password_input.get()
    if str(login) == 'owner' and password == '1234':
        import control.control_window
        control.control_window()
        window_entry.destroy()
    elif dict_password_login.get(login) == password:
        import admin.admin_window
        admin.admin_window()
        window_entry.destroy()
    else:
        count -= 1
        if count > 0:
            messagebox.showerror('Ошибка ввода пароля или логина', f'У вас осталось {count} попытки')
        else:
            messagebox.showerror('Капча', 'Вы попали на проверку введите цифры правильно')
            capcha()

button_entry = Button(window_entry, text='Войти', command=check_password, font=('Arial', 50, 'bold'), bg='lime')
button_entry.pack()


if __name__ == '__main__':
    window_entry.mainloop()