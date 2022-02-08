class Solution(object):
    def countPoints(self, rings):
        r_list = []
        g_list = []
        b_list = []
        for i in range(len(rings)/2):
            if rings[i*2] == 'R':
                r_list.append(rings[i*2+1])
            elif rings[i*2] == 'G':
                g_list.append(rings[i*2+1])
            elif rings[i*2] == 'B':
                b_list.append(rings[i*2+1])
        
        return len(set(r_list) & set(g_list) & set(b_list))