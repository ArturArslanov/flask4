from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return '<strong>Миссия Колонизация Марса</strong>'


@app.route('/promotion')
def mission():
    text = ["Человечество вырастает из детства.",
            "Человечеству мала одна планета. ",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!"]
    for i in range(len(text)):
        text[i] = f'<strong>{text[i]}<br>'
    return ' '.join(text)


@app.route('/index')
def index():
    return '<strong>И на Марсе будут яблони цвести!</strong>'


@app.route('/image_mars')
def show_png():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет Марс!</title>
                  </head>
                  <body>
                  <h1> Жди нас, Марс! </h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    <p></p>
                    <p> марс пригоден для жизни </p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
