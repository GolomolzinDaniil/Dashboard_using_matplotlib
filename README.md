# Создание Дашборда на основе синтетических данных

## Что делает проект
Этот проект предоставляет возможность создания Дашборда на основе синтетических данных: 

**Dashboard_using_matplotlib.py**
  - создает сетку подграфиков
  - генерируем синтетические данные
  - на основе данных строит соответсвующий график
  - объединяет их в сетку и сохраняет в формате *.png
---

## Файлы
- `Dashboard_using_matplotlib.py` – создание Дашборда
- `requirements.txt` - необходимые библиотеки для работы 

## Установка
Установите необходимые Python-библиотеки:  
```bash
pip install -r requirements.txt
```

## Пользование

Обработка текста:

```bash
python Dashboard_using_matplotlib.py
```

Обрабатывать с использованием определенного названия файла:
```bash
python Dashboard_using_matplotlib.py --output_img result.jpg
```

## Пример выходящих данных:


Выходящий файл (`result.jpg`):

<div align="center">
  <img src="https://github.com/GolomolzinDaniil/Dashboard_using_matplotlib/blob/main/images/example.jpg?raw=true" alt="Пример дашборда" width="600">
</div>

## Общие требования

- Python 3.6+
