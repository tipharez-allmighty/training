import string
import itertools

true_password = '1234dssd'
first_part = '1234'
possible_length = range(1,5)

possible_options = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def quess_password(first_part, true_password, possible_options, possible_length):
    for length in possible_length:
        for combination in itertools.product(possible_options, repeat=length):
            password_try = first_part + ''.join(combination)
            if password_try == true_password:
                return password_try
    
    return None

        
print(quess_password(first_part, true_password, possible_options, possible_length))
