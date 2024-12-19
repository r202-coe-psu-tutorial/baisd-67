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

    score = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


    def hit_monster(self, touch):
        if (self.x <= touch.x <= self.x+self.size[0]) and (self.y <= touch.y <= self.y+self.size[1]):
            self.score += 1
            print('hit', self.score)
            return True
        
        print('miss')
        return False

class HitTheBossGame(Widget):
    monster = ObjectProperty(None)
    score_panel = ObjectProperty(None)

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

    def on_touch_down(self, touch):
        if self.monster.hit_monster(touch):
            self.score_panel.text = f'Score: {self.monster.score}'

class HitTheBossApp(App):
    def build(self):
        game = HitTheBossGame()
        game.release_monster()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    HitTheBossApp().run()