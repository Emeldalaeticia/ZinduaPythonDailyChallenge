f = open('eng_words.txt', 'r')


f = open('eng_words.txt', 'r')

def find_palindromes(filename):
    palindromes = []
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if word == word[::-1]:
                    palindromes.append(word)
    return palindromes
palindromes = find_palindromes('eng_words.txt')
for word in palindromes:
    print(f"{word}: is palindromic")

with open('palindromes', 'w') as f:
    for word in palindromes:
        f.write(f"{word}: is palindromic\n")