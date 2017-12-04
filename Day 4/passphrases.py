# Day 4: High-Entropy Passphrases
# http://adventofcode.com/2017/day/4

def check_unique_passphrases(words, check_anagrams=False): 
    unique_words = []
    for word in words:
        # Part two
        if check_anagrams:
            word = ''.join(sorted(word)) # sort letters a->z
        if word not in unique_words:
            unique_words.append(word)
        else:
            return False
    return True

def main():
    total_one = 0
    total_two = 0
    with open('input.txt', 'r') as file: 
        for row in file: 
            words = row.split()
            total_one += check_unique_passphrases(words)
            total_two += check_unique_passphrases(words, True)
    print('Part one: ' + str(total_one))
    print('Part two: ' + str(total_two))

if __name__ == '__main__': 
    main()