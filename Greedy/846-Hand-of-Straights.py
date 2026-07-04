from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        num_map = Counter(hand)

        for card in sorted(num_map):
            while num_map[card]>0:
                for nxt in range(card,card+groupSize):
                    if num_map[nxt]==0:
                        return False
                    num_map[nxt]-=1
        
        return True
            