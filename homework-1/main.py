"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="4468"
) as conn:
    with conn.cursor() as cur_emp:
        with open('north_data/employees_data.csv', 'r', encoding='utf=8') as file:
            reader = csv.reader(file)
            header = next(file)
            for row in reader:
                cur_emp.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)

    with conn.cursor() as cur_cust:
        with open('north_data/customers_data.csv', 'r', encoding='utf=8') as file:
            reader = csv.reader(file)
            header = next(file)
            for row in reader:
                cur_cust.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)

    with conn.cursor() as cur_order:
        with open('north_data/orders_data.csv', 'r', encoding='utf=8') as file:
            reader = csv.reader(file)
            header = next(file)
            for row in reader:
                cur_order.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)

conn.close()
