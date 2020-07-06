class Solution(object):
    def decodeString(self, s):
        
        if not s:
            return None
        
        stack = []
        cur_str = ""
        cur_num:int = 0
        
        for c in s:
            
            if c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            
            elif c == ']':
                
                cur_str = cur_str * stack.pop()
                cur_str = stack.pop() + cur_str
                
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)                
            else:
                cur_str += c
        
        return cur_str
    
sol = Solution()
assert(sol.decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef')
assert(sol.decodeString('3[a2[c]]') == 'accaccacc')
assert(sol.decodeString('abc3[cd]xyz') == 'abccdcdcdxyz')
    

