import random


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
        while self.value > 21 and self.ace:  # boolen value for aces
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

    def take_bet(self, chips):
        while True:
            try:
                chips.bet = int(input("how much money would you like to bet: "))
            except:
                print("Sorry i need real money")
            else:
                if chips.bet > chips.total:
                    print("Not enouhg money", chips.total)
                else:
                    break

    def ask_bet(slef):
        return (input("\nwould you make a bet: (y or n)").upper().startswith('Y'))

    def hit(slef,Deck, PlayerHand):
        PlayerHand.add_card(Deck.deal_one)
        PlayerHand.adjust_for_ace()

    def hit_or_stand(deck, hand):
        global playing  # to control an upcoming while loop
        while True:
            x = str(input("Hit or stand h or s: "))

            if x.lower() == "h":
                Deck().hit(deck, hand)

            elif x.lower() == 's':
                print("Player stands dealers turn")
                playing = False
            else:
                print("Enter an h or s")
                continue
            break


class Show_Deck():
    def show_some(player, dealer):

        print(f"The player has  ")
        for card in player.cards:
            print(card, player.value)
        print(f"The dealer has {dealer.cards[0]} {dealer.value}")

    def show_all(player, dealer):
        print(f"The player has  "*player.cards, sep=' ')
        print(player.value)

        print(f"The dealer has  "*dealer.cards,sep=' ')
        print(dealer.value)


class game_logic():

    def player_busts(player,dealer,chips):
        print("Dealer wins, player bust")
        chips.lose_bet()


    def player_wins(player,dealer,chips):
        print("Player wins")
        chips.win_bet()

    def dealer_busts(player,dealer,chips):
        print("Dealer busted player win")
        chips.win_bet()


    def dealer_wins(player,dealer,chips):
        print("Dealer wins")
        chips.lose_bet()

    def push():
        print ("tie game: push")

    def replay():
        # asks the player if they want to play again
        # returns True if they do want to play again.
        return (input(" would you like to keep playing: (y or n)").upper().startswith('Y'))
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
    chips().take_bet(player_chip)
    # Show cards (but keep one dealer card hidden)
    Show_Deck.show_some(player,dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        chips().hit_or_stand(player)
        # Show cards (but keep one dealer card hidden)
        Show_Deck.show_some(player,dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            game_logic().player_busts(player, dealer, chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value <= 17:
            dealer.chips().deal_one()
         # Show all cards
        Show_Deck().show_all(player, dealer)

        # Run different winning scenarios

        # Inform Player of their chips total
        print(f"player total is {player.value}")
        # Ask to play again
        if game_logic.replay() == False:
            break
    break





