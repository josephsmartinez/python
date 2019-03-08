class Duck:
  __metaclass__ = ABCMeta
  fly_behavior = None
  quack_behavior = None

  def display(self):
    pass
  def swim(self):
    print("swimming from the Duck class"
  def fly(self):
    self.fly_behavior().fly
  def quack(self):
    self.quack_behavior.quack()
  def set_fly_behavior(self, fly_behavior):
    self.fly_behavior = fly_behavior 
  def set_quack_behavior(self, quack_behavior):
    self.fly_behavior = quack_behavior

class RedHeadDuck(Duck):
  def __init__(self):
    self.quack_behavior = Quack()
    self.fly_behavior = FlyWithWings()

  def display(self):
    print("I am a cool Mallard duck.")

class MallardDuck(Duck):

class RubberDuck(Duck):

class DecoyDuck(Duck):
  def __init__(self):
  self.quack_behavior = Quack()
  self.fly_behavior = FlyWithWings()
  
class QuackBehavior():
  __metaclass__ = ABCMeta

class Quack:
  __metaclass__ = ABCMeta

  def quack(self):
    print("Quackkkkkkk!")

class Squeak(QuackBehavior):
  def quack(self):
    print("Sqeakkkkk")

class MuteQuack(QuackBehavior):
  def quack(self):
    print("----SILENCE----")

class FlyBehavior:
   __metaclass__ = ABCMeta

  def fly(self):
    pass

class FlyWithWings:

class FlyNoWay:
  def fly(self):
    print("I cannot fly")

class FakeQuack(Duck):
  def quack(self):
    print("kwack")

class FlyRocketPowered(FlyBehavior):
  def fly(self):
    print("ROCKET POWER!!!!")

# Add a new type of Duck, ModeDuck, that does not fly and quacks 
# and design:
# A) FakeQuack:
# B) FlyRocketPowered Class

if __name__ == '__main__':
  mallard = MallardDuck()
  mallard.quack()
  mallard.fly()
  mallard.display()

  daffy = RedHeadDuck()
  daffy.fly()
  