from tkinter import *

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.buttonAdd["command"] = self.addDataToLbx
        self.view.buttonUpdate["command"] = self.updateDataFromLBX
        self.view.buttonRemove["command"] = self.removeDataFromLBX
        self.view.listbox.bind('<<ListboxSelect>>', self.loadLbxDataToEntry)
        self.loadDataToLBX()

    def loadDataToLBX(self):
        data = self.model.getAllData()
        self.view.setListbox(data)

    def addDataToLbx(self):
        self.addToDB()
        self.loadDataToLBX()

    def removeDataFromLBX(self):
        self.removeDataFromDB()
        self.loadDataToLBX()

    def updateDataFromLBX(self):
        self.updateDB()
        self.loadDataToLBX()

    def loadLbxDataToEntry(self, event=None):
        title = self.view.getCursorTitle()
        author = self.view.getCursorAuthor()
        price = self.view.getCursorPrice()
        self.view.setTitle(title)
        self.view.setAuthor(author)
        self.view.setPrice(price)
        print("ID: ", self.view.getCursorID(), "\nTITLE: ", title, "\nAUTHOR: ", author, "\nPRICE: ", price)

    def addToDB(self):
        title = self.view.getTitleData()
        author = self.view.getAuthorData()
        price = self.view.getPriceData()
        self.model.addToTable(title, author, price)

    def updateDB(self):
        id = self.view.getCursorID()
        title = self.view.getTitleData()
        author = self.view.getAuthorData()
        price = self.view.getPriceData()
        self.model.updateTable(id, title, author, price)

    def removeDataFromDB(self):
        id = self.view.getCursorID()
        self.model.deleteDataFromTable(id)