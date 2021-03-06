# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import time
import os
# from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QInputDialog,QMainWindow, QPushButton, QApplication, QTextEdit,QFormLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer, Qt
from PyQt5.QtGui import QTextCursor, QIcon
import LIGGGHTSER

class Stream(QObject):
	"""Redirects console output to text widget."""
	newText = pyqtSignal(str)

	def write(self, text):
		self.newText.emit(str(text))


class Ui_MainWindow(object):
	def onUpdateText(self, text):
		"""Write console output to text widget."""
		cursor = self.process.textCursor()
		cursor.movePosition(QTextCursor.End)
		cursor.insertText(text)
		self.process.setTextCursor(cursor)
		self.process.ensureCursorVisible()

	def setupUi(self, MainWindow):
		lgs=LIGGGHTSER.read.Read('wd','0.1.0')
		##########writle mainwindow
		MainWindow.setObjectName("LIGGGHSTER")
		MainWindow.resize(800, 600)
		MainWindow.setWindowTitle('LIGGGHSTER')
		MainWindow.setWindowIcon(QIcon('LIGGGHTSER.ico'))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		##########writle pushButton
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(90, 90, 211, 41))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(lambda:self.read_file(MainWindow,lgs))
		##########writle textedit
		self.process = QTextEdit(MainWindow, readOnly=True)
		self.process.ensureCursorVisible()
		self.process.setLineWrapColumnOrWidth(500)
		self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
		self.process.setGeometry(QtCore.QRect(30, 380, 731, 161))
		self.process.setObjectName("console")
		###########################
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
####################################################################################################
		self.change_wd = QtWidgets.QPushButton(self.centralwidget)
		self.change_wd.setGeometry(QtCore.QRect(90, 30, 211, 41))
		self.change_wd.setObjectName("change_wd")
		self.change_wd.clicked.connect(lambda:self.change_workdir(MainWindow))
####################################################################################################
		self.clear = QtWidgets.QPushButton(self.centralwidget)
		self.clear.setGeometry(QtCore.QRect(90, 160, 211, 41))
		self.clear.setObjectName("clear")
		self.clear.clicked.connect(self.clear_tab)
####################################################################################################
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		sys.stdout = Stream(newText=self.onUpdateText)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		# MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
		self.pushButton.setText(_translate("MainWindow", "Read File"))
		self.change_wd.setText(_translate("MainWindow", "Change work directory"))
		self.clear.setText(_translate("MainWindow", "Clear"))

	def read_file(self,Marinwindow,lgs):
		try:
			filedict=lgs.read_file('./')
		except:
			print('cannot read directory'+os.getcwd())
			return
		title=list()
		for i in filedict:
			title.append(str(i))
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(370, 20, 391, 341))
		self.tabWidget.setObjectName("tabWidget")
		# self.tabWidget.setTabsClosable(True);
		# self.tabWidget.tabCloseRequested.connect(self.close_handler)
		self.tablist = [QtWidgets.QWidget() for i in range(len(filedict))]
		
		for i in range(len(filedict)):
			self.tablist[i].setObjectName(title[i])
			self.tabWidget.addTab(self.tablist[i], title[i])
			self.show_items(filedict,title[i],i)
		self.tabWidget.show()

	def show_items(self,filedict,title,number):
		layout = QGridLayout()
		if len(filedict[title])<9:
			heretable=QTableWidget(9,2)
		else:
			heretable=QTableWidget(len(filedict[title]),2)
		heretable.setHorizontalHeaderLabels(['FileName','size/KB'])
		heretable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		heretable.setColumnWidth(0,220)
		heretable.setColumnWidth(1,132)
		for i in range(len(filedict[title])):
			newitem = QTableWidgetItem(filedict[title][i])
			heretable.setItem(i,0,newitem)
			fsize = os.path.getsize(filedict[title][i])
			newitem2 = QTableWidgetItem(str(round(fsize/1024,4)))
			heretable.setItem(i,1,newitem2)
			newitem2.setTextAlignment(Qt.AlignRight)
		layout.addWidget(heretable,0,0)

		self.tablist[number].setLayout(layout)
		# print(self.tabWidget.geometry())


	def change_workdir(self,Marinwindow):
		dirname = QFileDialog.getExistingDirectory(MainWindow,'open','./')
		if dirname:
			try:
				os.chdir(dirname)
			except:
				print('error:cannot change to this directory'+dirname)

	def clear_tab(self,index):
		try:
			for i in self.tablist:
				self.tabWidget.removeTab(index)
		except:
			print('Delete table fail')

	def close_handler(self, index):
		print ('close_handler called, index = '+str(index))
		self.tabWidget.removeTab(index)

class mainwin(QtWidgets.QMainWindow):
	def closeEvent(self, event):
	#Shuts down application on close.
	# Return stdout to defaults.
		reply = QMessageBox.question(MainWindow, 'WARNING', 'Do you want to exit', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		reply.setIcon(QMessageBox,Warning)
		if reply == QMessageBox.Yes:
			sys.stdout = sys.__stdout__
			super().closeEvent(event)
			event.accept()		
		else:
			event.ignore()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = mainwin()
	# MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	# ui.show()
	# ui.mainw()
	sys.exit(app.exec_())
