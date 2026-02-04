from tkinter import messagebox
import sqlite3 as sql
from tabulate import tabulate


def bd_service():
    """Делаем запрос в бд для функции lst_service_price"""
    with sql.connect('sql/service_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT * FROM service_table;''')
            result = cursor.fetchall()
            headers = ['ID', 'Услуга', 'Цена', 'Время работы', 'Себестоимость', 'Прибыль']
            return tabulate(result, headers=headers, tablefmt='github')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_add_service(id_service: int, service: str, price: int, mean_time: float, cost_price: int, profit: int):
    """В бд добавяет service-услугу, price-цену, cost_price-себестоимость, profit-прибыль,
    эти данные валидируются по типу данных. Принятие данных из функции add_service
    """
    with sql.connect('sql/service_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS service_table (
            id_service INT, service TEXT, price INT, mean_time FLOAT, cost_price INT, profit INT);''')
            cursor.execute('''INSERT INTO service_table(id_service, service, price, mean_time, cost_price, profit)
            VALUES (?, ?, ?, ?, ?, ?);''', (id_service, service, price, mean_time, cost_price, profit))
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_del_service(id_service: int):
    """Делает запрос в бд и удаляет заданный id"""
    with sql.connect('sql/service_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute(f'''DELETE FROM service_table WHERE id_service = {id_service};''')
            messagebox.showinfo('Уведомление об удалении', f'Услуга под id {id_service} удалена')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')




def bd_mechanic():
    """Делаем запрос в бд для получения данных о механниках"""
    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT id_mechanic, name_mechanic, special_mechanic, 
            experience_mechanic, zp_mechanic, prize_mechanic FROM mechanic_table;''')
            result = cursor.fetchall()
            headers = ['ID', 'ФИО', 'Специализация', 'Опыт', 'З/П', 'Премия']
            return tabulate(result, headers=headers, tablefmt='github')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_add_mechanic(id_mechanic: int, name_mechanic: str, special_mechanic: str,
                    experience_mechanic: int, zp_mechanic: int, prize_mechanic: int):
    """Добавляет в бд нового механника, c полями, id, cпециальность механника, зп, премию"""
    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS mechanic_table(
            id_mechanic INT, name_mechanic TEXT, special_mechanic TEXT, experience_mechanic INT, zp_mechanic 
             INT, prize_mechanic INT, income INT);''')

            cursor.execute('''INSERT INTO mechanic_table(id_mechanic, name_mechanic, special_mechanic, 
            experience_mechanic, zp_mechanic, prize_mechanic, income) 
            VALUES (?, ?, ?, ?, ?, ?, ?);''', (id_mechanic, name_mechanic, special_mechanic,
                                               experience_mechanic, zp_mechanic, prize_mechanic, 0))
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_del_mechanic(id_mechanic: int):
    """Удаляет механника по id из бд из таблицы mechanic_table"""
    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute(f'''DELETE FROM mechanic_table WHERE id_mechanic = {id_mechanic};''')
            messagebox.showinfo('Уведомление об удалении', f'Механник под id {id_mechanic} удален')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')




def bd_admin():
    """Делаем запрос в бд для получения данных о администраторах, пароль, логин, зп + премия"""
    with sql.connect("sql/admin_table.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT * FROM admin_table''')
            result = cursor.fetchall()
            headers = ['ID', 'ФИО', 'Логин', 'Пароль', 'З/П', 'Премия']
            return tabulate(result, headers=headers, tablefmt='github')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_add_admin(id_admin: int, name_admin: str, login_admin: str, password_admin: str, zp_admin: int, prize_admin: int):
    """Через бд добавляем администратора в таблицу"""
    with sql.connect("sql/admin_table.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS admin_table(
            id_admin INT, name_admin TEXT, login_admin TEXT, password_admin TEXT, zp_admin INT, prize_admin INT);''')

            cursor.execute(f'''INSERT INTO admin_table(id_admin, name_admin, login_admin, password_admin, zp_admin,
            prize_admin) VALUES (?, ?, ?, ?, ?, ?);''', (id_admin, name_admin, login_admin, password_admin, zp_admin, prize_admin))
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def bd_del_admin(id_admin: int):
    """По id данное пользователю заходим в таблицу admin_table и удаляем администартора"""
    with sql.connect("sql/admin_table.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute(f'DELETE FROM admin_table WHERE id_admin = {id_admin};')
            messagebox.showinfo('Уведомление об удалении', f'Администратор под id {id_admin} удален')
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


def agree_next_month():
    """Из таблицы mechanic_table берем данные о прибыли, зп, премии, из admin_table
    аналогично кроме прибыли, затем создаем таблицу month_data и вписываем туда все затраты и
    чистую прибыль
    """
    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT zp_mechanic FROM mechanic_table;''')
            result_zp_mechanic = cursor.fetchall()
            cursor.execute('''SELECT prize_mechanic FROM mechanic_table;''')
            result_prize_mechanic = cursor.fetchall()
            cursor.execute('''SELECT income FROM mechanic_table;''')
            result_income = cursor.fetchall()
            zp_mechanic = sum([x[0] for x in result_zp_mechanic])
            prize_mechanic = sum([x[0] for x in result_prize_mechanic])
            pay_mechanic = int(zp_mechanic) + int(prize_mechanic) #затраты на выплаты механникам
            income_dirty = int(sum([x[0] for x in result_income])) #Грязный доход
        except Exception:
            messagebox.showerror('Ошибка', 'Ошибка при обращении к базе данных')

    with sql.connect('sql/admin_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT zp_admin FROM admin_table;''')
            result_admin_zp = cursor.fetchall()
            cursor.execute('''SELECT prize_admin FROM admin_table;''')
            result_prize_admin = cursor.fetchall()
            admin_zp = sum([x[0] for x in result_admin_zp])
            prize_admin = sum([x[0] for x in result_prize_admin])
            pay_admin = admin_zp + prize_admin #оплаты админам зп и премии
        except Exception:
            messagebox.showerror('Ошибка', 'Ошибка при обращении к базе данных')

    profitability = income_dirty - (pay_mechanic + pay_admin) #чистый доход
    pay_workers = pay_mechanic + pay_admin #расходы на выплаты рабочим

    with sql.connect('sql/month_data.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS month_data(number_month INT, 
            profitability INT, pay_workers INT);''')
            cursor.execute('''SELECT number_month FROM month_data;''')
            result_month = cursor.fetchall()
            if result_month:
                number_mount = 1 + max([x[0] for x in result_month])
            else:
                number_mount = 1
            cursor.execute('''INSERT INTO month_data(number_month, profitability, pay_workers)
            VALUES (?, ?, ?);''', (number_mount, profitability, pay_workers))
            messagebox.showinfo('Оповещение', 'Произошол переход на следующий месяц')
        except Exception:
            messagebox.showerror('Ошибка', 'Ошибка при обращении к базе данных')





