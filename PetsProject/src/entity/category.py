from dataclasses import dataclass


@dataclass(init=False)
class Category:
    id: int
    name: str

    def __init__(self, id_category=0, name=''):
        self.id = id_category
        self.name = name


