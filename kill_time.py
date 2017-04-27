import os,sys

fname = 'game_log_test.log'

klist = []

with open(fname) as f:
    klist = f.readlines()
#    for line ine f:
#        if begin in f:
#            klist.append(f.xreadlines())
#
klist = [x.strip('\n') for x in klist]
#klist = [x.split(' ') for x in klist]
#print klist[0]
start_indices_temp = [i for i, x in enumerate(klist) if x.find("InitGame") > 0]
end_indices = [i for i, x in enumerate(klist) if x.find("Fraglimit") > 0]
#print start_indices, end_indices
if end_indices[0] < start_indices_temp[0]:
    del end_indices[0]

start_indices = []
#go backwards from each "fraglimit" to find the last occurrence of "initgame"
for flr in end_indices:
    for (idx_ig, ig) in enumerate(start_indices_temp):
        if ig > flr:
            start_indices.append(start_indices_temp[idx_ig - 1])
            break
game_lines = zip(start_indices, end_indices)
#print start_indices, end_indices, game_lines[0][1]
#if len(start_indices) != len(end_indices):
#    #looks like Angelo walked in... at least once
#    for x in range(len(end_indices)):
#        if end_indices[x] - start_indices[x] > 90:
#            del start_indices[x]
#print start_indices, end_indices

if(len(start_indices) != len(end_indices)):
    print "error: weird number of games"
    sys.exit(0)
game = []
number_of_games = len(start_indices)
for item in klist[start_indices[0]:end_indices[0]+5]:
    game.append(item.split())
plist = []
for item in game:
    #assign character ids
    if item[1] == "ClientUserinfoChanged:":
        #new player:
        plist.append(item[3].split("\\")[1])
        #print plist
    if len(plist) == 3:
        
#if klist[0] != "^3Match has begun!":
#    sys.exit(0)


rmstr = ' has entered the game'
#plist = [klist[1].strip(rmstr), klist[2].strip(rmstr), klist[3].strip(rmstr)]
#print len(klist)

#loc = []
#for x in range(number_of_games):
#    for y in range(end_indices[x]+1 - start_indices[x]):
#        i = y+start_indices[x]
#        if y < 4:
#            #read in player names
#            print "hi"
#        if(i != len(klist) - 2):
#            loc.append([klist[i].find(plist[x]) for x in range(len(plist))])
#        else:
#            winner = plist[[klist[i].find(plist[x]) for x in range(len(plist))].index(0)]
#
##print loc
#kmat = [[0,0,0],[0,0,0],[0,0,0]]
#sui = [0,0,0]
##acceptor of kill, and donor of kill
#
#for i in range(len(loc)):
#    don = max(loc[i])
#    iacc = loc[i].index(0)
#    idon = loc[i].index(don)
#    if don == 0:
#        sui[idon] = sui[idon] + 1
#    else:
#        kmat[idon][iacc] = kmat[idon][iacc] + 1
#
#print plist[0]," killed ",plist[1]," ",kmat[0][1]," times"
#print plist[0]," killed ",plist[2]," ",kmat[0][2]," times, and had ",sui[0]," suicides.\n"
#print plist[1]," killed ",plist[0]," ",kmat[1][0]," times"
#print plist[1]," killed ",plist[2]," ",kmat[1][2]," times, and had ",sui[1]," suicides.\n"
#print plist[2]," killed ",plist[0]," ",kmat[2][0]," times"
#print plist[2]," killed ",plist[1]," ",kmat[2][1]," times, and had ",sui[2]," suicides.\n"
#
#print "Winner is: ", winner
##print kmat
#    
