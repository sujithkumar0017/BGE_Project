import json
from faker import Faker
import random
fake = Faker()
class random_data:
     def data(self):
          entity_management = {
              "Asset": {
                "weblink": fake.uri(),
                "identifier":fake.bothify(text='????-########', letters='ABCDE'),
                "rating": fake.random_int(min=0, max=15),
                "factoryBarcode": fake.ean(length=8),
                "description": "This created for testing purpose",
                "model":" ".join(["model",fake.random_int(min=0, max=15)]),
    
                     
          },
           "Asset_category":  {
              "name":" ".join(["model",fake.random_int(min=0, max=20)]) 
                     
          },
          "failure":
          {
            "name": " ".join(["Failure_reason",fake.random_int(min=0, max=20)])
          },
         "manufacture":
             {
                "weblink": fake.uri(),
                "email": fake.email(),
                "phoneCode": random.choice(["+91", "+55","+47","+237"]),
                "phoneNumber": str(random.randint(9000000000, 9999999999)),
                "address": fake.street_address(),
                "Corporate Brand Name":" ".join(["Manufacturer",fake.random_int(min=0, max=20)])
                },
          
         "medical":
            {
            "address": fake.street_address(),
            "phoneCode": random.choice(["+91", "+55","+47","+237"]),
            "phoneNumber": str(random.randint(9000000000, 9999999999)),
            "name": " ".join(["hospital",fake.random_int(min=0, max=20)])
        },
        "dno":
            {
              "name": " ".join(["DNO",fake.random_int(min=0, max=20)])
            },
        "sla":
        {
        "name": " ".join(["Level",fake.random_int(min=0, max=20)]),
        "description": "This created for testing purpose",
        }
          }

          f=open("/home/sujith/codebase/BGE_Framework_Design/TestCases/Package_Client_02","w")
          json.dump(entity_management,f)
          f.close()
     
          