from ex0.Card import Card
from abc import ABC, abstractmethod

class Combatable(ABC):
    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def defend(self, incoming_damage: int):
        pass

    @abstractmethod
    def get_combat_stats(self):
        pass