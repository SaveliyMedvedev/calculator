# TODO переопределить или сделать логику % для exec() либо самому написать полностью логику вычислений. 
# TODO сделать работу с десятичными дробями через decimal и определить вывод целых и нецелых чисел
# TODO клавиатура: 
#   1 запретить ввод букв и ненужных знаков
#   2 привязать enter на = 
#   3 привязать esc на AC
# TODO попробовать сделать дизайн (CSS)
# TODO исправить ввод "."


import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QLineEdit
)



# Класс нашего окна
class App(QWidget):
    def __init__(self):
        super().__init__()

        # Настраиваем окно
        self.setWindowTitle("calculator")
        self.setGeometry(100, 100, 300, 300)  # Указываем позицию и размеры окна

        # Создаем вертикальный макет
        main_layout = QVBoxLayout()

        # Поле ввода символов
        self.input_line = QLineEdit()
        self.input_line.setFixedHeight(40)
        # self.input_line.setStyleSheet("font-size: 18px; padding: 5px; background-color: #f0f0f0; border: 1px solid #ccc;")
        main_layout.addWidget(self.input_line)

        # Сетка для кнопок
        grid_layout = QGridLayout()

        button_icons = [
            ["AC", "del", "%", "/"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["pi", "0", ".", "="],
        ]

        for row in range(5):
            for col in range(4):
                icon = button_icons[row][col]
                
                button = QPushButton(icon) # добавление текста
                # button.setFixedSize(QtCore.QSize(60, 50)) # размер кнопки
               
                # Стиль кнопок
                #button.setStyleSheet("""
                #    background-color: #008CBA; 
                #    color: white; 
                #    font-size: 20px; 
                #    border-radius: 5px; 
                #    border: none;
                #""")
                
                # привязка функций к кнопкам

                if icon == "AC":
                    button.clicked.connect(self.clear_all)
                elif icon == "del":
                    button.clicked.connect(self.delete_last)
                elif icon == "=":
                    button.clicked.connect(self.calculate_result)
                elif icon == "pi":
                    button.clicked.connect(self.pi)
                elif icon == "%":
                    button.clicked.connect(self.percent)

                elif icon in ["+", "-", "×", "/"]:
                    button.clicked.connect(lambda _, op=icon: self.handle_operator(op))
                else:
                    button.clicked.connect(lambda _, digit=icon: self.handle_digit(digit))



                # Вставляем кнопку в сетку
                grid_layout.addWidget(button, row, col)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)


    def clear_all(self):
        self.input_line.clear()
    

    def delete_last(self):
        current_text = self.input_line.text()
        self.input_line.setText(current_text[:-1])

    def pi(self):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + "3.1415926535")

    def percent(self):
        # Логика процента (%)
        current_text = self.input_line.text()

        if not current_text:
            return
        
        last_char = current_text[-1]

        if last_char in "+-":
            # Сложение или вычитание
            left_operand = float(current_text[:-1]) if current_text[:-1] else 0
            percent_value = left_operand * 0.01
            self.input_line.setText(str(percent_value))
        elif last_char in "×/":
            # Умножение или деление
            left_operand = float(current_text[:-1]) if current_text[:-1] else 0
            percent_value = left_operand / 100
            self.input_line.setText(str(percent_value))
        else:
            # Просто число
            try:
                number = float(current_text)
                percent_value = number / 100
                self.input_line.setText(str(percent_value))
            except ValueError:
                self.input_line.setText("Ошибка")


    def calculate_result(self):
        try:
            result = eval(self.input_line.text().replace('×', '*'))  # Заменяем '×' на '*'
            self.input_line.setText(str(result))  # Отображаем результат
        except Exception as e:
            self.input_line.setText("Ошибка")

    
  
    def handle_operator(self, operator):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + operator)


    def handle_digit(self, digit):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + digit)

# Основная часть программы
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создаем приложение
    window = App()  # Создаем экземпляр нашего класса
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # Запускаем цикл приложения

