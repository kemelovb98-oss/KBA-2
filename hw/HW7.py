import sqlite3

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

cursor.execute("""
     CREATE TABLE IF NOT EXISTS products (
       title TEXT NOT NULL,
       price REAL DEFAULT 0.0,
       quantity INTEGER DEFAULT 0
       )
""")
conn.commit()
def create_product(title,price,quantity):
    cursor.execute("INSERT INTO products (title,price,quantity) VALUES (?,?,?)",
                   (title,price,quantity))
    conn.commit()
    print(f"Товар '{title}'успешно добавлен.")

def read_all_products():
    cursor.execute("SELECT rowid, * FROM products")
    items = cursor.fetchall()
    print("\n Список всех товаров:")
    for item in items:
        print(f"ID: {item[0]} | Название: {item[1]} | Цена: {item[2]} | Кол-во: {item[3]}")
def update_product_price(row_id, new_price):
    cursor.execute("UPDATE products SET price = ? WHERE rowid = ?", (new_price, row_id))
    conn.commit()
    print(f"\n Цена товара с ID {row_id} изменена на {new_price}.")

def delete_product(row_id):
    cursor.execute("DELETE FROM products WHERE rowid = ?", (row_id,))
    conn.commit()
    print(f"\n Товар с ID {row_id} удален.")

def get_by_rowid(row_id):
    cursor.execute("SELECT rowid, * FROM products WHERE rowid = ?", (row_id,))
    product = cursor.fetchone()
    if product:
        print(f"\n Найдена запись по ID {row_id}: {product}")
    else:
        print(f"\n Запись с ID {row_id} не найдена.")

create_product("iphone 16", 120000.0, 5)
create_product("MacBook Air", 150000.0, 3)
create_product("AirPods", 25000.0, 10)

read_all_products()

get_by_rowid(2)

update_product_price(1, 115000.0)

delete_product(3)

read_all_products()

conn.close()



