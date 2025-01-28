//Merge Strings Alternately

def merge_alternately(s1, s2):
    merged = []
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            merged.append(s1[i])
        if i < len(s2):
            merged.append(s2[i])
    return ''.join(merged)

a = input("Enter 1st string: ")
b = input("Enter 2nd string: ")

print(merge_alternately(a, b))
