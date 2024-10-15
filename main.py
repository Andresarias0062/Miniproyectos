from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget
import calcular
import sys
import matplotlib.pyplot as plt
import numpy as np

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()

        # Create input fields
        self.entry_o2p = QLineEdit(self)
        self.entry_o4p = QLineEdit(self)
        self.entry_cita2 = QLineEdit(self)
        self.entry_w2 = QLineEdit(self)

        # Create labels
        layout.addWidget(QLabel("o2p:"))
        layout.addWidget(self.entry_o2p)

        layout.addWidget(QLabel("o4p:"))
        layout.addWidget(self.entry_o4p)

        layout.addWidget(QLabel("cita2:"))
        layout.addWidget(self.entry_cita2)

        layout.addWidget(QLabel("w2:"))
        layout.addWidget(self.entry_w2)

        # Create calculate button
        self.calculate_button = QPushButton("Calcular", self)
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        # Create plot button
        self.plot_button = QPushButton("Graficar", self)
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        # Create result label
        self.result_label = QLabel("Resultado: ", self)
        layout.addWidget(self.result_label)

        # Set layout
        self.setLayout(layout)
        self.setWindowTitle("Calculadora Mecánica")
        self.show()

    def calculate(self):
        try:
            o2p = float(self.entry_o2p.text())
            o4p = float(self.entry_o4p.text())
            cita2 = float(self.entry_cita2.text())
            w2 = float(self.entry_w2.text())

            result = self.main(cita2, o2p, o4p, w2)
            self.result_label.setText(f"Resultado: \n{result}")
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese valores numéricos válidos.")

    def main(self, cita2, o2p, o4p, w2):
        if(cita2<0 or cita2>95.3):
            QMessageBox.critical(self, "Error", "Cita fuera de rango")
        cita3 = calcular.cita3(o2p, o4p, cita2)
        w3 = calcular.w3(w2, o2p, o4p, cita2, cita3)
        vA = calcular.velocidadA(w2, o2p)
        vB = calcular.velocidadB(w2, o2p, w3, o4p, cita2, cita3)

        alfa2 = 0
        alfa3 = calcular.alfa3(w2, o2p, w3, o4p, cita2, cita3)

        ap = calcular.aceleracionP(w2, o2p, cita2)
        ao = calcular.aceleracionO4(w2, o2p, cita2, alfa3, o4p, cita3, w3)
        
        return (f"Cita3: {cita3:.2f}\n"
                f"w3: {w3:.2f}\n"
                f"vA: {vA:.2f}\n"
                f"vB: {vB:.2f}\n"
                f"Alfa3: {alfa3:.2f}\n"
                f"Aceleración P: {ap:.2f}\n"
                f"Aceleración O4: {ao:.2f}")

    def plot_graph(self):
        try:
            o2p = float(self.entry_o2p.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese un valor numérico válido para o2p.")
            return

        # Define the x values (0 to 95)
        x = np.linspace(0, 95, 500)

        # Calculate y values
        y_cos = o2p * np.cos(np.radians(x))  # O2Pcos(x)
        y_sin = o2p * np.sin(np.radians(x))  # O2Psin(x)

        # Create the plot
        plt.figure()
        plt.plot(y_cos, y_sin, label=f'O2P = {o2p}')
        plt.xlabel("O2Pcos(x)")
        plt.ylabel("O2Psin(x)")
        plt.title("Graph of O2Pcos(x) vs O2Psin(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
