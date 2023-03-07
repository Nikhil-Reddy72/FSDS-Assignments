#!/usr/bin/env python
# coding: utf-8

# # Q1:  What exactly is []?

# ## Answer:
# The square bracket "[]" is indicated for listing the items. The empty square bracket means it contains no items.

# # Q2: In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# 
# ## Answer: 
# 
# spam[2] = 'hello'
# because spam[2] indicates the the index position of third value.

# # Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# 
# # Q3. What is the value of spam[int(int('3' * 2) / 11)]?
# 
# ## Answer:
# 
# the value of spam[int(int('3' * 2) / 11)] is [3].

# In[8]:


[int(int('3' * 2) / 11)]


# # Q4:What is the value of spam[-1]?
# 
# ## Answer:
# 
# The vlaue is 'd'. because it is negative indexing so, it starts in revers order.

# In[9]:


spam=['a', 'b', 'c', 'd']
print(spam[-1])


# # Q5: What is the value of spam[:2]?
# 
# ## Answer:
# The value is ['a', 'b']. because initial index number is given none and end index number is given 2. it means it will print upto 1 index value. 2 index value is excluded.

# In[20]:


spam=['a', 'b', 'c', 'd']
print(spam[:2])


# # Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.
# 
# # Q6. What is the value of bacon.index('cat')?
# 
# ## Answer:
# the value of bacon.index('cat') is 1

# In[21]:


bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.index('cat'))


# # Q7:How does bacon.append(99) change the look of the list value in bacon?
# 
# ## Answer:
#  bacon.append(99) change the look of the list value like [3.14, 'cat', 11, 'cat', True, 99].

# In[22]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99)
print(bacon)


# # Q8. How does bacon.remove('cat') change the look of the list in bacon?
# 
# ## Answer:
# 
# bacon.remove('cat') change the look of the list in bacon is like [3.14, 11, 'cat', True].

# In[23]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat')
print(bacon)


# # Q9. What are the list concatenation and list replication operators?
# 
# ## Answer:
# The operators for list concatenation is +, while the operator for replication is *.

# # Q10. What is difference between the list methods append() and insert()?
# 
# ## Answer:
# 
# The append() method will add items at end of the list only. But where as insert() method will add items anywhere in the list.

# # Q11. What are the two methods for removing items from a list?
# 
# ## Answer:
# The del() and remove() are the two methods for removing items from the list.

# # Q12. Describe how list values and string values are identical.
# 
# ## Answer:
# 
# Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with in and not in operators.

# # Q13. What's the difference between tuples and lists?
# 
# ## Answer:
# 
# lists are mutable , they can have values added, removed or changed. Tuples are written using parentheses,(and),while lists are use the square brackets [and]. The Tuples are immutable, thy cannot be changed at all. 

# # Q14. How do you type a tuple value that only contains the integer 42?
# 
# ## Answer:
# 
# (42,)(the trailing comma is mandatory). without comma we will get int data type not tuple data type.

# In[24]:


TUPLE1 = (42,)
print(type(TUPLE1))

TUPLE1 = (42)
print(type(TUPLE1))


# # Q15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# 
# ## Answer:
# 
# the tuple() and list() functions, respectively.

# # Q16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# 
# ## Answer:
# 
# They contain references to list values

# # Q17. How do you distinguish between copy.copy() and copy.deepcopy()?
# 
# ## Answer:
# 
# #### The copy.copy() function will do a shallow copy of a list, While the copy.deepcopy() function will do a deep copy of a list. That is ,only copy.deepcopy() will duplicate any lists inside the list.

# In[ ]:




