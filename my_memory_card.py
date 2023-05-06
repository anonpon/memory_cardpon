from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600,400)

text = QLabel('Какой национальности не существует')
button = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
vline1.addWidget(rbtn_1)
vline1.addWidget(rbtn_2)
vline2.addWidget(rbtn_3)
vline2.addWidget(rbtn_4)
hline = QHBoxLayout()
hline.addLayout(vline1)
hline.addLayout(vline2)
RadioGroupBox.setLayout(hline)
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
AnsGroupBox = QGroupBox()
correct = QLabel('Правильно или неправльно')
r_answer = QLabel('Правильный ответ')
vline3 = QVBoxLayout()
vline3.addWidget(correct)
vline3.addWidget(r_answer)
AnsGroupBox.setLayout(vline3)
AnsGroupBox.hide()
v = QVBoxLayout()
v.addWidget(text)

v.addWidget(RadioGroupBox)
v.addWidget(AnsGroupBox)
v.addWidget(button)

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

main_win.setLayout(v)
main_win.cur_question = -1 
def Show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
def Show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]        
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    text.setText(q.question)
    r_answer.setText(q.right_answer)
    Show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1 
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
    print('Статистика:')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('рейтинг:', main_win.score / main_win.total * 100 , '%')
    
def next_question():
    main_win.total +=1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    print('Статистика:')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
def show_correct(res):
    correct.setText(res)
    Show_result()
questions_list = []
q = Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Польский', 'Язык бебры')
questions_list.append(q)
questions_list.append(Question('Какая фамилия у Пушкина?', 'Пушкин', 'Лермонтов', 'мшкфредов', 'Гагарин'))
questions_list.append(Question('Из точки А в точку Б поехала твоя кукуха со скоростью света, вопрос: кто такая света?', 'Пушкин', 'ааа мшк фреде', 'сестра моя', 'Польша'))
questions_list.append(Question('Играли короче еврей, русский и немец в прятки....', 'еврей плохо спрятался, и его спалили', 'а потом перестали играть', 'немца расстреляли', 'Узбекистан'))
questions_list.append(Question('Серёжа, дело в шляпе...', 'Нюхай бебру', 'Какой Серёжа? Какая шляпа?', 'Дед выпей таблетки', 'а он говорит: попит'))
questions_list.append(Question('Сколько будет 2+2*2?', 'да', 'нет', 'почему', 'про мать лишнее было'))
questions_list.append(Question('−•− •− −•−   −−•• −−− •−− ••− −   −−− •−•• • −−• •− ', '−−− •−•• • −−• ', '•−−• −−− •−•• •• −• •− ', '−••• −−− •−• •• ••• ', '•−−• −−− •−•• −••− −−−− •− '))
questions_list.append(Question('Продам тапок', 'где купить', 'какая цена', 'кирпич', 'Польша'))
questions_list.append(Question('Продам Вадима алгоритмика', 'Куплю за ответы', 'Куплю за попит', 'Куплю за лампочку', 'Олег'))
questions_list.append(Question('Христос воскрес', 'Ок', 'спрингтруп?', 'ааа мшкм фреде', 'пон'))
questions_list.append(Question('Как зовут Александра', 'Александр', 'Александра', 'Олег', 'Противотанковая самоходная артиллерийская установка «Мардер» III Ausf. М (Sd.Kfz.138). Чехословакия/Германия'))
button.clicked.connect(click_ok)
main_win.score = 0
main_win.total = 0
next_question()
main_win.show()
app.exec()
