import sys

def nim_minimax(piles, max_player):
    # base case: if no stones left, return 1 if max_player else -1
    if all(n == 0 for n in piles):
        return -1 if max_player else 1
  
    # initialize best value to -infinity for max player and +infinity for min player
    best_value = -sys.maxsize if max_player else sys.maxsize
  
    # iterate over piles
    for i in range(len(piles)):
     if piles[i] == 0:
           continue
  
        # try removing one stone
     for j in range(piles[i]+1):
        if j == 0: 
           continue
        piles[i] -= j
        value = nim_minimax(piles, not max_player)
        piles[i] += j
  
        # update best value
        if max_player:
            best_value = max(best_value, value)
            if best_value == 1:
                return best_value
        else:
            best_value = min(best_value, value)
            if best_value == -1:
                return best_value
  
    return best_value

print ("Enter the coins in piles: ")
p1 = input("Pile 1: ")
p2 = input("Pile 2: ")
p3 = input("Pile 3: ")
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)

piles = [p1, p2, p3]
if nim_minimax(piles, True)==1:
    print("Player 1 will always win if playing optimally")
else:
    print("Player 2 will always win if playing optimally")
