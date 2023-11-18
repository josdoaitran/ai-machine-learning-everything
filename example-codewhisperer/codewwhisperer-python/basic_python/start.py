# write a function to return the random number from 100 to 999
import random
import string

def random_number():
    return random.randint(100, 999)

# generate the list of fake name with minimum length is 5 and maximum length is 10
def fake_name_generator(min_length=5, max_length=10):
    return ''.join(random.choices(string.ascii_letters, k=random.randint(min_length, max_length)))
    

# write the executable main method to run this script
if __name__ == '__main__':
    print(random_number())
    print(fake_name_generator())
    print(fake_name_generator(max_length=8))
    



