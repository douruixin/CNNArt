# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreColor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreColor(object):
    def setupUi(self, PreColor):
        PreColor.setObjectName("PreColor")
        PreColor.resize(471, 459)
        self.verticalLayout = QtWidgets.QVBoxLayout(PreColor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_23 = QtWidgets.QLabel(PreColor)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(PreColor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(PreColor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1)
        self.b_22 = QtWidgets.QPushButton(self.page)
        self.b_22.setText("")
        self.b_22.setObjectName("b_22")
        self.gridLayout_3.addWidget(self.b_22, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.page)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 5, 1, 1, 1)
        self.b_21 = QtWidgets.QPushButton(self.page)
        self.b_21.setText("")
        self.b_21.setObjectName("b_21")
        self.gridLayout_3.addWidget(self.b_21, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.trans1 = QtWidgets.QLineEdit(self.page)
        self.trans1.setObjectName("trans1")
        self.gridLayout_3.addWidget(self.trans1, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 7, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 7, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.page)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 6, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.page)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 6, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.page)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 5, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.page)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 4, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.page)
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 4, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.page)
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 8, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.page)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.gridLayout_3.addWidget(self.label_40, 8, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ggglayout = QtWidgets.QGridLayout()
        self.ggglayout.setObjectName("ggglayout")
        self.label_35 = QtWidgets.QLabel(self.page_2)
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.ggglayout.addWidget(self.label_35, 5, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.page_2)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.ggglayout.addWidget(self.label_31, 7, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.page_2)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.ggglayout.addWidget(self.label_36, 4, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.page_2)
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.ggglayout.addWidget(self.label_37, 4, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.page_2)
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.ggglayout.addWidget(self.label_33, 6, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.page_2)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.ggglayout.addWidget(self.label_30, 7, 0, 1, 1)
        self.cb_81 = QtWidgets.QComboBox(self.page_2)
        self.cb_81.setObjectName("cb_81")
        self.cb_81.addItem("")
        self.cb_81.addItem("")
        self.cb_81.addItem("")
        self.cb_81.addItem("")
        self.cb_81.addItem("")
        self.ggglayout.addWidget(self.cb_81, 1, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.page_2)
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.ggglayout.addWidget(self.label_34, 5, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setObjectName("label_21")
        self.ggglayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.cb_83 = QtWidgets.QComboBox(self.page_2)
        self.cb_83.setObjectName("cb_83")
        self.cb_83.addItem("")
        self.cb_83.addItem("")
        self.cb_83.addItem("")
        self.cb_83.addItem("")
        self.cb_83.addItem("")
        self.ggglayout.addWidget(self.cb_83, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setObjectName("label")
        self.ggglayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.ggglayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.ggglayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.cb_82 = QtWidgets.QComboBox(self.page_2)
        self.cb_82.setObjectName("cb_82")
        self.cb_82.addItem("")
        self.cb_82.addItem("")
        self.cb_82.addItem("")
        self.cb_82.addItem("")
        self.cb_82.addItem("")
        self.ggglayout.addWidget(self.cb_82, 2, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.page_2)
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.ggglayout.addWidget(self.label_41, 8, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.page_2)
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.ggglayout.addWidget(self.label_42, 8, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.ggglayout)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.b_114 = QtWidgets.QPushButton(self.page_3)
        self.b_114.setText("")
        self.b_114.setObjectName("b_114")
        self.gridLayout_2.addWidget(self.b_114, 4, 1, 1, 1)
        self.cb_113 = QtWidgets.QComboBox(self.page_3)
        self.cb_113.setObjectName("cb_113")
        self.cb_113.addItem("")
        self.cb_113.addItem("")
        self.cb_113.addItem("")
        self.cb_113.addItem("")
        self.cb_113.addItem("")
        self.gridLayout_2.addWidget(self.cb_113, 9, 1, 1, 1)
        self.cb_111 = QtWidgets.QComboBox(self.page_3)
        self.cb_111.setObjectName("cb_111")
        self.cb_111.addItem("")
        self.cb_111.addItem("")
        self.cb_111.addItem("")
        self.cb_111.addItem("")
        self.cb_111.addItem("")
        self.gridLayout_2.addWidget(self.cb_111, 7, 1, 1, 1)
        self.cb_112 = QtWidgets.QComboBox(self.page_3)
        self.cb_112.setObjectName("cb_112")
        self.cb_112.addItem("")
        self.cb_112.addItem("")
        self.cb_112.addItem("")
        self.cb_112.addItem("")
        self.cb_112.addItem("")
        self.gridLayout_2.addWidget(self.cb_112, 8, 1, 1, 1)
        self.b_112 = QtWidgets.QPushButton(self.page_3)
        self.b_112.setText("")
        self.b_112.setObjectName("b_112")
        self.gridLayout_2.addWidget(self.b_112, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.page_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.b_113 = QtWidgets.QPushButton(self.page_3)
        self.b_113.setText("")
        self.b_113.setObjectName("b_113")
        self.gridLayout_2.addWidget(self.b_113, 3, 1, 1, 1)
        self.b_115 = QtWidgets.QPushButton(self.page_3)
        self.b_115.setText("")
        self.b_115.setObjectName("b_115")
        self.gridLayout_2.addWidget(self.b_115, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)
        self.trans3 = QtWidgets.QLineEdit(self.page_3)
        self.trans3.setObjectName("trans3")
        self.gridLayout_2.addWidget(self.trans3, 6, 1, 1, 1)
        self.b_111 = QtWidgets.QPushButton(self.page_3)
        self.b_111.setText("")
        self.b_111.setObjectName("b_111")
        self.gridLayout_2.addWidget(self.b_111, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 10, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.page_3)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 11, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.page_3)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 11, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(PreColor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PreColor)
        self.stackedWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(PreColor.accept)
        self.buttonBox.rejected.connect(PreColor.reject)
        QtCore.QMetaObject.connectSlotsByName(PreColor)

    def retranslateUi(self, PreColor):
        _translate = QtCore.QCoreApplication.translate
        PreColor.setWindowTitle(_translate("PreColor", "Default Colors"))
        self.label_23.setText(_translate("PreColor", "classes"))
        self.label_17.setText(_translate("PreColor", "2 classes"))
        self.label_15.setText(_translate("PreColor", "transparency (0~1)"))
        self.label_16.setText(_translate("PreColor", "artifacts"))
        self.label_14.setText(_translate("PreColor", "reference"))
        self.cb_81.setItemText(0, _translate("PreColor", "//"))
        self.cb_81.setItemText(1, _translate("PreColor", "\\\\"))
        self.cb_81.setItemText(2, _translate("PreColor", "XX"))
        self.cb_81.setItemText(3, _translate("PreColor", "--"))
        self.cb_81.setItemText(4, _translate("PreColor", "**"))
        self.label_21.setText(_translate("PreColor", "8 classes"))
        self.cb_83.setItemText(0, _translate("PreColor", "//"))
        self.cb_83.setItemText(1, _translate("PreColor", "\\\\"))
        self.cb_83.setItemText(2, _translate("PreColor", "XX"))
        self.cb_83.setItemText(3, _translate("PreColor", "--"))
        self.cb_83.setItemText(4, _translate("PreColor", "**"))
        self.label.setText(_translate("PreColor", "motion"))
        self.label_3.setText(_translate("PreColor", "noise"))
        self.label_2.setText(_translate("PreColor", "shim"))
        self.cb_82.setItemText(0, _translate("PreColor", "//"))
        self.cb_82.setItemText(1, _translate("PreColor", "\\\\"))
        self.cb_82.setItemText(2, _translate("PreColor", "XX"))
        self.cb_82.setItemText(3, _translate("PreColor", "--"))
        self.cb_82.setItemText(4, _translate("PreColor", "**"))
        self.label_5.setText(_translate("PreColor", "t1 head"))
        self.label_6.setText(_translate("PreColor", "t1 abdomen"))
        self.label_10.setText(_translate("PreColor", "transparency (0~1)"))
        self.label_7.setText(_translate("PreColor", "t2 abdomen"))
        self.cb_113.setItemText(0, _translate("PreColor", "//"))
        self.cb_113.setItemText(1, _translate("PreColor", "\\\\"))
        self.cb_113.setItemText(2, _translate("PreColor", "XX"))
        self.cb_113.setItemText(3, _translate("PreColor", "--"))
        self.cb_113.setItemText(4, _translate("PreColor", "**"))
        self.cb_111.setItemText(0, _translate("PreColor", "//"))
        self.cb_111.setItemText(1, _translate("PreColor", "\\\\"))
        self.cb_111.setItemText(2, _translate("PreColor", "XX"))
        self.cb_111.setItemText(3, _translate("PreColor", "--"))
        self.cb_111.setItemText(4, _translate("PreColor", "**"))
        self.cb_112.setItemText(0, _translate("PreColor", "//"))
        self.cb_112.setItemText(1, _translate("PreColor", "\\\\"))
        self.cb_112.setItemText(2, _translate("PreColor", "XX"))
        self.cb_112.setItemText(3, _translate("PreColor", "--"))
        self.cb_112.setItemText(4, _translate("PreColor", "**"))
        self.label_12.setText(_translate("PreColor", "motion"))
        self.label_22.setText(_translate("PreColor", "both"))
        self.label_8.setText(_translate("PreColor", "t1 liver"))
        self.label_13.setText(_translate("PreColor", "shim"))
        self.label_4.setText(_translate("PreColor", "11 classes"))
        self.label_9.setText(_translate("PreColor", "t2 liver"))

