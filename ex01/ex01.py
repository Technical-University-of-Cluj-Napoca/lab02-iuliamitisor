from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for s in strs:
        # Sort letters, make tuple and use as hash table key 
        # Afterwards append original string to key's list
        key = tuple(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

if __name__ == "__main__":
    input_str = input("Enter a list of strings (separated by spaces): ")
    input_strs = input_str.split()
    result = group_anagrams(input_strs)
    print(result)