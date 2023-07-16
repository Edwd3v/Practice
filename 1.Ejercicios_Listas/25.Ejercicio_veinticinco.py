# Filtra los strings de una lista que tengan más de 5 caracteres.

def run():

    words = ["apple", "banana", "car", "dog", "cat", "book", "tree", "sun", "moon", "chair", "computer", "music", "rain", "water", "fire", "flower", "sky", "bird", "love", "friend"]

    string_5 = []

    # Manera larga de representar la lista 
    for word in words:
        if len(word) > 4:
            string_5.append(word)
    
    print(string_5)

    # short mode
    string_51 = [word for word in words if len(word) > 4]
    print(string_51)


if __name__ == '__main__':
    run()