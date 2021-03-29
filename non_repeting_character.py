def first_non_repeating_letter(string):
   # string = string.lower()
    z = ""
    w = ""
    y = string.upper()
    print (string)
    print(y)
    c = 0
    if string == '':
        return z
    for i in y:
        w = ""
        if y.count(i) == 1:
            print (i)
            w = i.lower()
            if string.count(w)==1:
                return w
            return i
        c +=1
    if c>0:
        return ""