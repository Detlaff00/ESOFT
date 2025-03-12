def is_valid(s: str) -> bool:
    stack = []
    
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_pairs.values(): 
            stack.append(char)
        elif char in bracket_pairs.keys(): 
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
        else:
            pass
    
    return not stack  

# Примеры использования
print(is_valid("()"))        
print(is_valid("()[]{}"))    
print(is_valid("(]"))        
print(is_valid("([)]"))      
print(is_valid("{[]}"))      
print(is_valid(""))          
