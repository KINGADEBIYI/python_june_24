class Dog:
    name = 'precious'
    color = 'black'
    height = '7.2 ft'
    weight = '70lbs'
    breed = 'pitbull'


class Dog():

    def __init__ (self, name, color, height, weight, breed, age):
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight
        self.breed = breed
        self.age = age

    def __str__(self):
        return self.name
    
    def checkSpeed(self):
        if self.breed.casefold() == 'retrival':
            return f'{self.name} is a {self.breed}, can run at least 30kmph'
        elif self.breed.casefold() == 'chihuahua':
            return f'{self.name} is a {self.breed}, can run max 15kmph'
        elif self.breed.casefold() == 'yorkshire':
            return f'{self.name} is a {self.breed}, can run max 15kmph'
        elif self.breed.casefold() == 'malinois':
            return f'{self.name} is a {self.breed}, can run at least 35kmph'
        elif self.breed.casefold() == 'german shepard':
            return f'{self.name} is a {self.breed}, can run at least 35kmph'
        elif self.breed.casefold() == 'pitbull':
            return f'{self.name} is a {self.breed}, can run at least 25kmph'
        else:
            return f'{self.name} speed can not be defined'
        
    def aggresiveness(self):
        if self.breed.casefold() == 'retrival':
            return f'{self.name} is very kind'
        elif self.breed.casefold() == 'chihuahua':
            return f'{self.name} is born wicked'
        elif self.breed.casefold() == 'yorkshire':
            return f'{self.name} is friendly'
        elif self.breed.casefold() == 'malinios':
            return f'{self.name} is very aggresive'
        elif self.breed.casefold() == 'german shepard':
            return f'{self.name} is aggresive'
        elif self.breed.casefold() == 'pitbull':
            return f'{self.name} is max aggression'
        else:
            return f'{self.name} aggression can not be checked'

dog1 = Dog(
            name = 'precious',
            color = 'gray',
            height = 2,
            weight = 5,
            breed = 'pitbull',
            age = 12
        )
dog2 = Dog(
            name = 'john',
            color = 'brown',
            height = 1,
            weight = 3,
            breed = 'basengi',
            age = 12
        )
dog3 = Dog(
            name = 'persie',
            color = 'white',
            height = 2,
            weight = 5,
            breed = 'retrival',
            age = 7
        )
dog4 = Dog(
            name = 'lola',
            color = 'black',
            height = 6,
            weight = 5,
            breed = 'german shepard',
            age = 9
        )

print(dog1.name)
print(dog1.color)


'''
1) create a product object
name, desricption, brand, model, price
return discount

calculate the ttal number of object's price
'''