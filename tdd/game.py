class Game(object):
    def __init__(self) -> None:
        self.currentScore = 0
    
    def roll(self, count) -> None:
        self.currentScore += count
    
    def score(self) -> int:
        return self.currentScore