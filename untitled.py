# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Export_spare_parts(object):
    def setupUi(self, Export_spare_parts):
        Export_spare_parts.setObjectName("Export_spare_parts")
        Export_spare_parts.resize(1271, 337)
        self.groupBox = QtWidgets.QGroupBox(Export_spare_parts)
        self.groupBox.setGeometry(QtCore.QRect(470, 140, 171, 191))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_current = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_current.setEnabled(True)
        self.radioButton_current.setGeometry(QtCore.QRect(10, 30, 111, 18))
        self.radioButton_current.setChecked(True)
        self.radioButton_current.setObjectName("radioButton_current")
        self.radioButton_vw = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_vw.setGeometry(QtCore.QRect(10, 50, 82, 18))
        self.radioButton_vw.setObjectName("radioButton_vw")
        self.radioButton_dil = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_dil.setGeometry(QtCore.QRect(10, 70, 82, 18))
        self.radioButton_dil.setObjectName("radioButton_dil")
        self.radioButton_sk = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_sk.setGeometry(QtCore.QRect(10, 90, 82, 18))
        self.radioButton_sk.setObjectName("radioButton_sk")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 130, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton_nzp = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_nzp.setGeometry(QtCore.QRect(10, 110, 82, 18))
        self.radioButton_nzp.setObjectName("radioButton_nzp")
        self.del_from_iprr = QtWidgets.QPushButton(self.groupBox)
        self.del_from_iprr.setGeometry(QtCore.QRect(10, 160, 131, 23))
        self.del_from_iprr.setObjectName("del_from_iprr")
        self.groupBox_2 = QtWidgets.QGroupBox(Export_spare_parts)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 461, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(280, 50, 151, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_itemno = QtWidgets.QLabel(self.groupBox_2)
        self.label_itemno.setGeometry(QtCore.QRect(10, 280, 401, 16))
        self.label_itemno.setText("")
        self.label_itemno.setObjectName("label_itemno")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(310, 150, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 431, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.groupBox_2)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 190, 401, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.label_5.setObjectName("label_5")
        self.print_res = QtWidgets.QLabel(self.groupBox_2)
        self.print_res.setGeometry(QtCore.QRect(10, 260, 381, 16))
        self.print_res.setText("")
        self.print_res.setObjectName("print_res")
        self.provider_check = QtWidgets.QCheckBox(self.groupBox_2)
        self.provider_check.setGeometry(QtCore.QRect(190, 40, 81, 18))
        self.provider_check.setObjectName("provider_check")
        self.later = QtWidgets.QLineEdit(self.groupBox_2)
        self.later.setGeometry(QtCore.QRect(140, 160, 113, 20))
        self.later.setObjectName("later")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_2.setObjectName("label_2")
        self.open_excel_button = QtWidgets.QPushButton(self.groupBox_2)
        self.open_excel_button.setGeometry(QtCore.QRect(304, 10, 111, 23))
        self.open_excel_button.setObjectName("open_excel_button")
        self.name_ = QtWidgets.QLineEdit(self.groupBox_2)
        self.name_.setGeometry(QtCore.QRect(140, 60, 41, 16))
        self.name_.setObjectName("name_")
        self.enter_price = QtWidgets.QLineEdit(self.groupBox_2)
        self.enter_price.setGeometry(QtCore.QRect(140, 120, 41, 16))
        self.enter_price.setObjectName("enter_price")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label_13.setObjectName("label_13")
        self.provider_ = QtWidgets.QLineEdit(self.groupBox_2)
        self.provider_.setGeometry(QtCore.QRect(140, 40, 41, 16))
        self.provider_.setObjectName("provider_")
        self.group_ = QtWidgets.QLineEdit(self.groupBox_2)
        self.group_.setGeometry(QtCore.QRect(140, 80, 41, 16))
        self.group_.setObjectName("group_")
        self.discount_ = QtWidgets.QLineEdit(self.groupBox_2)
        self.discount_.setGeometry(QtCore.QRect(140, 100, 41, 16))
        self.discount_.setObjectName("discount_")
        self.retail_ = QtWidgets.QLineEdit(self.groupBox_2)
        self.retail_.setGeometry(QtCore.QRect(140, 140, 41, 16))
        self.retail_.setObjectName("retail_")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.group_check = QtWidgets.QCheckBox(self.groupBox_2)
        self.group_check.setGeometry(QtCore.QRect(190, 80, 91, 18))
        self.group_check.setObjectName("group_check")
        self.code_ = QtWidgets.QLineEdit(self.groupBox_2)
        self.code_.setGeometry(QtCore.QRect(140, 20, 41, 16))
        self.code_.setObjectName("code_")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_4.setObjectName("label_4")
        self.disccount_check = QtWidgets.QCheckBox(self.groupBox_2)
        self.disccount_check.setGeometry(QtCore.QRect(190, 100, 81, 18))
        self.disccount_check.setObjectName("disccount_check")
        self.groupBox_3 = QtWidgets.QGroupBox(Export_spare_parts)
        self.groupBox_3.setGeometry(QtCore.QRect(470, 10, 731, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.retail_3 = QtWidgets.QLabel(self.groupBox_3)
        self.retail_3.setGeometry(QtCore.QRect(620, 80, 91, 16))
        self.retail_3.setText("")
        self.retail_3.setObjectName("retail_3")
        self.name_3 = QtWidgets.QLabel(self.groupBox_3)
        self.name_3.setGeometry(QtCore.QRect(210, 80, 91, 16))
        self.name_3.setText("")
        self.name_3.setObjectName("name_3")
        self.name = QtWidgets.QLabel(self.groupBox_3)
        self.name.setGeometry(QtCore.QRect(210, 40, 91, 16))
        self.name.setText("")
        self.name.setObjectName("name")
        self.enter_price_l_3 = QtWidgets.QLabel(self.groupBox_3)
        self.enter_price_l_3.setGeometry(QtCore.QRect(510, 80, 91, 16))
        self.enter_price_l_3.setText("")
        self.enter_price_l_3.setObjectName("enter_price_l_3")
        self.provider_4 = QtWidgets.QLabel(self.groupBox_3)
        self.provider_4.setGeometry(QtCore.QRect(110, 100, 91, 16))
        self.provider_4.setText("")
        self.provider_4.setObjectName("provider_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_11.setObjectName("label_11")
        self.retail_2 = QtWidgets.QLabel(self.groupBox_3)
        self.retail_2.setGeometry(QtCore.QRect(620, 60, 91, 16))
        self.retail_2.setText("")
        self.retail_2.setObjectName("retail_2")
        self.group_4 = QtWidgets.QLabel(self.groupBox_3)
        self.group_4.setGeometry(QtCore.QRect(310, 100, 91, 16))
        self.group_4.setText("")
        self.group_4.setObjectName("group_4")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(310, 20, 51, 16))
        self.label_15.setObjectName("label_15")
        self.discount = QtWidgets.QLabel(self.groupBox_3)
        self.discount.setGeometry(QtCore.QRect(410, 40, 91, 16))
        self.discount.setText("")
        self.discount.setObjectName("discount")
        self.discount_4 = QtWidgets.QLabel(self.groupBox_3)
        self.discount_4.setGeometry(QtCore.QRect(410, 100, 91, 16))
        self.discount_4.setText("")
        self.discount_4.setObjectName("discount_4")
        self.provider_3 = QtWidgets.QLabel(self.groupBox_3)
        self.provider_3.setGeometry(QtCore.QRect(110, 80, 91, 16))
        self.provider_3.setText("")
        self.provider_3.setObjectName("provider_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(110, 20, 81, 16))
        self.label_16.setObjectName("label_16")
        self.provider_2 = QtWidgets.QLabel(self.groupBox_3)
        self.provider_2.setGeometry(QtCore.QRect(110, 60, 91, 16))
        self.provider_2.setText("")
        self.provider_2.setObjectName("provider_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(620, 20, 111, 16))
        self.label_10.setObjectName("label_10")
        self.discount_2 = QtWidgets.QLabel(self.groupBox_3)
        self.discount_2.setGeometry(QtCore.QRect(410, 60, 91, 16))
        self.discount_2.setText("")
        self.discount_2.setObjectName("discount_2")
        self.group_3 = QtWidgets.QLabel(self.groupBox_3)
        self.group_3.setGeometry(QtCore.QRect(310, 80, 91, 16))
        self.group_3.setText("")
        self.group_3.setObjectName("group_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(410, 20, 51, 16))
        self.label_12.setObjectName("label_12")
        self.group = QtWidgets.QLabel(self.groupBox_3)
        self.group.setGeometry(QtCore.QRect(310, 40, 91, 16))
        self.group.setText("")
        self.group.setObjectName("group")
        self.provider_1 = QtWidgets.QLabel(self.groupBox_3)
        self.provider_1.setGeometry(QtCore.QRect(110, 40, 91, 16))
        self.provider_1.setText("")
        self.provider_1.setObjectName("provider_1")
        self.name_2 = QtWidgets.QLabel(self.groupBox_3)
        self.name_2.setGeometry(QtCore.QRect(210, 60, 91, 16))
        self.name_2.setText("")
        self.name_2.setObjectName("name_2")
        self.name_4 = QtWidgets.QLabel(self.groupBox_3)
        self.name_4.setGeometry(QtCore.QRect(210, 100, 91, 16))
        self.name_4.setText("")
        self.name_4.setObjectName("name_4")
        self.code = QtWidgets.QLabel(self.groupBox_3)
        self.code.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.code.setText("")
        self.code.setObjectName("code")
        self.code_3 = QtWidgets.QLabel(self.groupBox_3)
        self.code_3.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.code_3.setText("")
        self.code_3.setObjectName("code_3")
        self.enter_price_l = QtWidgets.QLabel(self.groupBox_3)
        self.enter_price_l.setGeometry(QtCore.QRect(510, 40, 91, 16))
        self.enter_price_l.setText("")
        self.enter_price_l.setObjectName("enter_price_l")
        self.enter_price_l_2 = QtWidgets.QLabel(self.groupBox_3)
        self.enter_price_l_2.setGeometry(QtCore.QRect(510, 60, 91, 16))
        self.enter_price_l_2.setText("")
        self.enter_price_l_2.setObjectName("enter_price_l_2")
        self.group_2 = QtWidgets.QLabel(self.groupBox_3)
        self.group_2.setGeometry(QtCore.QRect(310, 60, 91, 16))
        self.group_2.setText("")
        self.group_2.setObjectName("group_2")
        self.code_4 = QtWidgets.QLabel(self.groupBox_3)
        self.code_4.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.code_4.setText("")
        self.code_4.setObjectName("code_4")
        self.retail = QtWidgets.QLabel(self.groupBox_3)
        self.retail.setGeometry(QtCore.QRect(620, 40, 91, 16))
        self.retail.setText("")
        self.retail.setObjectName("retail")
        self.retail_4 = QtWidgets.QLabel(self.groupBox_3)
        self.retail_4.setGeometry(QtCore.QRect(620, 100, 91, 16))
        self.retail_4.setText("")
        self.retail_4.setObjectName("retail_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(510, 20, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(210, 20, 51, 16))
        self.label_14.setObjectName("label_14")
        self.code_2 = QtWidgets.QLabel(self.groupBox_3)
        self.code_2.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.code_2.setText("")
        self.code_2.setObjectName("code_2")
        self.discount_3 = QtWidgets.QLabel(self.groupBox_3)
        self.discount_3.setGeometry(QtCore.QRect(410, 80, 91, 16))
        self.discount_3.setText("")
        self.discount_3.setObjectName("discount_3")
        self.enter_price_l_4 = QtWidgets.QLabel(self.groupBox_3)
        self.enter_price_l_4.setGeometry(QtCore.QRect(510, 100, 91, 16))
        self.enter_price_l_4.setText("")
        self.enter_price_l_4.setObjectName("enter_price_l_4")

        self.retranslateUi(Export_spare_parts)
        QtCore.QMetaObject.connectSlotsByName(Export_spare_parts)

    def retranslateUi(self, Export_spare_parts):
        _translate = QtCore.QCoreApplication.translate
        Export_spare_parts.setWindowTitle(_translate("Export_spare_parts", "Export spare"))
        self.groupBox.setTitle(_translate("Export_spare_parts", "Запуск процедур"))
        self.radioButton_current.setText(_translate("Export_spare_parts", "Текущий каталог"))
        self.radioButton_vw.setText(_translate("Export_spare_parts", "VW"))
        self.radioButton_dil.setText(_translate("Export_spare_parts", "DIL"))
        self.radioButton_sk.setText(_translate("Export_spare_parts", "SK"))
        self.pushButton_2.setText(_translate("Export_spare_parts", "Обновления каталога"))
        self.radioButton_nzp.setText(_translate("Export_spare_parts", "NZP"))
        self.del_from_iprr.setText(_translate("Export_spare_parts", "Удалить с IPRR"))
        self.groupBox_2.setTitle(_translate("Export_spare_parts", "Экспорт с файла в временную таблицу"))
        self.label_7.setText(_translate("Export_spare_parts", "                       ..."))
        self.label_8.setText(_translate("Export_spare_parts", "Группа скид.:"))
        self.pushButton.setText(_translate("Export_spare_parts", "Предосмотр"))
        self.commandLinkButton.setText(_translate("Export_spare_parts", "Начать экспорт "))
        self.label_3.setText(_translate("Export_spare_parts", "Группа товар.:"))
        self.label_6.setText(_translate("Export_spare_parts", "Название страницы:"))
        self.label_5.setText(_translate("Export_spare_parts", "РРЦ:"))
        self.provider_check.setText(_translate("Export_spare_parts", "утановить"))
        self.later.setText(_translate("Export_spare_parts", "Лист1"))
        self.label_2.setText(_translate("Export_spare_parts", "Наименование :"))
        self.open_excel_button.setText(_translate("Export_spare_parts", "выберите excel"))
        self.name_.setText(_translate("Export_spare_parts", "c2"))
        self.enter_price.setText(_translate("Export_spare_parts", "e2"))
        self.label_13.setText(_translate("Export_spare_parts", "Поставщик"))
        self.provider_.setText(_translate("Export_spare_parts", "b2"))
        self.group_.setText(_translate("Export_spare_parts", "g2"))
        self.discount_.setText(_translate("Export_spare_parts", "d2"))
        self.retail_.setText(_translate("Export_spare_parts", "f2"))
        self.label.setText(_translate("Export_spare_parts", "Каталожный номер:"))
        self.group_check.setText(_translate("Export_spare_parts", "утановить"))
        self.code_.setText(_translate("Export_spare_parts", "a2"))
        self.label_4.setText(_translate("Export_spare_parts", "Входящая цена:"))
        self.disccount_check.setText(_translate("Export_spare_parts", "утановить"))
        self.groupBox_3.setTitle(_translate("Export_spare_parts", "Предосмотр"))
        self.label_11.setText(_translate("Export_spare_parts", "Код запчасти:"))
        self.label_15.setText(_translate("Export_spare_parts", "Группа:"))
        self.label_16.setText(_translate("Export_spare_parts", "Поставщик:"))
        self.label_10.setText(_translate("Export_spare_parts", "Розница:"))
        self.label_12.setText(_translate("Export_spare_parts", "Скидка:"))
        self.label_9.setText(_translate("Export_spare_parts", "Входящая цена:"))
        self.label_14.setText(_translate("Export_spare_parts", "Название:"))
