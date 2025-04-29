def combine_anagrams(words_array):
    anagrams = []
    for idx, word in enumerate(words_array):
        if any(word in internal_list for internal_list in anagrams): continue
        local_anagrams = [word]
        for temp_word in words_array[idx+1:]:
            if len(temp_word) == len(word) and sorted(temp_word) == sorted(word):
                local_anagrams.append(temp_word)
        anagrams.append(local_anagrams)
    return anagrams

assert combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar","creams", "scream"]) == [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]