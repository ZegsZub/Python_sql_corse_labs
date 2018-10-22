# lab №3 additional task | Var 10 Sergey Zubrilin 10/22/18


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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


img = mpimg.imread("img_for_add_task.png", )

m, n, k = img.shape
fig = plt.figure(figsize=(16, 9))
plt.axis("off")

# rm_colour(img, 'blue')
# change_brightness(img, mod='reduce')
plt.imshow(img[:, :, :], aspect='equal')
fig.savefig('add_task.png', dpi=100, bbox_inches='tight')
plt.show()