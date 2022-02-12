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
                    <img src="{url_for('static', filename='img/mars.png')}" >
                    <p></p>
                    <p><strong> марс пригоден для жизни !!! </strong> </p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" >
                    <p></p>
                    <div class="alert alert-primary" role="alert">
                      колонизация марса будет
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Марс достижимая планета
                    </div>
                    <div class="alert alert-success" role="alert">
                    земли марса будут покорены
                    </div>
                  </body>
                </html>'''
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
