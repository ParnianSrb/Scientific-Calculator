import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The Ui File
        uic.loadUi('P2-Calculator.ui', self)

        # Define Widgets
        self.btn_open = self.findChild(QPushButton, 'btn_open')
        self.btn_Deg = self.findChild(QPushButton, 'btn_Deg')
        self.btn_sin = self.findChild(QPushButton, 'btn_sin')
        self.btn_arcsin = self.findChild(QPushButton, 'btn_arcsin')
        self.btn_nf = self.findChild(QPushButton, 'btn_nf')
        self.btn_xx = self.findChild(QPushButton, 'btn_xx')
        self.btn_close = self.findChild(QPushButton, 'btn_close')
        self.btn_Rad = self.findChild(QPushButton, 'btn_Rad')
        self.btn_cos = self.findChild(QPushButton, 'btn_cos')
        self.btn_arccos = self.findChild(QPushButton, 'btn_arccos')
        self.btn_xy = self.findChild(QPushButton, 'btn_xy')
        self.btn_exp = self.findChild(QPushButton, 'btn_exp')
        self.btn_xxx = self.findChild(QPushButton, 'btn_xxx')
        self.btn_tan = self.findChild(QPushButton, 'btn_tan')
        self.btn_arctan = self.findChild(QPushButton, 'btn_arctan')
        self.btn_ans = self.findChild(QPushButton, 'btn_ans')
        self.btn_pi = self.findChild(QPushButton, 'btn_pi')
        self.btn_abs = self.findChild(QPushButton, 'btn_abs')
        self.btn_log = self.findChild(QPushButton, 'btn_log')
        self.btn_ln = self.findChild(QPushButton, 'btn_ln')
        self.btn_C = self.findChild(QPushButton, 'btn_C')
        self.btn_7 = self.findChild(QPushButton, 'btn_7')
        self.btn_4 = self.findChild(QPushButton, 'btn_4')
        self.btn_1 = self.findChild(QPushButton, 'btn_1')
        self.btn_0 = self.findChild(QPushButton, 'btn_0')
        self.btn_del = self.findChild(QPushButton, 'btn_del')
        self.btn_8 = self.findChild(QPushButton, 'btn_8')
        self.btn_5 = self.findChild(QPushButton, 'btn_5')
        self.btn_2 = self.findChild(QPushButton, 'btn_2')
        self.btn_equal = self.findChild(QPushButton, 'btn_equal')
        self.btn_plus_minus = self.findChild(QPushButton, 'btn_plus_minus')
        self.btn_9 = self.findChild(QPushButton, 'btn_9')
        self.btn_6 = self.findChild(QPushButton, 'btn_6')
        self.btn_3 = self.findChild(QPushButton, 'btn_3')
        self.btn_m = self.findChild(QPushButton, 'btn_m')
        self.btn_divide = self.findChild(QPushButton, 'btn_divide')
        self.btn_x = self.findChild(QPushButton, 'btn_x')
        self.btn_minus = self.findChild(QPushButton, 'btn_minus')
        self.btn_plus = self.findChild(QPushButton, 'btn_plus')
        self.btn_dot = self.findChild(QPushButton, 'btn_dot')
        self.btn_sqrt = self.findChild(QPushButton, 'btn_sqrt')
        self.btn_MC = self.findChild(QPushButton, 'btn_MC')
        self.btn_MR = self.findChild(QPushButton, 'btn_MR')
        self.btn_Mplus = self.findChild(QPushButton, 'btn_Mplus')

        self.label_output = self.findChild(QLabel, 'label_output')
        self.label = self.findChild(QLabel, 'label')

        # Click Buttons
        self.btn_0.clicked.connect(lambda: self.press_it('0'))
        self.btn_1.clicked.connect(lambda: self.press_it('1'))
        self.btn_2.clicked.connect(lambda: self.press_it('2'))
        self.btn_3.clicked.connect(lambda: self.press_it('3'))
        self.btn_4.clicked.connect(lambda: self.press_it('4'))
        self.btn_5.clicked.connect(lambda: self.press_it('5'))
        self.btn_6.clicked.connect(lambda: self.press_it('6'))
        self.btn_7.clicked.connect(lambda: self.press_it('7'))
        self.btn_8.clicked.connect(lambda: self.press_it('8'))
        self.btn_9.clicked.connect(lambda: self.press_it('9'))

        self.btn_open.clicked.connect(lambda: self.press_it('('))
        self.btn_close.clicked.connect(lambda: self.press_it(')'))

        self.btn_sqrt.clicked.connect(lambda: self.press_it('sqrt'))
        self.btn_xx.clicked.connect(lambda: self.press_it('x^2'))
        self.btn_xxx.clicked.connect(lambda: self.press_it('x^3'))
        self.btn_xy.clicked.connect(lambda: self.press_it('x^y'))

        self.btn_nf.clicked.connect(lambda: self.press_it('n!'))

        self.btn_sin.clicked.connect(lambda: self.press_it('sin'))
        self.btn_cos.clicked.connect(lambda: self.press_it('cos'))
        self.btn_tan.clicked.connect(lambda: self.press_it('tan'))
        self.btn_Rad.clicked.connect(lambda: self.press_it('rad'))
        self.btn_Deg.clicked.connect(lambda: self.press_it('Deg'))

        self.btn_arcsin.clicked.connect(lambda: self.press_it('asin'))
        self.btn_arccos.clicked.connect(lambda: self.press_it('acos'))
        self.btn_arctan.clicked.connect(lambda: self.press_it('atan'))

        self.btn_minus.clicked.connect(lambda: self.press_it('minus'))
        self.btn_plus.clicked.connect(lambda: self.press_it('plus'))
        self.btn_x.clicked.connect(lambda: self.press_it('x'))
        self.btn_divide.clicked.connect(lambda: self.press_it('/'))

        self.btn_log.clicked.connect(lambda: self.press_it('log'))
        self.btn_ln.clicked.connect(lambda: self.press_it('ln'))
        self.btn_exp.clicked.connect(lambda: self.press_it('exp'))

        self.btn_pi.clicked.connect(lambda: self.press_it('pi'))

        self.btn_abs.clicked.connect(lambda: self.press_it('abs'))

        self.btn_equal.clicked.connect(self.math_it)
        self.btn_plus_minus.clicked.connect(self.plus_minus)
        self.btn_del.clicked.connect(self.delete_it)
        self.btn_C.clicked.connect(self.clear)
        self.btn_dot.clicked.connect(self.dot_it)
        self.btn_ans.clicked.connect(self.ans)
        self.btn_MC.clicked.connect(self.mc)
        self.btn_MR.clicked.connect(self.mr)
        self.btn_Mplus.clicked.connect(self.m_plus)
        self.btn_m.clicked.connect(self.m_minus)

        # Show The App
        self.show()

    def press_it(self, pressed):
        if self.label_output.text() == '0':
            self.label_output.setText('')
        self.text = self.label_output.text()

        if pressed == '0':
            self.label_output.setText(f'{self.text}0')
        elif pressed == '1':
            self.label_output.setText(f'{self.text}1')
        elif pressed == '2':
            self.label_output.setText(f'{self.text}2')
        elif pressed == '3':
            self.label_output.setText(f'{self.text}3')
        elif pressed == '4':
            self.label_output.setText(f'{self.text}4')
        elif pressed == '5':
            self.label_output.setText(f'{self.text}5')
        elif pressed == '6':
            self.label_output.setText(f'{self.text}6')
        elif pressed == '7':
            self.label_output.setText(f'{self.text}7')
        elif pressed == '8':
            self.label_output.setText(f'{self.text}8')
        elif pressed == '9':
            self.label_output.setText(f'{self.text}9')

        elif pressed == '(':
            self.label_output.setText(f'{self.text}(')
        elif pressed == ')':
            self.label_output.setText(f'{self.text})')

        elif pressed == 'sqrt':
            self.text = eval(self.text)
            self.sqrt = math.sqrt(float(self.text))
            self.label_output.setText(str(self.sqrt))

        elif pressed == 'x^2':
            self.text = eval(self.text)
            self.xx = math.pow(float(self.text), 2)
            self.label_output.setText(str(self.xx))

        elif pressed == 'x^3':
            self.text = eval(self.text)
            self.cube = math.pow(float(self.text), 3)
            self.label_output.setText(str(self.cube))

        elif pressed == 'n!':
            self.nf = 1
            self.text = float(self.text)
            i = 0
            while i < self.text:
                self.nf = (self.text - i) * self.nf
                i += 1
            self.label_output.setText(str(self.nf))

        elif pressed == 'x^y':
            self.label_output.setText(f'{self.text}^')

        elif pressed == 'sin':
            self.label_output.setText(f'sin({self.text})')

        elif pressed == 'cos':
            self.label_output.setText(f'cos({self.text})')

        elif pressed == 'tan':
            self.label_output.setText(f'tan({self.text})')

        elif pressed == 'rad':
            self.rad = math.radians(float(self.text))
            self.label_output.setText(str(self.rad))

        elif pressed == 'Deg':
            self.degree = math.degrees(float(self.text))
            self.label_output.setText(str(self.degree))

        elif pressed == 'asin':
            self.label_output.setText(f'asin({self.text})')

        elif pressed == 'acos':
            self.label_output.setText(f'acos({self.text})')

        elif pressed == 'atan':
            self.label_output.setText(f'atan({self.text})')

        elif pressed == 'minus':
            self.label_output.setText(f'{self.text}-')

        elif pressed == 'plus':
            self.label_output.setText(f'{self.text}+')

        elif pressed == 'x':
            self.label_output.setText(f'{self.text}*')

        elif pressed == '/':
            self.label_output.setText(f'{self.text}/')

        elif pressed == 'log':
            self.label_output.setText(f'log({self.text})')

        elif pressed == 'ln':
            self.label_output.setText(f'ln({self.text})')

        elif pressed == 'exp':
            self.text = float(self.text)
            self.exp = math.exp(self.text)
            self.label_output.setText(str(self.exp))

        elif pressed == 'pi':
            self.label_output.setText(f'{self.text}3.14')

        elif pressed == 'abs':
            self.text = float(self.text)
            self.output = abs(self.text)
            self.label_output.setText(str(self.output))

    def math_it(self):
        self.text = self.label_output.text()
        if 'log' in self.text:
            self.text = float(self.text[4: -1])
            self.output = math.log(self.text, 10)
            self.label_output.setText(str(self.output))
        elif 'ln' in self.text:
            self.text = float(self.text[3: -1])
            self.output = math.log(self.text, math.e)
            self.label_output.setText(str(self.output))
        elif '^' in self.text:
            self.output = math.pow(float(self.text[0]), float(self.text[2]))
            self.label_output.setText(str(self.output))
        elif self.text[0:3] == 'sin':
            self.output = math.sin(float(self.text[4: -1]))
            self.label_output.setText(str(self.output))
        elif self.text[0:3] == 'cos':
            self.output = math.cos(float(self.text[4: -1]))
            self.label_output.setText(str(self.output))
        elif self.text[0:3] == 'tan':
            self.output = math.tan(float(self.text[4: -1]))
            self.label_output.setText(str(self.output))
        elif self.text[0:4] == 'asin':
            self.output = math.asin(float(self.text[5: -1]))
            self.label_output.setText(str(self.output))
        elif self.text[0:4] == 'acos':
            self.output = math.acos(float(self.text[5: -1]))
            self.label_output.setText(str(self.output))
        elif self.text[0:4] == 'atan':
            self.output = math.atan(float(self.text[5: -1]))
            self.label_output.setText(str(self.output))
        else:
            output = eval(self.text)
            self.label_output.setText(str(output))

    def plus_minus(self):
        self.text = self.label_output.text()
        if self.text[0].isnumeric():
            self.label_output.setText(f'-{self.text}')
        elif self.text[0] == '-':
            self.label_output.setText(self.text[1:])
            # self.label_output.setText(self.text.replace('-', ''))

    def delete_it(self):
        self.text = self.label_output.text()
        self.label_output.setText(self.text[:-1])

    def dot_it(self):
        self.text = self.label_output.text()
        if '.' not in self.text:
            if self.text[0] == '0':
                self.label_output.setText('0.')
                self.text = self.text[1:]
            else:
                self.label_output.setText(f'{self.text}.')
        else:
            operators = '+-*/'
            i = -1
            while self.text[i] not in operators:
                i = i - 1
            if '.' not in self.text[i:]:
                self.label_output.setText(f'{self.text}.')
            else:
                pass

    def clear(self):
        self.ans_output = self.label_output.text()
        self.label_output.setText('0')

    def ans(self):
         self.label_output.setText(self.ans_output)

    def mc(self):
        self.ans_output = '0'

    def mr(self):
        self.mr = self.label_output.text()
        if self.mr == '0':
            self.mr = self.label_output.text()[1:]
        self.label_output.setText(f'{self.mr}{self.ans_output}')

    def m_plus(self):
        self.output = float(self.ans_output) + float(self.label_output.text())
        self.ans_output = str(self.output)
        self.label_output.setText(self.ans_output)

    def m_minus(self):
        self.output = float(self.ans_output) - float(self.label_output.text())
        self.ans_output = str(self.output)
        self.label_output.setText(self.ans_output)


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
