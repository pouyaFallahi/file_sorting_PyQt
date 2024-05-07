import sys
from file_sorting import file_sorting, len_files
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,QProgressBar,
                               QTextEdit, QWidget)


class UiWidget(object):
    def setup_ui(self, main_windows):
        if not main_windows.objectName():
            main_windows.setObjectName(u"main_windows")
        main_windows.resize(821, 448)
        self.label_masseage = QLabel(main_windows)
        self.label_masseage.setObjectName(u"label_masseage")
        self.label_masseage.setGeometry(QRect(10, 10, 301, 17))
        self.button_browse = QPushButton(main_windows)
        self.button_browse.setObjectName(u"button_browse")
        self.button_browse.setGeometry(QRect(730, 30, 81, 31))
        self.path_file = QTextEdit(main_windows)
        self.path_file.setObjectName(u"path_file")
        self.path_file.setGeometry(QRect(10, 30, 711, 31))
        self.button_start = QPushButton(main_windows)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(10, 70, 88, 34))
        self.progressBar = QProgressBar(main_windows)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 70, 711, 31))
        self.progressBar.setValue(24)
        self.progressBar.raise_()
        self.button_browse.raise_()
        self.label_masseage.raise_()
        self.path_file.raise_()
        self.button_start.raise_()

        self.retranslate_ui(main_windows)

        QMetaObject.connectSlotsByName(main_windows)

    # setupUi
    def retranslate_ui(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_masseage.setText(
            QCoreApplication.translate("Widget", u"Address of the directory or drive you want to sort:", None))
        self.button_browse.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.button_start.setText(QCoreApplication.translate("main_windows", u"Start", None))
        self.button_browse.clicked.connect(self.browse_file)
        self.button_start.clicked.connect(self.start_sorting)
        self.progressBar.hide()
        self.progressBar.setValue(0)

    # retranslateUi

    def browse_file(self):
        file_name = QFileDialog.getExistingDirectory()
        self.path_file.setText(file_name)

    def start_sorting(self):
        url = self.path_file.toPlainText() + '/'
        items = len_files(url)
        y = 100 / items
        for i in range(items):
            file_sorting(url)
            self.progressBar.show()
            self.progressBar.setValue(y * i)
        self.progressBar.setValue(100)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = UiWidget()
    ui.setup_ui(Widget)
    Widget.show()
    sys.exit(app.exec())
