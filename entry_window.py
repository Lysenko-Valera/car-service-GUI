import tkinter as tk
from tkinter import Entry, Label, Tk, Button, PhotoImage

window_entry = Tk() #создаем окно входа
window_entry.title('Вход в систему')
window_entry.geometry('1000x700')
window_entry.resizable(width=False, height=False)
# window.iconbitmap('icon_app.JPG')
window_entry.config(bg = '')

# photo_bg = PhotoImage(file='img_app/mersedes_photo.png')
#
# label_photo = Label(window, image=photo_bg)
# label_photo.place(x=0, y=0, relwidth=1, relheight=1)

label = Label(window_entry, text='Доброго пожаловать в систему.',
                 font=('Arial', 35, 'bold'), bg='orange')
label.pack()

label = Label(window_entry, text='Введите логин:',
                 font=('Arial', 20, 'bold'), bg='black', fg='white', anchor='w')
label.pack(fill='x')

login_input = Entry(window_entry, font=('Arial', 20), width=25, justify='left')
login_input.pack()

label = Label(window_entry, text='Введите пароль:',
                 font=('Arial', 20, 'bold'), bg='black', fg='white', anchor='w')
label.pack(fill='x')

password_input = Entry(window_entry, font=('Arial', 20), width=25, justify='left')
password_input.pack()

button_entry = Button(window_entry, text='Войти', font=('Arial', 50), bg='lime')
button_entry.pack()


window_entry.mainloop()