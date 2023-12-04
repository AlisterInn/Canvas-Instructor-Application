from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [{'id': 1, 'name': 'Student 1'}, {'id': 2, 'name': 'Student 2'}]
assignments = [{'assi no': 1, 'title': 'Assignment 1'}, {'assi no': 2, 'title': 'Assignment 2'}]
tests = [{'test no': 1, 'title': 'Test 1'}, {'test no': 2, 'title': 'Test 2'}]

@app.route('/')
def index():
    return render_template("index.html", students=students, assignments=assignments, tests=tests)

@app.route('/add', methods=['POST'])
def add():
    if request.form['type'] == "student":
        students.append({'id': len(students) + 1, 'name': request.form['name']})
    elif request.form['type'] == "assignment":
        assignments.append({'assi no': len(assignments) + 1, 'title': request.form['title']})
    elif request.form['type'] == "test":
        tests.append({'test no': len(tests) + 1, 'title': request.form['title']})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
