846. Hand of Straights
Medium

Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

#my own solution using python3 after solving identical question 1296:


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = Counter(hand)
        for card in hand: 
            if freq[card] > 0:
                for i in range(card, card + groupSize):
                    if freq[i] == 0:
                        return False
                    freq[i] -= 1
        return True
