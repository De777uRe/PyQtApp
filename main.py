from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QFontMetrics

if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationDisplayName("Application")
    window = QWidget()
    window.setBaseSize(500, 500)

    main_layout = QGridLayout()

    main_label = QLabel("Financial Data")
    header_font = QFont("Times", 16)
    main_label.setFont(header_font)
    main_layout.addWidget(main_label, 0, 1)

    header_spacer = QSpacerItem(50, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)
    main_layout.addItem(header_spacer, 1, 0)

    # Label
    loan_term_label = QLabel("Loan Term*")
    form_font = QFont("Times", 12)
    loan_term_label.setFont(form_font)
    main_layout.addWidget(loan_term_label, 2, 0)
    # Text Edit
    loan_term_edit = QTextEdit()
    loan_term_edit.setFixedHeight(25)
    loan_term_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    main_layout.addWidget(loan_term_edit, 2, 1)

    # Label
    loan_to_value_label = QLabel("Loan To Value (%)*")
    loan_to_value_label.setFont(form_font)
    main_layout.addWidget(loan_to_value_label, 3, 0)
    # Text Edit
    loan_to_value_edit = QTextEdit()
    loan_to_value_edit.setFixedHeight(25)
    loan_to_value_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    main_layout.addWidget(loan_to_value_edit, 3, 1)

    # Label
    dscr_label = QLabel("DSCR")
    dscr_label.setFont(form_font)
    main_layout.addWidget(dscr_label, 4, 0)
    # Text Edit
    dscr_edit = QTextEdit()
    dscr_edit.setFixedHeight(25)
    dscr_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    main_layout.addWidget(dscr_edit, 4, 1)

    window.setLayout(main_layout)
    window.show()
    app.exec_()