

def main() -> str:
    _word = input("Enter a word : ").lower()
    word:list = [str(i) for i in _word]
    length_of_words:int  = len(word)
    print(word)
    print(length_of_words)
    
    pointer_1:int  = 0
    pointer_2:int  = int(length_of_words)-1

    results = []
    try:
        for i in range(length_of_words):
            ptr1_value = word[pointer_1]
            ptr2_value = word[pointer_2]
            if pointer_1 == None or pointer_2 == None:
                results.append(0)
                return "Not a word!"


            if ptr1_value == ptr2_value:
                pointer_1 += 1
                pointer_2 -= 1
                results.append(1)

            else:
                results.append(0)

        if (results.index(0)):
            return "No!, it is not a palindrome"
    except ValueError:
        return "YES!, It is a palindrome!."
        
print(main())