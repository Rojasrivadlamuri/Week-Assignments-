#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1.TEAM ASSESMENTS

The Team Leader of Testing team of XYZ company decided to assess the team members by organising a programming event. So he gave the team a task.
The task is given an array of size N, find the number of distinct elements in the array and print them in ascending order. Those members who answer, will get some reward.
Write a program to help the Team Leader to evaluate the solutions of the team members.

Input format:
The first line contains a single integer that denotes the size of the array, N.
The second line contains N space separated integer values of the array.

Output format:
The first line is an integer that denotes the number of the distinct elements i nthe array.
The second line is a series of integers seperated by space that denotes the distinct elements.

Sample Input 1:
5
1 2 1 2 1
Sample Output 1:
2
1 2

Sample Input 2:
5
145 25 21 25 36
Sample Output 2:
4
21 25 36 145


# In[4]:


n=int(input("enter number of elements:"))
list1=list(map(int,input("\nenter the number:").split()))
set1=set(list1)
list2=list(map(int,set1))
list2.sort()
print(len(list2))
for i in list2:
    print(i,end=" ")


# In[ ]:





# In[ ]:





# In[ ]:


Q2.ANUSHKA’S PROBLEM

Anuska has created a robot that will take instructions and work accordingly. Due to budget problem, she has set the memory low. To overcome that, she has to encode the instruction. Given the instruction S, count the consecutive characters and each character will be folowed by its frequency.
For example, if the instruction is "aaaabb", the encoded instruction is "a4b2".

Note:If the frequency is one, the count need not be printed.

Input format:
The first input is a string that denotes the instruction, S.

Output format
Output is a string that denotes the encoded string.

Sample input 1:
aaaabb
Sample output 1:
a4b2

Sample input 2:
sggvvvgss
Sample output 2:
sg2v3gs2 


# In[24]:


def decoding(s):

    i = 0
    while( i < len(s) - 1 ) :
        count = 1
        while s[i] == s[i+1] :
            i += 1
            count += 1
            if i + 1 == len(s) :
                break
        print(str(s[i]), end = "")
        if count!=1:
            print(str(count), end="")
        i += 1
    print()
if __name__  == "__main__" :

    decoding(input("Enter a string:"))


# In[ ]:





# In[ ]:


Q3.SKILL TESTING
Amar's team is assigned with a project that deals with the digital signals. He is aware that the digital signals will be represented as arrays. He wants to test his team with respect to their strength in arrays.As part of the skill testing, the  task is as follows.
You are given an array of integers of size N.
Consider all its contiguous subarrays of length k and find the maximum sum.
Do this for all k from 1 to the length of the input array.
Write a program to evaluate the task done by the kids.

Input format:
The first line contains a single integer denotes the size of the array, N.
The second line contains N-space separated integer that corresponds to the values of the array.

Output format:
The output consists of N-space separated integer values of the result array.

Sample Input 1:
5
-1 2 1 3 -2
Sample Output 1:
3 4 6 5 3

Explanation:
For inputArray = [-1, 2, 1, 3, -2], the output should be [3, 2, 1, 0, 0].
The contiguous subarray
    of K = 1, each subarray will have 1 element. The sub-array with maximum sum is [3]. So result[0] = 3.
    of K = 2, each subarray will have 2 elements. The sub-array with maximum sum is [1,3]. So result[1] = 4.
    of K = 3, each subarray will have 3 elements. The sub-array with maximum sum is [2,1,3]. So result[2] = 6.
    of K = 4, each subarray will have 4 elements. The sub-array with maximum sum is [-1,2,1,3]. So result[1] = 5.
    of K = 5, each subarray will have 5 elements. The sub-array with maximum sum is [-1,2,1,3,-2]. So result[1] = 3.
So the result array is [3, 4, 6, 5, 3].

Sample Input 2:
5
2 3 2 -2 3
Sample Output 2:
3 5 7 6 8 


# In[ ]:





# In[ ]:





# In[ ]:




