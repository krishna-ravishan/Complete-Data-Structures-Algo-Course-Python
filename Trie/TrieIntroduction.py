#  A Trie is a tree based data structure that organises information in a hierarchy.
# It is a prefix tree that is used in the representation of strings over a set of finite alphabets
# Enables fast lookups

# Properties:
# Used to store or search string in a space and time efficient way
# Any node in trie can store non repetitive multiple characters
# every node stores link of next character of string
# Every node keeps track of the end of string

# Problems such as spell checker and auto completion
# We'll use hash map?
# Trie Creation

class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfString = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()

# Inserting a string in Trie
# CASE 1: A Trie is blank. First create  a new Trie Node then add the character to dictionary and link to child node (next character) and keep linking till end of string reached.
# CASE 2: New string prefix is common to string prefix. Traverse to the end of string prefix which is not common, insert the character in the dictionary along with the link to it's child characters
# CASE 3: New string prefix already present as complete string. Add character to end of string node dictionary and link to another end of string node
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully Inserted")
# Seaching for a string in a Trie
# Case 1: String does not exist in trie. Value of root 
# Case 2: String exists in Trie. After string EOS is required. EOS is True
# Case 3: String is a prefix of another string but it does not exist in Trie. EOS is False

    def searchString(self, word):
        current = self.root
        # if word[0] not in current.children:
        #     return False
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        if current.endOfString == True:
            return True
        return False
# Case 1: Some other prefix of string is same as the one that we want to delete
# Case 2: The string is a prefix of other string
# Case 3: Other string is prefix of string
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfStrong = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False

    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

newTrie = Trie()
newTrie.insertString('App')
newTrie.insertString('Api')
print(newTrie)
print(newTrie.searchString('Appp'))
