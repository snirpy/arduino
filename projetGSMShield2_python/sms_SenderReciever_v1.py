import sys
from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PySide6.QtCore import QTimer
import serial

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GSM-SMS by KORRI")

        # Connect to the serial port
        self.serial_port = serial.Serial('/dev/cu.usbmodem1401', baudrate=9600)

        # Set up your GUI here, load UI file, create widgets, etc.

        # Set up a timer to check for new SMS periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_for_sms)
        self.timer.start(1000)  # Adjust the interval as needed
        self.lblImage = QLabel("")
        self.lblImage.setAlignment(QtCore.Qt.AlignCenter)

        pixmap = QtGui.QPixmap("sms.png")
        self.lblImage.setPixmap(pixmap)

        # Create input fields for phone number and message
        self.phone_number_input = QLineEdit("0650874313", self)
        self.message_input = QLineEdit("Hello from ilyas", self)

        # Create buttons for sending and receiving SMS
        self.send_button = QPushButton("Envoyer SMS", self)
        self.clear_button = QPushButton("Clear Screen", self)
        self.send_button.clicked.connect(self.send_sms)
        self.clear_button.clicked.connect(self.clearMessages)

        # Create a QTextEdit widget for displaying received SMS
        self.sms_display = QTextEdit(self)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.lblImage)
        layout.addWidget(QLabel("Numéro de téléphone :"))
        layout.addWidget(self.phone_number_input)
        layout.addWidget(QLabel("Message :"))
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(QLabel("SMS reçus :"))
        layout.addWidget(self.sms_display)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def clearMessages(self):
        self.sms_display.clear()
        self.sms_display.setPlainText("Waiting for SMS ...")

        pass

    def check_for_sms(self):
        # Check for new SMS in the serial port
        if self.serial_port.in_waiting:
            new_sms = self.serial_port.readline().decode('utf-8').strip()

            # Update your GUI with the new SMS
            self.update_gui_with_sms(new_sms)

    def update_gui_with_sms(self, sms):
        # Update the text area with the new SMS
        current_text = self.sms_display.toPlainText()
        new_text = f"{current_text}\nReceived SMS: {sms}"
        self.sms_display.setPlainText(new_text)

    def send_sms(self):
        # Get phone number and message from input fields
        phone_number = self.phone_number_input.text()
        message = self.message_input.text()

        # Check if phone number and message are not empty
        if not phone_number or not message:
            print("Veuillez saisir un numéro de téléphone et un message.")
            return

        # Envoyer le SMS en utilisant le port série
        sms_data = f"{phone_number}:{message}\r"
        self.serial_port.write(sms_data.encode())

        # Effacer le champ de saisie du message et du numéro après l'envoi
        self.message_input.clear()
        # self.phone_number_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
