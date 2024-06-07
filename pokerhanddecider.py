import random

Dict ={}#'A':14,'K':13,'Q':12,'J':11,'T':10,9:9,8:8,7:7,6:6,5:5,4:4,3:3,2:2
Dict['2']=2
Dict['3']=3
Dict['4']=4
Dict['5']=5
Dict['6']=6
Dict['7']=7
Dict['8']=8
Dict['9']=9
Dict['T']=10
Dict['J']=1
Dict['Q']=12
Dict['K']=13
Dict['A']=14

def j_counter(hand):
    counter=0
    for x in hand:
        if x=='J':
            counter+=1
    return counter       

def isstraight(hand):
    straighthand=[]
    for i in hand:
        straighthand.append(Dict[i])
    straighthand.sort()
    for x in range(4):
        if straighthand[x]!=straighthand[x+1]-1:
            return False
    return True

def isfourofakinds(hand):
    hand=str(hand)
    counter=0
    max=0
    while counter<len(hand):
        if max<hand.count(hand[counter]):
            max=hand.count(hand[counter])
        counter+=1
    return max==4

def isthreeofakinds(hand):
    hand=str(hand)
    counter=0
    max=0
    while counter<len(hand):
        if max<hand.count(hand[counter]):
            max=hand.count(hand[counter])
        counter+=1
    return max==3

with open("seven.txt","r", encoding="utf-8") as file:
    random_five_hands=[]
    randomnums=[]
    for x in range(5):
        n=random.randint(0,1000)
        randomnums.append(n)
    bids=[]
    highhands=[]
    onepairs=[]
    twopairs=[]
    threeofakinds=[]
    straights=[]
    fullhouses=[]
    fourofakinds=[]
    fiveofakinds=[]
    for id,line in enumerate(file):
        data=line.strip().split()
        hand=data[0]
        bid=data[1]
        for id22,num in enumerate (randomnums):
            if num==id:
                random_five_hands.append((hand,bid))
    print(random_five_hands)
    for id,line in enumerate(random_five_hands):
        hand=random_five_hands[id][0]
        bid=random_five_hands[id][1]
        bids.append(int(bid))
        if all(ele == hand[0] for ele in hand):
            c=0
            place=False
            if len(fiveofakinds)==0:
                fiveofakinds.append((hand,bids[id]))
                continue
            while c<len(fiveofakinds):
                for x in range(5):
                    if Dict[fiveofakinds[c][0][x]]==Dict[hand[x]]:
                        continue
                    elif Dict[fiveofakinds[c][0][x]]<Dict[hand[x]]:
                        break
                    elif Dict[fiveofakinds[c][0][x]]>Dict[hand[x]]:
                        place=True
                        break
                if place:
                    fiveofakinds.insert(c,(hand,bids[id]))
                    break
                if c==len(fiveofakinds)-1:
                    fiveofakinds.append((hand,bids[id]))
                    break
                c+=1

        elif len(set(hand))+3 == len(hand):
            counter=0
            max=0
            while counter<len(hand):
                if max<hand.count(hand[counter]):
                    max=hand.count(hand[counter])
                counter+=1
            if max==4:
                c=0
                place=False
                if len(fourofakinds)==0:
                    fourofakinds.append((hand,bids[id]))
                    continue
                while c<len(fourofakinds):
                    for x in range(5):
                        if Dict[fourofakinds[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[fourofakinds[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[fourofakinds[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        fourofakinds.insert(c,(hand,bids[id]))
                        break
                    if c==len(fourofakinds)-1:
                        fourofakinds.append((hand,bids[id]))
                        break
                    c+=1
            else:
                c=0
                place=False
                if len(fullhouses)==0:
                    fullhouses.append((hand,bids[id]))
                    continue
                while c<len(fullhouses):
                    for x in range(5):
                        if Dict[fullhouses[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[fullhouses[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[fullhouses[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        fullhouses.insert(c,(hand,bids[id]))
                        break
                    if c==len(fullhouses)-1:
                        fullhouses.append((hand,bids[id]))
                        break
                    c+=1
        elif len(set(hand))+2 == len(hand):
            counter=0
            max=0
            while counter<len(hand):
                if max<hand.count(hand[counter]):
                    max=hand.count(hand[counter])
                counter+=1
            if max==3:
                c=0
                place=False
                if len(threeofakinds)==0:
                    threeofakinds.append((hand,bids[id]))
                    continue
                while c<len(threeofakinds):
                    for x in range(5):
                        if Dict[threeofakinds[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[threeofakinds[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[threeofakinds[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        threeofakinds.insert(c,(hand,bids[id]))
                        break
                    if c==len(threeofakinds)-1:
                        threeofakinds.append((hand,bids[id]))
                        break
                    c+=1
            else:
                c=0
                place=False
                if len(twopairs)==0:
                    twopairs.append((hand,bids[id]))
                    continue
                while c<len(twopairs):
                    for x in range(5):
                        if Dict[twopairs[c][0][x]]==Dict[hand[x]]:
                            continue
                        elif Dict[twopairs[c][0][x]]<Dict[hand[x]]:
                            break
                        elif Dict[twopairs[c][0][x]]>Dict[hand[x]]:
                            place=True
                            break
                    if place:
                        twopairs.insert(c,(hand,bids[id]))
                        break
                    if c==len(twopairs)-1:
                        twopairs.append((hand,bids[id]))
                        break
                    c+=1
        elif len(set(hand))+1 == len(hand):
            c=0
            place=False
            if len(onepairs)==0:
                onepairs.append((hand,bids[id]))
                continue
            while c<len(onepairs):
                for x in range(5):
                    if Dict[onepairs[c][0][x]]==Dict[hand[x]]:
                        continue
                    elif Dict[onepairs[c][0][x]]<Dict[hand[x]]:
                        break
                    elif Dict[onepairs[c][0][x]]>Dict[hand[x]]:
                        place=True
                        break
                if place:
                    onepairs.insert(c,(hand,bids[id]))
                    break
                if c==len(onepairs)-1:
                        onepairs.append((hand,bids[id]))
                        break
                c+=1
        elif len(set(hand)) == len(hand):
            c=0
            place=False
            if (isstraight(hand)):
                straights.append(hand)
            elif len(highhands)==0:
                highhands.append((hand,bids[id]))
                continue
            while c<len(highhands):
                for x in range(5):
                    if Dict[highhands[c][0][x]]==Dict[hand[x]]:
                        continue
                    elif Dict[highhands[c][0][x]]<Dict[hand[x]]:
                        break
                    elif Dict[highhands[c][0][x]]>Dict[hand[x]]:
                        place=True
                        break
                if place:
                    highhands.insert(c,(hand,bids[id]))
                    break
                if c==len(highhands)-1:
                    highhands.append((hand,bids[id]))
                    break
                c+=1
    print("highhand",highhands)
    print("onepair",onepairs)
    print("twopair",twopairs)
    print("threeofkind",threeofakinds)
    print("straight",straights)
    print("fullhouses",fullhouses)
    print("fourofakind",fourofakinds)
    print("fiveofakind",fiveofakinds)
    winner=None
    if len(fiveofakinds)!=0:
        winner=fiveofakinds[-1]
    elif len(fourofakinds)!=0:
        winner=fourofakinds[-1]
    elif len(fullhouses)!=0:
        winner=fullhouses[-1]
    elif len(straights)!=0:
        winner=straights[-1]
    elif len(threeofakinds)!=0:
        winner=threeofakinds[-1]
    elif len(twopairs)!=0:
        winner=twopairs[-1]
    elif len(onepairs)!=0:
        winner=onepairs[-1]
    elif len(highhands)!=0:
        winner=highhands[-1]
    winings=sum(bids)-int(winner[1])
    print("winner hand: " + winner[0])
    print("prizemoney:",winings)