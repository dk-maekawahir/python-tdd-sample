from tdd.game import Game

class TestBowlingGame(object):
    def setup_method(self, method):
        self.game = Game()

    def test_gutter_game(self):
        self.roll_many(20, 0)        
        assert self.game.score() == 0

    def test_all1_game(self):        
        self.roll_many(20, 1)
        assert self.game.score() == 20

    def test_spare_game(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        assert self.game.score() == 16

    def test_strike_game(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(5)

        self.roll_many(16, 0)
        assert self.game.score() == 26

    def roll_strike(self):
        self.game.roll(10)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)
    
    def roll_many(self, roll_count, pins):
        for i in range(roll_count):
            self.game.roll(pins)
        