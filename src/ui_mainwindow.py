# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(True)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/iconsLight/assets/light/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/iconsLight/assets/light/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        icon2 = QIcon()
        icon2.addFile(u":/iconsLight/assets/light/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_As.setIcon(icon2)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon()
        icon3.addFile(u":/iconsLight/assets/light/Custom_x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionBold = QAction(MainWindow)
        self.actionBold.setObjectName(u"actionBold")
        self.actionBold.setCheckable(True)
        self.actionBold.setChecked(False)
        icon4 = QIcon()
        icon4.addFile(u":/iconsLight/assets/light/bold.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBold.setIcon(icon4)
        self.actionItalic = QAction(MainWindow)
        self.actionItalic.setObjectName(u"actionItalic")
        self.actionItalic.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/iconsLight/assets/light/italic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionItalic.setIcon(icon5)
        self.actionUnderline = QAction(MainWindow)
        self.actionUnderline.setObjectName(u"actionUnderline")
        self.actionUnderline.setCheckable(True)
        icon6 = QIcon()
        icon6.addFile(u":/iconsLight/assets/light/underline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUnderline.setIcon(icon6)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon7 = QIcon()
        icon7.addFile(u":/iconsLight/assets/light/scissors.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon7)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon8 = QIcon()
        icon8.addFile(u":/iconsLight/assets/light/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon8)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon9 = QIcon()
        icon9.addFile(u":/iconsLight/assets/light/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon9)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon10 = QIcon()
        icon10.addFile(u":/iconsLight/assets/light/corner-up-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon10)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon11 = QIcon()
        icon11.addFile(u":/iconsLight/assets/light/corner-up-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon11)
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon12 = QIcon()
        icon12.addFile(u":/iconsLight/assets/light/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear.setIcon(icon12)
        self.actionLeftAlign = QAction(MainWindow)
        self.actionLeftAlign.setObjectName(u"actionLeftAlign")
        self.actionLeftAlign.setCheckable(True)
        icon13 = QIcon()
        icon13.addFile(u":/iconsLight/assets/light/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLeftAlign.setIcon(icon13)
        self.actionRightAlign = QAction(MainWindow)
        self.actionRightAlign.setObjectName(u"actionRightAlign")
        self.actionRightAlign.setCheckable(True)
        icon14 = QIcon()
        icon14.addFile(u":/iconsLight/assets/light/align-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRightAlign.setIcon(icon14)
        self.actionCenterAlign = QAction(MainWindow)
        self.actionCenterAlign.setObjectName(u"actionCenterAlign")
        self.actionCenterAlign.setCheckable(True)
        icon15 = QIcon()
        icon15.addFile(u":/iconsLight/assets/light/align-center.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCenterAlign.setIcon(icon15)
        self.actionJustifyAlign = QAction(MainWindow)
        self.actionJustifyAlign.setObjectName(u"actionJustifyAlign")
        self.actionJustifyAlign.setCheckable(True)
        icon16 = QIcon()
        icon16.addFile(u":/iconsLight/assets/light/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionJustifyAlign.setIcon(icon16)
        self.actionEnableTextGen = QAction(MainWindow)
        self.actionEnableTextGen.setObjectName(u"actionEnableTextGen")
        self.actionEnableTextGen.setCheckable(True)
        icon17 = QIcon()
        icon17.addFile(u":/iconsLight/assets/light/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEnableTextGen.setIcon(icon17)
        self.actionGenText = QAction(MainWindow)
        self.actionGenText.setObjectName(u"actionGenText")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self._2 = QVBoxLayout(self.centralwidget)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self._2.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setNativeMenuBar(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setAutoFillBackground(True)
        self.toolBar.setIconSize(QSize(16, 16))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionClear)
        self.toolBar.addAction(self.actionEnableTextGen)
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionUnderline)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLeftAlign)
        self.toolBar.addAction(self.actionCenterAlign)
        self.toolBar.addAction(self.actionRightAlign)
        self.toolBar.addAction(self.actionJustifyAlign)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(statustip)
        self.actionOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Open an existing file", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionBold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
#if QT_CONFIG(shortcut)
        self.actionBold.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionItalic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
#if QT_CONFIG(shortcut)
        self.actionItalic.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnderline.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
#if QT_CONFIG(shortcut)
        self.actionUnderline.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(shortcut)
        self.actionClear.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionLeftAlign.setText(QCoreApplication.translate("MainWindow", u"LeftAlign", None))
        self.actionRightAlign.setText(QCoreApplication.translate("MainWindow", u"RightAlign", None))
        self.actionCenterAlign.setText(QCoreApplication.translate("MainWindow", u"CenterAlign", None))
        self.actionJustifyAlign.setText(QCoreApplication.translate("MainWindow", u"JustifyAlign", None))
        self.actionEnableTextGen.setText(QCoreApplication.translate("MainWindow", u"EnableTextGen", None))
        self.actionGenText.setText(QCoreApplication.translate("MainWindow", u"GenText", None))
#if QT_CONFIG(shortcut)
        self.actionGenText.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+Space", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi
