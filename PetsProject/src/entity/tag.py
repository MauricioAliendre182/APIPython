from dataclasses import dataclass


@dataclass(init=False)
class Tag:
    id: int
    name: str

    def __init__(self, id_tag=0, name=''):
        self.id = id_tag
        self.name = name
