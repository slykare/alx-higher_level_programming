#!/usr/bin/python3
'''
1-my_list.py
class MyList that inherits from list.
'''


class MyList(list):
    '''
    class MyList that inherits from list
    '''

    def print_sorted(self):
        '''
        prints the list, but sorted (ascending sort)
        '''

        newlist = self[:]
        newlist.sort()
        print("{}".format(newlist))
