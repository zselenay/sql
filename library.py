import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               author TEXT NOT NULL,
               genre TEXT,
               year INTEGER
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS members(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS loans(
               members_id INTEGER NOT NULL,
               books_id INTEGER NOT NULL,
               loan_date TEXT NOT NULL,
               return_date TEXT,
               id INTEGER PRIMARY KEY,
               FOREIGN KEY (members_id) REFERENCES members(id),
               FOREIGN KEY (books_id) REFERENCES books(id)
)
''')
cursor.execute("INSERT OR IGNORE INTO books (id,title, author, genre, year) VALUES (?, ?, ?, ?,?)",
               (1,"Suç ve Ceza", "Dostoyevski", "Roman", 1866))
cursor.execute("INSERT OR IGNORE INTO books (id,title, author, genre, year) VALUES (?, ?, ?, ?,?)",
               (2,"Leyla ile Mecnun", "Fuzuli", "Mesnevi", 1535))
cursor.execute("INSERT OR IGNORE INTO books (id,title, author, genre, year) VALUES (?, ?, ?, ?,?)",
               (3,"Kürk Mantolu Madonna", "Sabahattin Ali", "Roman", 1943))
cursor.execute("INSERT OR IGNORE INTO members (id,name) VALUES (?, ?)",
               (1,"Ali"))
cursor.execute("INSERT OR IGNORE INTO members (id,name) VALUES (?, ?)",
               (2,"Zeynep"))
cursor.execute("INSERT OR IGNORE INTO members (id,name) VALUES (?, ?)",
               (3,"Selin"))
cursor.execute("INSERT OR IGNORE INTO loans (id,members_id, books_id, loan_date, return_date) VALUES (?, ?, ?, ?,?)",
               (1,2 ,3, "2025-03-09",None))
cursor.execute("INSERT OR IGNORE INTO loans (id,members_id, books_id, loan_date, return_date) VALUES (?, ?, ?, ?,?)",
               (2,1 ,1, "2025-05-11","2025-06-12"))
cursor.execute("INSERT OR IGNORE INTO loans (id,members_id, books_id, loan_date, return_date) VALUES (?, ?, ?, ?,?)",
               (3,3 ,2, "2025-02-07","2025-07-18"))
cursor.execute("SELECT members.name, books.title, loans.loan_date FROM loans "
               "JOIN books ON loans.books_id = books.id "
               "JOIN members ON loans.members_id = members.id "
               "WHERE return_date IS NULL")
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("SELECT * FROM loans ORDER BY loan_date ASC")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.commit()