#21 exercise

import random

#add total_points for two players
total1=0
total2=0
draws=0

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
print(xarti)
color = ["H", "S", "C", "D"]
for i in xarti:
    for j in color:
        xartia.append([i,j])




for round in range (0,100):
#create xartia for each round
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
#first play:pop until first is figure or 10
    while True:
        first=xartia.pop()
        if first[0] in figures or first[0] == 10:
            break
    player1.append(first)
    while sum1<16:
        sum1=0

        player1.append(xartia.pop())
    # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        print(sum1)
    if sum1>21:
        print("P2 wins!")
        total2+=1
    else:
    

        print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
#first play:pop until first is NOT figure and NOT  10
        while True:
            first=xartia.pop()
            if first[0] not in figures and first[0] != 10:
                break
        player1.append(first)
        
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
#print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(sum2)
        if sum2>21: 
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            total1+=1
        elif sum2>sum1:
            print("P2 wins!")
            total2+=1
        else:
            print("draw!")
            draws+=1
 
#print the results 
print("Player1 wins :", total1)
print("Player2 wins :", total2)
print("Draws:",draws)
