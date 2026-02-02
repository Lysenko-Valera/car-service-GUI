import sqlite3 as sql
from tkinter import messagebox


def profit_diagram_bd():
    """Делаем запрос в бд и из таблицы month_data берем чистую прибыль по месяцам, и в переменные
    заносим список месяцов список прибыльности по месяцам
    """
    with sql.connect('sql/month_data.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT number_month FROM month_data''')
            result_number_month = cursor.fetchall()
            result_month_lst = [x[0] for x in result_number_month]
            cursor.execute('''SELECT profitability FROM month_data''')
            result_profitability = cursor.fetchall()
            result_income_lst = [x[0] for x in result_profitability]
        except Exception:
            messagebox.showerror('Ошибка', f'Произошла ошибка при обращении к базе данных {Exception}')
            return
    return (result_month_lst, result_income_lst)


def pay_workers_diagram_bd():
    """Делаем запрос в бд и из таблицы mechanic_table берем данные о затратах без учета зп, тоесть
     столбец income
    """
    with sql.connect('sql/month_data.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT number_month FROM month_data''')
            result_number = cursor.fetchall()
            lst_num_month = [x[0] for x in result_number]
            cursor.execute('''SELECT pay_workers FROM month_data''')
            result_pay_workers = cursor.fetchall()
            lst_pay_workers = [x[0] for x in result_pay_workers]
        except:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')
            return
        return (lst_num_month, lst_pay_workers)