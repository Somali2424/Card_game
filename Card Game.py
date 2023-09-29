#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[2]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank +  " of "  + self.suit


# In[3]:


three_of_clubs=Card('Hearts',"Three")


# In[4]:


print(three_of_clubs)


# In[5]:


class Deck:
    
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                # create the card object
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()


# In[6]:


new_deck=Deck()


# In[7]:


new_deck.shuffle()


# In[ ]:


for card_object in new_deck.all_cards:
    print(card_object)


# In[ ]:


mylist=[12,3,4]


# In[ ]:


print(mylist)


# In[ ]:


class Player:
    
    def __init__(self,name):
        
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            #list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #for a single card objects
            self.all_cards.append(new_cards)
        pass
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


# In[ ]:


new_player=Player("Somali")


# In[ ]:


new_player.add_cards([mycard,mycard,mycard,mycard])


# In[ ]:


print(new_player)


# In[ ]:


print(new_player.remove_one())


# In[ ]:


print(new_player)


# In[ ]:


#Game setup
player_one=Player("One")
player_two=Player("Two")

new_deck =Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# In[ ]:


game_on=True


# In[ ]:


round_num=0

while game_on:
    round_num+=1
    print(f'round {round_num}')
    if len(player_one.all_cards)==0:
        print('Player 1, out of cards. Player 2 wins!')
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print('Player 2, out of cards. Player 1 wins!')
        game_on=False
        break
    #Start a new game
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    
    at_war=True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
    
            at_war=False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
    
            at_war=False
        else:
            print('War!')
            if len(player_one.all_cards) < 3:
                print("Player1 unable to declare war")
                print("player 2 wins")
                game_one=False
                break
                
            elif len(player_two.all_cards) < 3:
                print("Player2 unable to declare war")
                print("player 1 wins")
                game_one=False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


 # while_at war*


# In[ ]:


n=[1,2,3]


# In[ ]:


n.pop(0)


# In[ ]:




