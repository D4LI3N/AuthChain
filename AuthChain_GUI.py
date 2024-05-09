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
        self.reg_label = QLabel('Sign up:')
        self.reg_username_label = QLabel('Username:')
        self.reg_username_edit = QLineEdit()
        self.reg_password_label = QLabel('Password:')
        self.reg_password_edit = QLineEdit()
        self.reg_button = QPushButton('Sign up')

        # Widgets for login
        self.login_label = QLabel('Login:')
        self.login_username_label = QLabel('Username:')
        self.login_username_edit = QLineEdit()
        self.login_password_label = QLabel('Password:')
        self.login_password_edit = QLineEdit()
        self.login_button = QPushButton('Login')

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
            QMessageBox.information(self, 'Sign up success', f'User {username} was successfully registered on the AuthChain's chain!\nBlock index: {block_index}')
        else:
            QMessageBox.warning(self, 'Sign up unsuccessful', 'Fill out all fields!')

    def login_user(self):
        username = self.login_username_edit.text()
        password = self.login_password_edit.text()

        if username and password:
            if self.blockchain.login_user(username, password):
                QMessageBox.information(self, 'Login successful', f'Welcome: {username}!')
            else:
                QMessageBox.warning(self, 'Login unsuccessful', 'Invalid username or password!')
        else:
            QMessageBox.warning(self, 'Login unseccessful', 'Fill out all fields!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())
