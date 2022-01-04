#importing libraries and init program
import pygame
import sys
import os
from pygame.locals import *
pygame.init()

import random

#changes cwd to the project folder
os.chdir('..')

#fps value
fps = 30 
frame_per_sec = pygame.time.Clock()

#colors
green = (0, 100, 0)
blue = (0, 153, 255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (230, 184, 0)

#display w caption
display_surf = pygame.display.set_mode((1920,1080))
display_surf.fill(green)
pygame.display.set_caption("Blackjack")

#deck
deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#bust booleans
player_bust = False
dealer_bust = False
#stand booleans
player_stand = False
#quit boolean
quit = False
#deck values
player_deck = 0
dealer_deck = 0
#lists
player_list = []
dealer_list = []
#dealer positions
dealer_x = 740
dealer_y = 122
#player positions
player_x = 740
player_y = 662

#function to hit
def hit(person_deck, person_list, person, person_x, person_y):
    card = deck[random.randint(0,12)]
    if isinstance(card, str) and card!= "A":
        card_value = 10
        if "A" in person_list and (person_deck +10 > 21):
            card_value = 0
        person_list.append(card)
        image = display_card(card)
        display_surf.blit(image, (person_x, person_y))
        return card_value
    elif card == "A":
        if (person_deck + 11 > 21):
            person_list.append(card)
            hard_hand(person_list)
            card_value = 1
            image = display_card(card)
            display_surf.blit(image, (person_x, person_y))
            return card_value
        else:
            person_list.append(card)
            card_value = 11
            image = display_card(card)
            display_surf.blit(image, (person_x, person_y))
            return card_value
    else:
        person_list.append(card)
        if "A" in person_list and (person_deck + card > 21):
            hard_hand(person_list)
            card_value = (card - 10)
        else:
            card_value = card
        image = display_card(card)
        display_surf.blit(image, (person_x, person_y))
        return card

#changes the list once it changes to a hard hand
def hard_hand(person_list):
    for i in range(0, len(person_list)):
        if person_list[i] == "A":
            person_list[i] = "a"

#makes the card to image
def display_card(card):
    if card == 2:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '2.jpg'))
        return image
    elif card == 3:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '3.jpg'))
        return image
    elif card == 4:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '4.jpg'))
        return image
    elif card == 5:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '5.jpg'))
        return image
    elif card == 6:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '6.jpg'))
        return image
    elif card == 7:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '7.jpg'))
        return image
    elif card == 8:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '8.jpg'))
        return image
    elif card == 9:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '9.jpg'))
        return image
    elif card == 10:
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', '10.jpg'))
        return image
    elif card == "J":
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', 'J.jpg'))
        return image
    elif card == "Q":
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', 'Q.jpq'))
        return image
    elif card == "K":
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', 'K.jpg'))
        return image
    elif card == "A":
        image = pygame.image.load(os.path.join(os.getcwd(), 'Assets', 'A.jpg'))
        return image

class button():
    def __init__(self, color, x, y, width, height, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, black, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        #draws button to screen
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.SysFont("trebuchet ms", 40)
        text = font.render(self.text, 1, (0,0,0))
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

def is_clicked(x, y, width, height):
    if (pygame.mouse.get_pos()[0] >= x and pygame.mouse.get_pos()[0] <= (x + width)) and (pygame.mouse.get_pos()[1] >= y and pygame.mouse.get_pos()[1] <= (y + height)):
        return True

hit_button = button(blue, 806, 510, 130, 60, "HIT")
hit_button.draw(display_surf)

stand_button = button(yellow, 982, 510, 130, 60, "STAND")
stand_button.draw(display_surf)

exit_button = button(red, 60, 60, 60, 60, "X")
exit_button.draw(display_surf)



#Deal dealer's deck
image = pygame.image.load(r'C:\Users\charl\source\repos\blackjack3.0\Assets\template.jpg')
display_surf.blit(image, (dealer_x, dealer_y))
dealer_x += 240
dealer_deck += hit(dealer_deck, dealer_list, "dealer", dealer_x, dealer_y)
dealer_x +=240

#deal player's deck
for i in range(2):
    player_deck += hit(player_deck, player_list, "player", player_x, player_y)
    player_x += 240

while True:
    pygame.display.update()
    for event in pygame.event.get():
        #checks to see if the exit button was clicked
        #if event.type == QUIT:
        #    quit = True
        #    break
        #checks to see if the mouse clicked the hit button
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if is_clicked(806, 510, 130, 60):
                #player hit
                player_deck += hit(player_deck, player_list, "player", player_x, player_y)
                player_x += 240
                if player_deck > 21:
                    pygame.display.update()
                    player_bust = True
                    break
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if is_clicked(60, 60, 60, 60):
                quit = True
                #pygame.quit()
                break
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if is_clicked(982, 510, 130, 60):
                player_stand = True
                break
    frame_per_sec.tick(fps)
    if quit == True:
        break
    if player_stand == True:
        break
    if player_bust == True:
        break
            
    
#dealer's turn
if quit == False:
    if player_bust == False:
        dealer_x -= 480
        dealer_deck += hit(dealer_deck, dealer_list, "dealer", dealer_x, dealer_y)
        dealer_x += 480
        while True:
            pygame.display.update()
            if dealer_deck < 17:
                dealer_deck += hit(dealer_deck, dealer_list, "dealer", dealer_x, dealer_y)
                dealer_x += 240
                pygame.time.delay(1000)
                if dealer_deck > 21:
                    pygame.display.update()
                    dealer_bust = True
                    break
            if dealer_deck == 17 and "A" in dealer_list:
                dealer_deck += hit(dealer_deck, dealer_list, "dealer", dealer_x, dealer_y)
                dealer_x += 240
                break
            if dealer_deck >= 17:
                break
            frame_per_sec.tick(fps)


#evaluates who won and creates a banner to say who won
if player_bust == True:
    end_button = button(red, 740, 464, 440, 152, "BUST")
    end_button.draw(display_surf)
elif dealer_bust == True:
    end_button = button(yellow, 740, 464, 440, 152, "DEALER BUSTED")
    end_button.draw(display_surf)
elif dealer_deck > player_deck and dealer_bust == False:
    end_button = button(red, 740, 464, 440, 152, "DEALER WINS")
    end_button.draw(display_surf)
elif player_deck > dealer_deck and player_bust == False:
    end_button = button(yellow, 740, 464, 440, 152, "PLAYER WINS")
    end_button.draw(display_surf)
elif player_deck == dealer_deck:
    end_button = button(white, 740, 464, 440, 152, "STAND")
    end_button.draw(display_surf)

#adds the end banner and checks to see if clicks exit button
if quit == False:
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            #checks to see if the exit button was clicked
            if event.type == QUIT:
                quit = True
                break
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if is_clicked(60, 60, 60, 60):
                    pygame.quit()
                    quit = True
                    break
        if quit == True:
            break
        frame_per_sec.tick(fps)