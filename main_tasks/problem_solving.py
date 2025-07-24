def get_vowels_count(word:str)->int:
    word=word.lower()
    v=["a","e","i","o","u"]
    counter=0
    for i in word:
        if i in v:
            counter+=1
    return counter



def generate_multiplication_table(x:int)->None:
    print(f"Multiplication table of {x}")
    for i in range(1,x+1):
        print(f"{i } * {x} = {i*x}")
    print("="*20)


def generate_inverted_mario_pyramid(x:int)->None:
    for i in range(1,x+1):
        result=""
        for _ in range(x-i):
            result+=" "
        for _ in range(i):
            result+="*"
        print(result)

if __name__ == "main":
    print(get_vowels_count("Hello World"))
    generate_multiplication_table(5)
    generate_inverted_mario_pyramid(5)