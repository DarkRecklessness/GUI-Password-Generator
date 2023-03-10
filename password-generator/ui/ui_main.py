# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 540)
        icon = QIcon()
        icon.addFile(u":/icons/icons/outline_key_black_24dp.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: #121212;\n"
"	color: white;\n"
"	font-family: Verdana;\n"
"	font-size: 16pt;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid gray;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower, #btn_upper, #btn_special, #btn_digits {\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-color: #090;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 4px solid #090;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #006300;\n"
"	border-color: #090;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setEnabled(False)
        self.icon_lock.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/lock_white_24dp.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.icon_lock.setIcon(icon1)
        self.icon_lock.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.icon_lock)

        self.layout_passwords = QHBoxLayout()
        self.layout_passwords.setObjectName(u"layout_passwords")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy)
        self.frame_password.setStyleSheet(u"QFrame {\n"
"	border: 2px solid gray;\n"
"	border-radius: 5px;\n"
"	margin-right: 0;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border-color: #090;\n"
"}")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	margin: 0;\n"
"	font-size: 20pt;\n"
"}")

        self.horizontalLayout_2.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	margin: 0;\n"
"	backgrond-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/visibility_off_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/visibility_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon2)
        self.btn_visibility.setIconSize(QSize(30, 30))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout_2.addWidget(self.btn_visibility)


        self.layout_passwords.addWidget(self.frame_password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
"	margin-right: 0;\n"
"	margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/refresh_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.layout_passwords.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton {\n"
"	padding: 5px;\n"
"	margin-left: 0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/content_copy_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon4)
        self.btn_copy.setIconSize(QSize(42, 42))

        self.layout_passwords.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.layout_passwords)

        self.layour_info = QHBoxLayout()
        self.layour_info.setObjectName(u"layour_info")
        self.label_strenght = QLabel(self.centralwidget)
        self.label_strenght.setObjectName(u"label_strenght")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_strenght.sizePolicy().hasHeightForWidth())
        self.label_strenght.setSizePolicy(sizePolicy1)
        self.label_strenght.setAlignment(Qt.AlignCenter)

        self.layour_info.addWidget(self.label_strenght)

        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy1.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy1)
        self.label_entropy.setAlignment(Qt.AlignCenter)

        self.layour_info.addWidget(self.label_entropy)


        self.verticalLayout.addLayout(self.layour_info)

        self.layout_lenght = QHBoxLayout()
        self.layout_lenght.setObjectName(u"layout_lenght")
        self.slider_lenght = QSlider(self.centralwidget)
        self.slider_lenght.setObjectName(u"slider_lenght")
        self.slider_lenght.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_lenght.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: transparent;\n"
"	height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background-color: #090;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"	background-color: gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color: white;\n"
"	width: 22px;\n"
"	border-radius: 10px;\n"
"	margin-top: -8px;\n"
"	margin-bottom: -8px;\n"
"}\n"
"")
        self.slider_lenght.setMaximum(100)
        self.slider_lenght.setValue(12)
        self.slider_lenght.setOrientation(Qt.Horizontal)

        self.layout_lenght.addWidget(self.slider_lenght)

        self.spinbox_lenght = QSpinBox(self.centralwidget)
        self.spinbox_lenght.setObjectName(u"spinbox_lenght")
        self.spinbox_lenght.setStyleSheet(u"QSpinBox {\n"
"	border: 2px solid gray;\n"
"	border-radius: 5px;\n"
"	background: transparent;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	border-color: #009900\n"
"} ")
        self.spinbox_lenght.setAlignment(Qt.AlignCenter)
        self.spinbox_lenght.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_lenght.setMaximum(100)
        self.spinbox_lenght.setValue(12)

        self.layout_lenght.addWidget(self.spinbox_lenght)


        self.verticalLayout.addLayout(self.layout_lenght)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_characters.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_special.setCheckable(True)

        self.layout_characters.addWidget(self.btn_special)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.icon_lock.setText("")
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
#if QT_CONFIG(shortcut)
        self.btn_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_copy.setText("")
#if QT_CONFIG(shortcut)
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.label_strenght.setText("")
        self.label_entropy.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"#?$", None))
    # retranslateUi

