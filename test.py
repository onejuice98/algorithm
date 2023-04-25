line = input()
ans = ""
for i in line:
    if i == "/n":
        break
    if i.isupper():
        ans = ans + i.lower()
    elsej
        ans = ans + i.upper()
    
print(ans)
