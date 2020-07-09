# HigherOrLowerNonOOP

import random

# Cards for deck:
sTuple = ('Spades', 'Hearts', 'Diamonds', 'Clubs')  # highest to lowest
rTuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Joker')
nCards = 8


def getCard(deckListIn):
    if len(deckListIn) == 0:
        return 'no more cards'
    thisCard = deckListIn.pop()  # pops one off of the top of the deck and returns
    return thisCard


def shuffle(deckListIn):
    deckListOut = deckListIn[:]  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut


# main code:
def main():
    print()
    print('Welcome to Higher Or Lower Game!')
    print('''You have to choose if the next card to be shown will be higher or lower 
than the current card. Getting it right adds 20 points, get it wrong and you 
lose 15 points. You have 50 points to start.''')
    
    startingDeckList = []

    for suit in sTuple:
        for thisValue, rank in enumerate(rTuple):
            cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
            if rank != 'Joker':
                startingDeckList.append(cardDict)
            else:
                if suit == 'Hearts':
                    startingDeckList.append(cardDict)
                else:
                    if suit == 'Spades':
                        startingDeckList.append(cardDict)

    # print all dictionaries build by cardDict:
    # for card in startingDeckList:
    #     print(card)

    # initial score
    score = 50

    # to play multiple games:
    while True:
        print()
        gameDeckList = shuffle(startingDeckList)
        currentCardDict = getCard(gameDeckList)
        currentCardRank = currentCardDict['rank']
        currentCardValue = currentCardDict['value']
        currentCardSuit = currentCardDict['suit']
        print('Current score:', score)
        print('Starting card:', currentCardRank + ' of ' + currentCardSuit)
        print()

        for cardNumber in range(0, 8):   # play one game of 8 cards
            answer = input('Will the next card be higher or lower than a/an ' +
                           currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ')
            answer = answer.lower()
            nextCardDict  = getCard(gameDeckList)
            nextCardRank  = nextCardDict['rank']
            nextCardSuit  = nextCardDict['suit']
            nextCardValue = nextCardDict['value']
            print()
            print('Current:', currentCardRank + ' of ' + currentCardSuit)
            print('Next:', nextCardRank + ' of ' + nextCardSuit)

            if answer == 'h':
                if nextCardValue > currentCardValue:
                    print('It was a HIGHER')
                    score = score + 20
                else:
                    print('It was a LOWER')
                    score = score - 15

            elif answer == 'l':
                if nextCardValue < currentCardValue:
                    print('It was a LOWER')
                    score = score + 20

                elif nextCardValue == currentCardValue:
                    if nextCardSuit > currentCardSuit:
                        print('You got same cards, but HIGHER suit')
                        score = score + 20

                    elif nextCardSuit < currentCardSuit:
                        print('You got same cards, but LOWER suit')
                        score = score - 15

                    else:
                        print('Nothing changed')
                        score = score
                else:
                    score = score - 15
                    print('It was a HIGHER')

            print('Your score is:', score)
            print()

            currentCardRank  = nextCardRank
            currentCardValue = nextCardValue
            currentCardSuit  = nextCardSuit

        goAgain = input('To play again, press ENTER, or "q" to quit: ')
        if goAgain == 'q':
            break

    print('OK bye')

if __name__ == '__main__':
    main()