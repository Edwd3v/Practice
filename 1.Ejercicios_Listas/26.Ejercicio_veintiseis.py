# Dada una lista de palabras, genera una lista que contenga las palabras en mayúsculas.

def run():

    words = ["apple", "banana", "car", "dog", "cat", "book", "tree", "sun", "moon", "chair", "computer", "music", "rain", "water", "fire", "flower", "sky", "bird", "love", "friend"]  

    # Long Mode
    '''
    upper = []  
    
    for word in words:
        word = word.upper()
        upper.append(word)
    print(upper)
    '''

    # Short mode
    upper_2 = [word.upper() for word in words ]
    print(upper_2)

if __name__ == '__main__':
    run()