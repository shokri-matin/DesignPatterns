import abc
from typing import TypeVar, Generic, List

T = TypeVar('T')
K = TypeVar('K')

class IRepository(Generic[T, K], abc.ABC):

    @abc.abstractmethod
    def readAll(self) -> List[T]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def read(self, id: K) -> T:
        raise NotImplementedError
    
    @abc.abstractmethod
    def create(self, entity: T) -> T:
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, entity: T) -> T:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, entity: T) -> T:
        raise NotImplementedError