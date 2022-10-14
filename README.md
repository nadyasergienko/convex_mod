---
date: 
author:
- Н. А. Сергиенко
title: Модификация проекта «Выпуклая оболочка»
---

### Постановка задачи

Необходимо модифицировать код эталонного проекта таким образом, чтобы вычислялась 
и печаталась следующая характеристика выпуклой оболочки: сумма углов, под которыми рёбра выпуклой оболочки
пересекают заданный отрезок. Отрезок задаётся двумя его концами — различными точками плоскости. 
Возвращаемое значение: сумма углов в градусах.

### Алгоритм решения

Задача модификации сводится к решению задачи о пересечении отрезков с последующим вычислением угла между ними.
На плоскости эта задача решается с помощью векторного произведения. Отрезоки `AB` и `CD` пересекаются, если концы
каждого из них лежат в разных полуплоскотях относительно другого отрезка. Чтобы узнать, лежат ли точки A и B в
разных полуплоскостях относительно `CD`, я перемножаю векторно $\vec {CA}$ и $\vec {CD}$, а также $\vec {CB}$ и
$\vec {CD}$. Если компоненты z получившихся векторов имеют разные знаки (или хотя бы одна из них равна нулю), то
условие выполняется. Аналогично для точек C, D и отрезка `AB`. Данную проверку осуществляет статический метод 
`crossing` класса `R2Point`. Он возвращает угол между отрезками в случае их пересечения, иначе ноль. Для
вычисления вектороного произведения и угла между отрезками были созданы методы `vect` и `angle` соответственно.
Решение является индуктивным. При добавлении новой точки из суммы углов вычитаются значения, возвращаемые
методом `crossing` для удаляемых ребер (освещенных из точки) и добавляются значения, соответствующие новым ребрам.

### Краткий комментарий к решению

- Ключевое понятие проекта: *освещённость ребра из точки* 
- Вспомогательные классы:
    - `R2Point` — точка на плоскости
    - `Deq` — контейнер дек (double ended queue)
- Основные классы:
    - `Figure` — «абстрактная» фигура
    - `Void` — нульугольник
    - `Point` — одноугольник
    - `Segment` — двуугольник
    - `Polygon` — многоугольник
- Файлы проекта:
    - `README.md` — данный файл
    - `README.html` — полученный из файла `README.md` `html`-файл
    - `r2point.py` — реализация класса `R2Point`
    - `deq.py` —  реализация класса `Deq`
    - `convex.py` — реализация основных классов
    - `run_convex.py` — файл запуска
    - `tk_drawer.py` — интерфейс к графической библиотеке
    - `run_tk_convex.py` — файл запуска с использованием графики
    - `tests/test_r2point.py` — тесты к классу `R2Point`
    - `tests/test_convex.py` — тесты к основным классам
    - `tests/test_modification.py` — тесты, иллюстрирующие правильность выполнения задачи модификации

Файлы `run_tk_convex.py` и `run_tk_convex.py` являются исполняемыми (они имеют
бит `x`), в первой строке каждого из них используется [шебанг](https://ru.wikipedia.org/wiki/%D0%A8%D0%B5%D0%B1%D0%B0%D0%BD%D0%B3_(Unix)) и команда `env` с
опцией (ключом) `-S`. Это обеспечивает передачу интерпретатору языка Python
опции (ключа) `-B`, отменяющего генерацию `pyc`-файлов в директории
`__pycache__`.

### Соблюдение соглашений о стиле программного кода

Для языка Python существуют [соглашения о стиле
кода](https://www.python.org/dev/peps/pep-0008/). Они являются лишь
рекомендациями (интерпретатор игнорирует их нарушение), но основную их
часть при написании программ целесообразно соблюдать. Существует простой
способ проверить соблюдение считающегося правильным
стиля записи кода с помощью утилиты (программы) `pycodestyle`. Утилита
`yapf` позволяет даже изменить код в соответствии с этими соглашениями.

Команда 

    pycodestyle r2point.py

позволяет, например, проверить соблюдение стиля для файла `r2point.py`.
С помощью очень мощной и часто используемой утилиты `find` проверить
корректность стиля всех файлов проекта можно так:

    find . -name '*.py' -exec pycodestyle {} \;

Эта команда находит все файлы с расширением `py` и запускает программу
`pycodestyle` последовательно для каждого из них.

### Запуск тестов

Уже известная нам команда (см. материал, посвящённый тестированию программ)

    python -B -m pytest -p no:cacheprovider tests

запускает pytest, выполняя все начинающиеся с `test` методы классов,
имена которых начинаются с `Test`, содержащиеся во всех файлах `test_*.py`
директории `tests`.

### Запуск программы

`./run_convex.py`

### Запуск программы с графическим интерфейсом

`./run_tk_convex.py`