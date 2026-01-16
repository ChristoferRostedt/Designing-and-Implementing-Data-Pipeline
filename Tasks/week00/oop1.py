'''
Store personal information
Define each person with data:
    first name
    last name
    age occupation
Create a new person called Matti and assign personal details
'''
class person:
    # def __init__(self, firstName, lastName, age, occupation):
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.age = age
    #     self.occupation = occupation

    firstName = str
    lastName = str
    age = 0
    occupation = str

def main() -> None:
    # Matti = person("Matti", "Suomalainen", 21, "Engineer")

    Matti = person()
    Matti.firstName = "Matti"
    Matti.lastName = "Suomalainen"
    Matti.age = 21
    
    print(Matti.age)
    return None

if __name__ == "__main__":
    main()