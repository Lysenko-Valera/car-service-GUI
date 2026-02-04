from tkinter import Label, Button, Toplevel
from tkinter.constants import CENTER
import control.button_control as bcntr
import control.db_button_control as bd_bctr
import diagram.profit_diagram as profit_diagram
from PIL import Image, ImageTk


def agree_next_month():
    """Создаем окно где есть только label и button по нажатю на кнопку сохраняються данные в бд"""
    agree_window = Toplevel()
    agree_window.title('Переход на следующий месяц')
    agree_window.geometry('500x250')
    agree_window.resizable(width=False, height=False)

    label = Label(agree_window, text='Окно соглашения. \n Нажмите на кнопку <перейти>, \n если хотите перейти на следующий месяц',
                  font=('Arial', 20, 'bold'), bg='orange', fg='white').pack()
    button_agree = Button(agree_window, command=bd_bctr.agree_next_month, text='Согласен',
                          font=('Arial', 30, 'bold'), bg='red', fg='black', width=14)
    button_agree.pack()


window_cntr = Toplevel()
window_cntr.title('Окно контроля')
window_cntr.geometry('1400x800')
window_cntr.resizable(False,False)


def button_help_cntr(text, command:None):
    return Button(window_cntr, command=command,
           text=text, width=18, font=('Arial', 26, 'bold'), bg='yellow',
                  height=2)


def control_window():
    img = Image.open('img_and_gif/shester.webp')
    img = img.resize((1400, 800))
    img_photo = ImageTk.PhotoImage(img)

    img_label = Label(window_cntr, image=img_photo)
    img_label.place(x=0, y=0)

    label = Label(window_cntr, text='Добро пожаловать в окно контроля', font=('Arial', 35, 'bold'), bg='orange', fg='white').pack()

    label = Label(window_cntr, text='Услуги и цены: ', font=('Arial', 25, 'bold'), bg='black', fg='white').place(x=0, y=47)

    button_lst_service_price = button_help_cntr('Услуги и цены', bcntr.lst_service_price).place(x=0, y=77)

    button_del_service = button_help_cntr('Удалить услугу', bcntr.del_service).place(relx=0.5, y=115, anchor=CENTER)

    button_lst_service_price = button_help_cntr('Добавить услугу', bcntr.add_service).place(x=1095, y=77)

    label = Label(window_cntr, text='Сотрудники Fergus AutoHub ', font=('Arial', 25, 'bold'), bg='black', fg='white').place(x=0, y=160)

    button_del_service = button_help_cntr('  Механники  ', bcntr.mechanic_see).place(x=0, y=192)

    button_del_service = button_help_cntr('Администраторы', bcntr.admin_see).place(relx=0.5, y=230, anchor=CENTER)

    button_del_service = button_help_cntr('Удаление/Добавление', bcntr.del_or_add_work).place(x=1095, y=192)

    label = Label(window_cntr, text='Бизнес организация: ', font=('Arial', 25, 'bold'), bg='black', fg='white').place(x=0, y=290)

    button_del_service = button_help_cntr('Рентабельность', profit_diagram.profit_diagram).place(x=0, y=324)

    button_next_month = Button(window_cntr, text='Переход месяца', command=agree_next_month,
                               font=('Arial', 26, 'bold'), bg='red', fg='black',  width=18, height=2).place(relx=0.5, y=365, anchor=CENTER)

    button_del_service = button_help_cntr('Выплаты рабочим', profit_diagram.pay_workers_diagram).place(x=1095, y=330)


    window_cntr.mainloop()

