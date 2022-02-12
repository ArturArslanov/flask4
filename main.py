from pprint import pprint

from flask import Flask, url_for, request

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


@app.route('/choice/<string:planet>')
def any_(planet: str):
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
                    <h1 id=redh>Жди нас, {planet}!</h1>
                    <h1> {planet} не может остаться пустой планетой </h1>
                    <p></p>
                    <div class="alert alert-primary" role="alert">
                      колонизация {planet} будет  
                    </div>
                    <div class="alert alert-warning" role="alert">
                      {planet} наша вторая земля
                    </div>
                    <div class="alert alert-info" role="alert">
                     сделаем {planet} пригодной для жизни
                    </div>
                    <div class="alert alert-light" role="alert">
                      {planet} очень близок
                    </div>
                    <div class="alert alert-dark" role="alert">
                      присоединяйся
                    </div>
                    </div>
                  </body>
                </html>'''


@app.route('/form', methods=['POST', 'GET'])
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
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
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1> <center> Анкета  претендента</h1>
                            <p id="block1">на колонизатора </p>
                            <div>
                                <form class="login_form" method="post">
                                <input class="form-control form-control-lg" type="text" aria-label=".form-control-lg example"
                                    placeholder="введите ваше фамилию">
                                <p> фамилия </p>
                                    <input class="form-control form-control-lg" type="text" aria-label=".form-control-lg example"
                                    placeholder="введите ваше имя">
                                    <p> имя</p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                     placeholder="Введите адрес почты" name="email">
                                    <p> почта </p>
                                    <select class="form-select" aria-label="Default select example">
                                      <option value="1">начальное</option>
                                      <option value="2">среднее</option>
                                      <option value="3">высшее</option>
                                    </select>
                                    <p> образование </p>
                                                          <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            инженер-исследователь
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            пилот
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            строитель
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            экзобиолог
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            врач
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            климатолог
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            специалист по радиационной защите
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            астрогеолог
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            гляциолог
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            инженер жизнеобеспечения
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            метеоролог
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            оператор марсохода
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            киберинженер
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            штурман
                                          </label>
                                        </div>
                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                          <label class="form-check-label" for="flexCheckDefault">
                                            пилот дронов
                                          </label>
                                        </div>
                                        <p> пол </p>
                                        <div class="form-check">
                                        
                                          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                          <label class="form-check-label" for="flexRadioDefault1">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
                                          <label class="form-check-label" for="flexRadioDefault2">
                                            Женский
                                          </label>
                                        </div>
                                        <div class="mb-3">
                                          <label for="exampleFormControlTextarea1" class="form-label">какая у вас 
                                          мотивация?</label>
                                          <textarea class="form-control" id="exampleFormControlTextarea1" 
                                          rows="4"></textarea>
                                        </div>
                                    <div class="form-check form-switch">
                                      <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                                      <label class="form-check-label" for="flexSwitchCheckDefault">готовы ли вы остаться на Марск?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


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
                    <h1 id=redh>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" >
                    <p></p>
                    <div class="alert alert-primary" role="alert">
                      колонизация марса будет  
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Марс наша вторая земля
                    </div>
                    <div class="alert alert-info" role="alert">
                     сделаем планету пригодной для жизни
                    </div>
                    <div class="alert alert-light" role="alert">
                      марс очень близок
                    </div>
                    <div class="alert alert-dark" role="alert">
                      присоединяйся
                    </div>
                    </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def show_results(nickname, level, rating):
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
                        <title>результаты</title>
                      </head>
                      <body>
                        <h1 id=redh>результаты отбора</h1>
                        <h1 id=bluep> претендент на участие {nickname} </h1>
                        <div class="alert alert-warning" role="alert">
                            ваш рэйтинг {level}
                        </div>
                        <div class="alert alert-info" role="alert">
                            составляет {rating}
                        </div>
                        <div class="alert alert-dark" role="alert">
                            желаем удачи
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
