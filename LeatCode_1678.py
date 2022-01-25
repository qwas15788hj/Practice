class Solution(object):
    def interpret(self, command):
        words = ['G', '()', '(al)']
        list = ['G', 'o', 'al']
        
        for i in range(len(words)):
            command = command.replace(words[i], list[i])
        
        return command