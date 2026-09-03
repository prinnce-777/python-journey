dict = {
    "a": 10,
    "b": 20,
    "c": 30
} 
dict2 ={}
for key in dict:  #key prints the keys of the dictionary
    t = dict[key]
    dict2[t] = key
print(dict2)