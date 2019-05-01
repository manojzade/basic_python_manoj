# 15)	WAP to reverse/inverse key:value like below.
dict1 = { 'a': 1, 'b':2 }
# Expected result : dict2 = { 1: 'a', 2: 'b' }

new_dict={}
new_dict= dict([(b,a) for  a,b in dict1.items()])
print(new_dict)
