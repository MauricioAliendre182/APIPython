from dataclasses import dataclass
from PetsProject.src.entity.category import Category
from PetsProject.src.entity.tag import Tag


@dataclass(init=False)
class Pet:
    id: int
    category: Category
    name: str
    photoUrls: [str]
    tags: [Tag]
    status: str

    def __init__(self, id=0, name= '', photoUrls=[''], tags=[Tag()], category=Category(), status='available'):
        self.id = id
        self.name = name
        self.category = category
        self.tags = tags
        self.photoUrls = photoUrls
        self.status = status

