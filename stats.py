def word_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def character_count(book):
    case = book.lower()
    characters = list(case)
    character_count={}
    for character in characters:
        if character in character_count:
            character_count[character] +=1
        else:
            character_count[character]= 1
    return character_count



