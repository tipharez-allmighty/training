from abc import ABC, abstractmethod


class LivingCreature(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def max_health(self):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @abstractmethod
    def decreaseHealth(self):
        pass

    @abstractmethod
    def increaseHealth(self):
        pass


class Item(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        return f"Item called {self.name}"


class AttackItem(Item):
    @property
    @abstractmethod
    def attack(self):
        pass


class DefenceItem(Item):
    @property
    @abstractmethod
    def defence(self):
        pass


class ConsumableItem(Item):
    @abstractmethod
    def consume(self):
        pass
