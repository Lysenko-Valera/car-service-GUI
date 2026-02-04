from tkinter import Button, Label, Entry, Toplevel
from tkinter.scrolledtext import ScrolledText
import control.button_control_admin as bca
import control.db_button_control as bdb
import control.button_control_mechanic as bmc
import diagram.mechanic_diagram as chart_mech


def lst_service_price():
    """Функция для кнопки button_service_price из базы данных берет услуги их цены, себестоимость и прибыль,
    выводит это все через Text и с методом скроллинга
    """
    window_lst_service_price = Toplevel()
    window_lst_service_price.title('Список услуг')
    window_lst_service_price.geometry('1000x360')
    window_lst_service_price.resizable(width=False, height=False)

    label = Label(window_lst_service_price, text='Список услуг их цен, себестоимости, прибыли', font=('Arial', 20, 'bold'), bg='orange', fg='white').pack()
    scroll_text = ScrolledText(window_lst_service_price, width=200, height=200, font=('Courier New', 18, 'bold'), bg='black', fg='white')
    scroll_text.insert('1.0', bdb.bd_service())
    scroll_text.configure(state='disabled') #Запрещаем заменять текст
    scroll_text.pack()


def del_service():
    """Создаем окно для удаления услуги по id, надо ввести id, а затем id будет отправленно в функцию del_bd_service"""
    window_del_service = Toplevel()
    window_del_service.title('окно удаление услуги')
    window_del_service.geometry('300x230')
    window_del_service.resizable(width=False, height=False)

    lable = Label(window_del_service, text='Введите id, затем нажмите\n на кнопку \"Удалить\"',
                  bg='orange', fg='white', font=('Arial', 20, 'bold')).pack()
    entry_del_service = Entry(window_del_service, font=('Arial', 25, 'bold'), justify='left')
    entry_del_service.pack()
    def collecting_del_service():
        del_service = entry_del_service.get()
        bdb.bd_del_service(int(del_service))
    button_del_confirm_service = Button(window_del_service, text='Удалить', command=collecting_del_service,
                                        font=('Arial', 25, 'bold'), bg='red', fg='black').pack()


def add_service():
    """У пользователя чз новое окно берет данные service, price, cost_price, profit по нажатию на кнопку отправляет их в бд"""
    window_add_service = Toplevel()
    window_add_service.title('Окно добавления услуги')
    window_add_service.geometry('400x570')
    window_add_service.resizable(width=False, height=False)

    label = Label(window_add_service, text='Добавьте новые услуги\n вводя следующие данные:',
                  font=('Arial', 25, 'bold'), bg='orange', fg='white').pack()

    label = Label(window_add_service, text='Введите id новой услуги:', font=('Arial', 15, 'bold'), bg='black',fg='white').pack()
    entry_id_service = Entry(window_add_service, font=('Arial', 25, 'bold'), justify='left')
    entry_id_service.pack()
    label = Label(window_add_service, text='Введите название новой услуги:', font=('Arial', 15, 'bold'), bg='black', fg='white').pack()
    entry_new_service = Entry(window_add_service, font=('Arial', 25, 'bold'), justify='left')
    entry_new_service.pack()
    label = Label(window_add_service, text='Введите цену новой услуги: ', font=('Arial', 15, 'bold'), bg='black',fg='white').pack()
    entry_price_service = Entry(window_add_service, font=('Arial', 25, 'bold'), justify='left')
    entry_price_service.pack()
    label = Label(window_add_service, text='Введите среднее время выполнения:', font=('Arial', 15, 'bold'), bg='black', fg='white').pack()
    entry_time_service = Entry(window_add_service, font=('Arial', 25, 'bold'), justify='left')
    entry_time_service.pack()
    label = Label(window_add_service, text='Введите себестоимость новой услуги', font=('Arial', 15, 'bold'), bg='black',fg='white').pack()
    entry_cost_price_service = Entry(window_add_service, font=('Arial', 25, 'bold'), justify='left')
    entry_cost_price_service.pack()
    label = Label(window_add_service, text='Введите прибыльность с новой услуги', font=('Arial', 15, 'bold'), bg='black',fg='white').pack()
    entry_profit_sevice = Entry(window_add_service, font=('Arial', 25, 'bold'), justify='left')
    entry_profit_sevice.pack()

    def service_add_help():
        id_service = entry_id_service.get()
        new_service = entry_new_service.get()
        price_service = entry_price_service.get()
        time_service = entry_time_service.get()
        cost_price_service = entry_cost_price_service.get()
        profit_sevice = entry_profit_sevice.get()
        bdb.bd_add_service(int(id_service), str(new_service), int(price_service), float(time_service), int(cost_price_service), int(profit_sevice))

    button_add_service = Button(window_add_service, text='Добавить', command=service_add_help,
                                font=('Arial', 25, 'bold'), bg='lime', fg='black').pack()


def mechanic_see():
    """Создаем окно где получаем данные о механниках, кто чем занят, их успех в графике за неделю, месяц, год, их зп + премию"""
    window_mechanic_see = Toplevel()
    window_mechanic_see.title('Информация о механниках')
    window_mechanic_see.geometry('1000x360')
    window_mechanic_see.resizable(width=False, height=False)

    label = Label(window_mechanic_see, text='Информация о механниках', font=('Arial', 25, 'bold'), bg='orange', fg='white').pack()
    button_see_graph_mechanic = Button(window_mechanic_see, text='Просмотреть успех', command=chart_mech.mechanic_chart,
                                       font=('Arial', 25, 'bold'), bg='lime', fg='black').pack()
    scroll_text = ScrolledText(window_mechanic_see, width=100, height=100, font=('Courier New', 20, 'bold'), bg='black', fg='white')
    scroll_text.insert('1.0', bdb.bd_mechanic())
    scroll_text.configure(state='disabled') #Запрещаем заменять текст
    scroll_text.pack()


def admin_see():
    """Создаем окно где выводятся все администраторы, пароль, логин, зп + премия"""
    window_admin_see = Toplevel()
    window_admin_see.title('Информация о администраторах')
    window_admin_see.geometry('1000x360')
    window_admin_see.resizable(width=False, height=False)

    label = Label(window_admin_see, text='Информация о администраторах', font=('Arial', 25, 'bold'), bg='orange', fg='white').pack()
    scroll_text = ScrolledText(window_admin_see, width=200, height=200, font=('Courier New', 20, 'bold'), bg='black', fg='white')
    scroll_text.insert('1.0', bdb.bd_admin())
    scroll_text.configure(state='disabled')
    scroll_text.pack()


def del_or_add_work():
    """Делаем дополнительное окно где по нажатию кнопки удаляем/добавляем механника/администраторы,
     по нажатию на кнопку открывается еще одно окно
     """
    window_add_del_work = Toplevel()
    window_add_del_work.title('Добавление/удаление сотрудников')
    window_add_del_work.geometry('600x500')
    window_add_del_work.resizable(width=False, height=False)

    label = Label(window_add_del_work, text='Выберите кнопку кого хотите\n удалить/добавить', font=('Arial', 25, 'bold'), bg='orange', fg='white').pack()
    label = Label(window_add_del_work, text='Механники', font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    button_add_mechanic = Button(window_add_del_work, width=10, text='Добавить', command=bmc.button_add_mechanic,
                                 font=('Arial', 35, 'bold'), bg='lime', fg='black').pack()
    button_del_mechanic = Button(window_add_del_work, width=10, text='Удалить', command=bmc.button_del_mechanic,
                                 font=('Arial', 35, 'bold'), bg='red', fg='black').pack()
    label = Label(window_add_del_work, text='Администраторы', font=('Arial', 20, 'bold'), bg='black', fg='white').pack()
    button_add_admin = Button(window_add_del_work, width=10, text='Добавить', command=bca.button_add_admin,
                                 font=('Arial', 35, 'bold'), bg='lime', fg='black').pack()
    button_del_admin = Button(window_add_del_work, width=10, text='Удалить', command=bca.button_del_admin,
                                 font=('Arial', 35, 'bold'), bg='red', fg='black').pack()












