# Куда пойти — Москва глазами Артёма

[Django](https://www.djangoproject.com/) сайт, представляющий собой карту с интересными местами Москвы.

Фронтенд сайта взят [ЗДЕСЬ](https://github.com/devmanorg/where-to-go-frontend/).

Тестовые данные для наполнения взяты [ЗДЕСЬ](https://github.com/devmanorg/where-to-go-places).

Ознакомиться с функционалом сайта, вы можете, перейдя на опубликованную [действующую версию сайта](https://riminprog.pythonanywhere.com/).

## Как это работает

Находясь на [демонстрационной версии сайта](https://riminprog.pythonanywhere.com/) нажимайте отмеченные на карте точки, чтобы увидеть подробную информацию об отмеченном месте. При нажатии на точку, в правом углу откроется всплывающее окно с названием, картинкой и подробной информацией о выбранном объекте. Также на большинстве объектов, при наличии фото, будет доступен слайдер изображений выбранного объекта.

Для добавления новых, редактирования или удаления существующих объектов перейдите в [административную зону сайта](https://riminprog.pythonanywhere.com/admin) (ЛОГИН: `guest`, ПАРОЛЬ: `12345678Aa`). Для создания нового объекта на карте в первую очередь добавьте объект `Place`. для этого заполните все необходимые поля на странице добавления объекта:
* `Название места` - данное название будет выведено поверх маркера объекта места на карте, а также отображено в заголовке подробной карточки объекта.
* `Короткое описание` - описание выводимое над слайдером фотографий в подробной карточке объекта.
* `Длинное описание` - описание выводимое под слайдером фотографий в подробной карточке объекта.
* `Широта` - географическая широта. Указывать в формате float. Пример указания северной широты Москвы: 55.7522
* `Долгота` - географическая долгота. Указывать в формате float. Пример указания восточной долготы Москвы: 37.6156

 После того как объект `Place` будет создан, при обновлении сайта, у вас на карте появится новый маркер с только что добавленным местом. При клике на него, будет открываться карточка с подробным описанием объекта. Для того чтобы добавить к объекту картинки, добавьте объект `Image`, в котором заполните следующие поля:
 * `Изображение` - выберите изображение для загрузки
 * `Порядковый номер` - проставьте любое целое положительное число от 1. По указанному номеру изображения будут упорядочиваться при выводе в слайдере сайта. Изображение под номером 1 будет выведено в заголовке подробной информации карточки объекта.
 * `К какому месту относится изображение` - выберите созданный ранее объект `Place`, чтобы привязать к нему созданное изображение.

 Для упрощения наполнения мест изображениями, можете подгружать новые изображения со страницы редактирования `Place`. Прокрутите вниз страницы редактирования и при нажатии кнопки `Добавить еще Image`, добавляйте новые изображения напрямую со страницы объекта. Для изменения порядка вывода изображений, перетаскивайте изображения в нужном порядке, кликая и удерживая по серой зоне, расоложенной слева от загруженного изображения.

## Запуск локальной версии сайта

- Для запуска сайта вам понадобится Python третьей версии.
- Скачайте репозиторий с кодом и прилегающими файлами.
- Установите зависимости командой `pip install -r requirements.txt`.
- Создайте базу данных SQLite командой `python3 manage.py migrate`.
- Запустите разработческий сервер командой `python3 manage.py runserver`.
- В браузере перейдите на сайт по [адресу](http://127.0.0.1:8000/).

В случае успешного запуска, в консоль будет выведен ряд следующих уведомлений:
```
System check identified no issues (0 silenced).
September 29, 2021 - 12:00:38
Django version 3.2.7, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 4 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Наполнение сайта

Каталог `media` корневого раздела проекта, содержит все загружаемые изображения для локаций на карте.

Каталог `static` корневого раздела проекта, содержат компоненты обеспечивающих работу фронтенда сайта.

Каталог `template` корневого раздела проекта, содержат шаблон главной html страницы сайта.

Тестовые данные для сайта получены по ссылкам на json файлы, расположенные [ЗДЕСЬ](https://github.com/devmanorg/where-to-go-places). Для более быстрого наполнения сайта создана кастомная команда для `manage.py`. Таким образом при вызове `python3 manage.py load_place PLACE_URL` и передаче аргумента `PLACE_URL`, содержащего данные json [как в данном примере](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json), происходит автоматическое наполнение базы данных и на карту добавляются новые места.

Ниже пример структуры json файла, который должен быть получен в качестве ответа при указании в качестве аргумента ссылки `PLACE_URL`, при вызове кастомной команды `load_place`:
```
{
    "title": "НАЗВАНИЕ",
    "imgs": [
        "ССЫЛКА_НА_ИЗОБРАЖЕНИЕ_1",
        "ССЫЛКА_НА_ИЗОБРАЖЕНИЕ_2",
        ...
    ],
    "description_short": "КОРОТКОЕ_ОПИСАНИЕ_МЕСТА",
    "description_long": "ДЛИННОЕ_HTML_ОПИСАНИЕ_МЕСТА",
    "coordinates": {
        "lng": "ДОЛГОТА",
        "lat": "ШИРОТА"
    }
}
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
