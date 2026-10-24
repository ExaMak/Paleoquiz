import tkinter as tk
questions = [
    {
        'question': 'Какой из этих архозавров не обитал в мелу?',
        'answers': ['Паказух', 'Гремлин', 'Телеозавр', 'Хатцегоптерикс'],
        'correct': 3
    },
    {
        'question': 'К какому инфраотряду относится гремлин?',
        'answers': ['Цератопсы', 'Стегозавры', 'Анкилозавры', 'Орнитоподы'],
        'correct': 1
    },
    {
        'question': 'К какой группе рыб относится биргерия?',
        'answers': ['Лопастепёрые', 'Хрящевые', 'Акантоды', 'Лучепёрые'],
        'correct': 4
    },
    {
        'question': 'Какое из этих растений характерно для карбона?',
        'answers': ['Плевромейя', 'Сигиллярия', 'Гинкго', 'Археоптерис'],
        'correct': 2
    },
    {
        'question': 'Какая из этих групп пережила пермское вымирание?',
        'answers': ['Акантоды', 'Ксенокантообразные', 'Эвриптериды', 'Диноцефалы'],
        'correct': 2
    },
    {
        'question': 'На сколько отделов подразделялся каменноугольный период?',
        'answers': ['На 3', 'На 5', 'На 2', 'Не подразделяется'],
        'correct': 3
    },
    {
        'question': 'Кто такой коллидозух?',
        'answers': ['Амфибия', 'Динозавр', 'Синапсид', 'Проколофон'],
        'correct': 1
    },
    {
        'question': 'Какое из этих событий характерно для протерозоя?',
        'answers': ['Появление хордовых', 'Образование суперконтинента Родинии', 'Распад суперконтинента Ваальбры', 'Кембрийский взрыв'],
        'correct': 2
    },
    {
        'question': 'Кто из перечисленных плезиозавров не относится к плиозавроидам?',
        'answers': ['Ромалеозавр', 'Макроплата', 'Тринакромерум', 'Талассиодракон'],
        'correct': 3
    },
    {
        'question': 'Что такое палеоценоз?',
        'answers': ['Это место обитания всего 1 вымершего животного, растения и гриба', 'Это совокупность вымерших организмов, живущих в общей экосиситеме', 'Это единственное место находки какого-либо вымершего организма', 'Название вымершей группы иглокожих'],
        'correct': 2
    },
    {
        'question': 'Кто такие ругозы?',
        'answers': ['Аммониты', 'Губки', 'Водоросли', 'Кораллы'],
        'correct': 4
    },
    {
        'question': 'Какое из этих событий не характерно для палеогена?',
        'answers': ['Появление китообразных', 'Вымирание хористодер', 'Термический максимум в кайнозое', 'Вымирание последней группы нептичьих динозавров'],
        'correct': 2
    },
]
c_questions = 0
score=0
window =tk.Tk()
def answer(x):
    global c_questions
    global score
    if x == (questions[c_questions]['correct']):
        r.config(text='Верно', font='Arial', padx=100, pady=20, bg='green')
        score=score+1
    else:
        r.config(text='Неверно', font='Arial', padx=100, pady=20, bg='red')
    c_questions = c_questions + 1
    if c_questions<len(questions):
        l.config(text=questions[c_questions]['question'])
        b1.config(text=questions[c_questions]['answers'][0])
        b2.config(text=questions[c_questions]['answers'][1])
        b3.config(text=questions[c_questions]['answers'][2])
        b4.config(text=questions[c_questions]['answers'][3])
    else:
        l.config(text='Викторина закончена!')
        r.config(text=str(score)+'/'+str(len(questions)))
        b1.config(text='-')
        b2.config(text='-')
        b3.config(text='-')
        b4.config(text='-')
l = tk.Label(text=questions[c_questions]['question'], font='Arial', padx=100, pady=20)
l.pack()
r = tk.Label(text='')
r.pack(side='bottom')
f1 = tk.Frame(window)
f1.pack(side='left')
f2 = tk.Frame(window)
f2.pack(side='right')
b1 = tk.Button(f1, text=questions[c_questions]['answers'][0], font='Arial', padx=100, pady=20, command=lambda:answer(1))
b1.pack()
b2 = tk.Button(f2, text=questions[c_questions]['answers'][1], font='Arial', padx=100, pady=20, command=lambda:answer(2))
b2.pack()
b3 = tk.Button(f1, text=questions[c_questions]['answers'][2], font='Arial', padx=100, pady=20, command=lambda:answer(3))
b3.pack()
b4 = tk.Button(f2, text=questions[c_questions]['answers'][3], font='Arial', padx=100, pady=20, command=lambda:answer(4))
b4.pack()
window.mainloop()