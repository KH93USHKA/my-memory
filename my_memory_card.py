
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QGroupBox, QLabel, QRadioButton, QPushButton, QHBoxLayout, QVBoxLayout, QButtonGroup
from random import shuffle, randint

def show_result():
    group_box.hide()
    ans_groupbox.show()
    main_btn.setText('Следующий вопрос')

def show_question():
    group_box.show()
    ans_groupbox.hide()
    main_btn.setText('Ответить')
    RadioGroupBox.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroupBox.setExclusive(True)


def next_question():
    print('Всего вопросов', main_win.count, '\nверные:', main_win.score)
    main_win.count += 1
    cur_question = randint(0, len(questions_list) - 1)
    q1 = questions_list[cur_question]
    ask(q1)

def start_test():
    if main_btn.text() == 'Ответить':
         check_answer()
    else:
        next_question()

class Question():
    def __init__(self, question, r_answer, w_answer1, w_answer2, w_answer3):
        self.question = question
        self.r_answer = r_answer
        self.w_answer1 = w_answer1
        self.w_answer2 = w_answer2
        self.w_answer3 = w_answer3
        
        

def ask(qt: Question):
    shuffle(answers)
    answers[0].setText(qt.r_answer)
    answers[1].setText(qt.w_answer1)
    answers[2].setText(qt.w_answer2)
    answers[3].setText(qt.w_answer3)
    q.setText(qt.question)
    correct_answer.setText(qt.r_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        print('Всего вопросов', main_win.count, '\n', ' Верные:', main_win.score, 'Рейтинг:', main_win.score/main_win.count*100)
        show_correct('Верно')
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверно')

app = QApplication([])
main_win = QWidget()
main_win.count = 0
main_win.score = 0
main_win.setWindowTitle('Memory card')


q = QLabel('Какой национальности не существует?')
group_box = QGroupBox('Варианты ответов')

btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')

answers = [btn1, btn2, btn3, btn4]

RadioGroupBox = QButtonGroup()

RadioGroupBox.addButton(btn1)
RadioGroupBox.addButton(btn2)
RadioGroupBox.addButton(btn3)
RadioGroupBox.addButton(btn4)
RadioGroupBox.setExclusive(False)
btn1.setChecked(False)
btn2.setChecked(False)
btn3.setChecked(False)
btn4.setChecked(False)
RadioGroupBox.setExclusive(True)

h_layout1 = QHBoxLayout()

v_layout1 = QVBoxLayout()
v_layout2 = QVBoxLayout()

v_layout1.addWidget(btn1)
v_layout1.addWidget(btn3)

v_layout2.addWidget(btn2)
v_layout2.addWidget(btn4)

h_layout1.addLayout(v_layout1)
h_layout1.addLayout(v_layout2)

group_box.setLayout(h_layout1)

main_btn = QPushButton('Ответить')

main_layout = QVBoxLayout()

main_h_layout1 = QHBoxLayout()
main_h_layout2 = QHBoxLayout()
main_h_layout3 = QHBoxLayout()

ans_groupbox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
correct_answer = QLabel('Верный ответ')

res_layout = QVBoxLayout()
res_layout.addWidget(result, alignment=(Qt.AlignLeft|Qt.AlignTop))
res_layout.addWidget(correct_answer, alignment=Qt.AlignCenter, stretch=2)
ans_groupbox.setLayout(res_layout)

main_h_layout1.addWidget(q)
main_h_layout2.addWidget(group_box)
main_h_layout2.addWidget(ans_groupbox)
main_h_layout3.addWidget(main_btn)

ans_groupbox.hide()

main_h_layout3.addStretch(1)
main_h_layout3.addWidget(main_btn, stretch=2) 
main_h_layout3.addStretch(1)

main_layout.addLayout(main_h_layout1, stretch=2)
main_layout.addLayout(main_h_layout2, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(main_h_layout3, stretch=1)
main_layout.addStretch(1)
main_layout.setSpacing(5)

# v_layout1 = QVBoxLayout()
# v_layout2 = QVBoxLayout()

# v_layout1.addWidget(btn1)
# v_layout1.addWidget(btn3)

# v_layout2.addWidget(btn2)
# v_layout2.addWidget(btn4)

# h_layout1.addLayout(v_layout1)
# h_layout1.addLayout(v_layout2)

# group_box.setLayout(h_layout1)

# ans_groupbox = QGroupBox('Результат теста')
# result = QLabel('Правильно/Неправильно')
# correct_answer = QLabel('Верный ответ')



# main_btn = QPushButton('Ответить')
main_btn.clicked.connect(start_test)

# main_layout = QVBoxLayout()
# main_layout.addWidget(q)
# main_layout.addWidget(group_box)
# main_layout.addWidget(main_btn)

questions_list = []
questions_list.append(Question('Who?', 'You', 'I', 'We', 'He'))
questions_list.append(Question('Why?', 'Bec', 'That', 'OK', 'Idk'))


main_win.setLayout(main_layout)
main_win.show()
app.exec_()