import zombiedice, random


class MyRandomZombie:

    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:

        while diceRollResults is not None:
            coinflip = random.randint(1, 2)

            if coinflip == 1:
                zombiedice.roll()
            else:
                break


class MyTwoBrainZombie:

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brainsRolled = 0

        while diceRollResults is not None:
            brainsRolled += diceRollResults['brains']

            if brainsRolled < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class MyTwoShotgunZombie:

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        gunsRolled = 0

        while diceRollResults is not None:
            gunsRolled += diceRollResults['shotgun']

            if gunsRolled < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class MyFourTimeZombie:

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        rollCount = random.randint(1,4)
        gunsRolled = 0

        while rollCount > 0:
            diceRollResults = zombiedice.roll()
            rollCount -= 1
            gunsRolled += diceRollResults['shotgun']
            if gunsRolled > 1:
                break


class MyMoreGunsThanBrainsZombie:

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        gunsRolled = 0
        brainsRolled = 0

        while diceRollResults is not None:
            gunsRolled += diceRollResults['shotgun']
            brainsRolled += diceRollResults['brains']

            if gunsRolled > brainsRolled:
                break
            diceRollResults = zombiedice.roll()


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyRandomZombie(name='My Random Zombie Bot'),
    MyTwoBrainZombie(name='My 2 Brain Zombie'),
    MyTwoShotgunZombie(name='My 2 Shotgun Zombie'),
    MyFourTimeZombie(name='My 4 Time Zombie'),
    MyMoreGunsThanBrainsZombie(name='My More Guns Than Brains Zombie'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
