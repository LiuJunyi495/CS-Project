# TODO: error handling
#    1 searching or sorting algorithm
#    2 data strutures
#    Mini-games
#    Power ups
#    Penalties
#    Wining condition 


import tkinter.messagebox
import tkinter as tk
import random

# u5547386 - Start
class Grid:
    """A superclass of all grids in the map."""
    def __init__(self, number, grid_type=None):
        self.number = number # The number of the grid.
        self.type = grid_type

class BossGrid(Grid):
    """A subclass of gird contained boss."""
    def __init__(self, number):
        super().__init__(number, "Boss")
        # Make sure boss has a suitable power.
        self.power = int(number * random.uniform(1, 1.5)) 
    
    def boss_battle(self, player_power): 
        return player_power > self.power
    
class GameGrid(Grid):
    """A subclass of gird contained game."""
    def __init__(self, number):
        super().__init__(number, "Game")
        card_game = CardDeck()
        coin_game = Coin()
        # Randomly choose a game for the Grid.
        self.game = random.choice([f"{random.choice(card_game.card_challenges)}", "Coin Flip", "Rock\nPaper\nScissors"]) 

class PointGrid(Grid):
    """A subclass of gird where player can collect points."""
    def __init__(self, number):
        super().__init__(number, "Point")
        # Edited by 5554570.
        # 20% chance of generating a high point value.
        self.point = random.randint(6, 10) if random.random() < 0.2 else random.randint(1, 5)
        # Edited by 5554570.
# u5547386 - End

# 5554570 - beggining.
class Player:
    """Represents the player in the game."""
    def __init__(self, health_points, combat_effectiveness):
        self.health_points = health_points
        self.combat_effectiveness = combat_effectiveness
        self.player_position = 0

    def move(self, steps):
        # Move the player position without exceeding the grid limit.
        self.player_position += steps
        self.player_position = max(0, self.player_position)
        self.player_position = min(self.player_position, len(grids) - 1)

    def update_hp(self, hp_change):
        # Updating the players health points and making sure it doesn't go below zero.
        self.health_points += hp_change
        self.health_points = max(0, self.health_points)
        hp_label.config(text=f"HP: {self.health_points}", width=self.health_points) # Edited by u5547386 - Update label in the function
        if self.health_points < 1:
            # Edited by u5547386 - add lose condition
            tk.messagebox.showinfo(title='You lose this game!',message="You were defeated by the boss!\nLet's try again.")
            self.player_position = 0
            restart()
            hp_label.config(text=f"HP: {self.health_points}", width=self.health_points)
            ce_label.config(text=f"CE: {self.combat_effectiveness}", width=min(50,self.combat_effectiveness))
            # Edited by u5547386
    
    def update_ce(self, ce_change):
        # Updating the players combat effectiveness and making sure it doesn't go below zero.
        self.combat_effectiveness += ce_change
        self.combat_effectiveness = max(0, self.combat_effectiveness)
        ce_label.config(text=f"CE: {self.combat_effectiveness}", width=min(50,player.combat_effectiveness)) # Edited by u5547386 - Update label in the function
# Creating the card deck Game.
class CardDeck:
    def __init__(self):
        # Defining the deck of cards and card challenge variables.
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King"]
        self.deck = [f"{value} of {suit}" for suit in self.suits for value in self.values]
        self.red_cards = [f"{card}" for card in self.deck if "Hearts" in card or "Diamonds" in card]
        self.black_cards = [f"{card}" for card in self.deck if "Clubs" in card or "Spades" in card]
        self.odd_cards = [f"{card}" for card in self.deck if card[0] in ["Ace", "3", "5", "7", "9", "Queen"]]
        self.even_cards = [f"{card}" for card in self.deck if card[0] in ["2", "4", "6", "8", "Jack", "King"]]
        # Defining the card challenges.
        self.card_challenges = [ "Draw a\nred card", "Draw a\nblack card", "Draw an\nodd card", "Draw an\neven card"]

    def draw_card(self):
        """Drawing a random card feom the deck."""
        return random.choice(self.deck)

    def card_in_deck(self, challenge, card):
        """Check if the card is in the deck."""
        # Using a linear searching algorithm to check if the card is in the deck.
        if "red" in challenge:
            for i in self.red_cards:
                if i == card:
                    return True
        if "black" in challenge:
            for i in self.black_cards:
                if i == card:
                    return True
        if "odd" in challenge:
            for i in self.odd_cards:
                if i == card:
                    return True
        if "even" in challenge:
            for i in self.even_cards:
                if i == card:
                    return True
        return False # Return False if the card is not in the deck.
    
def roll_dice():
    """Simulates rolling a die."""
    return random.randint(1, 6)
# 5554570 - end.

#   5553980 - start
extra_dice = 0
class PnP:
    def CEmin():
        value = -random.randint(5, 10)
        player.update_ce(value)
        challenges_text.insert(tk.END, f"You Loss!\nPenalty: {value} CE")

    def CEmax():
        value = random.randint(5, 10)
        player.update_ce(value)
        challenges_text.insert(tk.END, f"You Win!\nPower up: +{value} CE")
    def reset():
        global extra_dice
        extra_dice = 0
    
    def moveF():
        global extra_dice
        extra_dice = random.randint(1, 3)
        challenges_text.insert(tk.END, f"You Win!\nPower up: +{extra_dice} steps on next roll")

        extra_dice_result.config(text=f"Roll applied to next move: +{extra_dice}")
    def moveB():
        global extra_dice
        extra_dice = -(random.randint(1, 3))
        challenges_text.insert(tk.END, f"You Loss!\nPenalty: {extra_dice} steps on next roll")

        extra_dice_result.config(text=f"Roll applied to next move: {extra_dice}")

class Coin:
    def __init__(self):
        self.values = ["Heads", "Tails"]
    def flip_coin(self):
        return random.choice(self.values)
    def success(self, challenge, coin):
        return challenge == coin
    
class RPS:
    def __init__(self):
        self.values = ["Rock", "Paper", "Scissors"]
    def choose_rps(self):
        return random.choice(self.values)
    def success(self, choice, challenge):
        if choice == challenge:
            result = "Draw"
        elif (choice == "Rock" and challenge == "Scissors") or \
             (choice == "Paper" and challenge == "Rock") or \
             (choice == "Scissors" and challenge == "Paper"):
            result = "Player wins"
        else:
            result = "Computer wins"
        return result

#   5553980 - end

# u5547386 - Start
def generate_grid(number):
    """Generates a grid based on the giver number."""
    if number == 0:     # starting point. 
        return Grid(number, "Start")
    elif number == 48:  # ending point.
        return Grid(number, "End")
    # Edited by 5554570.
    # Making sure that there wouldn't be any boss battles in the first 6 squares.
    elif number < 7:    
        # 70% chance it is a point grid.
        return PointGrid(number) if random.randint(1, 2) == 1 else GameGrid(number)
    # Edited by 5554570
    # Generate a number to choose grid according to fixed probabilities.
    else:         
        r = random.randint(1, 5)   
        if r <= 2:
            return PointGrid(number)    # Probability 50%.
        elif r <= 4:
            return GameGrid(number)     # Probability 40%.
        else:
            return BossGrid(number)     # Probability 10%.
    
# Use a list to storage grids.
grids = [generate_grid(i) for i in range(49)]   

def create_grid(canvas, grid, x, y, player_position):
    """Draw a grid in canvas."""
    canvas.create_text(x+90, y+10, text=str(grid.number+1))
    canvas.create_rectangle(x, y, x+100, y+100)
    # Draw different types of grids with specific attributes.
    if grid.type == "Point":
        canvas.create_text(x+50, y+50, fill = "blue", text="Point\n"+str(grid.point))
    elif grid.type == "Game":
        canvas.create_text(x+50, y+50, fill = "orange", text=grid.game)
    elif grid.type == "Boss":
        canvas.create_text(x+50, y+50, fill = "red", text="Boss\n"+str(grid.power))
    elif grid.type == "Start":
        canvas.create_text(x+50, y+50, text="Start")
    elif grid.type == "End":
        canvas.create_text(x+50, y+50, text="End")
    # Shows the players position.
    if grid.number == player_position:
        canvas.create_oval(x+30, y+30, x+70, y+70, fill="green")
# u5547386 - End

# 5554570 - beggining.
def reach_end(player_position, end_position):
    return player_position == end_position

def roll_and_move():
    """Rolls the dice, moves the player, and checks for challenges."""
    global extra_dice_result, dice_result, challenges_text # Make the widgets global so they can be updated.
    steps = roll_dice()
    player.move(steps+extra_dice)
    PnP.reset()
    update_grid()
    dice_result.config(text=f"Dice Roll: {steps}")
    extra_dice_result.config(text=f"Roll applied to next move: {0}")
    current_grid = grids[player.player_position]

    if reach_end(player.player_position, 48):
        print("End reached")
        # Edited by u5547386 - edit winning condition
        choice=tk.messagebox.askyesno(title='You win this game!',message="CONGRATULATIONS!\nYou have reached the top of the hill.\nDo you what to play again?")
        if choice == True:
            player.player_position = 0
            restart()
            hp_label.config(text=f"HP: {player.health_points}", width=player.health_points)
            ce_label.config(text=f"CE: {player.combat_effectiveness}", width=min(50,player.combat_effectiveness))
        else:
            roll_button.destroy()
        # Edited by u5547386
        
    if isinstance(current_grid, PointGrid):
        # Handling the point change.
        player.update_ce(current_grid.point) # Edit by u5547386 - Collect point as CE instead of HP.
        
        # Update the challenge list text with the challenge and outcome.
        challenges_text.delete(1.0, tk.END)
        challenges_text.insert(tk.END, f"Points gained: {current_grid.point}\n")

    if isinstance(current_grid, BossGrid):
        # Handling the boss challenge.
        challenge_success = current_grid.boss_battle(player.combat_effectiveness)
        challenges_text.delete(1.0, tk.END)
        challenges_text.insert(tk.END, f"Boss Power: {current_grid.power}\n")
        challenges_text.insert(tk.END, f"Player Power: {player.combat_effectiveness}\n")
        challenges_text.insert(tk.END, f"You Win!\n" if challenge_success else f"You loss!\nHP - 20")
        # Player losses 20 hp if they loss
        if not challenge_success:
            player.update_hp(-20)
        

    if isinstance(current_grid, GameGrid) and "Draw" in current_grid.game:
        # Handling the card challenge.
        card_game = CardDeck()
        drawn_card = card_game.draw_card()
        challenge_success = card_game.card_in_deck(current_grid.game, drawn_card)
        challenges_text.delete(1.0, tk.END)   # Clear the previous challenges.
        challenges_text.insert(tk.END, f"Challenge: {current_grid.game}\n")
        challenges_text.insert(tk.END, f"Drawn Card: {drawn_card}\n")
        pnp_result = random.choice(["dice", "CE"])
        if challenge_success:
            if "dice" in pnp_result:
                PnP.moveF()
            elif "CE" in pnp_result:
                PnP.CEmax()
        else:
            if "dice" in pnp_result:
                PnP.moveB()
            elif "CE" in pnp_result:
                PnP.CEmin()
        
        # Handling the other game challenges.
        """ if game2:
            if game3:
            # Update the move list text with the challenge and outcome.
            challenges_text.insert(tk.END, f"challenge: {current_grid.game}\n")
            challenges_text.insert(tk.END, f"Success!\nPower up: XXX" if challenge_success else f"Failed!\nPanelty: XXX")"""
# 5554570 - end.
        


    #   5553980 - start
    if isinstance(current_grid, GameGrid) and "Coin" in current_grid.game:
        challenges_text.delete(1.0, tk.END)   # Clear the previous challenges.
        challenges_text.insert(tk.END, f"Guess the face of\nthe flipped coin\n")

        inpt = ""
        coin_game = Coin()
        button1 = tk.Button(challenges_frame, text="Heads", command=lambda c="Heads": check(c, button1, button2))
        button1.pack()
        button2 = tk.Button(challenges_frame, text="Tails", command=lambda c="Tails": check(c, button1, button2))
        button2.pack()
        roll_button.destroy()
        def check(cc, b1, b2):
            global inpt
            global roll_button
            inpt = cc
            flip_result = coin_game.flip_coin()
            challenge_success = coin_game.success(inpt, flip_result)
            roll_button = tk.Button(challenges_frame, text="Roll Dice", command=roll_and_move)
            roll_button.pack()

            challenges_text.insert(tk.END, f"Your Choice: {inpt}\n")
            challenges_text.insert(tk.END, f"Flip result: {flip_result}\n")
            b1.destroy()
            b2.destroy()
            pnp_result = random.choice(["dice", "CE"])
            if challenge_success:
                if "dice" in pnp_result:
                    PnP.moveF()
                elif "CE" in pnp_result:
                    PnP.CEmax()
            else:
                if "dice" in pnp_result:
                    PnP.moveB()
                elif "CE" in pnp_result:
                    PnP.CEmin()

    
    if isinstance(current_grid, GameGrid) and "Rock" in current_grid.game:
        challenges_text.delete(1.0, tk.END)   # Clear the previous challenges.

        def attempt():
            challenges_text.insert(tk.END, f"a game of Rock-Paper-Scissors\n")

            inpt = ""
            rps_game = RPS()
            button1 = tk.Button(challenges_frame, text="Rock", command=lambda c="Rock": check(c, button1, button2, button3))
            button1.pack()
            button2 = tk.Button(challenges_frame, text="Paper", command=lambda c="Paper": check(c, button1, button2, button3))
            button2.pack()
            button3 = tk.Button(challenges_frame, text="Scissors", command=lambda c="Scissors": check(c, button1, button2, button3))
            button3.pack()
            roll_button.destroy()
            def check(cc, b1, b2, b3):
                global inpt
                global roll_button
                inpt = cc
                rps_choice = rps_game.choose_rps()
                challenge_success = rps_game.success(inpt, rps_choice)
                roll_button = tk.Button(challenges_frame, text="Roll Dice", command=roll_and_move)
                roll_button.pack()

                challenges_text.insert(tk.END, f"Your Choice: {inpt}\n")
                challenges_text.insert(tk.END, f"Computer Choice: {rps_choice}\n")
                b1.destroy()
                b2.destroy()
                b3.destroy()
                pnp_result = random.choice(["dice", "CE"])
                if "Player" in challenge_success:
                    if "dice" in pnp_result:
                        PnP.moveF()
                    elif "CE" in pnp_result:
                        PnP.CEmax()
                elif "Computer" in challenge_success:
                    if "dice" in pnp_result:
                        PnP.moveB()
                    elif "CE" in pnp_result:
                        PnP.CEmin()
                else:
                    challenges_text.insert(tk.END, "It's a draw\n")
                    attempt()
        attempt()
    #   5553980 - end

# u5547386 - Start
def update_grid():
    """Updates the disdlplay of the game."""
    game_area.delete("all")
    for grid in grids:
        x = grid.number % 7 * 100 + 10    # Remainder = Column number.
        y = grid.number // 7 * 100 +10    # Quotient = Row number.
        create_grid(game_area, grid, x, y, player.player_position)
    game_area.pack()

def restart():
    """Start the game again"""
    player.health_points=50
    player.combat_effectiveness=10
    PnP.reset()
    update_grid()
    dice_result.config(text=f"Dice Roll: {0}")
    extra_dice_result.config(text=f"Roll applied to next move: {0}")
    current_grid = grids[0]
    challenges_text.delete(1.0, tk.END)
# u5547386 - End

# 5554570 - beggining.
player = Player(50, 10) # Player starts with 50 health points and 10 combat effectiveness.

# Main application window.
root = tk.Tk()
root.title("King Of The Hill")

# Create the game area. 
game_area = tk.Canvas(root, width=710, height=710, bg="white") 
game_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 

update_grid() # Draw the initial grid.

# Create a side panel for additional information. 
side_panel = tk.Frame(root, bg="#C7F1F0", width=400) 
side_panel.pack_propagate(False) # Prevents resizing
side_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10) 

# Create a player information frame. 
player_info_frame = tk.Frame(side_panel, bg="#C7F1F0")
player_info_frame.pack(fill=tk.X)
player_label = tk.Label(player_info_frame, text="Player Info", bg="#C7F1F0")
player_label.pack()
# Edited by 5554570.
# Show hp and ce as a bar. Show the value in class, instead of a fix number.
# Display a image.
hp_label = tk.Label(player_info_frame, text=f"HP: {player.health_points}", bg="red", width=player.health_points)
hp_label.pack()
ce_label = tk.Label(player_info_frame, text=f"CE: {player.combat_effectiveness}", fg='white', bg="blue", width=player.combat_effectiveness)
ce_label.pack()
try:
    img_png = tk.PhotoImage(file = 'hills.png')
    label_img = tk.Label(side_panel, image = img_png)
    label_img.pack(side="bottom")
except tk.TclError:
    print("couldn't open 'hills.png'. Please read User Guide Document.")

# Edited by 5554570. 

# Create a frame to display the challenges and outcomes.
challenges_frame = tk.Frame(side_panel, bg="#C7F1F0")
challenges_frame.pack(fill=tk.X)
challenges_label = tk.Label(challenges_frame, text="Challenge:", bg="#C7F1F0")
challenges_label.pack()
challenges_text = tk.Text(challenges_frame, height=10, width=30)
challenges_text.pack()

# Creates a game control frame.
controls_frame = tk.Frame(side_panel, bg="#C7F1F0")
controls_frame.pack(fill=tk.X)
roll_button = tk.Button(controls_frame, text="Roll Dice", command=roll_and_move)
roll_button.pack()
dice_result = tk.Label(controls_frame, text="Roll: ", bg="#C7F1F0")
dice_result.pack()
extra_dice_result = tk.Label(controls_frame, text="Extra Roll: ", bg="#C7F1F0")
extra_dice_result.pack()
quit_button = tk.Button(controls_frame, text="Quit", command=root.destroy)
quit_button.pack()
# 5554570 - end.

# Runs the game.
root.mainloop()
