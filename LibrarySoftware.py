#Book Worm SoftWare was created by Farshid Javadi on 17/10/99
# as a project in the DataBase lesson
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
###################
#/////////////////#
class edit_books(QtWidgets.QDialog):
    def __init__(self):
        super(edit_books,self).__init__()
        uic.loadUi('edit_books.ui',self)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        self.list_all_book.setColumnWidth(0, 400)
        self.list_all_book.setColumnWidth(1, 200)
        self.list_all_book.setColumnWidth(2, 200)
        self.list_all_book.setColumnWidth(3, 200)
        self.list_all_book.setColumnWidth(4, 200)
        self.list_all_book.setColumnWidth(5, 200)
        self.list_all_book.setColumnWidth(6, 200)
        self.list_all_book.setColumnWidth(7, 200)
        self.list_all_book.setColumnWidth(8, 100)
        self.list_all_book.setColumnWidth(9, 200)
        self.list_all_book.setColumnWidth(10, 200)
        self.list_all_book.setColumnWidth(11, 150)
        self.list_all_book.setColumnWidth(12, 150)
        book = cur.execute(f"select  * from TBooks")
        self.list_all_book.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_book.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_book.setItem(row, column, QTableWidgetItem(str(item)))
        cur.close
        self.ExitPushButton.clicked.connect(self.close)
        self.SavePushButton.clicked.connect(self.edit_book)
        # self.refreshPushButton.clicked.connect(self.refresh_table)
    # def refresh_table(self):
    def edit_book(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        ti = self.TitleLineEdit.text()
        au = self.PublisherLineEdit.text()
        ed = self.EditionLineEdit.text()
        bt = self.BookTypeLineEdit.text()
        Isb = self.ISBNLineEdit.text()
        pr = self.PriceLineEdit.text()
        py = self.PublicationYearLineEdit.text()
        Iy = self.InventoryLineEdit.text()
        bd = self.BookIDLineEdit.text()
        ss = self.statusLineEdit.text()
        cur.execute(f"update TBooks  set Title ='{ti}',Publisher ='{au}' ,Edition ='{ed}' ,BookType ='{bt}' ,ISBN ='{Isb}'\
            ,Price ='{pr}' ,PublicationYear ='{py}',Inventory ='{Iy}' ,BookID ='{bd}'  where Status ='{ss}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('Information of this Book was Update Successfully')
        msg.setWindowTitle('Edit Books')
        msg.exec()
        self.TitleLineEdit.setText('')
        self.PublisherLineEdit.setText('')
        self.EditionLineEdit.setText('')
        self.BookTypeLineEdit.setText('')
        self.ISBNLineEdit.setText('')
        self.PriceLineEdit.setText('')
        self.PublicationYearLineEdit.setText('')
        self.InventoryLineEdit.setText('')
        self.BookIDLineEdit.setText('')
        self.statusLineEdit.setText('')
        cur.close()
###################
#/////////////////#
class all_librarians (QtWidgets.QDialog):
     def __init__(self):
        super(all_librarians,self).__init__()
        uic.loadUi('all_librarian.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.list_all_librarian.setColumnWidth(0,300)
        self.list_all_librarian.setColumnWidth(1,400)
        self.list_all_librarian.setColumnWidth(2,200)
        self.list_all_librarian.setColumnWidth(3,200)
        self.list_all_librarian.setColumnWidth(4,200)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Member = cur.execute(f"select  * from TLibrarian")
        self.list_all_librarian.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_librarian.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_librarian.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
###################
#/////////////////#
class all_members (QtWidgets.QDialog):
     def __init__(self):
        super(all_members,self).__init__()
        uic.loadUi('all_member.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.list_all_member.setColumnWidth(0,300)
        self.list_all_member.setColumnWidth(1,400)
        self.list_all_member.setColumnWidth(2,200)
        self.list_all_member.setColumnWidth(3,200)
        self.list_all_member.setColumnWidth(4,200)
        self.list_all_member.setColumnWidth(5,200)
        self.list_all_member.setColumnWidth(6,200)
        self.list_all_member.setColumnWidth(7,200)
        self.list_all_member.setColumnWidth(8,200)
        self.list_all_member.setColumnWidth(9,200)
        self.list_all_member.setColumnWidth(10,150)
        self.list_all_member.setColumnWidth(11,100)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Member = cur.execute(f"select  * from TMembership")
        self.list_all_member.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_member.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_member.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
###################
#/////////////////#
class all_authors (QtWidgets.QDialog):
     def __init__(self):
        super(all_authors,self).__init__()
        uic.loadUi('all_author.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.list_all_author.setColumnWidth(0,300)
        self.list_all_author.setColumnWidth(1,400)
        self.list_all_author.setColumnWidth(2,200)
        self.list_all_author.setColumnWidth(3,200)
        self.list_all_author.setColumnWidth(4,100)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Member = cur.execute(f"select  * from TAuthor")
        self.list_all_author.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_author.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_author.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
###################
#/////////////////#
class all_authors (QtWidgets.QDialog):
     def __init__(self):
        super(all_authors,self).__init__()
        uic.loadUi('all_author.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.list_all_author.setColumnWidth(0,300)
        self.list_all_author.setColumnWidth(1,400)
        self.list_all_author.setColumnWidth(2,200)
        self.list_all_author.setColumnWidth(3,200)
        self.list_all_author.setColumnWidth(4,100)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Member = cur.execute(f"select  * from TAuthor")
        self.list_all_author.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_author.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_author.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
###################
#/////////////////#
class widget(QtWidgets.QWidget):
    def __init__(self):
        super(widget,self).__init__()
        uic.loadUi('UserPass.ui',self)
        self.LoginPushButton.clicked.connect(self.Handel_Login)
        self.ExitPushButton.clicked.connect(self.close)
    def Handel_Login(self):
        userName =self.UserNameLineEdit.text()
        password = self.PasswordLineEdit.text()
        if userName == 'farshid' and password == 'admin':
            print('user match')
            self.window2 = main_form()
            self.close()
            self.window2.show()
        else:
            self.Textlabel.setText('Username or password is incorrect...')
            self.UserNameLineEdit.setText('')
            self.PasswordLineEdit.setText('')
####################
#//////////////////#
class all_books(QtWidgets.QDialog):
    def __init__(self):
        super(all_books,self).__init__()
        uic.loadUi('all_books.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.list_all_book.setColumnWidth(0,400)
        self.list_all_book.setColumnWidth(1,200)
        self.list_all_book.setColumnWidth(2,200)
        self.list_all_book.setColumnWidth(3,200)
        self.list_all_book.setColumnWidth(4,200)
        self.list_all_book.setColumnWidth(5,200)
        self.list_all_book.setColumnWidth(6,200)
        self.list_all_book.setColumnWidth(7,200)
        self.list_all_book.setColumnWidth(8,100)
        self.list_all_book.setColumnWidth(9,200)
        self.list_all_book.setColumnWidth(10,200)
        self.list_all_book.setColumnWidth(11,150)
        self.list_all_book.setColumnWidth(12,150)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Member = cur.execute(f"select  * from TBooks")
        self.list_all_book.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_book.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_book.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
####################
#//////////////////#
class delete_books(QtWidgets.QDialog):
    def __init__(self):
        super(delete_books,self).__init__()
        uic.loadUi('DeleteBooks.ui',self)    
####################
#//////////////////#
class borrow_books(QtWidgets.QDialog):
    def __init__(self):
        super(borrow_books,self).__init__()
        uic.loadUi('borrow.ui',self)
        self.BookIDLineEdit.textChanged.connect(self.filter_bd)
        self.ISBNLineEdit.textChanged.connect(self.filter_IN)
        self.MemberIDLineEdit.textChanged.connect(self.filter_MSh)
        self.MembershipLastNameLineEdit.textChanged.connect(self.filter_LN)
        # self.BorrowPushButton.clicked.connect(self.Borrow)
        # self.ClearPushButton.clicked.connect(self.filter_bd)
        self.ExitPushButton.clicked.connect(self.close)
        self.TableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.TableWidget.setColumnWidth(0,70)
        self.TableWidget.setColumnWidth(1,200)
        self.TableWidget.setColumnWidth(2,200)
        self.TableWidget.setColumnWidth(3,200)
        self.TableWidget.setColumnWidth(4,200)
        self.TableWidget.setColumnWidth(5,200)
        self.TableWidget.setColumnWidth(5,300)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Member = cur.execute(f"select MemberID,LastName,NationalCode,RegisteryDate,ExpirityDate,MembershipType,Status from TMembership")
        self.TableWidget.setRowCount(0)
        for row, form in enumerate(cur):
            self.TableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.TableWidget.setItem(row, column,QTableWidgetItem(str(item)))
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Book = cur.execute(f"select BookID,Title,ISBN,Inventory,Edition,Status from TBooks")
        self.ListTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ListTable.setColumnWidth(0,100)
        self.ListTable.setColumnWidth(1,380)
        self.ListTable.setColumnWidth(2,300)
        self.ListTable.setColumnWidth(3,110)
        self.ListTable.setColumnWidth(4,110)
        self.ListTable.setColumnWidth(5,150)
        self.ListTable.setRowCount(0)
        for row, form in enumerate(cur): 
            self.ListTable.insertRow(row)
            for column, item in enumerate(form):
                self.ListTable.setItem(row, column,QTableWidgetItem(str(item)))    
    def filter_bd (self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Book = cur.execute(f"select BookID,Title,ISBN,Inventory,Edition,Status from TBooks  where BookID = {self.BookIDLineEdit.text()} ")
        self.ListTable.setRowCount(0)
        for row, form in enumerate(cur): 
            self.ListTable.insertRow(row)
            for column, item in enumerate(form):
                self.ListTable.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
    def filter_IN (self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Book = cur.execute(f"select BookID,Title,ISBN,Inventory,Edition,Status from TBooks where ISBN = {self.ISBNLineEdit.text()}")
        self.ListTable.setRowCount(0)
        for row, form in enumerate(cur): 
            self.ListTable.insertRow(row)
            for column, item in enumerate(form):
                self.ListTable.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
    
    def filter_MSh (self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        cur = sqlite_connection.cursor()
        Book = cur.execute(f"select MemberID,LastName,NationalCode,RegisteryDate,ExpirityDate,MembershipType,Status from TMembership where MemberID = {self.MemberIDLineEdit.text()}")
        self.TableWidget.setRowCount(0)
        for row, form in enumerate(cur): 
            self.TableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.TableWidget.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
    def filter_LN (self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Book = cur.execute(f"select MemberID,LastName,NationalCode,RegisteryDate,ExpirityDate,MembershipType,Status from TMembership where LastName = {self.MembershipLastNameLineEdit.text()}")
        self.TableWidget.setRowCount(0)
        for row, form in enumerate(cur): 
            self.TableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.TableWidget.setItem(row, column,QTableWidgetItem(str(item)))
        cur.close
    # def Borrow(self):
    #     if Clicked.BorrowPushButton :
    #         sqlite_connection = sqlite3.connect("BWSoftDB.db")
    #         cur = sqlite_connection.cursor()
    #         Book = cur.execute(f"
    #         print('This Book Borrowed')
####################
#//////////////////#
class add_librarian(QtWidgets.QDialog):
    def __init__(self):
        super(add_librarian,self).__init__()
        uic.loadUi('AddLibrarian.ui',self)
        self.SavePushButton.clicked.connect(self.insert_librarian)
        self.ExitPushButton.clicked.connect(self.close)

    def insert_librarian(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeLineEdit.text()
        pc = self.PersonnelCodeLineEdit.text()
        ed = self.EntryDateLineEdit.text()
        cur.execute(f"insert into TLibrarian (FirstName,LastName,NationalCode,PersonnelCode,EntryDate)\
            values('{fn}','{ln}','{nc}','{pc}','{ed}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Librarian was Added Successfully')
        msg.setWindowTitle('Add Librarian')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeLineEdit.setText('')
        self.PersonnelCodeLineEdit.setText('')
        self.EntryDateLineEdit.setText('')
        cur.close    
####################
#//////////////////#
class Membership(QtWidgets.QDialog):
    def __init__(self):
        super(Membership,self).__init__()
        uic.loadUi('AddLibraryMember.ui',self)
        self.SavePushButton.clicked.connect(self.insert_Membership)
        self.ExitPushButton.clicked.connect(self.close)

    def insert_Membership(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeLineEdit.text()
        ry = self.RegisteryDateLineEdit.text()
        ed = self.ExpirityDateLineEdit.text()
        mp = self.MembershipTypeLineEdit.text()
        cy = self.CityLineEdit.text()
        st = self.StreetLineEdit.text()
        pc = self.PostalCodeLineEdit.text()
        ay = self.AlleyLineEdit.text()
        ss = self.StatusLineEdit.text()
        cur.execute(f"insert into TMembership (FirstName,LastName,NationalCode,RegisteryDate,ExpirityDate,MembershipType,City,Street,PostalCode,Alley,Status)\
            values('{fn}','{ln}','{nc}','{ry}','{ed}','{mp}','{cy}','{st}','{pc}','{ay}','{ss}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Membership was Added Successfully')
        msg.setWindowTitle('Membership')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeLineEdit.setText('')
        self.RegisteryDateLineEdit.setText('')
        self.ExpirityDateLineEdit.setText('')
        self.MembershipTypeLineEdit.setText('')
        self.CityLineEdit.setText('')
        self.StreetLineEdit.setText('')
        self.PostalCodeLineEdit.setText('')
        self.AlleyLineEdit.setText('')
        self.StatusLineEdit.setText('')
        cur.close
####################
#//////////////////#
class add_books_author(QtWidgets.QDialog):
    def __init__(self):
        super(add_books_author,self).__init__()
        uic.loadUi('AddBooksAuthor.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.SavePushButton.clicked.connect(self.insert_author_books)

    def insert_author_books(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeineEdit.text()
        od = self.ORCIDLineEdit.text()
        cur.execute(f"insert into TAuthor (FirstName,LastName,NationalCode,ORCIDcode)\
            values('{fn}','{ln}','{nc}','{od}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Author was Added Successfully')
        msg.setWindowTitle('Books Author')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeineEdit.setText('')
        self.ORCIDLineEdit.setText('')
        cur.close()
####################
#//////////////////#
class main_form(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_form,self).__init__()
        uic.loadUi('Main_form.ui',self)
        self.actoinAddBooks.triggered.connect(self.show_add_books)
        self.actionAdd_Books_Author.triggered.connect(self.show_add_books_author)
        self.actionAdd_Library_Member.triggered.connect(self.show_Membership)
        self.actionAdd_Librarian.triggered.connect(self.show_add_librarian)
        self.actionBook_Borrow.triggered.connect(self.show_borrow_books)
        self.actionBooksDelete.triggered.connect(self.show_delete_books)
        self.actionList_All_Books.triggered.connect(self.show_all_books)
        self.actionList_All_Authors.triggered.connect(self.show_all_author)
        self.actionList_All_Members.triggered.connect(self.show_all_member)
        self.actionList_All_Librarians.triggered.connect(self.show_all_librarian)
        self.actionEdit_Books.triggered.connect(self.show_edit_books)

    def show_edit_books(self):
        self.edit = edit_books()
        self.edit.setModal(True)
        self.edit.show()
        self.actionExit.triggered.connect(self.close)

    def show_all_librarian(self):
        self.librarian = all_librarians()
        self.librarian.setModal(True)
        self.librarian.show()
        self.actionExit.triggered.connect(self.close)
    def show_all_member(self):
        self.member = all_members()
        self.member.setModal(True)
        self.member.show()


    def show_all_author(self):
        self.author = all_authors()
        self.author.setModal(True)
        self.author.show()


    def show_all_books(self):
        self.all = all_books()
        self.all.setModal(True)
        self.all.show()


    def show_delete_books(self):
        self.db = delete_books()
        self.db.setModal(True)
        self.db.show()


    def show_borrow_books(self):
        self.bb = borrow_books()
        self.bb.setModal(True)
        self.bb.show()


    def show_Membership(self):
        self.mp = Membership()
        self.mp.setModal(True)
        self.mp.show()

    def show_add_librarian(self):
        self.an = add_librarian()
        self.an.setModal(True)
        self.an.show()

    def show_add_books_author(self):
        self.Au = add_books_author()
        self.Au.setModal(True)
        self.Au.show()


    def show_add_books(self):
        print('Add Books clicked')
        self.A =add_books()
        self.A.setModal(True)
        self.A.show()
####################
#//////////////////#
class add_books(QtWidgets.QDialog):
    def __init__(self):
        super(add_books,self).__init__()
        uic.loadUi('add_books.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.SavePushButton.clicked.connect(self.insert_records)


    def insert_records(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        ti = self.TitleLineEdit.text()
        au = self.PublisherLineEdit.text()
        ed = self.EditionLineEdit.text()
        bt = self.BookTypeLineEdit.text()
        Isb= self.ISBNLineEdit.text()
        pr = self.PriceLineEdit.text()
        py = self.PublicationYearLineEdit.text()
        Iy = self.InventoryLineEdit.text()
        bd = self.BookIDLineEdit.text()
        ss = self.statusLineEdit.text()
        cur.execute(f"insert into TBooks (Title,Publisher,Edition,BookType,ISBN,Price,PublicationYear,Inventory,BookID,Status)\
            values('{ti}','{au}','{ed}','{bt}','{Isb}','{pr}','{py}','{Iy}','{bd}','{ss}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Book was Added Successfully')
        msg.setWindowTitle('Add Books')
        msg.exec()
        self.TitleLineEdit.setText('')
        self.PublisherLineEdit.setText('')
        self.EditionLineEdit.setText('')
        self.BookTypeLineEdit.setText('')
        self.ISBNLineEdit.setText('')
        self.PriceLineEdit.setText('')
        self.PublicationYearLineEdit.setText('')
        self.InventoryLineEdit.setText('')
        self.BookIDLineEdit.setText('')
        self.statusLineEdit.setText('')
        cur.close()
#==================#
app =QApplication([])
w = widget()
w.show()
app.exec()