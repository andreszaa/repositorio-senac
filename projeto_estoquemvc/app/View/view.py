from tkinter import *
class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Estoque")
        self.root.geometry('550x350')
        self.createWidgets()

    def createWidgets(self):
        self.labelTitle = Label(self.root, text="Nome: ")
        self.labelTitle.grid(row=0, column=0, padx=5, pady=5)

        self.entryTitleTextVar = StringVar()
        self.entryTitle = Entry(self.root, textvariable=self.entryTitleTextVar)
        self.entryTitle.grid(row=0, column=1, padx=5, pady=5)

        self.labelAuthor = Label(self.root, text="Quantidade: ")
        self.labelAuthor.grid(row=1, column=0, padx=5, pady=5)

        self.entryAuthorTextVar = StringVar()
        self.entryAuthor = Entry(self.root, textvariable=self.entryAuthorTextVar)
        self.entryAuthor.grid(row=1, column=1, padx=5, pady=5)

        self.labelPrice = Label(self.root, text="Preço: ")
        self.labelPrice.grid(row=2, column=0, padx=5, pady=5)

        self.entryPriceTextVar = StringVar()
        self.entryPrice = Entry(self.root, textvariable=self.entryPriceTextVar)
        self.entryPrice.grid(row=2, column=1, padx=5, pady=5)

        self.buttonAdd = Button(self.root, text="Adicionar")
        self.buttonAdd.grid(row=3, column=0, pady=5)

        self.buttonUpdate = Button(self.root, text="Atualizar")
        self.buttonUpdate.grid(row=3, column=1, pady=5)

        self.buttonRemove = Button(self.root, text="Deletar")
        self.buttonRemove.grid(row=3, column=2, pady=5)

        self.listbox = Listbox(self.root, width=60)
        self.listbox.grid(row=4, column=1, padx=5, pady=5)

    def getTitleData(self):
        return self.entryTitleTextVar.get()

    def getAuthorData(self):
        return self.entryAuthorTextVar.get()
    
    def getPriceData(self):
        return self.entryPriceTextVar.get()

    def setTitle(self, title):
        self.entryTitleTextVar.set(title)

    def setAuthor(self, author):
        self.entryAuthorTextVar.set(author)

    def setPrice(self, Price):
        self.entryPriceTextVar.set(Price)

    def getCursorID(self, event=None):
        selectedLbData = self.listbox.curselection()
        id = self.listbox.get(selectedLbData)[0]
        return id

    def getCursorTitle(self):
        selectedLbData = self.listbox.curselection()
        title = self.listbox.get(selectedLbData)[1]
        return title

    def getCursorAuthor(self):
        selectedLbData = self.listbox.curselection()
        author = self.listbox.get(selectedLbData)[2]
        return author
    
    def getCursorPrice(self):
        selectedLbData = self.listbox.curselection()
        price = self.listbox.get(selectedLbData)[3]
        return price

    def setListbox(self, data):
        self.listbox.delete(0, END)
        for values in data:
            self.listbox.insert(END, values)