from search_engine import search_loop
from BST import BST, Node, read_dictionary
import random

if __name__ == "__main__":
    dictionary_words = read_dictionary("dictionary.txt")
    random.shuffle(dictionary_words[:2000]) # shuffle so tree is more balanced
    bst = BST()
    for word in dictionary_words[:2000]:
        bst.insert(Node(word))
    print("All words inserted! Type to search.")
    search_loop(bst)