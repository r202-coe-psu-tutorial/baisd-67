from random import randint

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget  

from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class Monster(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class HitTheBossGame(Widget):
    monster = ObjectProperty(None)


    def release_monster(self):
        self.monster.center = self.center
        self.monster.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.monster.move()

        # bounce off top and bottom
        if (self.monster.y < 0) or (self.monster.top > self.height):
            self.monster.velocity_y *= -1

        # bounce off left and right
        if (self.monster.x < 0) or (self.monster.right > self.width):
            self.monster.velocity_x *= -1

class HitTheBossApp(App):
    def build(self):
        game = HitTheBossGame()
        game.release_monster()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    HitTheBossApp().run()