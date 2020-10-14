import numpy as np
#import pandas as pd

'''
n = int(input())
address = [input() for i in range(n)]
'''
address = []
with open('route2.txt') as f:
    file_data = f.readlines()
    for line in file_data:
        address.append(line.rstrip()[1:])

print(address)
#dictionary = pd.DataFrame(columns=list(range(33)))
'''
for x in address:
    id_prefix = x.split('/')
    ad = id_prefix[0]
    pre = int(id_prefix[1])
    ad_split = ''.join(['0'*(8-len(bin(int(x))[2:])) + bin(int(x))[2:] for x in ad.split('.')])
    ad_split = ad_split + '0'*(32-len(ad_split))
    a = [int(x) for x in ad_split]
    a.append(pre)
    a = {i:a[i] for i in range(len(a))}
    dictionary = dictionary.append(a, ignore_index=True)

test_list = ['41.74.1.1', '66.31.10.3', '133.5.1.1', '209.143.75.1', '221.121.128.1']
#test_list = ['1.0.128.100', '1.0.137.100', '1.0.120.100']

for test in test_list:
    test = ''.join(['0'*(8-len(bin(int(x))[2:])) + bin(int(x))[2:] for x in test.split('.')])
    dictionary_pre = dictionary
    for i in range(len(test)):
        dictionary0 = dictionary_pre[dictionary_pre[i]==int(test[i])]
        if len(dictionary0) == 0:
            break
        dictionary_pre = dictionary0
    dictionary_sort = dictionary_pre.sort_values(32, ascending=False)
    print(dictionary_sort.index.values[0])
'''
    