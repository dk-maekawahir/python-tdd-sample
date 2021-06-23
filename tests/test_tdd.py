from tdd.game import Game

class TestBowlingGame(object):
    def setup_method(self, method):
        self.game = Game()


    def test_gutter_game(self):
        for i in range(20):
            self.game.roll(0)
        
        assert self.game.score() == 0

    def test_all1_game(self):        
        for i in range(20):
            self.game.roll(1)
        
        assert self.game.score() == 20