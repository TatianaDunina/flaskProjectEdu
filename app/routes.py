from app import app


@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is an informational page.'

@app.route('/calc/<a>/<b>')
def calc(a, b):
    try:
        a_int = int(a)
        b_int = int(b)
        sum_num = a_int + b_int
        return f'The sum of {a_int} and {b_int} is {sum_num}'
    except ValueError:
        return 'Передаваемые параметры должны быть целыми числами'

@app.route('/reverse/')
@app.route('/reverse/<word>')
def reverse(word=None):
    if not word:
        return 'Передаваемая строка должна содержать хотя бы один символ'
    return f'{word[::-1]}'

@app.route('/user/<name>/<int:age>')
def show_user(name, age):
    if age <= 0:
        return 'Передаваемый параметр "возраст" должен быть больше 0'
    return f'Hello, {name}. You are {age} years old.'