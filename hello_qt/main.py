from PySide6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        
        
        
        
if __name__ == "__main__":
    app = QApplication()
    
    main_window = MainWindow()
    main_window.show()
    app.exec()