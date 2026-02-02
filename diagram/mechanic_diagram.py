import matplotlib.pyplot as plt
import sqlite3 as sql
from tkinter import messagebox


def mechanic_chart():
    """Создаеться диаграмма, она показывает прибыльность с одного механника,
    по оси x пишеться id механника, по оси y пишеться прибыльность, данные беруться из таблици mechanic_table
    """
    with sql.connect('sql/mechanic_table.db') as con:
        cur = con.cursor()
        try:
            cur.execute('''SELECT id_mechanic FROM mechanic_table;''')
            result_id = cur.fetchall()
            cur.execute('''SELECT income FROM mechanic_table;''')
            result_income = cur.fetchall()

            income_mechanic = [int(x[0]) for x in result_income]
            id_mechanic = [int(x[0]) for x in result_id]
        except Exception:
            messagebox.showerror('Ошибка', 'Произошла ошибка при обращении к базе данных')


    fig = plt.figure(figsize=(7, 7), facecolor='#B0C4DE')
    plt.suptitle('Прибыль от механников')
    plt.figtext(0.2, 0.9, 'Диаграмма показывает то сколько денег принес каждый механник')

    ax = fig.add_subplot()
    ax.set(facecolor='#B0C4DE')

    ax.bar(list(map(int, id_mechanic)), income_mechanic)

    plt.xlabel('ID Механника')
    plt.ylabel('Прибыль с механника')
    ax.grid()

    plt.show()
