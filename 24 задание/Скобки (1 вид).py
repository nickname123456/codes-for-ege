s = open('24-301.txt').read()
max_length = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')' and stack:
        start = stack.pop()
        expr = s[start:i+1]
        temp_stack = []
        valid = True
        for c in expr:
            if c == '(':
                temp_stack.append(c)
            elif c == ')':
                if not temp_stack:
                    valid = False
                    break
                temp_stack.pop()
        if valid and not temp_stack:
            max_length = max(max_length, i - start + 1)

print(max_length)