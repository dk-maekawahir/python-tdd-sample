from tdd.game import Game

def test_gutter_game():
    game = Game()

    for i in range(20):
        game.roll(0)
    
    assert game.score() == 0

def test_all1_game():
    game = Game()
    
    for i in range(20):
        game.roll(1)
    
    assert game.score() == 20