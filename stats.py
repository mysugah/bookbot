def split_n_count(string):
    words = string.split()
    return print(f"Found {len(words)} total words")

def each_char_count(string):
    lowercase = string.lower()
    str_to_int = {}

    for character in lowercase:
        if character in str_to_int:
            str_to_int[character] += 1
        else:
            str_to_int[character] = 1

    return str_to_int

def sorter(dictionary):
    sorting = []
    def sort_on(items):
        return items["num"]
        
    for entry in dictionary:
        if entry.isalpha() == True:
            sorting.append({
                "char" : entry,
                "num" : dictionary[entry],
            })
        else:
            continue
        
    sorting.sort(reverse = True, key = sort_on)
    return sorting