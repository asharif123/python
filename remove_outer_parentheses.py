##create function to remove outer parentheses
##ex: (()) should output () or ()(()) should output ()()
 def removeOuterParentheses(self, S):
        S = list(S)
        new_list = []
        total = 0
        for index,char in enumerate(S):
            if char == "(":
                total += 1
            elif char == ")":
                total -= 1
##add any chars that are neither opening (total > 1 and char == "(") or 
#closing (total == 0) to 'new_list'
            if (char == "(" and total > 1) or (char == ")" and total != 0):
                new_list.append(char)
        return ''.join(new_list)



removeOuterParentheses('(()())(())')
