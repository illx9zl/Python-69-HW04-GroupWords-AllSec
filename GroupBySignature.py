def group_by_signature(words: list) -> list:
    pass
    from collections import defaultdict
    groups = defaultdict(list)
    signature_to_first_index = {}
    
    for i, word in enumerate(words):
        if not word.isalpha():
            if not word.isalpha():
                continue
        signature = ''.join(sorted(word))

        if signature not in signature_to_first_index:
            signature_to_first_index[signature] = i
        groups[signature].append(word)
    result_groups = list(groups.values())
    result_groups.sort(key=lambda group: signature_to_first_index[''.join(sorted(group[0]))])
    return result_groups

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
