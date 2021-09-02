# A =[1,2,4]
# B= [3,5,7,8,9]
# n = len(A)
# m = len(B)
# p1 = 0
# p2 =0
# C = []
# while p1 < n or p2 < m:
#     if p1 ==len(A):
#         C.append(B[p2])
#     else:

#         if A[p1] < B[p2]:
#             C.append(A[p1])
#             p1 += 1
#         else:
#             C.append(A[p2])
#             p2 += 1
# print(C)


def longestCommonPrefix(strs) :
    if "" in strs:
        return ""

    if len(strs) == 1:
        return strs[0]

    # finding string of min length
    min_len_str = strs[0]
    for string in strs:
        if len(string) < len(min_len_str):
            min_len_str = string
    # print(min_len_str)
            
    ans = ''
    # checking ch present in all strings
    for i in range(len(min_len_str)):
        for j in range(len(strs)):
            
            if strs[j][i] == min_len_str[i]:
                # print(strs[j][i],min_len_str[i])
                ans += min_len_str[i]
                # print(ans,'ans')
                
            else:
                return ans[0:i*len(strs):len(strs)]
            
    return ans[0:(i+1)*len(strs):len(strs)]

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
            

