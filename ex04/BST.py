class Node:
    def __init__(self, word : str):
        self.word = word
        self.left = None
        self.right = None

class BST:                   
    def __init__(self):
        self.head = None

    def insert_node(self, current_node: Node, new_node: Node) -> None:
        if new_node.word < current_node.word:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_node(current_node.left, new_node)
        elif new_node.word > current_node.word:
            if current_node.right is None:
                current_node.right = new_node
            else: 
                self.insert_node(current_node.right, new_node)

    def insert(self, new_node: Node) -> Node:
        if self.head is None:
            self.head = new_node
        else:
            self.insert_node(self.head, new_node)
        return self.head

    def find_prefix(self, current_node: Node, prefix: str, result: list[str]) -> list[str]:
        if current_node is None:
            return
        self.find_prefix(current_node.left, prefix, result)
        if current_node.word.startswith(prefix):
            result.append(current_node.word)
        self.find_prefix(current_node.right, prefix, result)
        
    def autocomplete(self, prefix: str) -> list[str]:
        result = []
        self.find_prefix(self.head, prefix, result)
        return result
    
def read_dictionary(filename: str) -> list[str]:
    """Reads a dictionary file and returns a list of words.

    Args:
        filename (str): The name of the file containing the dictionary.
    Returns:
        list[str]: A list of words from the dictionary.
    """
    with open(filename, "r") as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    return words