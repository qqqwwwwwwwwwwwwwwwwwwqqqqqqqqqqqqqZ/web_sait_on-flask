# Тут буде код веб-програми
from flask import Flask,redirect,url_for,session,request,render_template
from random import randint,shuffle
from db_scripts import get_question_after,get_quizes,cheack_answer
import os

def start_quiz(id):
    session['quiz']=id
    session['last_question']=0
    session['corect_answers']=0
    session['total']=0
def quiz_form():
    quiz_list =  get_quizes()
    return render_template('start.html',quiz_list = quiz_list)
def index():
    if request.method == 'GET':
        start_quiz(-1)
        return quiz_form()
    else:
        id = request.form.get('quiz')
        start_quiz(id)
        return redirect(url_for('test'))
def queshen_form(qesh):
    answers =[qesh[2],qesh[3],qesh[4],qesh[5]]
    shuffle(answers)
    return render_template("test.html",qeshuon = qesh[1],id = qesh[0],answers = answers)
def save_answers():
    answer1 = request.form.get('ans_text')
    id = request.form.get('q_id')
    session['last_question'] = id
    session['total'] += 1 
    if cheack_answer(id,answer1):
        session["corect_answers"]+=1
def test():
    if request.method=='POST':
        save_answers()
    new_question = get_question_after(session['last_question'],session['quiz'])
    if new_question is None or len(new_question) == 0:
        return redirect(url_for('result'))
    else:
        return queshen_form(new_question)
def result():
    return render_template('result.html',corect = session['corect_answers'],total = session['total'])
folder = os.getcwd()
app = Flask(__name__,template_folder= folder,static_folder= folder)
app.add_url_rule('/','index',index,methods = ['get','post'])
app.add_url_rule('/test','test',test,methods = ['get','post'])
app.add_url_rule('/result','result',result)
app.config['SECRET_KEY']='aboboba'
if __name__ == '__main__':
    app.run()