



def longestCommonPrefix(strs):
    output_string = ''
    result_string = ''
    longest_string = strs[0]
    
    for string in strs:
        if len(longest_string) >= len(string):
            longest_string = string
    # print(longest_string,'ls',string)
    i = 0
    while i < len(longest_string):
        for string in strs:
            if longest_string[i] in string[i]:
                output_string += longest_string[i]
            else:
                print(output_string,'return',i)
        i += 1
    print(output_string,'os')
    for i in range(len(strs)):
        if output_string[i] != output_string[0]:
            return 'hi'

    
        
    # if len(output_string) % len(strs) == 0:
    #     set_of_string= set(output_string)
    #     for ch in set_of_string:
    #         result_string += ch
    #     print(result_string)
    #     return result_string
    # else:
    #     ran = len(output_string) % len(strs)
    #     new_string = output_string[:-ran]
    #     set_of_string = set(new_string)
    #     for ch in set_of_string:
    #         result_string += ch
    #     return result_string
    print(list(output_string))
    str_dict = {}
    for ch in list(output_string):
        if ch not in str_dict:
            str_dict[ch] = 1
        else:
            str_dict[ch] += 1
    print(str_dict)
    for k in str_dict.keys():
        if str_dict[k] % len(strs) ==  0:
            result_string += k
        
    return result_string

    


    
    
# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["cir","car"]
print(longestCommonPrefix(strs))
