import matplotlib.pyplot as plt
import argparse
import random
from string import ascii_uppercase as letters


def Dashboard_using_matplotlib(output_img: str) -> None:

    ''' Создание Дашборда (линейный и столбчатый графики, гистограмма, круговая диаграмма) '''

    # нужно реализовать построение графиков для Дашборда на основе синтетических данных.
    # так как для каждого типа графиков нужны свои данные, значит я могу генерировать их как захочу

    # 1. line plot
    plt.subplot(2,2,1)
    xs = range(15)
    ys = [random.randint(0, 50) for _ in range(len(xs))]
    plt.plot(xs, ys, color="#0c5ac0")
    plt.title('Линейный график')

    # 2. bar plot
    plt.subplot(2,2,2)
    xs = list(letters[:7])
    ys = [random.randint(0, 50) for _ in range(len(xs))]
    plt.bar(xs, ys, color="#48bc38")
    plt.title('Столбчатый график')

    # 3. histogram
    plt.subplot(2,2,3)
    xs = [random.gauss(0,1) for _ in range(1000)]
    plt.hist(xs, color="#9C37B8")
    plt.title('Гистрограмма')

    # 4. pie chart
    plt.subplot(2,2,4)
    titles = list(letters[:7])
    xs = [random.randint(0, 50) for _ in range(len(titles))]
    plt.pie(xs, labels=titles)
    plt.title('Круговая диаграмма')


    # общий вывод и сохранение
    # какие-то траблы с наслаиванием надписей
    plt.tight_layout(h_pad=1.0)
    plt.savefig(output_img)
    plt.show()


def main(output_img: str) -> None:
    Dashboard_using_matplotlib(output_img)


if __name__ == '__main__':

    parse = argparse.ArgumentParser('Создание Дашборда на основе переданных данных')
    parse.add_argument('--output_img', '-out', type=str, default='result.jpg', help='Название выходящего PNG изображения')

    args = parse.parse_args()

    main(args.output_img)