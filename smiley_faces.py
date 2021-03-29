def count_smileys(arr):
    count = 0
    for x in arr:
        if x == ':)' or x== ':D' or x== ';-D' or x== ':~)' or x == ';~D' or x==';)' or x == ';D' or x== ':~D'or x== ';-)' or x== ':-D' or x== ':-D':
            count = count+1
        else:
            continue
    return count