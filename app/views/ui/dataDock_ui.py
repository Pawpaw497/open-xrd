# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataDock.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_dataViewerDock(object):
    def setupUi(self, dataViewerDock):
        if not dataViewerDock.objectName():
            dataViewerDock.setObjectName(u"dataViewerDock")
        dataViewerDock.resize(400, 300)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.dockWidgetContents)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        dataViewerDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(dataViewerDock)

        QMetaObject.connectSlotsByName(dataViewerDock)
    # setupUi

    def retranslateUi(self, dataViewerDock):
        dataViewerDock.setWindowTitle(QCoreApplication.translate("dataViewerDock", u"Data Viewer", None))
    # retranslateUi

