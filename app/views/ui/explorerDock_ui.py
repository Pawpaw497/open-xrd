# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'explorerDock.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTreeView,
    QVBoxLayout, QWidget)

class Ui_explorerDock(object):
    def setupUi(self, explorerDock):
        if not explorerDock.objectName():
            explorerDock.setObjectName(u"explorerDock")
        explorerDock.resize(495, 523)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectAllButton = QPushButton(self.dockWidgetContents)
        self.selectAllButton.setObjectName(u"selectAllButton")

        self.horizontalLayout.addWidget(self.selectAllButton)

        self.unselectAllButton = QPushButton(self.dockWidgetContents)
        self.unselectAllButton.setObjectName(u"unselectAllButton")

        self.horizontalLayout.addWidget(self.unselectAllButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.treeView = QTreeView(self.dockWidgetContents)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout.addWidget(self.treeView)

        explorerDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(explorerDock)

        QMetaObject.connectSlotsByName(explorerDock)
    # setupUi

    def retranslateUi(self, explorerDock):
        explorerDock.setWindowTitle(QCoreApplication.translate("explorerDock", u"DockWidget", None))
        self.selectAllButton.setText(QCoreApplication.translate("explorerDock", u"Select All", None))
        self.unselectAllButton.setText(QCoreApplication.translate("explorerDock", u"Unselect All", None))
    # retranslateUi

