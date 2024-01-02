filepath = 'input7.txt'
from collections import Counter
import numpy as np
hands = dict()
with open(filepath) as fp:
   line = fp.readline()
   while line:
       hands[line.strip('\n').split()[0]]= int(line.strip('\n').split()[1])
       line = fp.readline()

def convertToHex(hand,isWild):
  if not isWild:
    return hand.replace('A','E').replace('K','D').replace('Q','C').replace('J','B').replace('T','A')
  else:
    return hand.replace('A','D').replace('K','C').replace('Q','B').replace('J','1').replace('T','A')
       
hands_list = list(hands.keys())
handClass = {6:set(),5:set(),4:set(),3:set(),2:set(),1:set(),0:set()}
for cur_hand in hands_list:
  hand_count = Counter(cur_hand)
  counts = list(hand_count.values())
  count_count = Counter(counts)
  if 5 in count_count:
    handClass[6].add(cur_hand)
  elif 4 in count_count:
    handClass[5].add(cur_hand)
  elif 3 in count_count:
    handClass[3+count_count[2]].add(cur_hand) # If there's a pair, add to full house, else 3oak
  elif 2 in count_count:
    handClass[count_count[2]].add(cur_hand) # Add to handClass 1 or 2 if it's pair or two pair
  else:
    handClass[0].add(cur_hand)

winnings = 0
rank = 1
for i in range(0,7):
  if len(handClass[i])==0:
    continue
  cur_hand_list = list(handClass[i])
  cur_list_hex = []
  for h in cur_hand_list:
    cur_list_hex.append(convertToHex(h,False))
  cur_list_dec = []
  for ch in cur_list_hex:
    cur_list_dec.append(int(ch,16))
  sorted_idx = list(np.argsort(cur_list_dec))
  for idx in sorted_idx:
    winnings+= rank*hands[cur_hand_list[idx]]
    rank+=1
print(winnings)

# Part 2
hands_list = list(hands.keys())
handClass = {6:set(),5:set(),4:set(),3:set(),2:set(),1:set(),0:set()}
for cur_hand in hands_list:
  hand_count = Counter(cur_hand)
  counts = list(hand_count.values())
  count_count = Counter(counts)
  if 'J' in hand_count:
    if hand_count['J']>=4:
      handClass[6].add(cur_hand)
    elif hand_count['J'] == 3:
        handClass[5+count_count[2]].add(cur_hand) # If pair, add to 5oak, else 4oak
    elif hand_count['J'] == 2:
      if 3 in count_count:
        handClass[6].add(cur_hand)
      elif count_count[2]==2:
        handClass[5].add(cur_hand) # If there's another pair besides J
      else:
        handClass[3].add(cur_hand) # Pair of Js and 3 unique, 3oak
    elif hand_count['J']==1:
      if 4 in count_count:
        handClass[6].add(cur_hand)
      elif 3 in count_count:
        handClass[5].add(cur_hand)
      elif 2 in count_count:
        handClass[2+count_count[2]].add(cur_hand)
      else:
        handClass[1].add(cur_hand)
  else:
    if 5 in count_count:
      handClass[6].add(cur_hand)
    elif 4 in count_count:
      handClass[5].add(cur_hand)
    elif 3 in count_count:
      handClass[3+count_count[2]].add(cur_hand) # If there's a pair, add to full house, else 3oak
    elif 2 in count_count:
      handClass[count_count[2]].add(cur_hand) # If there's another pair, add to
    else:
      handClass[0].add(cur_hand)
      
winnings = 0
rank = 1
for i in range(0,7):
  if len(handClass[i])==0:
    continue
  cur_hand_list = list(handClass[i])
  cur_list_hex = []
  for h in cur_hand_list:
    cur_list_hex.append(convertToHex(h,True))
  cur_list_dec = []
  for ch in cur_list_hex:
    cur_list_dec.append(int(ch,16))
  sorted_idx = list(np.argsort(cur_list_dec))
  for idx in sorted_idx:
    winnings+= rank*hands[cur_hand_list[idx]]
    rank+=1
    
print(winnings)