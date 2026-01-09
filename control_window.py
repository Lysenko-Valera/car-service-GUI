from tkinter import Tk, Label, Button, PhotoImage
import tkinter as tk


window_cntr = Tk()
window_cntr.title('Окно контроля')
window_cntr.geometry('1000x800')
window_cntr.resizable(False,False)
# window_cntr.iconbitmap('icon_app.JPG')

img = PhotoImage(file='./img_app/mersedes_photo.png')
img_label = Label(window_cntr, image=img)
img_label.pack()


def button_help_cntr(text, command:None):
    return Button(window_cntr, command=command,
           text=text, font=('Arial', 26, 'bold'), bg='yellow',
                  height=2)


label = Label(window_cntr, text='Добро пожаловать в окно контроля', font=('Arial', 35, 'bold'), bg='orange', fg='white')
label.pack()

label = Label(window_cntr, text='Услуги и цены: ', font=('Arial', 25, 'bold'), bg='black', fg='white')
label.place(x=0, y=47)

button_lst_service_price = button_help_cntr('Услуги и цены', None)
button_lst_service_price.place(x=0, y=77)

button_del_service = button_help_cntr('Удалить услугу', None)
button_del_service.place(x=373, y=77)

button_lst_service_price = button_help_cntr('Добавить услугу', None)
button_lst_service_price.place(x=746, y=77)

label = Label(window_cntr, text='Рабочии: ', font=('Arial', 25, 'bold'), bg='black', fg='white')
label.place(x=0, y=160)

button_del_service = button_help_cntr('  Механники  ', None)
button_del_service.place(x=0, y=192)

button_del_service = button_help_cntr('Администраторы', None)
button_del_service.place(x=360, y=192)

button_del_service = button_help_cntr('Удаление/Добавление', None)
button_del_service.place(x=675, y=192)

label = Label(window_cntr, text='Бизнес организация: ', font=('Arial', 25, 'bold'), bg='black', fg='white')
label.place(x=0, y=290)

button_del_service = button_help_cntr('  Прибыль  ', None)
button_del_service.place(x=0, y=324)

button_del_service = button_help_cntr('Убыль', None)
button_del_service.place(x=420, y=324)

button_del_service = button_help_cntr('Выплаты рабочим', None)
button_del_service.place(x=722, y=324)


window_cntr.mainloop()