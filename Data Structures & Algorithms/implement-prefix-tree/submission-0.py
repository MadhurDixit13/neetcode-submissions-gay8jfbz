class Node:
  def __init__(self):
    self.isEnd = False
    self.children = [None] * 26 
  

class PrefixTree:

    def __init__(self):
        self.head = Node()

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.head
        for i in word:
            if curr.children[self.char_to_index(i)] == None:
                curr.children[self.char_to_index(i)] = Node()
                curr = curr.children[self.char_to_index(i)]
            else:
                curr = curr.children[self.char_to_index(i)]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.head
        for i in word:
            if curr.children[self.char_to_index(i)] == None:
                return False
            else:
                curr = curr.children[self.char_to_index(i)]
        if not curr.isEnd:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for i in prefix:
            if curr.children[self.char_to_index(i)] == None:
                return False
            else:
                curr = curr.children[self.char_to_index(i)]
        return True

        
        