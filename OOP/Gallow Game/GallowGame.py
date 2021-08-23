import random

class Gallow():
    def __init__(self, gallows, state, letters) -> None:
        self.gallows = gallows
        self.state = state
        self.letters = letters

    def show(self, scored):
        print(self.gallows[self.state])
        for x in self.letters:
            if x in scored:
                print(x, end='')
            else:
                print('_', end='')
        print('\n')

    def gameWin(self):
        print('CONGRATULATIONS\nYOU WIN!')
        input('Press Enter to exit')
        exit()
    def gameOver(self):
        print('YOU LOSE!')
        print(f'The word is "{word}"')
        input('Press Enter to exit')
        exit()

def getWordGame():
    """Function that choose the word to the game
    Returns:
        [str]: word of the game
    """
    with open('./OOP/Gallow Game/words.txt', 'r') as file:
        words = file.read().splitlines()
        return random.choice(words)


def getUserTry(gameLetters):
    userLetter = str(input('-->')).lower().strip()[0]
    if userLetter in gameLetters:
        if userLetter in scored:
            pass
        else:
            scored.append(userLetter)
    else: 
        setattr(gallow, 'state', gallow.state + 1)
        print('You Missed!')
        
    main()



def main():

    gallow.show(scored=scored)
    if gallow.state == 6:
        gallow.gameOver()
    elif len(scored) == len(list(set(gallow.letters))):
        gallow.gameWin()
    getUserTry(gameLetters=gallow.letters)

gallows = [
'''
______
|    |
|
|
|
''',
'''
______
|    |
|    0
|
|
''',
'''
______
|    |
|    0
|    |
|
''',
'''
______
|    |
|    0
|   /|
|
''',
r'''
______
|    |
|    0
|   /|\
|
''',
r'''
______
|    |
|    0
|   /|\
|   /
''',
r'''
______
|    |
|    0
|   /|\
|   / \
'''
]
word = getWordGame()
letters = list(word)
scored = []
gallow = Gallow(gallows=gallows, state=0, letters=letters)

if __name__ == '__main__':
    main()


