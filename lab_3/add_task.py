# lab №3 additional task | Var 10 Sergey Zubrilin 10/22/18


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


def data_for_colour_gist(img_array, colour='red'):
    """
    возвращает одномерный массив метаданных относяшихся к пикселям заданного цвета
    :param img_array: numpy.ndarray
    :param colour: {'red', 'green', 'blue'}
    :return: numpy.ndarray
    """
    c_dict = {'red': 0, 'green': 1, 'blue': 2}
    data_for_gist = img_array[:, :, c_dict[colour]].reshape(m * n)
    data_for_gist = data_for_gist[data_for_gist > 0.0]      # удалил белые пикслеи, что бы белая рамка не
                                                            # мешала строить график
    return data_for_gist


def rm_colour(img_array, colour='red'):
    """
    Удаляет один из RGB цветов
    :param img_array: numpy.ndarray
    :param colour: {'red', 'green', 'blue'}
    :return: numpy.ndarray
    """
    c_dict = {'red': 0, 'green': 1, 'blue': 2}
    img_array[:, :, c_dict[colour]] = 0
    return img_array


def change_brightness(img_array, mod='increase', value=0.5):
    """

    :param mod: {'reduce, 'increase'}
    :param img_array: numpy.ndarray
    :param value: float {0.0, 0.99}
    :return: numpy.ndarray
    """
    if mod == 'increase':
        img_array[:, :, :] += ((1-img_array[:, :, :])*value)
    if mod == 'reduce':
        img_array[:, :, :] *= value

    return img_array


img = mpimg.imread("img_for_add_task.png")
img = plt.imread("img_for_add_task.png")

m, n, k = img.shape
fig = plt.figure(figsize=(16, 9))
plt.axis("off")


# rm_colour(img, 'blue')
# change_brightness(img, mod='reduce')
plt.imshow(img, interpolation='nearest')

fig.savefig('add_task.png', dpi=n/16)
plt.show()


g_data = data_for_colour_gist(img)
fig, ax = plt.subplots(figsize=(10, 10))
ax.hist(g_data, bins=10)
ax.set_xlim((min(g_data), max(g_data)))
fig.savefig('add_task_colour_gist.png', dpi=200, bbox_inches='tight')

