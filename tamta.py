str=input("Enter ")
strings=[]
for i in range(4):
    strings.append(input ("Enter") )
longest_string_length = max([len(string) for string in strings])
print(f"The length of the longest string is {longest_string_length}.")