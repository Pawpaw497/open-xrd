# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'baseline.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGridLayout,
    QGroupBox, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_baselineWidget(object):
    def setupUi(self, baselineWidget):
        if not baselineWidget.objectName():
            baselineWidget.setObjectName(u"baselineWidget")
        baselineWidget.resize(400, 300)
        baselineWidget.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(baselineWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(baselineWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rollingButton = QRadioButton(self.groupBox)
        self.rollingButton.setObjectName(u"rollingButton")

        self.gridLayout.addWidget(self.rollingButton, 1, 1, 1, 1)

        self.alsButton = QRadioButton(self.groupBox)
        self.alsButton.setObjectName(u"alsButton")

        self.gridLayout.addWidget(self.alsButton, 0, 1, 1, 1)

        self.snipButton = QRadioButton(self.groupBox)
        self.snipButton.setObjectName(u"snipButton")
        self.snipButton.setChecked(True)

        self.gridLayout.addWidget(self.snipButton, 0, 0, 1, 1)

        self.polyButton = QRadioButton(self.groupBox)
        self.polyButton.setObjectName(u"polyButton")

        self.gridLayout.addWidget(self.polyButton, 1, 0, 1, 1)

        self.modPolyButton = QRadioButton(self.groupBox)
        self.modPolyButton.setObjectName(u"modPolyButton")

        self.gridLayout.addWidget(self.modPolyButton, 2, 0, 1, 1)

        self.anchorButton = QRadioButton(self.groupBox)
        self.anchorButton.setObjectName(u"anchorButton")

        self.gridLayout.addWidget(self.anchorButton, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(baselineWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(baselineWidget)

        QMetaObject.connectSlotsByName(baselineWidget)
    # setupUi

    def retranslateUi(self, baselineWidget):
        baselineWidget.setWindowTitle(QCoreApplication.translate("baselineWidget", u"Baseline", None))
        self.groupBox.setTitle(QCoreApplication.translate("baselineWidget", u"Method", None))
        self.rollingButton.setText(QCoreApplication.translate("baselineWidget", u"rolling_ball", None))
        self.alsButton.setText(QCoreApplication.translate("baselineWidget", u"als", None))
        self.snipButton.setText(QCoreApplication.translate("baselineWidget", u"snip", None))
        self.polyButton.setText(QCoreApplication.translate("baselineWidget", u"poly", None))
        self.modPolyButton.setText(QCoreApplication.translate("baselineWidget", u"modPoly", None))
        self.anchorButton.setText(QCoreApplication.translate("baselineWidget", u"anchor", None))
    # retranslateUi

