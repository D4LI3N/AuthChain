import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from AuthChain import AuthChain

class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.blockchain = AuthChain()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('AuthChain GUI')
        self.setGeometry(100, 100, 300, 150)

        # Widgets for registration
        self.reg_label = QLabel('Registracija:')
        self.reg_username_label = QLabel('Korisničko ime:')
        self.reg_username_edit = QLineEdit()
        self.reg_password_label = QLabel('Lozinka:')
        self.reg_password_edit = QLineEdit()
        self.reg_button = QPushButton('Registruj korisnika')

        # Widgets for login
        self.login_label = QLabel('Prijava:')
        self.login_username_label = QLabel('Korisničko ime:')
        self.login_username_edit = QLineEdit()
        self.login_password_label = QLabel('Lozinka:')
        self.login_password_edit = QLineEdit()
        self.login_button = QPushButton('Prijavi korisnika')

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.reg_label)
        layout.addWidget(self.reg_username_label)
        layout.addWidget(self.reg_username_edit)
        layout.addWidget(self.reg_password_label)
        layout.addWidget(self.reg_password_edit)
        layout.addWidget(self.reg_button)
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_username_label)
        layout.addWidget(self.login_username_edit)
        layout.addWidget(self.login_password_label)
        layout.addWidget(self.login_password_edit)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        # Signals
        self.reg_button.clicked.connect(self.register_user)
        self.login_button.clicked.connect(self.login_user)

    def register_user(self):
        username = self.reg_username_edit.text()
        password = self.reg_password_edit.text()

        if username and password:
            block_index = self.blockchain.register_user(username, password)
            QMessageBox.information(self, 'Registracija uspešna', f'Korisnik {username} uspešno registrovan na AuthChain lanac!\nIndex bloka: {block_index}')
        else:
            QMessageBox.warning(self, 'Registracija ne-uspešna', 'Ispunite oba polja!')

    def login_user(self):
        username = self.login_username_edit.text()
        password = self.login_password_edit.text()

        if username and password:
            if self.blockchain.login_user(username, password):
                QMessageBox.information(self, 'Prijava uspešna', f'Dobrodošli: {username}!')
            else:
                QMessageBox.warning(self, 'Prijava ne-uspešna', 'Netočno korisničko ime ili lozinka!')
        else:
            QMessageBox.warning(self, 'Prijava ne-uspešna', 'Ispunite oba polja!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())
