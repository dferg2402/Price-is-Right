#Danae Ferguson
#U33752946
#The program simulates a single bid in the Price is Right! Worked with Nathalie D.

'''
1. Generate random number between $1000 and $5000 for winning price using
   randint(). 

2. Ask 4 players for bid.

3. Check for over bid.

4. Check for exact bid

5. Compare to bid
'''

import random
from math import fabs

win_price = random.randint(1000, 5000)
print(f'${win_price:,.2f}')

bid1 = int(input('Player 1, what is your bid? '))
bid2 = int(input('Player 2, what is your bid? '))
bid3 = int(input('Player 3, what is your bid? '))
bid4 = int(input('Player 4, what is your bid? '))

#While loop to close program after 
count = 0
while count < 1:
    if bid1 > win_price and bid2 > win_price and bid3 > win_price and bid4 > win_price:
        print('Buzz! Aww... everyone has overbid!')
        count += 1

    else:
        #How to do this efficiently 
            #Use or operator for exact price
            #Check if player bid is less than or equal to the winning price
            #Set Minimum difference to 9999 (for overbidders), set reveal price bool to false
            #if player difference is less than minimum difference,
            #set mindiff to player diff, set winning player to player w/ mindiff
            #set reveal price bool to true
            #if reveal price true print winning statement
        if bid1 == win_price:
            print('Ding Ding Ding! One player got it exactly right and gets $500!')
        elif bid2 == win_price:
            print('Ding Ding Ding! One player got it exactly right and gets $500!')
        elif bid3 == win_price:
            print('Ding Ding Ding! One player got it exactly right and gets $500!')
        elif bid4 == win_price:
            print('Ding Ding Ding! One player got it exactly right and gets $500!')
            
        #To find closest bid, I took absolute value between the winning price and
        #each bid and compared them to each other.
        #Marked with 0 because it a is non winning bid
        
        bid_dist1 = fabs(bid1 - win_price)
        bid_dist2 = fabs(bid2 - win_price)
        bid_dist3 = fabs(bid3 - win_price)
        bid_dist4 = fabs(bid4 - win_price)



        if bid_dist1 > bid_dist2:
            bid1 = 0
            if bid_dist2 > bid_dist3:
                bid2 = 0
                if bid_dist3 > bid_dist4:
                    bid3 = 0
                else: bid4 = 0
            else:
                bid3 = 0
        else:
            bid2 = 0
            
        if bid1 != 0:
            if bid_dist1 > bid_dist3:
                bid1 = 0
                if bid_dist3 > bid_dist4:
                    bid3 = 0
            else:
                bid3 = 0
            if bid_dist1 > bid_dist4:
                bid1 = 0
                if bid_dist4 > bid_dist3:
                    bid4 = 0
            else:
                bid4 = 0

        if bid2 != 0:
            if bid_dist2 > bid_dist4:
                bid2 = 0
            else:
                bid4 = 0

        if bid1 != 0:
            print(f'Actual price is ${win_price:,.2f}! Player 1, come on up!')
            
        elif bid2 != 0:
            print(f'Actual price is ${win_price:,.2f}! Player 2, come on up!')

        elif bid3 != 0:
            print(f'Actual price is ${win_price:,.2f}! Player 3, come on up!')

        else:
            print(f'Actual price is ${win_price:,.2f}! Player 4, come on up!')
        count += 1


    
 
        



