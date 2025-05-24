def get_num_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for word in text:
        for character in word:
            new_char = character.lower()
            if char_count.get(new_char):
                char_count[new_char]+=1
            else:
                char_count[new_char]=1
    return char_count

def sort_on(dict):
    return dict["num"]

def format_char_count(char_count):
    dict_list = []
    for key,value in char_count.items():
        dict_list.append({"char":key,"num":value})
        
    dict_list.sort(reverse=True,key=sort_on)
    return dict_list

