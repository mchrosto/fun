import pandas as pd 

people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

df = pd.DataFrame(people)

print(df)

df.set