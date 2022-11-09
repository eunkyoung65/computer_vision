# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 900)
        palette = QPalette()
        brush = QBrush(QColor(37, 13, 66, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(46, 55, 48, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(78, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush4)
        brush5 = QBrush(QColor(255, 247, 248, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        brush6 = QBrush(QColor(120, 120, 120, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        MainWindow.setPalette(palette)
        
        self.help_action = QAction("도움창 보기", MainWindow,)
        self.help_action.setObjectName(u"도움창 보기")
        self.plus_image = QAction(MainWindow)
        self.plus_image.setObjectName(u"이미지 더하기")
        self.out_action = QAction(MainWindow)
        self.out_action.setObjectName(u"나가기")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.func_list = QComboBox(self.centralwidget)
        self.func_list.addItem("")
        self.func_list.addItem("")
        self.func_list.addItem("")
        self.func_list.addItem("")
        self.func_list.setObjectName(u"func_list")

        self.gridLayout.addWidget(self.func_list, 7, 1, 1, 1)

        self.Load_botton = QPushButton(self.centralwidget)
        self.Load_botton.setObjectName(u"Load_botton")
        palette1 = QPalette()
        brush7 = QBrush(QColor(170, 170, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        self.Load_botton.setPalette(palette1)
        icon = QIcon("C:\photoshop\folder.png")
        icon.addFile(u"C:\photoshop\folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Load_botton.setIcon(icon)
        self.Load_botton.setAutoDefault(False)

        self.gridLayout.addWidget(self.Load_botton, 6, 1, 1, 1)
        
        ## label 위치 (총 3개 , label, pluslabel_2, label_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label") #label

        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        
        self.pluslabel_2 = QLabel(self.centralwidget)
        self.pluslabel_2.setObjectName(u"pluslabel_2")
        palette2 = QPalette()
        brush8 = QBrush(QColor(224, 217, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        self.pluslabel_2.setPalette(palette2) #pluslabel_2

        self.gridLayout.addWidget(self.pluslabel_2, 11, 0, 1, 1)
        #pluslable_2

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3") #label_3

        self.gridLayout.addWidget(self.label_3, 11, 1, 1, 1)
        #label_3

        self.Save_button = QPushButton(self.centralwidget)
        self.Save_button.setObjectName(u"Save_button") #SaveButton
        palette3 = QPalette()
        brush9 = QBrush(QColor(240, 239, 240, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush9)
        brush10 = QBrush(QColor(126, 255, 247, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        self.Save_button.setPalette(palette3)
        icon1 = QIcon()
        icon1.addFile(u"C:\photoshop\arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save_button.setIcon(icon1)

        self.gridLayout.addWidget(self.Save_button, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1462, 38))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setCursor(QCursor(Qt.WhatsThisCursor))
        self.menu_O = QMenu(self.menubar)
        self.menu_O.setObjectName(u"menu_O")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_O.menuAction())
        self.menu.addAction(self.plus_image)
        self.menu_2.addAction(self.help_action)
        self.menu_O.addAction(self.out_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.help_action.setText(QCoreApplication.translate("MainWindow", u"\ubcf4\uae30(L)", None))
#if QT_CONFIG(tooltip)
        self.help_action.setToolTip(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0 \ubcf4\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.plus_image.setText(QCoreApplication.translate("MainWindow", u"\ub354\ud560 \uc774\ubbf8\uc9c0 \ubd88\ub7ec\uc624\uae30(A)", None))
        self.out_action.setText(QCoreApplication.translate("MainWindow", u"\ub098\uac00\uae30(T)", None))
        self.func_list.setItemText(0, QCoreApplication.translate("MainWindow", u"\uae30\ub2a5\uc744 \uc120\ud0dd\ud574\uc8fc\uc138\uc694.", None))
        self.func_list.setItemText(1, QCoreApplication.translate("MainWindow", u"Flip_image", None))
        self.func_list.setItemText(2, QCoreApplication.translate("MainWindow", u"Polar_image", None))
        self.func_list.setItemText(3, QCoreApplication.translate("MainWindow", u"Mozaic_image", None))

#if QT_CONFIG(tooltip)
        self.Load_botton.setToolTip(QCoreApplication.translate("MainWindow", u"\uc0ac\uc9c4 \ubd88\ub7ec\uc624\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.Load_botton.setText(QCoreApplication.translate("MainWindow", u"Load_image", None))
        self.pluslabel_2.setText(QCoreApplication.translate("MainWindow", u"\ub354\ud560 \uc774\ubbf8\uc9c0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Image1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uacfc \uc774\ubbf8\uc9c0", None))
        self.Save_button.setText(QCoreApplication.translate("MainWindow", u"Save_image", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ub354\ud560 \uc774\ubbf8\uc9c0 \ubd88\ub7ec\uc624\uae30(A)", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0(H)", None))
        self.menu_O.setTitle(QCoreApplication.translate("MainWindow", u"\ub098\uac00\uae30(O)", None))
    # retranslateUi

