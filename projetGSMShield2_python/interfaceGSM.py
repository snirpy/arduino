from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class GSMInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Créer des widgets d'interface utilisateur
        self.status_label = QLabel('État du GSM: Déconnecté', self)
        self.sensor_data_label = QLabel('Données du Capteur: N/A', self)

        self.phone_number_label = QLabel('Numéro de Téléphone:', self)
        self.phone_number_input = QLineEdit(self)

        self.enable_button = QPushButton('Activer Surveillance', self)
        self.disable_button = QPushButton('Désactiver Surveillance', self)

        # Organiser les widgets dans une mise en page verticale
        layout = QVBoxLayout(self)
        layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.sensor_data_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.phone_number_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.phone_number_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.enable_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.disable_button, alignment=Qt.AlignCenter)

        # Configurer la fenêtre principale
        self.setWindowTitle('GSM Interface')
        self.setGeometry(100, 100, 400, 300)

        # Connecter les signaux et les slots (non implémentés ici)

if __name__ == '__main__':
    app = QApplication([])
    window = GSMInterface()
    window.show()
    app.exec()
