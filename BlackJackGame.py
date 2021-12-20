import random

import deer as deer

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

playing = True


class Cards():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return (f"{self.rank} of {self.suit}")


class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Cards(suit, rank))

    def __str__(self):
        deck_display = ''
        for card in self.all_cards:
            deck_display += '' + Cards.__str__()
        return "The deck has " + deck_display

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class PlayerHand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)  # from the deck.deal
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:  # boolen value for aces
            self.value -= 10
            self.aces -= 1


class chips():

    def __init__(self):
        self.total = 500  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


    # class game_logic():
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nhow much money would you like to bet: "))
        except:
            print("Sorry i need real money")
        else:
            if chips.bet > chips.total:
                print("Not enouhg money", chips.total)
            else:
                break



def hit(deck, player):
    player.add_card(deck.deal_one())
    player.adjust_for_ace()

def show_some(player, dealer):

    print(f"The player has: ")
    for card in player.cards:
        print(card,end = ' & ')
    print(player.value)
    print(f"\nThe dealer has:\n{dealer.cards[0]}")

def show_all(player, dealer):  # sourcery skip: remove-redundant-fstring
    for card in player.cards:
        print(card,end = ' & ')
    print(player.value)

    for card in dealer.cards:
        print(card,end = ' & ')

def hit_or_stand(deck, player):
    global playing  # to control an upcoming while loop
    while True:
        x = str(input("\nHit or stand h or s: "))

        if x.lower() == "h":
            hit(deck, player)

        elif x.lower() == 's':
            print("\nPlayer stands dealers turn")
            playing = False
        else:
            print("Enter an h or s")
            continue
        break

def player_busts(player,dealer,chips):
    print("\nDealer wins, player bust")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("\nPlayer wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busted player win")
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print("\nDealer wins")
    chips.lose_bet()

def push():
    print ("\ntie game: push")

def replay():
    # asks the player if they want to play again
    # returns True if they do want to play again.
    return (input("\n\n would you like to keep playing: (y or n)").upper().startswith('Y'))
    # #run the main game


while True:
    # Print an opening statement
    print("are you ready to play black jack ")
    # Create & shuffle the deck, deal two cards to each player
    game_deck = Deck()
    game_deck.shuffle()

    player = PlayerHand()
    dealer = PlayerHand()
    for x in range(2):
        # deal two cards to player
        player.add_card(game_deck.deal_one())
        dealer.add_card(game_deck.deal_one())
    # Set up the Player's chips
    player_chip = chips()
    print("You get to start with 500")
    # Prompt the Player for their bet
    take_bet(player_chip)
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(game_deck,player)
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player, dealer,player_chip)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value < 17:
            hit(game_deck,dealer)
         # Show all cards
           # show_all(player, dealer)

        # Run different winning scenarios
            if dealer.value > 21:
                dealer_busts(player,dealer,player_chip)
            elif player.value >21:
                player_busts(player, dealer,player_chip)
            elif dealer.value > player.value:
                dealer_wins(player, dealer,player_chip)
            elif player.value > dealer.value:
                player_wins(player, dealer,player_chip)
            else:
                push(dealer.value,player.value)

            # Inform Player of their chips total
    print(f"player total is {player_chip.total}")


        # Ask to play again
    if replay() == True:
        playing = True
        continue
    else:
        print("Thanks for playing")
        break









