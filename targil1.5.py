

def longestName():
    with open("names.txt") as file:
        return max([line.strip() for line in file],key=len)



print(longestName())