import time
import random

def typing_test():
    wrd= ["python is fun", "programming is fun", "Go ahead", " mouse", " hello developer", "plagiarism", "language is easy", "syntax ", "practice", "speed"]

    input("Press Enter ")
    
    expected= random.choice(wrd)
    print(f"Type the wrd: {expected}")
    
    starting_time = time.time()
    user_input = input()
    ending_time = time.time()
    
    if user_input == expected:
        elapsed_time = ending_time - starting_time
        
        wrd_per_minute = (len(expected) / elapsed_time) * 60
        print(f"Hurrah!! You typed the word correctly in {elapsed_time:.2f} seconds.")
        print(f"Your speed is {wrd_per_minute:.2f} wrd per minute.")

    else:
        print("Oops! You made a mistake...Please Try again...")

if __name__ == "__main__":
    typing_test()
