# abstract_class : 객체를 만들 수 없는 클래스
                #  기본클래스, 부모클래스 역할
    
from abc import *  # abtract base class

class Character(metaclass = ABCMeta):
    def __init__(self):
        self.hp = 100
        self.attack_power = 20
        
    def attack(self, other, attack_kind):
        other.get_damage(self.attack_power, attack_kind)
        
    @abstractmethod
    def get_damage(self, attack_power, attack_kind):
        pass
    
if __name__ == '__main__':
    ch1 = Character()