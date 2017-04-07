from person import Person


class Retailer(Person):
    price = 1000
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money)
        self.product = product
        
    def sell(self, how_many):
        total = self.price * how_many
        
        self.product -= how_many
        #other.product += how_many
        
        other.give_money(self, total)
        
    def __str__(self):
        return super().__str__() + '''
I am a retailer
I have {} products'''.format(self.product)
    
if __name__ == "__main__":
    r1 = Retailer("yang", 20, 5000, 20)
    p1 = Person("kim", 12, 10000)
    print(r1)
    print(p1)
    r1.sell(p1, 3)
    print(r1)
    print(p1)
    
