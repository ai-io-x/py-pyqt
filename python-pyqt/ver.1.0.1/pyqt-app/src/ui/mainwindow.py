from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Application")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        label = QLabel("Welcome to the PyQt Application!")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())