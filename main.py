from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QHBoxLayout, QMainWindow, QPushButton, QSizePolicy, \
    QSpacerItem, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QFontMetrics
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setBaseSize(500, 500)
        self.centralwidget = QWidget(MainWindow)
        self.main_layout = QGridLayout()

        self.main_label = QLabel("Financial Data")
        self.header_font = QFont("Times", 16)
        self.main_label.setFont(self.header_font)
        self.main_layout.addWidget(self.main_label, 0, 1)

        self.header_spacer = QSpacerItem(50, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.main_layout.addItem(self.header_spacer, 1, 0)

        # Label
        self.loan_term_label = QLabel("Loan Term*")
        self.form_font = QFont("Times", 12)
        self.loan_term_label.setFont(self.form_font)
        self.main_layout.addWidget(self.loan_term_label, 2, 0)
        # Text Edit
        self.loan_term_edit = QLineEdit()
        self.loan_term_edit.setFixedHeight(25)
        self.loan_term_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.main_layout.addWidget(self.loan_term_edit, 2, 1)

        # Label
        self.loan_to_value_label = QLabel("Loan To Value (%)*")
        self.loan_to_value_label.setFont(self.form_font)
        self.main_layout.addWidget(self.loan_to_value_label, 3, 0)
        # Text Edit
        self.loan_to_value_edit = QLineEdit()
        self.loan_to_value_edit.setFixedHeight(25)
        self.loan_to_value_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.main_layout.addWidget(self.loan_to_value_edit, 3, 1)

        # Label
        self.dscr_label = QLabel("DSCR")
        self.dscr_label.setFont(self.form_font)
        self.main_layout.addWidget(self.dscr_label, 4, 0)
        # Text Edit
        self.dscr_edit = QLineEdit()
        self.dscr_edit.setFixedHeight(25)
        self.dscr_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.main_layout.addWidget(self.dscr_edit, 4, 1)

        # Label
        self.loan_amort_label = QLabel("Loan Amort")
        self.loan_amort_label.setFont(self.form_font)
        self.main_layout.addWidget(self.loan_amort_label, 5, 0)
        # Text Edit
        self.loan_amort_edit = QLineEdit()
        self.loan_amort_edit.setFixedHeight(25)
        self.loan_amort_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.main_layout.addWidget(self.loan_amort_edit, 5, 1)

        # Spacer
        self.form_btn_spacer = QSpacerItem(50, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.main_layout.addItem(self.form_btn_spacer, 6, 0)

        # Previous Button
        self.prev_btn = QPushButton("Previous")
        self.main_layout.addWidget(self.prev_btn, 7, 0)
        # Spacer
        self.btn_spacer = QSpacerItem(50, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.main_layout.addItem(self.btn_spacer, 7, 1)
        # Next Button
        self.next_btn = QPushButton("Next")
        self.next_btn.clicked.connect(self.nextBtnClicked)
        self.main_layout.addWidget(self.next_btn, 7, 2)

        self.centralwidget.setLayout(self.main_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application"))

    def nextBtnClicked(self):
        is_form_valid = self.main_validation()
        self.loan_amort_edit.setText(str(is_form_valid))

    def main_validation(self):
        is_valid = self.loan_term_edit.text().isdigit()
        is_valid &= self.loan_to_value_edit.text().isdigit()

        return is_valid


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setApplicationDisplayName("Application")

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
