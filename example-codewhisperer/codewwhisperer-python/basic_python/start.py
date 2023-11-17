# write a function to return the random number from 100 to 999
import random
import string

def random_number():
    return random.randint(100, 999)

# generate the list of fake name with minimum length 5 and maximum length 10
def generate_fake_name(length):
    return "".join(random.choices(string.ascii_letters, k=length))
    

# write the main method to run script

if __name__ == "__main__":
    print(random_number)
    print(generate_fake_name(7))
