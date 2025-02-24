from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowTitle("hello qt")
        
        self.__setup_ui()
        
    def __on__submit(self):
        nombre= self.nombre_input.text()
        print(nombre)
        self.nombre_input.clear()
        self.label.setText(nombre)
        
       
        
        
    def __setup_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Hola Mundo")
        
        self.nombre_input = QLineEdit()
        self.nombre_input.returnPressed.connect(self.__on__submit)
        
        btn_1 = QPushButton("imprimir texto")
        btn_1.clicked.connect(self.__on__submit)
        
        
        
        layout.addWidget(self.label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(btn_1)
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication()
    
    main_window = MainWindow()
    main_window.show()
    app.exec()