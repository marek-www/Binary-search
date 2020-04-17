# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:56:19 2020

@author: Marek
"""
def define_list():

    defined_list = list()
    while True:        
        inp = input('Insert number to the list or enter "done":\n')
        if inp == 'done':
            break
        else:
            try:
                num = int(inp)
            except:
                print('Not a number!')  
        defined_list.append(num)
    defined_list.sort()
    return(defined_list)

def searched_num():
    
    while True:
        try:
            num = int(input('What number are you looking for?\n'))
            break
        except:
            print('Not a number!')
    return num
        
def list_construct(*args):
    
    default_list = list()
    
    for arg in args:
        default_list.append(arg)
    default_list.sort()
#    print(default_list)
    return default_list

def search(number, lst):
    
    i = 0
    while True:
        
        i += 1
        if len(lst) == 1:
            print(f'Not found after {i} iterations')
            break
        
        if x > lst[(len(lst)//2)]:
            lst = lst[len(lst)//2:]
            
        elif x < lst[(len(lst)//2)]:
            lst = lst[:len(lst)//2]
            
        else:
            print(f'Found in {i} iterations')
            break    

x = searched_num()
#data = list_construct(32, 4, 88, 93, 13, 35, 24, 19, 55, 44, 77, 66, 69, 5, 42, 36, 59)
data = define_list()
search(x, data)