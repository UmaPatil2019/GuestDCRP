
#file to generate random emails for testing purppose
import random
import string
def random_string_generator(size =5, chars=string.ascii_lowercase+string.digits):
    #an email id with 5 characters is created. for loop concatenates one character a t at time
    #to create 5 characters email id, where each digit/num is convereted to chars
    return  ''.join(random.choice(chars) for x in range(size))