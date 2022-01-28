class Solution(object):
    def findCenter(self, edges):
        a = edges[0][0]
        b = edges[0][1]
        if a in edges[1]:
            return a
        else:
            return b