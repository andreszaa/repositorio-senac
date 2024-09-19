import sqlite3

class Model:
    def __init__(self):
        self.con = sqlite3.connect('books.db')
        self.cur = self.con.cursor()
        self.createTable()  # Criar tabela no banco de dados

    def createTable(self):
        # Criando a tabela Books se ela não existir
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price TEXT NOT NULL
        )
        """)
        self.con.commit()

    def addToTable(self, title, author, price):
        self.values = (str(title), str(author),  str(price))
        self.cur.execute("INSERT INTO Books (title, author, price) values (?,?,?)", self.values)
        self.con.commit()

    def updateTable(self, id, title, author, price):
        self.values = (str(title), str(author), str(price), int(id))
        self.cur.execute("UPDATE Books SET title = ?, author= ?, price= ? WHERE id = ?", self.values)
        self.con.commit()

    def deleteDataFromTable(self, id):
        self.values = (int(id),)
        self.cur.execute("DELETE FROM Books WHERE id = ?", self.values)
        self.con.commit()

    def getAllData(self):
        self.cur.execute("SELECT * FROM Books")
        result = self.cur.fetchall()
        self.con.commit()
        return result
