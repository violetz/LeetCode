import sys
sys.path.append('/media/xiaowei/Study/Software Learning/Python/LeetCode')
from DataStructures.LinkedQueue import *

def RevInt(i_num):
    i_total = 0
    q_digits = LinkedQueue()
    while i_num:
        q_digits.enqueue(i_num % 10)
        i_num = i_num / 10
        i_total += 1
    i_revnum = 0
    while not q_digits.is_empty():
        i_revnum = i_revnum * 10 + q_digits.dequeue()
    return i_revnum
    
        
