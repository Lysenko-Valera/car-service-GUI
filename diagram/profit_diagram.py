import matplotlib.pyplot as plt
import sqlite3 as sql
from tkinter import messagebox
import diagram.profit_diagram_bd as profit_bd


month_separator = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

def profit_diagram():
    """Создает диаграмму, на которой указанно за год сколько было потраченно денег по месяцам в виде диаграммы,
    данные о прибыли запрашиваем чз бз из таблици month_data
    """
    fig = plt.figure(figsize=(15, 8), facecolor='#A9A9A9')
    plt.suptitle('Прибыль', color = '#0000FF')
    plt.figtext(0.4, 0.9, 'Прибыль год', size = 20, color = '#0000FF')

    ax = fig.add_subplot()
    ax.set(facecolor = '#B0C4DE')

    lst_month, lst_income_month = profit_bd.profit_diagram_bd()
    lst_month = month_separator[:max(lst_month) + 1]
    ax.bar(lst_month, lst_income_month, color = '#D2691E') #Строим дистограмму

    plt.xlabel('Месяц', color = '#0000FF')
    plt.ylabel('Прибыль', color = '#0000FF')
    plt.grid()

    plt.show()


def pay_workers_diagram():
    """Создаем диаграмму которая по месяцам показывает сколько приходилось денег на выплаты рабочим,
    данные о выплатах для рабочих запрашиваем из таблицы pay_workers_table, где указанны вся З/П и премия
    """
    fig = plt.figure(facecolor='#B0C4DE')
    plt.suptitle('Выплаты рабочим')
    plt.figtext(0.3, 0.9, 'Выплаты рабочим', size = 20, color = '#0000FF')

    ax = fig.add_subplot()
    ax.set(facecolor = 'red')

    number_month, lst_pay_workers = profit_bd.pay_workers_diagram_bd()

    ax.bar(month_separator[:max(number_month) + 1], lst_pay_workers)

    plt.xlabel('Месеца', color='red')
    plt.ylabel('Выплаты', color='red')
    plt.grid()


    plt.show()