from tkinter import Button, Label, Tk
# from PIL import  Image, ImageTk, ImageSequence
import admin.button_admin as buttad


window_admin_cntr = Tk()
window_admin_cntr.title('Окно администратора')
window_admin_cntr.geometry('1400x800')
window_admin_cntr.resizable(width=False, height=False)


def button_help_admin(text: str, command:None):
    return Button(window_admin_cntr, command=command, text=text, width=18, height=2,
                         font=('Arial', 28, 'bold'), bg='green', fg='black')


def admin_window():
    """pass"""
    label = Label(window_admin_cntr, text='Система управления админ панелью', width=40,
                 font=('Arial', 35, 'bold'), bg='orange').pack()

    label = Label(window_admin_cntr, text='Выберите что хотите сделать нажав кнопку:', width=45,
                 font=('Arial', 30, 'bold'), bg='black', fg='white').pack()

    button_list_services = button_help_admin('Услуги и цены', buttad.see_service_and_price).place(x=0, y=100)

    button_order_cr = button_help_admin('Создать заказ', buttad.create_order).place(x=1076, y=100)

    button_mechanik = button_help_admin('Показ механников', buttad.mechanic_admin).place(x=0, y=210)

    button_stop_order = button_help_admin('Завершить заказ', buttad.completion_order).place(x=1076, y=210)

    button_see_service = button_help_admin('Завершенные заказы', buttad.see_completion_order).place(x=545, y=100)

    button_active_order = button_help_admin('Активные заказы', buttad.see_active_order).place(x=545, y=210)

