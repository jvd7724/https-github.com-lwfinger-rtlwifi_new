#Book Worm SoftWare was created by Farshid Javadi on 17/10/99
# as a project in the DataBase lesson
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
###################
######Clock########
class clock(QtWidgets.QDialog):
    def __init__(self):
        super(clock,self).__init__()
        uic.loadUi('Clock.ui',self)
###################
###EditLibrarianS###
class edit_librarian(QtWidgets.QDialog):
    def __init__(self):
        super(edit_librarian,self).__init__()
        uic.loadUi('EditLibrarian.ui',self)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        self.SavePushButton.clicked.connect(self.edit_librarian)
        self.ExitPushButton.clicked.connect(self.close)
        self.list_all_librarian.setColumnWidth(0, 200)
        self.list_all_librarian.setColumnWidth(1, 200)
        self.list_all_librarian.setColumnWidth(2, 200)
        self.list_all_librarian.setColumnWidth(3, 200)
        self.list_all_librarian.setColumnWidth(4, 200)
        librarian = cur.execute(f"select  * from TLibrarian")
        self.list_all_librarian.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_librarian.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_librarian.setItem(row, column, QTableWidgetItem(str(item)))
        cur.close
    def edit_librarian(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeLineEdit.text()
        pc = self.PersonnelCodeLineEdit.text()
        ed = self.EntryDateLineEdit.text()
        ID = self.LibrarianIDLineEdit.text()
        cur.execute(f"update  TLibrarian set FirstName='{fn}',LastName='{ln}',NationalCode='{nc}'\
            ,PersonnelCode='{pc}',EntryDate='{ed}'where ID ='{ID}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Librarian was updated Successfully')
        msg.setWindowTitle('Update Librarian')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeLineEdit.setText('')
        self.PersonnelCodeLineEdit.setText('')
        self.EntryDateLineEdit.setText('')
        ID = self.LibrarianIDLineEdit.setText('')
        cur.close
###################
####EditMembers####
class edit_members(QtWidgets.QDialog):
    def __init__(self):
        super(edit_members,self).__init__()
        uic.loadUi('edit_members.ui',self)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        self.list_all_member.setColumnWidth(0,400)
        self.list_all_member.setColumnWidth(1,200)
        self.list_all_member.setColumnWidth(2,200)
        self.list_all_member.setColumnWidth(3,200)
        self.list_all_member.setColumnWidth(4,200)
        self.list_all_member.setColumnWidth(5,200)
        self.list_all_member.setColumnWidth(6,200)
        self.list_all_member.setColumnWidth(7,200)
        self.list_all_member.setColumnWidth(8,200)
        self.list_all_member.setColumnWidth(9,200)
        self.list_all_member.setColumnWidth(10,100)
        self.list_all_member.setColumnWidth(11,100)
        book = cur.execute(f"select  * from TMembership")
        self.list_all_member.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_member.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_member.setItem(row, column, QTableWidgetItem(str(item)))
        cur.close
        self.ExitPushButton.clicked.connect(self.close)
        self.SavePushButton.clicked.connect(self.edit_member)
        # self.refreshPushButton.clicked.connect(self.refresh_table)
    # def refresh_table(self):
    def edit_member(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeLineEdit.text()
        ri = self.RegisteryDateLineEdit.text()
        ex = self.ExpirityDateLineEdit.text()
        Mt = self.MembershipTypeLineEdit.text()
        ct = self.CityLineEdit.text()
        st = self.StreetLineEdit.text()
        pc = self.PostalCodeLineEdit.text()
        MI = self.MemberIDLineEdit.text()
        ss = self.StatusLineEdit.text()

        cur.execute(f"update TMembership set FirstName ='{fn}',LastName ='{ln}' ,NationalCode ='{nc}'\
            ,RegisteryDate ='{ri}'\
            ,ExpirityDate='{ex}',MembershipType='{Mt}',City='{ct}',Street='{st}',PostalCode='{pc}'\
            ,Status='{ss}' where MemberID ='{MI}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('Information of this member was Update Successfully')
        msg.setWindowTitle('Edit Member')
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
        self.MemberIDLineEdit.setText('')
        self.StatusLineEdit.setText('')
        cur.close()
###################
####EditAuthor#####
class edit_authors(QtWidgets.QDialog):
    def __init__(self):
        super(edit_authors,self).__init__()
        uic.loadUi('edit_author.ui',self)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        self.list_all_author.setColumnWidth(0,400)
        self.list_all_author.setColumnWidth(1,200)
        self.list_all_author.setColumnWidth(2,200)
        self.list_all_author.setColumnWidth(3,200)
        self.list_all_author.setColumnWidth(4,200)
        book = cur.execute(f"select  * from TAuthor")
        self.list_all_author.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_author.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_author.setItem(row, column, QTableWidgetItem(str(item)))
        cur.close
        self.ExitPushButton.clicked.connect(self.close)
        self.SavePushButton.clicked.connect(self.edit_author)
        # self.refreshPushButton.clicked.connect(self.refresh_table)
    # def refresh_table(self):
    def edit_author(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeLineEdit.text()
        OC = self.ORCIDcodeLineEdit.text()
        MI = self.MemberIDLineEdit.text()
        cur.execute(f"update TAuthor  set FNAuthor ='{fn}',LNAuthor ='{ln}' ,NationalCode ='{nc}' ,ORCIDcode ='{OC}' where MemberID ='{MI}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('Information of this author was Update Successfully')
        msg.setWindowTitle('Edit Author')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeLineEdit.setText('')
        self.ORCIDcodeLineEdit.setText('')
        self.MemberIDLineEdit.setText('')
        cur.close()
###################
#####EditBooks#####
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
###AllLibrarians###
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
        self.list_all_librarian.setColumnWidth(5,200)
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
####AllMember######
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
#####AllAuthors####
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
#####AllAuthors#####
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
######Login########
class login(QtWidgets.QWidget):
    def __init__(self):
        super(login,self).__init__()
        uic.loadUi('UserPass.ui',self)
        self.LoginPushButton.clicked.connect(self.Handel_Login)
        self.ExitPushButton.clicked.connect(self.close)
    def Handel_Login(self):
        userName =self.UserNameLineEdit.text()
        password = self.PasswordLineEdit.text()
        if userName == '' and password == '':
            print('user match')
            self.window2 = main_form()
            self.close()
            self.window2.show()
        else:
            self.Textlabel.setText('Username or password is incorrect...')
            self.UserNameLineEdit.setText('')
            self.PasswordLineEdit.setText('')
####################
######AllBooks######
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
##DeleteLibrarians##
class delete_librarian(QtWidgets.QDialog):
    def __init__(self):
        super(delete_librarian,self).__init__()
        uic.loadUi('DeleteLibrarian.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.DeletePushButton.clicked.connect(self.delete_librarians)
        self.ExitPushButton.clicked.connect(self.close)
        self.list_all_Librarian.setColumnWidth(0,300)
        self.list_all_Librarian.setColumnWidth(1,400)
        self.list_all_Librarian.setColumnWidth(2,200)
        self.list_all_Librarian.setColumnWidth(3,200)
        self.list_all_Librarian.setColumnWidth(4,200)
        self.list_all_Librarian.setColumnWidth(5,200)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        delete = cur.execute(f"select  * from TLibrarian")
        self.list_all_Librarian.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_Librarian.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_Librarian.setItem(row,column, QTableWidgetItem(str(item)))
        cur.close
    def delete_librarians(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        LI = self.LibrarianIDLineEdit.text()
        deleteBooks = cur.execute(f"delete from TLibrarian  where LibrarianID ='{LI}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('This Librarian was Delete Successfully')
        msg.setWindowTitle('Delete Librarian')
        msg.exec()
        self.LibrarianIDLineEdit.setText('')
        cur.close
####################
####DeleteMembers####
class delete_member(QtWidgets.QDialog):
    def __init__(self):
        super(delete_member,self).__init__()
        uic.loadUi('DeleteMember.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.DeletePushButton.clicked.connect(self.delete_member)
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
        delete = cur.execute(f"select  * from TMembership")
        self.list_all_member.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_member.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_member.setItem(row,column, QTableWidgetItem(str(item)))
        cur.close
    def delete_member(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        MI = self.MemberIDLineEdit.text()
        deleteBooks = cur.execute(f"delete from TMembership  where MemberID ='{MI}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('This Member was Delete Successfully')
        msg.setWindowTitle('Delete Members')
        msg.exec()
        self.MemberIDLineEdit.setText('')
        cur.close
####################
####DeleteAuthor####
class delete_author(QtWidgets.QDialog):
    def __init__(self):
        super(delete_author,self).__init__()
        uic.loadUi('DeleteAuthor.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.DeletePushButton.clicked.connect(self.delete_authors)
        self.list_all_author.setColumnWidth(0,400)
        self.list_all_author.setColumnWidth(1,200)
        self.list_all_author.setColumnWidth(2,200)
        self.list_all_author.setColumnWidth(3,200)
        self.list_all_author.setColumnWidth(4,200)
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        delete = cur.execute(f"select  * from TAuthor")
        self.list_all_author.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_author.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_author.setItem(row,column, QTableWidgetItem(str(item)))
        cur.close
    def delete_authors(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        AI = self.BookIDLineEdit.text()
        deleteBooks = cur.execute(f"delete from TAuthor  where AuthorID ='{AI}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('this Author was Delete Successfully')
        msg.setWindowTitle('Delete Authors')
        msg.exec()
        self.BookIDLineEdit.setText('')
        cur.close
####################
####DeleteBooks#####
class delete_books(QtWidgets.QDialog):
    def __init__(self):
        super(delete_books,self).__init__()
        uic.loadUi('DeleteBooks.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.DeletePushButton.clicked.connect(self.delete_books)
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
        delete = cur.execute(f"select  * from TBooks")
        self.list_all_book.setRowCount(0)
        for row, form in enumerate(cur):
            self.list_all_book.insertRow(row)
            for column, item in enumerate(form):
                self.list_all_book.setItem(row,column, QTableWidgetItem(str(item)))
        cur.close
    def delete_books(self):
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        bi = self.BookIDLineEdit.text()
        deleteBooks = cur.execute(f"delete from TBooks  where BookID ='{bi}'")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('this Book was Delete Successfully')
        msg.setWindowTitle('Delete Books')
        msg.exec()
        self.BookIDLineEdit.setText('')
        cur.close
####################
#####BorrowBooks####
class borrow_books(QtWidgets.QDialog):
    def __init__(self):
        super(borrow_books,self).__init__()
        uic.loadUi('borrow.ui',self)
        # self.BookIDLineEdit.textChanged.connect(self.filter_bd)
        # self.ISBNLineEdit.textChanged.connect(self.filter_IN)
        # self.MemberIDLineEdit.textChanged.connect(self.filter_MSh)
        self.BorrowPushButton.clicked.connect(self.Borrow)
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
        Member = cur.execute(f"select MemberID,LastName,NationalCode,RegisteryDate,\
            ExpirityDate,MembershipType,Status from TMembership")
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
        sqlite_connection = sqlite3.connect("BWSoftDB.db")
        cur = sqlite_connection.cursor()
        Book = cur.execute(f"select * from TBorrowBooks")
        self.BorrowListTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.BorrowListTable.setColumnWidth(0,100)
        self.BorrowListTable.setColumnWidth(1,200)
        self.BorrowListTable.setColumnWidth(2,200)
        self.BorrowListTable.setColumnWidth(3,110)
        self.BorrowListTable.setRowCount(0)
        for row, form in enumerate(cur):
            self.BorrowListTable.insertRow(row)
            for column, item in enumerate(form):
                self.BorrowListTable.setItem(row, column, QTableWidgetItem(str(item)))
    # def filter_bd (self):
    #     sqlite_connection = sqlite3.connect("BWSoftDB.db")
    #     cur = sqlite_connection.cursor()
    #     Book = cur.execute(f"select BookID,Title,ISBN,Inventory,Edition,Status \
    #         from TBooks  where BookID = {self.BookIDLineEdit.text()}")
    #     self.ListTable.setRowCount(0)
    #     for row, form in enumerate(cur):
    #         self.ListTable.insertRow(row)
    #         for column, item in enumerate(form):
    #             self.ListTable.setItem(row, column,QTableWidgetItem(str(item)))
    #     cur.close
    # def filter_IN (self):
    #     sqlite_connection = sqlite3.connect("BWSoftDB.db")
    #     cur = sqlite_connection.cursor()
    #     Book = cur.execute(f"select BookID,Title,ISBN,Inventory,Edition,Status\
    #         from TBooks where ISBN = {self.ISBNLineEdit.text()}")
    #     self.ListTable.setRowCount(0)
    #     for row, form in enumerate(cur):
    #         self.ListTable.insertRow(row)
    #         for column, item in enumerate(form):
    #             self.ListTable.setItem(row, column,QTableWidgetItem(str(item)))
    #     cur.close
    # def filter_MSh (self):
    #     sqlite_connection = sqlite3.connect("BWSoftDB.db")
    #     cur = sqlite_connection.cursor()
    #     cur = sqlite_connection.cursor()
    #     member = cur.execute(f"select MemberID,LastName,NationalCode,RegisteryDate,\
    #         ExpirityDate,MembershipType,Status from TMembership \
    #         where MemberID = {self.MemberIDLineEdit.text()}")
    #     self.TableWidget.setRowCount(0)
    #     for row, form in enumerate(cur):
    #         self.TableWidget.insertRow(row)
    #         for column, item in enumerate(form):
    #             self.TableWidget.setItem(row, column,QTableWidgetItem(str(item)))
    #     cur.close
    def Borrow(self):
            sqlite_connection = sqlite3.connect("BWSoftDB.db")
            cur = sqlite_connection.cursor()
            BI = self.BookIDLineEdit.text()
            NC = self.NatioNAaCodeLineEdit.text()
            MI = self.MemberIDLineEdit.text()
            SS = self.BookStatusLineEdit.text()
            Borrow = cur.execute(f"insert into TBorrowBooks (BookID,NationalCode,MembershipID,Status)\
                 values('{BI}','{NC}','{MI}','{SS}')")
            sqlite_connection.commit()
            # Borrow = cur.execute(f"select count(*) from TBorrowBooks where BookID = 1 and Status = 1")
            msg = QMessageBox(self)
            msg.setText('This Book Borrowed')
            msg.setWindowTitle('BorrowBook')
            msg.exec()
            cur.close()
####################
#####AddMember######
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
        LI = self.LibrarianIDLineEdit.text()
        cur.execute(f"insert into TLibrarian (FirstName,LastName,NationalCode,PersonnelCode,EntryDate,ID)\
            values('{fn}','{ln}','{nc}','{pc}','{ed}','{LI}')")
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
        self.LibrarianIDLineEdit.setText('')
        cur.close
####################
#####AddMember######
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
        mi = self.MemberIDLineEdit.text()
        ss = self.StatusLineEdit.text()
        cur.execute(f"insert into TMembership (FirstName,LastName,NationalCode,RegisteryDate,ExpirityDate,MembershipType,City,Street,PostalCode,MemberID,Status)\
            values('{fn}','{ln}','{nc}','{ry}','{ed}','{mp}','{cy}','{st}','{pc}','{mi}','{ss}')")
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
        self.MemberIDLineEdit.setText('')
        self.StatusLineEdit.setText('')
        cur.close
####################
###AddBooksAuthor###
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
######MainForm######
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
        self.actionEdit_Books_Author.triggered.connect(self.show_edit_author)
        self.actionEdit_Library_Member.triggered.connect(self.show_edit_member)
        self.actionEdit_Librarian.triggered.connect(self.show_edit_librarian)
        self.actionAuthorDelete.triggered.connect(self.show_author_delete)
        self.actionMemberDelete.triggered.connect(self.show_member_delete)
        self.actionLibrarianDelete.triggered.connect(self.show_librarian_delete)
        self.actionClock.triggered.connect(self.show_clock)
        self.actionExit.triggered.connect(self.close)
    def show_clock(self):
        self.ck = clock()
        self.ck.setModal(True)
        self.ck.show()
    def show_edit_librarian(self):
        self.ketabdar = edit_librarian()
        self.ketabdar.setModal(True)
        self.ketabdar.show()
    def show_edit_member(self):
        self.member = edit_members()
        self.member.setModal(True)
        self.member.show()
    def show_edit_author(self):
        self.auedit = edit_authors()
        self.auedit.setModal(True)
        self.auedit.show()
    def show_edit_books(self):
        self.edit = edit_books()
        self.edit.setModal(True)
        self.edit.show()
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
    def show_librarian_delete(self):
        self.lib = delete_librarian()
        self.lib.setModal(True)
        self.lib.show()
    def show_member_delete(self):
        self.mem = delete_member()
        self.mem.setModal(True)
        self.mem.show()
    def show_author_delete(self):
        self.Au = delete_author()
        self.Au.setModal(True)
        self.Au.show()
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
#####AddBooks#######
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
        oc = self.OrcidCodeLineEdit.text()
        ss = self.statusLineEdit.text()
        cur.execute(f"insert into TBooks (Title,Publisher,Edition,BookType,ISBN,Price,PublicationYear,Inventory,BookID,ORCIDcode,Status)\
            values('{ti}','{au}','{ed}','{bt}','{Isb}','{pr}','{py}','{Iy}','{bd}','{oc}','{ss}')")
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
        self.OrcidCodeLineEdit.setText('')
        self.statusLineEdit.setText('')
        cur.close()
#==================#
app =QApplication([])
w = login()
w.show()
app.exec()