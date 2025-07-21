def merge(S1, S2, S):
    i = j = 0  
    while i + j < len(S):  
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]  
            i += 1
        else:
            S[i + j] = S2[j]  
            j += 1

def merge_sort(S):
    if len(S) < 2:
        return  
    mid = len(S) // 2  
    S1 = S[:mid]       
    S2 = S[mid:]       
    merge_sort(S1)     
    merge_sort(S2)     
    merge(S1, S2, S)   


numbers = [38, 27, 43, 3, 9, 82, 10]

print(f"Original list:", numbers)

merge_sort(numbers)

print(f"Sorted list:  ", numbers)
