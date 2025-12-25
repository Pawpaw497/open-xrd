# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_config.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_importConfigDialog(object):
    def setupUi(self, importConfigDialog):
        if not importConfigDialog.objectName():
            importConfigDialog.setObjectName(u"importConfigDialog")
        importConfigDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(importConfigDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(importConfigDialog)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.labelPath = QLabel(importConfigDialog)
        self.labelPath.setObjectName(u"labelPath")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelPath.sizePolicy().hasHeightForWidth())
        self.labelPath.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.labelPath)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.intensityButton = QRadioButton(importConfigDialog)
        self.intensityButton.setObjectName(u"intensityButton")

        self.gridLayout.addWidget(self.intensityButton, 1, 1, 1, 1)

        self.label_2 = QLabel(importConfigDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.xrdButton = QRadioButton(importConfigDialog)
        self.xrdButton.setObjectName(u"xrdButton")

        self.gridLayout.addWidget(self.xrdButton, 2, 1, 1, 1)

        self.label = QLabel(importConfigDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dSpacingButton = QRadioButton(importConfigDialog)
        self.dSpacingButton.setObjectName(u"dSpacingButton")

        self.gridLayout.addWidget(self.dSpacingButton, 0, 2, 1, 1)

        self.label_3 = QLabel(importConfigDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.normIntensityButton = QRadioButton(importConfigDialog)
        self.normIntensityButton.setObjectName(u"normIntensityButton")

        self.gridLayout.addWidget(self.normIntensityButton, 1, 2, 1, 1)

        self.xrrButton = QRadioButton(importConfigDialog)
        self.xrrButton.setObjectName(u"xrrButton")

        self.gridLayout.addWidget(self.xrrButton, 2, 2, 1, 1)

        self.twoThetaButton = QRadioButton(importConfigDialog)
        self.twoThetaButton.setObjectName(u"twoThetaButton")

        self.gridLayout.addWidget(self.twoThetaButton, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(importConfigDialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_4)

        self.wavelengthComboBox = QComboBox(importConfigDialog)
        self.wavelengthComboBox.setObjectName(u"wavelengthComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.wavelengthComboBox.sizePolicy().hasHeightForWidth())
        self.wavelengthComboBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.wavelengthComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(importConfigDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(importConfigDialog)
        self.buttonBox.accepted.connect(importConfigDialog.accept)
        self.buttonBox.rejected.connect(importConfigDialog.reject)

        QMetaObject.connectSlotsByName(importConfigDialog)
    # setupUi

    def retranslateUi(self, importConfigDialog):
        importConfigDialog.setWindowTitle(QCoreApplication.translate("importConfigDialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("importConfigDialog", u"Path: ", None))
        self.labelPath.setText("")
        self.intensityButton.setText(QCoreApplication.translate("importConfigDialog", u"Intensity", None))
        self.label_2.setText(QCoreApplication.translate("importConfigDialog", u"y-type", None))
        self.xrdButton.setText(QCoreApplication.translate("importConfigDialog", u"XRD", None))
        self.label.setText(QCoreApplication.translate("importConfigDialog", u"x-type", None))
        self.dSpacingButton.setText(QCoreApplication.translate("importConfigDialog", u"d-spacing", None))
        self.label_3.setText(QCoreApplication.translate("importConfigDialog", u"Data type", None))
        self.normIntensityButton.setText(QCoreApplication.translate("importConfigDialog", u"Normalized Intensity", None))
        self.xrrButton.setText(QCoreApplication.translate("importConfigDialog", u"XRR", None))
        self.twoThetaButton.setText(QCoreApplication.translate("importConfigDialog", u"2theta", None))
        self.label_4.setText(QCoreApplication.translate("importConfigDialog", u"Wavelength:", None))
    # retranslateUi

