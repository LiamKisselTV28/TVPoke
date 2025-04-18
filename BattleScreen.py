from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *
from TVPoke.Pokemon import 
from TVPoke.BaseClasses.Trainer import Trainer

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = [
            Move1(),
            Move2(),
            Move3(),
            Move4(),
            Label((17, 90), 35, 20, "Inactive HP", 16, (0,0,0)),
            Label((83, 45), 35, 20, "Active HP", 16, (0,0,0)),
            ]


        y = 0
        #two rows of three
        for trainer in self.trainers:
            x = 0
            y += 100/3
            for poke in trainer.pokemon:
                x += 100/4
                self.elements.append(Image((x, y), 20, 20, poke.img))
                self.elements.append(Label((x, y + 10), 20, 10, poke.name))
                
for move in Trainer.poke[move]

class Move1(Button):
    def __init__(self, move):
        super().__init__((55,30), width=25, height=15, text=move.name, textColorRGB=(0,0,0))
    def onClick(self, screen):
        return super().onClick(screen)

class Move2(Button):
    def __init__(self):
        super().__init__((85,30), width=25, height=15, text="move2", textColorRGB=(0,0,0))
    def onClick(self, screen):
        return super().onClick(screen)

class Move3(Button):
    def __init__(self):
        super().__init__((55,10), width=25, height=15, text="move3", textColorRGB=(0,0,0))
    def onClick(self, screen):
        return super().onClick(screen)
    
class Move4(Button):
    def __init__(self):
        super().__init__((85,10), width=25, height=15, text="move4", textColorRGB=(0,0,0))
    def onClick(self, screen):
        return super().onClick(screen)
    