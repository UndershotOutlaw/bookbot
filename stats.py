def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    count_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1
    return count_dict


def sort_on(d):
    return d['num']


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({'char': ch, 'num': num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list