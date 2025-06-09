def get_num_words(split_string):
    num_words = len(split_string.split())
    #return f'{num_words} words found in the document'
    return num_words

def get_char_count(split_string):
    out_dict = {}
    for c in split_string.lower():
        if not c in out_dict.keys():
            out_dict[c] = 0
        out_dict[c] += 1
    return out_dict

def sort_counts(count_dict):
    out_list = []

    def sort_on(dict):
        return dict["num"]

    for k in count_dict:
        if k.isalpha():
            out_list.append({"char":k,"num":count_dict[k]})

    out_list.sort(reverse=True,key=sort_on)
    return out_list

def print_report(split_string, filepath="books/frankenstein.txt"):
    num_words = get_num_words(split_string)
    count_dict = get_char_count(split_string)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}')
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")

    for x in sort_counts(count_dict):
        print(f'{x["char"]}: {x["num"]}')
