def str2(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'in'

print(str2("play"))  
print(str2("playing"))   
print(str2("go"))        

