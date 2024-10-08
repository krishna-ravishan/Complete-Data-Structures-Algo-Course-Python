# HASHING

# Hashing is a method of sorting and indexing data. The idea behind hashing is to allow large amounts of data to be indexed using keys commonly created by formulas.

# Apple -> Magic Function -> 18
# Application -> Magic Function -> 20
# Appmillers -> Magic Function -> 22

# Why is it needed? Say we need to create an app that allows for searching. We want app to perform as fast as possible. Hashing provides for faster searching time complexity of O(1)/O(N). For comparison, searching in tree is O(logn), linkedlist O(N), and array using binary search O(logn)

# Hashing Terminology

# 1. Hash Function: It is a function that can be used to map of arbitrary size to data of fixed size
# 2. Key: It is input data given by the user
# 3. Hash Value: Its a value returned by a hash function
# 4. Hash Table: A DS that implements an associative array abstract data type, a structure that helps map keys to values
# 5. Collision: A collision occurs when two different keys to a hash function produce the same output

# EG: # Apple -> Magic Function -> 20
# Application -> Magic Function -> 20. Therefore we get collisions.

# Hash Functions

# 1. Input from user is of Integer data type
# Mod Function
def mod(number, cellNumber):
    return number % cellNumber

# ASCII Function
def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

# The properties of hash functions:

# 1. It distributes hash values uniformly across hash tables
# 2. It has to use all input data
# 3. Generates unique hash values and avoids collision

# Types of collision resolution techniques

# How to solve the problem of collision. First is direct chaining and second is open addressing under which you have linear probing, quadratic probing, and double hashing.

# DIRECT CHAINING: Implements the buckets as linked list. Colliding elements are stored in this list. Pros are that hash tables never get full but it has poor time complexity for large number of insertions

# Eg if both ABCD and EDGH have hash value 2 then the index 2 of array will consist of a linked list chain where each next/link stores the address of the next node.

# OPEN ADDRESSING: Colliding elements are stores in other vacant buckets. During storage and lookup these are found through so called probing. Easy implementation but problem arises when hash table is full, which affects time complexity for search operation.

# Linear Probing: It places new key into closest following empty cell
# Quadratic Probing: Adding arbitrary quadratic polynomial to the index until empty cell is found. 2 + 2^x where x can be 0 to n for such repeated instances of hash values
# Double Hashing: Interval between probes is computed by another hash function

# Hash Table is Full: (This problem does not arise with double chaining)
# Solution is Open Addressing: create 2x size of current hash table and recall hashing for current keys


# If input size is known we always use open addressing and if we perform delete operation frequently then we use direct chaining

# Practical Use of Hashing
# 1. Used for password verification
# 2. File system path is mapped to physical location on disk

# Hashing vs other Data Structures
#  On an average hashing insertion deletion search performs with O(1) time complexity if hash function is good. If not then it takes O(N) time complexity




