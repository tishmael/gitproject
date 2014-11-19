__author__ = 'ishmael'

from flask import Flask

app = Flask(__name__)

@app.route('/kigali')
def index():
    return 'I am in the capital of Rwanda'

@app.route('/greeting')
def greet():
    return 'Hello John'

# @app.route('/counter/<int:value>')
# def say_number(value):
#     if value <=5:
#         if value == 1:
#             return 'Number one'
#         elif value == 2:
#             return 'Number two'
#         elif value == 3:
#             return 'Number Three'
#         elif value == 4:
#             return 'Number Four'
#         elif value == 5:
#             return 'Number Five'
#         else:
#             return 'Unknown number'


@app.route('/find/<int:value>')
def my_number(value):
    list = ['zero','one','two','three','four','five']
    if value <=5:
        return 'hello %s' % list[value]
    else:
        return 'out of range numbers'


# @app.route('/counter/<int:value>')
# def say_number(value):
#     dict = { 1:'one', 2:'two',3:'three',4:'four', 5:'five'}
#     return ' %s' % dict.get(value, 'unknown')


if __name__ == '__main__':
    app.run(port=2000, debug=True)