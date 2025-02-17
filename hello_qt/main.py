from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle("Hello Qt")
        
        self.__setup_ui()
        
    def __setup_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Hola Mundo")
        layout.addWidget(label)
        
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication()
    
    main_window = MainWindow()
    main_window.show()
    app.exec()