n1 = str(input("Enter  your name: "))
n2 = str(input("Enter your partner name: "))
lst_n2 = list(n2)
# print(lst_n2)
l1 = len(n1)
l2 = len(n2)
full_len = l1+l2
# print(full_len)
for i in n1:
    for j in lst_n2:
        if i == j:
            full_len = full_len-2
            lst_n2.remove(j)
            break
        pass
# print(full_len)
flames = ['F', 'L', 'A', 'M', 'E', 'S']

flam_len = len(flames)
t_flames = flames*full_len*2

# print(t_flames)
while len(t_flames) >= 1:
    if len(t_flames) > full_len:
        position = t_flames[full_len-1]
        t_flames = t_flames[full_len:]
        temp = "".join(t_flames)
        temp = temp.replace(position, "")
        t_flames = list(temp)
        # print(t_flames)
    else:
        t_flames = t_flames*full_len

# print(position)

if position == 'F':
    print("Both are Friends")
elif position == 'L':
    print("Both are Lovers")
elif position == 'A':
    print("Both have Attraction")
elif position == 'M':
    print("Both will get Married")
elif position == 'E':
    print("Both are Enemies")
else:
    print("Both are Siblings")
