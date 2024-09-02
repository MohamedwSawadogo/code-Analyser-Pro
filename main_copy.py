from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from connexion import Ui_MainWindow  # Remplacez 'ui_login' par le nom de votre fichier converti sans l'extension '.py'

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connecter le bouton "Log in" à la méthode de gestion de la connexion
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        # Récupérer les identifiants
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Vérifier les identifiants (exemple simple)
        if username == "admin" and password == "password":  # Remplacez par votre propre logique de validation
            QMessageBox.information(self, "Succès", "Connexion réussie")
            # Ajoutez ici la logique pour ouvrir la fenêtre suivante
        else:
            QMessageBox.warning(self, "Erreur", "Échec de la connexion")

if __name__ == "__main__":
    app = QApplication([])  # Crée l'application Qt
    window = LoginWindow()  # Crée une instance de votre fenêtre de connexion
    window.show()  # Affiche la fenêtre de connexion
    app.exec()  # Exécute l'application
