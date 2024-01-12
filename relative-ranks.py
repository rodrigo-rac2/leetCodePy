# Problem: https://leetcode.com/problems/relative-ranks/

# heap solution:
import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output = []
        score_i = [ s*-1 for s in score] 
        score_h = heapsort(score_i)
        for s in score:
            pos = score_h.index(s*-1)
            match pos:
                case 0:
                    output.append("Gold Medal")
                case 1:
                    output.append("Silver Medal")
                case 2:
                    output.append("Bronze Medal")
                case _:
                    output.append(f"{pos + 1}")
        return output

# ordered list solution
# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         output = []
#         score_h = sorted(score,reverse=True)
#         for s in score:
#             pos = score_h.index(s)
#             match pos:
#                 case 0:
#                     output.append("Gold Medal")
#                 case 1:
#                     output.append("Silver Medal")
#                 case 2:
#                     output.append("Bronze Medal")
#                 case _:
#                     output.append(f"{pos + 1}")
#         return output

