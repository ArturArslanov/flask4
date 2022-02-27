import os
from pprint import pprint

from flask import Flask, url_for, request

app = Flask(__name__)
photography = 'img/ino.png'
photo_2 = 'img/time.png'


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


@app.route('/load_photo', methods=['POST', 'GET'])
def show_res():
    print(request.method)
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
                               <h1> <center> Загрузите фотографию</center></h1>
                               <p id="block1">для участия в комиссии </p>
                                <div class="alert alert-danger" role="alert">
                                <form method="post" enctype="multipart/form-data">
                                     приложите фотографию
                                     <div class="mb-3">
                                      <label for="formFile" class="form-label">[/?~?/]</label>
                                      <input class="form-control" type="file" id="formFile" name='aleks'>
                                    </div>
                                    <img src="{url_for('static', filename=f'{photography}')}" >
                                    <div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </div>
                                    </form>
                                </div>
                             </body>
                           </html>'''
    elif request.method == 'POST':
        g = True
        if request.files.get('aleks'):
            file = request.files['aleks']
        else:
            file = open(f'static/{photography}', 'rb')
            g = False
        with open(f'static/{photo_2}', 'wb') as f:
            f.write(file.read())
        if not g:
            file.close()
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
                                       <h1> <center> Загрузите фотографию</center></h1>
                                       <p id="block1">для участия в комиссии </p>
                                        <div class="alert alert-danger" role="alert">
                                        <form method="post" enctype="multipart/form-data">
                                             приложите фотографию
                                             <div class="mb-3">
                                              <label for="formFile" class="form-label">[/?~?/]</label>
                                              <input class="form-control" type="file" id="formFile" name='aleks'>
                                            </div>
                                            <img src="{url_for('static', filename=f'{photo_2}')}" >
                                            <div>
                                                <button type="submit" class="btn btn-primary">загрузить</button>
                                            </div>
                                            </form> 
                                        </div>
                                     </body>
                                   </html>'''


# src="{url_for('static', filename=f'{"img/mars1.png"}')}"
@app.route("/carousel")
def mars_pictures():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="style.css" crossorigin="anonymous">

                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                    <title>Пример формы</title>
                  </head>
                  <body>
                  
                    <h3 id="block1">Пейзажи Марса</h3>
                      <div id="carouselExampleControls" class="carousel slide carousel-fade" 
                      data-ride="carousel">
                      
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                            <img  src="{url_for('static', filename=f'{"img/mars1.png"}')}">
                            </div>
                            <div class="carousel-item">
                            <img  src="{url_for('static', filename=f'{"img/mars2.png"}')}" 
                            alt="Second slide">
                            </div>
                            <div class="carousel-item">
                            <img  src="{url_for('static', filename=f'{"img/mars3.png"}')}">
                            </div>
                        </div>
                        <a class="carousel-control-prev" href="#carouselExampleControls" data-slide="next">
                            <span aria-hidden="false"> 
                            поменять</span>
                        </a>
                        
                        </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
