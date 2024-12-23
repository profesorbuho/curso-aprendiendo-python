import re

phones_numbers = """
Phone numbers
099 123 4567
099 748 1234
0964561239
0947898181
099 1214 123 
098 6987 321
"""

single_number = "099 123 45678"
phone_regex = r"^\d{3}[ ]?\d{3,4}[ ]?\d{3,4}$"
if re.match(phone_regex, single_number):
    print( f"El número de telefono {single_number} es correcto." )
else:
    print( f"El número de telefono {single_number} NO es correcto." )

text_1 = "Lorem usuari0-02@hotmail.es ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sodales urna id viverra bibendum. Sed at sem lorem. Duis fermentum erat augue, at iaculis purus eleifend eu. Donec dignissim malesuada orci, in posuere lorem info@profesorbuho.com imperdiet in. Cras convallis sapien ut porttitor lobortis. Suspendisse john.doe@abc.edu.io at scelerisque turpis. Sed posuere egestas mattis. Vestibulum iaculis a metus a luctus. Etiam dictum mi non ana_123@gmail.com nulla dignissim, at vehicula lorem tristique. Orci varius natoque penatibus et magnis dis parl, nascetur. Phasellus ex just, consectetur pepito-27@email.gob.io eget hendrerit et, venenatis non eros. Integer hendrerit in erat consequat tincidunt."

email_regex = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-z]+"
first_email = re.search(email_regex, text_1)
print( first_email )
print( first_email.group() )

lorem_word = re.search(r"lorem", text_1, flags=re.I)
print( lorem_word )

number_123 = re.search(r"123\s$", phones_numbers, flags=re.M)
print( number_123 )

all_emails = re.findall(email_regex, text_1)
print( all_emails )

fruits = "manzana,pera,bana,naranja"
fruits_list = re.split(r",", fruits)
print( fruits_list )

text_2 = "My phone number is 0991234567"
digits_regex = r"\d"
hidden_number = re.sub(digits_regex, "*", text_2)
print( hidden_number )