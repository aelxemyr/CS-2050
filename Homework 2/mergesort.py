# Bennett Alex Myers
# CS 2050 - Homework 2
# 8 Feburary 2016

import unittest
import random

class merge_sort:
    
    def merge(self, lst, start, mid, end):
        sortedList = []
        i = start
        j = mid
        
        while i < mid and j < end:
            if lst[i] <= lst[j]:
                sortedList.append(lst[i])
                i += 1
            else:
                sortedList.append(lst[j])
                j += 1
                
        while i < mid:
            sortedList.append(lst[i])
            i += 1
            
        while j < end:
            sortedList.append(lst[j])
            j += 1
            
        for k in range(len(sortedList)):
            lst[start + k] = sortedList[k]
                
    def mergesort(self, lst, start, end):
        if start < end - 1:
            mid = (start + end) // 2
            self.mergesort(lst, start, mid)
            self.mergesort(lst, mid, end)
            self.merge(lst, start, mid, end)
        else:
            return
            
    def sort(self, lst):
        if lst == None:
            return lst
        self.mergesort(lst, 0, len(lst))
        return lst
        
class test_merge_sort (unittest.TestCase):
  def test_none(self):
    self.assertEquals(merge_sort().sort(None), None)
  def test_one(self):
    self.assertEquals(merge_sort().sort([1]), [1])
  def test_two(self):
    self.assertEquals(merge_sort().sort([2, 1]), [1, 2])
  def test_10(self):
    a = list(range(10))
    random.shuffle(a)
    b = list(a)
    b.sort()
    self.assertEquals(merge_sort().sort(a), b)