class Game(object):
    def __init__(self) -> None:
        self.rolls = []
    
    def roll(self, count) -> None:
        self.rolls.append(count)
    
    def score(self) -> int:
        score = 0
        roll_index = 0

        for frame in range(10):
            score += self.frame_score(roll_index)
            if(self.is_spare(roll_index)):
                score += self.rolls[roll_index + 2]
            roll_index += 2
        return score

    def is_spare(self, roll_index):
        return self.frame_score(roll_index) == 10

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
    