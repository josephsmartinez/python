from abc import ABCMeta

# Metaclass 
class Instrument:
    __metaclass__ = ABCMeta
    play_behavior = None

    def display(self):
        pass

    def playBehavior(self):
        print(self.play_behavior)


class Violin(Instrument):
    def __int__(self):
        self.play_behavior = Bow()

    def display(self):
        print("I am a violin")


class Tuba(Instrument):
    def __int__(self):
        self.play_behavior = BuzzLips()

    def display(self):
        print("I am a tuba")


class Clarinet(Instrument):
    def __int__(self):
        self.play_behavior = BuzzReed()

    def display(self):
        print("I am a clarinet")


class Harp(Instrument):
    def __int__(self):
        self.play_behavior = Strings()

    def display(self):
        print("I am a harp")


class DoubleBass(Instrument):
    def __int__(self):
        self.play_behavior = Bow()


class PlayBehavior:
    __metaclass__ = ABCMeta

    def performPlay(self):
        pass


class Bow(PlayBehavior):
    def performPlay(self):
        print("Play me with a bow")


class BuzzLips(PlayBehavior):
    def performPlay(self):
        print("Play me by blwoing and buzzing your lips")


class BuzzReed(PlayBehavior):
    def performPlay(self):
        print("Play me by blowing and buzzing a reed")


class Strings(PlayBehavior):
    def performPlay(self):
        print("Play me by plucking my strings")


if __name__ == '__main__':
    bow = Bow()
    bow.performPlay()
    
    buzzlips = BuzzLips()
    buzzlips.performPlay()

    buzzreed = BuzzReed()
    buzzreed.performPlay()

    string = Strings()
    string.performPlay()

    violin = Violin()
    violin.display()

    tuba = Tuba()
    tuba.display()

    clarinet = Clarinet()
    clarinet.display()

    harp = Harp()
    harp.display()

    double_bass = DoubleBass()
    double_bass.display()
