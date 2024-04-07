# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIReader.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/reader.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.last = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/last.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.last.setIcon(icon1)
        self.last.setObjectName("last")
        self.horizontalLayout.addWidget(self.last, 0, QtCore.Qt.AlignLeft)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon2)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/catlogs.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(0, icon3)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        self.files = QtWidgets.QMenu(self.menubar)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/files.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.files.setIcon(icon4)
        self.files.setObjectName("files")
        self.lastfile = QtWidgets.QMenu(self.files)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/file_last.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastfile.setIcon(icon5)
        self.lastfile.setObjectName("lastfile")
        self.setting = QtWidgets.QMenu(self.menubar)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/setting.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon6)
        self.setting.setObjectName("setting")
        self.fontcolor = QtWidgets.QMenu(self.setting)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/fontcolor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fontcolor.setIcon(icon7)
        self.fontcolor.setObjectName("fontcolor")
        self.bg = QtWidgets.QMenu(self.setting)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/bg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bg.setIcon(icon8)
        self.bg.setObjectName("bg")
        self.exit = QtWidgets.QMenu(self.menubar)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon9)
        self.exit.setObjectName("exit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionfile = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfile.setIcon(icon10)
        self.actionfile.setObjectName("actionfile")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.actionfont = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/font.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfont.setIcon(icon11)
        self.actionfont.setObjectName("actionfont")
        self.actioncolor = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/color.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncolor.setIcon(icon12)
        self.actioncolor.setObjectName("actioncolor")
        self.actionimport = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/import.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionimport.setIcon(icon13)
        self.actionimport.setObjectName("actionimport")
        self.actionclose = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icon/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionclose.setIcon(icon14)
        self.actionclose.setObjectName("actionclose")
        self.actiondefault = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icon/default.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondefault.setIcon(icon15)
        self.actiondefault.setObjectName("actiondefault")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setIcon(icon9)
        self.actionexit.setObjectName("actionexit")
        self.catlog = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icon/catlog.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.catlog.setIcon(icon16)
        self.catlog.setObjectName("catlog")
        self.files.addAction(self.actionfile)
        self.files.addAction(self.lastfile.menuAction())
        self.fontcolor.addAction(self.actionfont)
        self.fontcolor.addAction(self.actioncolor)
        self.bg.addAction(self.actionimport)
        self.bg.addAction(self.actionclose)
        self.setting.addAction(self.fontcolor.menuAction())
        self.setting.addAction(self.bg.menuAction())
        self.setting.addAction(self.actiondefault)
        self.exit.addAction(self.actionexit)
        self.menubar.addAction(self.files.menuAction())
        self.menubar.addAction(self.setting.menuAction())
        self.menubar.addAction(self.exit.menuAction())
        self.toolBar.addAction(self.catlog)

        self.retranslateUi(MainWindow)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "博文智见"))
        MainWindow.setStatusTip(_translate("MainWindow", "TXT阅读器"))
        self.last.setToolTip(_translate("MainWindow", "上一篇"))
        self.last.setStatusTip(_translate("MainWindow", "上一篇"))
        self.last.setText(_translate("MainWindow", "上一篇"))
        self.next.setToolTip(_translate("MainWindow", "下一篇"))
        self.next.setStatusTip(_translate("MainWindow", "下一篇"))
        self.next.setText(_translate("MainWindow", "下一篇"))
        self.treeWidget.setToolTip(_translate("MainWindow", "内容概括"))
        self.treeWidget.setStatusTip(_translate("MainWindow", "内容导读"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "内容导读"))
        self.files.setStatusTip(_translate("MainWindow", "文件"))
        self.files.setTitle(_translate("MainWindow", "文件"))
        self.lastfile.setToolTip(_translate("MainWindow", "打开最近的文件"))
        self.lastfile.setStatusTip(_translate("MainWindow", "打开最近的文件"))
        self.lastfile.setTitle(_translate("MainWindow", "打开最近的文件"))
        self.setting.setToolTip(_translate("MainWindow", "设置"))
        self.setting.setStatusTip(_translate("MainWindow", "设置"))
        self.setting.setTitle(_translate("MainWindow", "设置"))
        self.fontcolor.setTitle(_translate("MainWindow", "字体和颜色"))
        self.bg.setTitle(_translate("MainWindow", "背景图片"))
        self.exit.setToolTip(_translate("MainWindow", "关闭应用"))
        self.exit.setStatusTip(_translate("MainWindow", "关闭应用"))
        self.exit.setTitle(_translate("MainWindow", "退出"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "工具栏"))
        self.actionfile.setText(_translate("MainWindow", "获取推送"))
        self.actionfile.setStatusTip(_translate("MainWindow", "获取推送"))
        self.actionfile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.actionfont.setText(_translate("MainWindow", "选择字体"))
        self.actionfont.setStatusTip(_translate("MainWindow", "选择字体"))
        self.actioncolor.setText(_translate("MainWindow", "选择背景颜色"))
        self.actioncolor.setStatusTip(_translate("MainWindow", "选择背景颜色"))
        self.actionimport.setText(_translate("MainWindow", "导入背景图片"))
        self.actionimport.setStatusTip(_translate("MainWindow", "导入背景图片"))
        self.actionclose.setText(_translate("MainWindow", "关闭背景图片"))
        self.actionclose.setStatusTip(_translate("MainWindow", "关闭背景图片"))
        self.actiondefault.setText(_translate("MainWindow", "恢复默认设置"))
        self.actiondefault.setStatusTip(_translate("MainWindow", "恢复默认设置"))
        self.actionexit.setText(_translate("MainWindow", "退出应用"))
        self.actionexit.setStatusTip(_translate("MainWindow", "退出应用"))
        self.actionexit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.catlog.setText(_translate("MainWindow", "概括"))
        self.catlog.setToolTip(_translate("MainWindow", "获取到的所有文章的主要内容概括"))
#import resource_rc