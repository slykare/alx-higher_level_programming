#!/usr/bin/python3
'''
100-my_int.py
Inherits from int
'''


class MyInt(int):
    '''
    Class MyInt that inherits from int
        MyInt is a rebel. MyInt has == and != operators inverted
    '''
    def __eq__(self, otehr):
        '''
        Method that returns != check
        '''
        return int.__ne__(self, otehr)
    
    def __ne__(self, otehr):
        '''
        Method that returns == check
        '''
        return int.__eq__(self, otehr)
