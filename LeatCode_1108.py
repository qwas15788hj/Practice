class Solution(object):
    def defangIPaddr(self, address):
        list = address
        
        return list.replace('.', '[.]')