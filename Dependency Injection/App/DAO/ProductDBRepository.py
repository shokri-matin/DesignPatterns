import sys
import os

from typing import List

sys.path.append(r'App')

from IRepository import IRepository
from DMO.Product import Product

class ProductDBRepository(IRepository[Product, int]):

    def __init__(self, path: str):
        self.path = path

    def readAll(self) -> List[Product]:
        raise NotImplementedError
    

    def read(self, id: int) -> Product:
        raise NotImplementedError
    

    def create(self, entity: Product) -> Product:
        raise NotImplementedError
    

    def update(self, entity: Product) -> Product:
        raise NotImplementedError


    def delete(self, entity: Product) -> Product:
        raise NotImplementedError

productDbRepo = ProductDBRepository(path = "")
productDbRepo.readAll()