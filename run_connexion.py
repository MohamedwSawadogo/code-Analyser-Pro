import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from reel_connexion import Ui_MainWindow  # Importez la classe générée par Qt Designer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instanciez la classe générée par Qt Designer
        self.ui.setupUi(self)  # Configurez l'interface utilisateur

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # Créez l'objet de la fenêtre principale
    main_window.show()  # Affichez la fenêtre principale
    sys.exit(app.exec())
