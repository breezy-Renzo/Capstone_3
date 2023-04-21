from tabulate import tabulate

#Class defined

class Shoe:


#Constructor that assigns attributes
    
    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

#Function that returns cost 
    def get_cost(self):
        return self.cost

#Function that returns the quantity
    def get_quantity(self):
        return self.quantity

#Function that returns the product
    def get_product(self):
        return self.product

#Function that returns the country
    def get_country(self):
        return self.country

#Function that returns the code
    def get_code(self):
        return self.code


#Function that returns the string format of class object
    def __str__(self):
        return f'{self.product}, {self.country}, {self.code}, {self.cost}, {self.quantity}' 

#Function that reads data of shoe from file
def read_shoes_data():

    try:
        
        with open('inventory.txt', 'r') as f:
            line = f.readlines()
            line_1 = line[1].strip()
            shoe_object = line_1.split(',')
            return shoe_object

    except FileNotFoundError:
        print('File not found!')

##Function that captures info of user and creates new object
def capture_shoes():
    
    country = input('Enter country of shoe: ')
    code = input('Enter code of shoe: ')
    product = input('Enter name of product: ')
    cost = input('Enter cost of shoe: ')
    quantity = input('Enter quantity of shoe: ')

    new_shoe = f'\n{country},{code},{product},{cost},{quantity}\n'
    new_obj = Shoe(country, code, product, int(cost), int(quantity))
    shoes_list.append(new_obj)

    with open('inventory.txt', 'a') as f:
        f.write(new_shoe)
    
    return f'{product} have been captured'


#Function that returns all shoe objects in a tabulated format
def view_all():
    country = []
    code = []
    product = []
    cost = []
    quantity = []

    for line in shoes_list:
        country.append(line.get_country())
        code.append(line.get_code())
        product.append(line.get_product())
        cost.append(line.get_cost())
        quantity.append(line.get_quantity())
    new_list = zip(country, code, product, cost, quantity)    

    print(tabulate(new_list, headers = ('Country','Code', 'Product', 'Cost', 'Quantity')))


#Function that finds shoe with lowest quality and restocks it 
def restock(self):

    amount = int(input('Enter amount you wish to restock product with : '))
    new_amount =self.quantity + amount
    with open('inventory.txt','r') as f:
        line = f.read()
        data = line.replace(str(self.quantity), str(new_amount))

    with open('inventory.txt', 'w') as f:
        f.write(data)


#Function that allows user to enter code of shoe to search for it
def search_shoe():       
        
    search = input('Enter code of shoe you wish to see:')
    for i in range(len(shoes_list)):
        if shoes_list[i].code == search:
            print(f'You have chosen {shoes_list[i].product}')
        else:
            print('Code entered does not exist')
            


#Function that calculates and adds the value of each shoe to each shoe object

def value_per_item(self):

    for line in shoes_list:
        product = line.get_product()
        value = line.get_cost() * line.get_quantity()
        print(f'The value of {product} is {value}')


#Function that finds the shoe with the highest quality andputs it up for sale
def highest_qty():
    max_quant_list = []
    for i in range(len(shoes_list)):
        max_quant_list.append(shoes_list[i].quantity)

    for line in shoes_list:
        product = line.get_product()
        if line.quantity == max(min_quant_list):
            print(f'{product} has been put up for sale!')


#List that stores shoe objects
shoes_list = []

#Object of shoe class
shoe_1 = Shoe(read_shoes_data()[0], read_shoes_data()[1], read_shoes_data()[2], int(read_shoes_data()[3]), int(read_shoes_data()[4]))
        
#Shoe object isadded to list
shoes_list.append(shoe_1)

#While loop that runs until user chooses to exit
while True:

    user_choice = input('''Select one of the options below:

c  -  Capture shoe
va -  View all
r  -  Restock
s  -  Search shoe
h  -  Up for sale
vpt - Value of shoes
e-    Exit
:''').lower()
    
#calls capture_shoes function
    if user_choice == 'c':

        print()
        print(capture_shoes())
        print()

#calls view_all function
    elif user_choice == 'va':

        print()
        view_all()
        print()

#calls restock function
    elif user_choice == 'r':
        
        min_quant_list = []
        for i in range(len(shoes_list)):
            min_quant_list.append(shoes_list[i].quantity)

        for line in shoes_list:
            product = line.get_product()
            if line.quantity == min(min_quant_list):
                restock(line)
                print()
                print(f'{product} has been restocked')
                print()

#calls search_shoe function    
    elif user_choice == 's':
        print()
        search_shoe()
        print()

#calls highest_qty function
    elif user_choice == 'h':
        print()
        highest_qty()
        print()

#calls value_per_item function
    elif user_choice == 'vpt':

        print()
        value_per_item(shoes_list)
        print()

#user option that can end while loop
    elif user_choice == 'e':
        print()
        print('Goodbye')
        exit()

    else:
        print('incorrect choice')
        















