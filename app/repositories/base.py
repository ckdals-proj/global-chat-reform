from abc import ABC, abstractmethod

from typing import Dict

class BaseRepository(ABC):
    @abstractmethod
    def findAll(self):pass

    @abstractmethod
    def find(self):pass

    @abstractmethod
    def save(self):pass

    # @abstractmethod
    # def saveAll(self):pass

    # @abstractmethod
    # def update(self):pass


    # @abstractmethod
    # def delete(self):pass
