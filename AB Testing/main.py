import numpy as np
#import modin.pandas as pd --this doesn't work on win10 ray not supported 
import pandas as pd

file = pd.read_csv('ab_data.csv')
print(file.head())
#constructing an array of data : A/B
clickthrough_A = np.array([True] * 136+[False] * 53 )
clickthrough_B = np.array([True] * 153+[False] *36 )

#print(clickthrough_A,clickthrough_B)


def diff_frac(data_A, data_B):
    '''this definition finds the difference between average of data_A and data_B'''
    frac_A = np.sum(data_A)/len(data_A)
    frac_B = np.sum(data_B)/len(data_B)
    return frac_B,frac_A,frac_B-frac_A

'''CTA,CTB,diff_frac_obs = diff_frac(clickthrough_A,clickthrough_B)
print('Click through % of A {}\nClick through % of B {}\nDifference between average of B and A'.format(CTA,CTB,diff_frac_obs))
'''
def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate((data1,data2))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]

    return perm_sample_1, perm_sample_2

def permutation_replicate(data_1,data_2,func,size=1):
    '''generating multiple permutation replicates'''
    perm_replicates = np.empty(size)
    for i in range(size):
        #generating permutation samples
        perm_sample_1, perm_sample_2 = permutation_sample(data_1,data_2)
        #computing test statistic
        perm_replicates[i] = func(perm_sample_1,perm_sample_2)

    return perm_replicates


perm_replicates = permutation_replicate(clickthrough_A, clickthrough_B, diff_frac,10000)

p_value = np.sum(perm_replicates >=diff_frac_obs)/10000
'''p_value : The probability of obtaining a value of your test
statistic that is at least as extreme as what was
observed, under the assumption the null
hypothesis is true'''

print(p_value)

