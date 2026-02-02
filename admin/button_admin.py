from tkinter import Button, Label, Entry, Toplevel
from tkinter.scrolledtext import ScrolledText
import admin.bd_admin_window as bdaw
from admin.create_car.create_car import Car


def see_service_and_price():
    """Создаем окно где выводим сервисные услуги, их цены, среднее время работы и id услуги, выводиться это все чз scrolltext,
    берем данные из service_table, где храниться вся инфа об услугах
    """
    window_service_admin = Toplevel()
    window_service_admin.title('Сервисные услуги и цены')
    window_service_admin.geometry('900x500')
    window_service_admin.resizable(width=False, height=False)

    label = Label(window_service_admin, text='Список услуг, их цен, время выполнения, их id', font=('Arial', 25, 'bold'), bg='orange', fg='white').pack()

    scroll_text = ScrolledText(window_service_admin, width=200, height=200, font=('Courier New', 19, 'bold'),
                               bg='black', fg='white')
    scroll_text.insert('1.0', bdaw.bd_service_see_admin())
    scroll_text.configure(state='disabled')  # Запрещаем заменять текст
    scroll_text.pack()



def mechanic_admin():
    """Создаем окно где выводим id механника, ФИО, специальность, опыт работы, выводиться чз scrolltext,
    берем данные из mechanic_table делая запрос в бд
    """
    window_mechanic_admin = Toplevel()
    window_mechanic_admin.title('Механники')
    window_mechanic_admin.geometry('900x500')
    window_mechanic_admin.resizable(width=False, height=False)

    lable = Label(window_mechanic_admin, text='Список механников, их id, специальность, опыт работы', font=('Arial', 25, 'bold'), bg='orange', fg='white').pack()

    scroll_text = ScrolledText(window_mechanic_admin, width=200, height=200,
                               font=('Courier New', 17, 'bold'), bg='black', fg='white')
    scroll_text.insert('1.0', bdaw.bd_see_mechanic())
    scroll_text.configure(state='disabled')
    scroll_text.pack()


def create_order():
    """Создаем окно где пользователь вводит данные о машине, они при помощи класса Сar валидируються и записываються в
    бд, где в дальнейшем можно будет узнать эту таблицу по нажатию кнопки <Активные заказы>, или после удаления <Завершенные заказы>
    """
    window_order = Toplevel()
    window_order.title('Создание заказа')
    window_order.geometry('1200x800')
    window_order.resizable(width=False, height=False)

    def order_help(txt: str):
        label = Label(window_order, text=txt, font=('Arial', 18, 'bold'), bg='black', fg='white').pack()
        entry = Entry(window_order, font=('Arial', 20), width=25, justify='left')
        entry.pack()
        return entry

    label = Label(window_order, text='Создание заказа',
                     font=('Arial', 25, 'bold'), bg='orange', fg='black').pack()

    id_order = order_help('Введите id заказа')
    brand_auto = order_help('Введите брэнд авто:')
    model_auto = order_help('Введите модель авто:')
    year_auto = order_help('Введите год авто:')
    mileage_auto = order_help('Введите пробег авто:')
    vin_auto = order_help('Введите вин номер авто типа [1_][**********][6_] где _-цифра, а *-цифра|буква":')
    fuel_type_auto = order_help('Введите тип топлива 1 - бензин, 2 - дизель, 3 - газ:')
    engine_capacity_auto = order_help('Введите объем двигателя авто вещественным числом:')
    gas_tank_capacity_auto = order_help('Введите объем бензобака авто:')
    types_services_auto = order_help('id видов услуг через пробел')
    id_mechanic_order = order_help('Введите id механника')

    def help_order_create():
        id = id_order.get()
        brand = brand_auto.get()
        model = model_auto.get()
        year = year_auto.get()
        mileage = mileage_auto.get()
        vin = vin_auto.get()
        fuel_type = fuel_type_auto.get()
        engine_capacity = engine_capacity_auto.get()
        gas_tank_capacity = gas_tank_capacity_auto.get()
        id_mechanic_order_auto = id_mechanic_order.get()
        types_services = types_services_auto.get()

        Car(int(id), str(brand), str(model), int(year), int(mileage), str(vin),
                       int(fuel_type), float(engine_capacity), int(gas_tank_capacity), str(types_services), int(id_mechanic_order_auto))

        bdaw.bd_create_order(int(id), str(brand), str(model), int(year), int(mileage), str(vin), int(fuel_type), float(engine_capacity),
                             int(gas_tank_capacity), str(types_services), int(id_mechanic_order_auto))


    button_order_cr = Button(window_order, command=help_order_create, text='Сохранить данные', font=('Arial', 40), bg='lime', width=14)
    button_order_cr.pack()


def completion_order():
    """Создает окно для завершения заказа, по id заказа удаляет его из таблици активных заказов и переносит
    его в окно завершенных заказов где только vin и услуги сделанные для этого vin
    """
    window_completion_order = Toplevel()
    window_completion_order.title('Завершение заказа')
    window_completion_order.geometry('900x500')
    window_completion_order.resizable(width=False, height=False)

    label = Label(window_completion_order, text='Завершить заказ по id заказа',
                     font=('Arial', 30, 'bold'), bg='orange', fg='black').pack()
    label = Label(window_completion_order, text='Введите id заказа',
                     font=('Arial', 25, 'bold'), bg='black', fg='white').pack()
    index = Entry(window_completion_order, font=('Arial', 25, 'bold'))
    index.pack()

    def help_completion_order():
        id_del = index.get()
        bdaw.bd_completion_order(id_del)

    button_order_complete = Button(window_completion_order, command=help_completion_order, text='Завершить',
                                   font=('Arial', 40, 'bold'), bg='lime', fg='black', width=12)
    button_order_complete.pack()


def see_active_order():
    """Созадет окно для просмотра активных заказов, просматривает все данные которые ввел администратор в окне
    "Создание заказа", выводиться через scroll text, делая запрос в бд
    """
    window_see_active_order = Toplevel()
    window_see_active_order.title('Активные заказы')
    window_see_active_order.geometry('900x500')
    window_see_active_order.resizable(width=False, height=False)

    label = Label(window_see_active_order, text='Просмотр активных заказов', font=('Arial', 22, 'bold'), bg='orange', fg='black').pack()

    scroll_text = ScrolledText(window_see_active_order, width=200, height=200, font=('Courier New', 12, 'bold'),
                               bg='black', fg='white')
    scroll_text.insert('1.0', bdaw.bd_see_active_order())
    scroll_text.configure(state='disabled')
    scroll_text.pack()


def see_completion_order():
    """Созадет окно для просмотра завершенных заказов, выводит чз scroll text, выводя только
    vin машины и услуги сделанные для этого vin, сюда переносяться заказы которые были завершенны
    """
    window_see_completion_order = Toplevel()
    window_see_completion_order.title('Завершенные заказы')
    window_see_completion_order.geometry('900x500')
    window_see_completion_order.resizable(width=False, height=False)

    label = Label(window_see_completion_order, text='Просмотр завершенных заказов', font=('Arial', 22, 'bold'), bg='orange',
                  fg='black').pack()

    scroll_text = ScrolledText(window_see_completion_order, width=200, height=200, font=('Courier New', 25, 'bold'),
                               bg='black', fg='white')
    scroll_text.insert('1.0', bdaw.bd_see_completion_order())
    scroll_text.configure(state='disabled')
    scroll_text.pack()

