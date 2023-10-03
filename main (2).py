
# Define the Player class
class Player:
    def play(self):
        print("Player is playing cricket.")

# Define the Batsman class, inheriting from Player
class Batsman(Player):
    def play(self):
        print("Batsman is batting.")

# Define the Bowler class, inheriting from Player
class Bowler(Player):
    def play(self):
        print("Bowler is bowling.")

# Create objects of both Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play method for each object
batsman.play()
bowler.play()
