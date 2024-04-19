import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import random

class RouletteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculateur de chances à la roulette")

        # Layout principal
        layout = QVBoxLayout()

        # Entrée pour le numéro choisi par le joueur
        label_numero = QLabel("Entrez un numéro entre 0 et 36:")
        self.entry_numero = QLineEdit()
        layout.addWidget(label_numero)
        layout.addWidget(self.entry_numero)

        # Boutons pour calculer les chances pour un numéro spécifique et la moyenne des chances
        btn_calculer_chances = QPushButton("Calculer les chances")
        btn_calculer_moyenne = QPushButton("Calculer la moyenne des chances")

        layout.addWidget(btn_calculer_chances)
        layout.addWidget(btn_calculer_moyenne)

        self.setLayout(layout)

        # Connecter les boutons aux fonctions de calcul
        btn_calculer_chances.clicked.connect(self.calculer_chances)
        btn_calculer_moyenne.clicked.connect(self.calculer_moyenne)

    def simuler_roulettes(self, n_lancers):
        occurrences = {i: 0 for i in range(37)}  # Initialiser le compteur pour chaque numéro
        for _ in range(n_lancers):
            numero = random.randint(0, 36)  # Choisir un numéro aléatoire entre 0 et 36
            occurrences[numero] += 1  # Incrémenter le compteur pour ce numéro
        return occurrences

    def chances_gagner(self, numero, n_lancers):
        resultats = self.simuler_roulettes(n_lancers)
        total_occurrences = sum(resultats.values())
        occurrences_numero = resultats[numero]
        chance = (occurrences_numero / total_occurrences) * 100
        return chance

    def calculer_chances(self):
        numero_joueur = int(self.entry_numero.text())
        if 0 <= numero_joueur <= 36:
            chance_joueur = self.chances_gagner(numero_joueur, n_lancers)
            QMessageBox.information(self, "Chances de gagner", f"Votre chance de gagner avec le numéro {numero_joueur} est d'environ {chance_joueur:.2f}%")
        else:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer un numéro entre 0 et 36.")

    def calculer_moyenne(self):
        moyenne = sum(self.chances_gagner(numero, n_lancers) for numero in range(37)) / 37
        QMessageBox.information(self, "Moyenne des chances de gagner", f"La moyenne des chances de gagner pour tous les numéros est d'environ {moyenne:.2f}%")

n_lancers = 1000000

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RouletteApp()
    window.show()
    sys.exit(app.exec_())
