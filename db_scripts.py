import sqlite3
db_name = 'quiz.sqlite'
conn = None
cursor = None

def cheack_answer(id,answer):
    qwery = '''SELECT question.answer 
            FROM quiz_content, question 
            WHERE quiz_content.id = ? 
            AND quiz_content.question_id = question.id'''
    open()
    cursor.execute(qwery,(id,))
    result = cursor.fetchone()
    close()
    if result is None:
        return False
    else:
        if result[0] == answer:
            return True
        else:False
def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    ''' видаляє всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

#Функція призначена для створення таблиць та опису зв'язків між ними
def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS quiz(
       id INTEGER PRIMARY KEY,
       name VARCHAR
       )''')
    
    do('''CREATE TABLE IF NOT EXISTS question(
       id INTEGER PRIMARY KEY,
       question VARCHAR,
       answer VARCHAR,
       wrong1 VARCHAR,
       wrong2 VARCHAR,
       wrong3 VARCHAR
       )''')
    do('''CREATE TABLE IF NOT EXISTS quiz_content(
       id INTEGER PRIMARY KEY,
       quiz_id INTEGER,
       question_id INTEGER,
       FOREIGN KEY (quiz_id) REFERENCES quiz (id),
       FOREIGN KEY (question_id) REFERENCES question (id)
       )''')

    close()


#Заповнення інформацією таблиці question (список питань)
def add_questions():
    questions = [
        (' Як називається стенд Джотаро Куджо?', 'Star Platinum', 'Crazy Diamond', 'The World', 'Killer Queen'),
        ('Який стенд має здатність зупиняти час?', 'The World', 'Silver Chariot', 'Hermit Purple', 'Stone Free'),
        ('Як виглядає стенд Йошикаге Кіри?', 'Killer Queen', 'King Crimson', 'Made in Heaven', "Heaven's Door"),
        ('Яка здатність стенду Gold Experience Requiem?', "Скасовувати дії ворога до нуля?", "Управляти часом", "Контролювати душі", "Зупиняти рухи"),
        ('Який стенд належить Джозефу Джостару?', 'Hermit Purple', 'Anubis', 'Spice Girl,', 'White Album'),
        ('Що є головною особливістю стенду King Crimson?', ' Видалення часу', 'Створення копій', 'Лікування ран', 'Управління гравітацією'),
        ('Який стенд використовує Емеральд Сплеш?', 'Hierophant Green', 'Sticky Fingers', 'Magician’s Red', 'Tusk'),
        ('Хто володіє стендом Stone Free', 'Джолін Куджо', 'Джоске Хігашіката', 'Бруно Буччелаті', 'Діо Брандо'),
        ('Як називається стенд Гвідo Місти?', 'Sex Pistols', 'Moody Blues', 'Purple Haze', ' Weather Report'),
        ('Який стенд має здатність перетворювати предмети в інші матеріали?', 'Gold Experience', 'Beach Bo', 'Metallica', 'Soft & Wet'),
        ('Як називається фінальний стенд Енріко Пуччі?', 'Made in Heaven', 'Dirty Deeds Done Dirt Cheap', 'Cream', 'Scary Monsters'),
        ('Який стенд перетворився на реквієм завдяки стрілі?', 'Gold Experience', 'Killer Queen', 'King Crimson', 'The World'),
        ('Що є основною здатністю Gold Experience Requiem?', 'Скасовувати дії до нуля', 'Контролювати гравітацію', 'Подорожувати у часі', 'Зупиняти час'),
        ('Хто активував реквієм Gold Experience?', 'Джорно Джованна', 'Діо Брандо', 'Полнарефф', 'Бруно Буччелаті'),
        ('Який стенд володіє здатністю маніпуляції душами?', 'Chariot Requiem', 'The World Over Heaven', 'Silver Chariot', 'Crazy Diamond'),
        ('Що потрібно зробити, щоб зупинити Chariot Requiem?', 'Знищити стрілу', 'Зупинити час', 'Атакувати стенд власника', 'Використати інший реквієм'),
        ('Хто є власником Chariot Requiem?', "Жан-П'єр Полнарефф", 'Діаволо', 'Енріко Пуччі', 'Йошикаге Кіра'),
        ('Що викликає ефект Chariot Requiem?', 'Зміну душ між тілами', 'Повернення до життя', 'Параліч ворогів', 'Вибухову хвилю'),
        ('Що означає стан "нескінченна смерть" від Gold Experience Requiem?', 'Ворог вічно помирає у різних реальностях', 'Ворог залишається паралізованим', 'Ворог потрапляє у безмежну темряву', 'Ворог не може рухатись у часі'),
        ('Який стенд володіє здатністю видаляти час?', 'King Crimson', 'Made in Heaven', 'The World', 'Dirty Deeds Done Dirt Cheap'),
        ('Що є головною рисою стріли реквієму?', 'Активація нової форми стенду', 'Давання безсмертя', 'Контроль часу', 'Руйнування душ'),
        ('Хто є основним противником, якого переміг Gold Experience Requiem?', 'Діаволо', 'Йошикаге Кіра', 'Енріко Пуччі', 'Діо Брандо'),
        ("Хто з персонажів отримав стенд з назвою Requiem у JoJo's Bizarre Adventure?", "Джорно Джованна", "Джотаро Куджо", "Діо Брандо", "Джозеф Джостар"),
        ("Який стенд отримав форму Requiem у JoJo's Bizarre Adventure?", "Gold Experience", "Star Platinum", "Crazy Diamond", "The World"),
        ('Який блок потрібно добувати, щоб отримати алмази?', 'Алмазна руда', 'Лазуритна руда', 'Залізна руда', 'Мідна руда'),
        ('Яке зачарування допомагає отримати більше алмазів з одного блоку?', 'Щасливий видобуток', 'Шовковий дотик', 'Ефективність', 'Нерушимість'),
        ('Який рівень освітлення найкраще підходить для видобутку алмазів?', 'Будь-який рівень освітлення', 'Тільки повна темрява', 'Тільки під сонячним світлом', 'Тільки під лампами'),
        ('Чи можна знайти алмази у сундуках у скарбницях?', 'Так', 'Ні', 'Тільки у нижньому світі', 'Тільки у джунглях'),
        ('Яке зачарування допомагає не знищити алмази при видобутку?', 'Шовковий дотик', 'Щасливий видобуток', 'Ефективність', 'Захист'),
        ('Де ще можна знайти алмази, крім підземель?', 'У скарбницях і міських кораблях Енду', 'У джунглях', 'У пустельних колодязях', 'У сніжних рівнинах'),
        ('Як алмази виглядають у природі?', 'Блакитний блок у породі', 'Червоний блок у породі', 'Чорний блок у породі', 'Зелений блок у породі'),
        ('Який тип кирки дозволяє найшвидше копати до алмазів?', 'Незерітова кирка', 'Дерев’яна кирка', 'Кам’яна кирка', 'Золота кирка'),
        ('Що найкраще робити, щоб уникнути лави під час видобутку алмазів?', 'Рити тунелі обережно і тримати відро з водою', 'Використовувати меч', 'Будувати укриття', 'Копати тільки вночі'),
        ('Який режим гри дозволяє легко отримати алмази?', 'Творчий режим', 'Виживання', 'Хардкор', 'Пригодницький режим'),
        ("Яка глибина вважається найкращою для видобутку алмазів у Minecraft?" , "-59", "12", "0", "-30"),
        ("Який інструмент потрібен для видобутку алмазів у Minecraft?" , "Залізна кирка", "Кам'яна кирка", "Дерев'яна кирка", "Золотий меч")
        ]
    open()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close() 


#Заповнення інформацією таблиці quiz (опис вікторин)
def add_quiz():
    quizes = [
        ('стенди в дж', ),
        ('Хто отримав реквіем?', ),
        ('як добути алмази Minecraft', )]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()


#Вказуємо, до якої вікторини ставиться кожне запитання
def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)"
    #answer = input("Додати зв'язок? (y/n):")
    # while answer != 'n':
    #     quiz_id = int(input("id вікторини:"))
    #     question_id = int(input("id запитання:"))
    #     cursor.execute(query, [quiz_id, question_id])
    #     conn.commit()
    #     answer = input("Додати зв'язок? (y/n):")
    quid = 1
    for quiz in range(1,4):
        for wer in range(1,13):
            cursor.execute(query, [quiz, quid])
            quid += 1
            conn.commit()    
    close()


#Функція, яка повертатиме питання із заданої вікторини, що йде за питанням із заданим id
def get_question_after(question_id = 0, quiz_id=1):
    open()
    query='''
        SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
        FROM quiz_content, question
        WHERE quiz_content.question_id == question.id
        AND quiz_content.id > (?) AND  quiz_content.quiz_id == (?)
        ORDER BY quiz_content.id
    '''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result


def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()


def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')
def get_quizes():
    open()
    cursor.execute('SELECT * FROM quiz ORDER BY id')
    resalt = cursor.fetchall()
    close()
    return resalt
def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    add_links()
    show_tables()
    # Виведення в консоль питання з id=3, id вікторини = 1
    #print(get_question_after(3, 1))

if __name__ == "__main__":
    main()
