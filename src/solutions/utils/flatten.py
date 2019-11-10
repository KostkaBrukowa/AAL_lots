from typing import Iterable


def flatten(iterable: Iterable[any]) -> Iterable[any]:
    return [item for sublist in iterable for item in sublist]
