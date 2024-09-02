from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QDialog, QVBoxLayout, QLabel, QApplication, QProgressBar
from PySide6.QtGui import QPixmap
from reel_connexion import Ui_MainWindow as LoginUI

class VerificationThread(QThread):
    verification_complete = Signal(bool)
    progress_update = Signal(int)

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def run(self):
        steps = 5  # Nombre d'étapes pour la barre de progression
        progress_intervals = 100 // steps  # Intervalle de progression pour chaque étape

        for i in range(steps):
            self.msleep(400)  # Durée de sommeil par étape
            self.progress_update.emit((i + 1) * progress_intervals)

        # Vérification des identifiants après avoir mis à jour la barre de progression
        if self.username == "admin" and self.password == "password":
            self.verification_complete.emit(True)
        else:
            self.verification_complete.emit(False)

        # Assurez-vous que la barre de progression atteint 100 %
        self.progress_update.emit(100)

class CustomProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chargement")
        self.setWindowModality(Qt.WindowModal)
        self.setFixedSize(400, 200)

        layout = QVBoxLayout(self)

        logo_label = QLabel(self)
        logo_path = "SII-removebg-preview.png"
        pixmap = QPixmap(logo_path)
        if pixmap.isNull():
            print("Le chemin de l'image est incorrect ou l'image est absente.")
        else:
            logo_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        self.label = QLabel("Vérification des identifiants...", self)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(False)
        layout.addWidget(self.progress_bar, alignment=Qt.AlignCenter)

        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #8f8f91;
                border-radius: 5px;
            }
            QLabel {
                color: #333333;
                font-size: 14px;
                margin: 10px;
            }
            QProgressBar {
                border: 1px solid #8f8f91;
                border-radius: 5px;
                background-color: #e0e0e0;
            }
            QProgressBar::chunk {
                background-color: #76c7c0;
                width: 20px;
                margin: 1px;
            }
        """)

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.verify_credentials)
        self.resize(800, 600)

    def verify_credentials(self):
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        self.progress_dialog = CustomProgressDialog(self)
        self.progress_dialog.show()

        self.thread = VerificationThread(username, password)
        self.thread.progress_update.connect(self.update_progress)
        self.thread.verification_complete.connect(self.on_verification_complete)
        self.thread.finished.connect(self.progress_dialog.close)
        self.thread.start()

    def update_progress(self, value):
        self.progress_dialog.progress_bar.setValue(value)
        QApplication.processEvents()  # Forcer la mise à jour de l'interface utilisateur

    def on_verification_complete(self, success):
        if success:
            from main_window import MainWindow
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            self.progress_dialog.close()  # Fermer le dialog de progression avant de passer à la fenêtre principale
            QMessageBox.warning(self, "Erreur", "Identifiants incorrects")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
