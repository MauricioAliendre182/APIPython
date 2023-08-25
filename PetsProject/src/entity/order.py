from dataclasses import dataclass


@dataclass(init=False)
class Order:
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool

    def __init__(self,
                 id_order=0,
                 id_pet=0,
                 quantity=0,
                 shipDate='2023-09-01T02:53:05.018Z',
                 status='placed',
                 complete=True
                 ):
        self.id = id_order
        self.petId = id_pet
        self.quantity = quantity
        self.shipDate = shipDate
        self.status = status
        self.complete = complete