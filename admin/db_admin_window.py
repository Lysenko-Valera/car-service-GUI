import sqlite3 as sql
from tkinter import messagebox
from tabulate import tabulate


def bd_service_see_admin():
    """Чз service_table вытаскивает только 4 первые столбца, id, name_service, mean_time, price, после чего возвращает эти
    элементы в таблице типа tabulate
    """
    with sql.connect('sql/service_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT id_service, service, price, mean_time FROM service_table;''')
            result = cursor.fetchall()
            headers = ['id', 'Услуга', 'Цена', 'Ср.время']
            return tabulate(result, headers=headers, tablefmt='github')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_see_mechanic():
    """Делаем запрос в таблицу mechanic_table, где выбираем только
     id_mechanic, name_mechanic, special_mechanic, experience_mechanic
     """
    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()

        cursor.execute('''SELECT id_mechanic, name_mechanic, special_mechanic, experience_mechanic FROM mechanic_table;''')
        result = cursor.fetchall()
        headers = ['ID', 'ФИО', 'Специализация', 'Опыт']
    return tabulate(result, headers=headers, tablefmt='github')


def bd_create_order(id_order, brand: str, model: str, year: int, mileage: int, vin: str,
                    fuel_type: int, engine_capacity: float, gas_tank_capacity: int, service_car: str, id_mechanic: int):
    """Создаем заказ, при создании заказа создаем таблицу если ее нет, туда поступают такие данные как: |,
    и вся эта информация будет содержаться в таблице активных заказов,
     после удаления из этой таблици переходит в таблицу завершенных заказов
     """
    with sql.connect('sql/service_table.db') as con:
        cursor = con.cursor()
        try:
            service_ids = list(map(int, service_car.split(',')))
            tuples_count_ids = ','.join('?' * len(service_ids))
            cursor.execute(f'''SELECT price FROM service_table WHERE id_service IN ({tuples_count_ids});''', tuple(service_ids))
            price = sum(row[0] for row in cursor.fetchall())
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')
            return


    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''UPDATE mechanic_table SET income = income + ? WHERE id_mechanic = ?''', (price, id_mechanic))
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')
            return


    with sql.connect('sql/active_order_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS active_order_table(id_order INT, brand TEXT, model TEXT,
            year INT, mileage INT, vin TEXT, fuel_type INT, engine_capacity FLOAT,
             gas_tank_capacity INT, service_car TEXT, id_mechanic INT);''')
            cursor.execute('''INSERT INTO active_order_table(id_order, brand, model, year, mileage, vin,
             fuel_type, engine_capacity, gas_tank_capacity, service_car, id_mechanic)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (id_order, brand, model, year, mileage, vin,
                                                           fuel_type, engine_capacity, gas_tank_capacity, service_car, id_mechanic))
            messagebox.showinfo('Успех создание заказа', 'Заказ был создан, можете просмотреть его в окне активных заказах')
            messagebox.showinfo('Цена', f'Заказ вышел на сумму {price}')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')
            return


def bd_see_active_order():
    """Просматриваем все активные заказы и информацию по ним в active_order_table"""
    with sql.connect('sql/active_order_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT * FROM active_order_table;''')
            result = cursor.fetchall()
            headers = ['ID', 'Брэнд', 'Модель', 'Год', 'Пробег', 'VIN', 'Топливо', 'Объем ДВС', 'Бак', 'Сумма', 'ID механника']
            return tabulate(result, headers=headers, tablefmt='github')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_completion_order(id: int):
    """Делаем запрос в active_order_table, достаем от туда только VIN и service, создаем/записываем в таблицу
    completion_order_table ВИН(он будет единым, т.е если машина с таким же ВИН уже была, то к этому ВИН запишутся только сделанные услуги,

    ШАГИ удаления|записи:
    1. Из таблицы active_order_table достаем VIN и service_car из строки с id переданным пользователем
    2. Создаем таблицу completion_order_table, если она не создана
    3. Проверяем, есть ли в completion_order_table этот VIN, если есть, то только дописываем услуги, если нет, то добавляем в таблицу
    ВИН и записываем услуги
    4. Удаляем по id из active_order_table строку
    """
    with sql.connect('sql/active_order_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute(f'''SELECT vin, service_car FROM active_order_table WHERE id_order = ?;''', (id,))
            row = cursor.fetchone()
            vin, new_service = row
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при попытки обратиться к базе данных')
            return

    with sql.connect('sql/completion_order_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS completion_order_table(vin TEXT, services TEXT);''')
            if row:
                cursor.execute(f'''UPDATE completion_order_table SET services 
                = services || " " || ? WHERE vin = ?;''', (new_service, vin)) # Если заказы уже были на этот номер
                # то заказы только обновяться при помощи конкотенации
            else:
                cursor.execute('''INSERT INTO completion_order_table(vin, services)
                VALUES (?,?);''', (vin, new_service)) # если же вин номера такого не было то он добавиться в бд
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при попытке обращения к базе данных')
            return

    with sql.connect('sql/active_order_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute(f'''DELETE FROM active_order_table WHERE id_order = {id}''')
            messagebox.showinfo('Информирование об удаление', f'Заказ под {id} был удален')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при удалении заказа из базы данных')
            return

def bd_see_completion_order():
    """Из таблицы completion_order_table выводим все элементы"""
    with sql.connect('sql/completion_order_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT * FROM completion_order_table;''')
            result = cursor.fetchall()
            headers = ['VIN', 'Сделанные услуги']
            return tabulate(result, headers=headers, tablefmt='github')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')




