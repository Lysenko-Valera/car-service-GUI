import matplotlib.pyplot as plt
import sqlite3 as sql
from tkinter import messagebox


month_separator = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
lst_month = []
lst_income_month = []

def profit_chart_bd():
    """Делаем запрос в бд и из таблицы month_data берем чистую прибыль по месяцам, и в переменные
    заносим список месяцов список прибыльности по месяцам
    """
    pass



def profit_chart():
    """Создает диаграмму, на которой указанно за год сколько было потраченно денег по месяцам в виде диаграммы,
    данные о прибыли запрашиваем чз бз из таблици month_data
    """
    fig = plt.figure(figsize=(15, 8), facecolor='#A9A9A9')
    plt.suptitle('Прибыль', color = '#0000FF')
    plt.figtext(0.4, 0.9, 'Прибыль год', size = 20, color = '#0000FF')

    ax = fig.add_subplot()
    ax.set(facecolor = '#B0C4DE')

    ax.bar(month_separator, None, color = '#D2691E') #Строим дистограмму

    plt.xlabel('Месяц', color = '#0000FF')
    plt.ylabel('Прибыль', color = '#0000FF')
    plt.grid()


    plt.show()


def expenses_chart():
    """Создаем диаграмму, в диаграмме выводим информацию по месяцам о затратах (З/П и премия не в счет), эти данные берем из
    таблици month_data
    """
    fig = plt.figure(regsize=(10,10))
    plt.suptitle('Затраты: ')
    plt.figtext(0.5, 0.9, 'Данные о затратах по месяцам без учета выплаты З/П и премий')

    ax = fig.add_subplot()
    ax.set(facecolor = 'red')

    ax.bar(month_separator, None, color = '#D2691E')

    plt.xlabel('Месяца', color = 'red')
    plt.ylabel('Затраты, тыс руб', color = 'red')
    plt.grid()


    plt.show()


def pay_workers_chart():
    """Создаем диаграмму которая по месяцам показывает сколько приходилось денег на выплаты рабочим,
    данные о выплатах для рабочих запрашиваем из таблицы pay_workers_table, где указанны вся З/П и премия
    """
    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT zp_mechanic FROM mechanic_table;''')
            result_zp_mechanic = cursor.fetchall()
            mechanic_zp = sum([x[0] for x in result_zp_mechanic])
        except Exception:
            messagebox.showerror('Ошибка', 'Ошибка при работе с базой данных')

    with sql.connect('sql/mechanic_table.db') as con:
        cursor = con.cursor()
        try:
            cursor.execute('''SELECT zp_admin FROM admin_table;''')
            result_zp_admin = cursor.fetchall()
            admin_zp = sum([x[0] for x in result_zp_admin])
        except Exception:
            messagebox.showerror('Ошибка', 'Ошибка при работе с базой данных')

    fig = plt.figure(facecolor='#B0C4DE')
    plt.suptitle('Выплаты рабочим')
    plt.figtext('Диаграмма показывает сколько в каждом месеце были выплаты рабочим')

    ax = fig.add_subplot()
    ax.set(facecolor = 'red')
    #
    # ax.bar(, color='red')

    plt.xlabel('Месеца', color='red')
    plt.ylabel('Выплаты', color='red')
    plt.grid()


    plt.show()