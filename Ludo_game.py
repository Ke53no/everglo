import random

#make a blank map
Map = [0] * 52

#set up wrap point
wrap_list = [4, 17, 30, 43]
for number1 in wrap_list:
    Map[number1] = 1

#set up dashline and start point of dashing
dashline = [[80] * 4, [80] * 4, [80] * 4, [80] * 4]
dash_list = [10, 23, 36, 49]
for number2 in dash_list:
    Map[number2] = 2

#colour the map
red_list = list(range(1, 52, 4))
green_list = [i + 1 for i in red_list]
yellow_list = [i + 2 for i in red_list]
blue_list = [i - 1 for i in red_list]

#set up players and their tokens
playernum = list(range(0, 4))
playertokens = [[70]*4, [70]*4, [70]*4, [70]*4]

#print(Map)
#print(red_list)
#print(green_list)
#print(yellow_list)
#print(blue_list)

def roundup():
    for player in range(0, 4):
        for pos in playertokens[player]:
            if pos > 51:
                playertokens[player][playertokens[player].index(pos)] = pos - 52


def playgame(playernum):
    rollnum = random.randint(1,6)
    print('You got a ' + rollnum)
    to_take_off_num = playertokens[playernum].count(70)
    if rollnum == 6:
        decision = input("take off or move 6 steps? (T/M)")
        if decision == 'T':
            playertokens[playernum][to_take_off_num - 1] = 0 + 13 * playernum
        elif decision == 'M':
            chosen_token = int(input('which plane to move? (1/2/3/4)'))
            playertokens[playernum][chosen_token - 1] += rollnum
            roundup()
    else:
        chosen_token = int(input('which plane to move? (1/2/3/4)'))
        playertokens[playernum][chosen_token-1] += rollnum
        roundup()
    for pos in playertokens[playernum]:
        if pos in wrap_list:
            playertokens[playernum][playertokens[playernum].index(pos)] = pos + 12
        elif pos > dash_list[playernum]:
            playertokens[playernum][playertokens[playernum].index(pos)] = 80
            dashline[playernum][playertokens[playernum].index(pos)] = pos - dash_list[playernum]


