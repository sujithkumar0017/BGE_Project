import json
from faker import Faker
import random
fake = Faker()
class random_data:
     def data(self):
          client={
               "name":fake.name(),
               "phone_number_countryCode":random.choice(["+91", "+55","+47","+237","+1684"]),
               "phone_number":str(random.randint(9000000000, 9999999999)),
               "mobile_number_countryCode":random.choice(["+91", "+55","+47","+237","+1849"]),
               "mobile_number":str(random.randint(9000000000, 9999999999)),
               "address":fake.street_address(),
               "email":fake.email(),
               "city":fake.city(),
               "postalCode":fake.postcode(),
               "website":fake.uri(),
               #Plant Creation
               "plant_name":" ".join([fake.name(),"plant"]),
               "size": fake.random_digit_not_null_or_empty(),
               "acronym":fake.bothify(text='????-########', letters='ABCDE'),
               #Add User
               "user_first_name":fake.first_name(),
               "user_last_name":fake.last_name(),
               "user_email":"".join([fake.first_name(),"@yopmail.com"]),
               "user_password":"qwerty123",
               #Edit Name
               "edit_name":fake.first_name()
                     
          }

          f=open("/home/sujith/codebase/BGE_Framework_Design/TestCases/Package_Client_02/client.json","w")
          json.dump(client,f)
          f.close()