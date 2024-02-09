import psycopg2

conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres',
                        password='200701', port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR

);
""")

cur.execute("""INSERT INTO person(id, name, age, gender) VAlUES
(1, 'João', 12, 'm'),
(2, 'Leo', 16, 'm'),
(3, 'Ana', 60, 'f'),
(4, 'Maria', 70, 'f'),
(5, 'Vitória', 23, 'f');                                    
""")

cur.execute("""SELECT * FROM person WHERE name = 'Vitória';""")

print(f"{cur.fetchone()}\n")

cur.execute("""SELECT * FROM person Where age < 50;""")

print("under 50 are:")
for row in cur.fetchall():
    print(f"{row}\n")

sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("L", 50))

print(sql)

cur.execute(sql)

print(cur.fetchall())

conn.commit()

cur.close()
conn.close()