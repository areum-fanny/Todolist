from flask import Flask, render_template, request, redirect, url_for
import datetime, sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=["GET","POST"])
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        addTask(request.form['todo'],request.form['deadline'])
    tasks = conn.execute('SELECT * FROM tasks WHERE status = ?',(0,)).fetchall()
    conn.close()
    dict_tasks = {}
    for task in tasks:
        dt_string = task['deadline']
        format = "%Y-%m-%dT%H:%M"
        dt_object = datetime.datetime.strptime(dt_string, format)
        dict_tasks[task['id']] = [task['task'],dt_object]
    dict2 = dict(sorted(dict_tasks.items(),key=lambda x:x[1][1]))
    print(dict2.items())
    return render_template('index.html',tasks=dict2.items())

@app.route('/<int:id>/delete', methods=('GET','POST'))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
@app.route('/<int:id>/deletecompletedtask', methods=('GET','POST'))
def deletecompletedtask(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('completedtasks'))

@app.route('/completedtasks', methods=('GET','POST'))
def completedtasks():
    if request.method == 'POST':
        addTask(request.form['todo'],request.form['deadline'])
        return redirect(url_for('index'))
    else:
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM tasks WHERE status = ?',(1,)).fetchall()
        conn.close()
        dict_tasks = {}
        for task in tasks:
            dt_string = task['deadline']
            format = "%Y-%m-%dT%H:%M"
            dt_object = datetime.datetime.strptime(dt_string, format)
            dict_tasks[task['id']] = [task['task'],dt_object]
        dict2 = dict(sorted(dict_tasks.items(),key=lambda x:x[1][1]))
        print(dict2.items())
        return render_template('displaycompletedtasks.html',tasks=dict2.items())

def addTask(task,deadline):
    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (task, deadline) VALUES (?, ?)",(task, deadline))
    conn.commit()
    conn.close()
    

@app.route('/<int:id>/completetask', methods=('GET','POST'))
def completetask(id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks set status = ? WHERE id = ?', (1,id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))