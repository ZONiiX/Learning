import sqlite3

conn = sqlite3.connect('items.db')

c = conn.cursor()

c.execute("""CREATE TABLE items (
            item_id INTEGER AUTO_INCREMENT NOT NULL,
            name VARCHAR(30) NOT NULL, 
            price DECIMAL NOT NULL,
            URL VARCHAR(50) NOT NULL
)""")

items = [('')]

c.executemany("INSERT INTO items (?, ?, ?)", items)

conn.commit()
c.close()
