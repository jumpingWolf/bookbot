def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        char_in_text = char_dict(file_contents)
        ordered_list = char_dict_to_sorted(char_in_text)
        

    print(f"----Begin report of {path}----")
    print(f"{len(words)} words found in the document")
    print()

    for item in ordered_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["count"]} times")

    print("----End Report----")


def sort_on(d):
    return d["count"]


def char_dict_to_sorted(data):
    sorted_list = []
    for char in data:
        sorted_list.append({"char": char, "count": data[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def char_dict(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters        




        
main()
