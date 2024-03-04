import colorsys
import random


def _hsv_to_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(255 * r), int(255 * g), int(255 * b)


def get_distinct_colors(n, seed=0) -> list[tuple[int, int, int]]:
    """
    Получить n уникальных цветов
    """
    random.seed(seed)

    color_order = list(range(n))
    random.shuffle(color_order)
    hue_partition = 1.0 / (n + 1)
    return [_hsv_to_rgb(hue_partition * value, 1.0, 1.0) for value in color_order]


def normalize_rgb(color: tuple[int, int, int]) -> tuple[float, float, float]:
    return (color[0] / 255, color[1] / 255, color[2] / 255)
