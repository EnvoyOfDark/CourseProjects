import random
from IPython.display import clear_output


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_score(self):
        score = 0
        for card in self.hand:
            if card in ['J', 'Q', 'K']:
                score += 10
            elif card == 'A':
                score += 11
            else:
                score += int(card)
        return score

    def draw_card(self, deck):
        card = random.choice(deck)
        self.hand.append(card)
        deck.remove(card)

    def show_hand(self):
        print(f"{self.name}'s hand:", self.hand)
        print(f"{self.name}'s score:", self.get_score())


class Game:
    def __init__(self):
        self.deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        for i in range(2):
            self.player.draw_card(self.deck)
            self.dealer.draw_card(self.deck)

    def player_turn(self):
        while self.player.get_score() < 21:
            clear_output()
            print("Player's turn")
            self.player.show_hand()
            choice = input("\nDo you want to hit or stand? ")
            if choice.lower() == "hit":
                self.player.draw_card(self.deck)
            else:
                break
        clear_output()

    def dealer_turn(self):
        while self.dealer.get_score() < 17:
            self.dealer.draw_card(self.deck)
        clear_output()
        print("Dealer's turn")
        self.dealer.show_hand()

    def determine_winner(self):
        if self.player.get_score() > 21:
            print("Player busts! Dealer wins.")
        elif self.dealer.get_score() > 21:
            print("Dealer busts! Player wins.")
        elif self.player.get_score() > self.dealer.get_score():
            print("Player wins!")
        elif self.dealer.get_score() > self.player.get_score():
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play_game(self):
        clear_output()
        print("Welcome to Blackjack!\n")
        self.deal_initial_cards()
        self.player_turn()
        self.dealer_turn()
        self.determine_winner()
        while True:
            reset = input('Do you wanna play again [y/n]?: ')
            if reset == 'y':
                game = Game()
                game.play_game()
            else:
                break

if __name__ == '__main__':
   game = Game()
   game.play_game()
