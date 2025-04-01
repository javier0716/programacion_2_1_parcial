from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QSpinBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Hello QT")

        self.__setup_ui()
    
    def __on_submit(self):
        nombre =self.nombre_imput.text()
        self.nombre_imput.clear()
        self.label.setText(nombre)

        num = self.num_imput.value()
        print(num)
        self.num_imput.setValue(0)

        label = QLabel(nombre)

        layout = self.layout()
        layout.addWidget(label)

        print(layout)
    
    

    def __setup_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Hola Mundo")
       
        self.nombre_imput = QLineEdit()
        self.nombre_imput.returnPressed.connect(self.__on_submit)

        btn_1 = QPushButton("Imprimir Texto")
        btn_1.clicked.connect(self.__on_submit)
        
        self.num_imput = QSpinBox()
        

        layout.addWidget(self.label)
        layout.addWidget(self.nombre_imput)
        layout.addWidget(self.num_imput)
        layout.addWidget(btn_1)
 
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()

