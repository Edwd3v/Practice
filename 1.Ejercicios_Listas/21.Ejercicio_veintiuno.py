# 3. Genera una lista con las primeras letras de cada palabra en una lista de strings.

def run():

    words = ["apple", "banana", "naranja", "pera", "uva"]
    '''first_letter = []

    for word in words:
        first_letter.append(word[0])
    print(first_letter)
    '''

    first_letter_2 = [word[0] for word in words]
    print(first_letter_2)

if __name__ == '__main__':
    run()