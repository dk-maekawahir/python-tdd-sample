from tdd.game import Game

def test_gutter_game():
    game = Game()
    game.roll(0)
    
    assert game.score() == 0
