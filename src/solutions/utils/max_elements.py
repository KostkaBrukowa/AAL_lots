from typing import Iterable, Callable


def max_elements(iterable: Iterable[any], key: Callable[[any], any]):
    max_value = None
    max_elems = []
    for item in iterable:
        item_value = key(item)
        if max_value is None or item_value > max_value:
            max_value = item_value
            max_elems = [item]

        elif item_value >= max_value:
            max_elems.append(item)

    return max_elems


