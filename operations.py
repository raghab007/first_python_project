
# Functions  to buy laptop from manufacturer:
def laptop_id_buy(dictionary):
    """This function takes input of valid laptop id and returns it ..s"""
    invalid_laptop_id = True
    while invalid_laptop_id:
        try:
            laptop_id = int(input("Please provide the ID of the laptop you want to buy: "))
            if laptop_id <= 0 or laptop_id > len(dictionary):
                print("PLZ enter valid laptop id:")  
            else:
                valid_laptop_id = False
                return laptop_id
                

        except:
            print("Pls enter valid laptop ID :)")
            valid_laptop_id = True

def laptop_quantity_buy(dictionary, laptop_id):
    """This function prompts to input laptop quantity and returns it  """
    invalid_laptop_quantity= True
    while invalid_laptop_quantity:
        try:
            laptop_quantity = int(input("how many laptops do you want to buy? "))
            if laptop_quantity <=0:
                print("Please enter valid number of laptop you want to buy!!!!")

            else:
                laptop_quantity_available = dictionary[laptop_id]["Quantity"]
                dictionary[laptop_id]["Quantity"] = laptop_quantity_available + laptop_quantity
                total_price = laptop_quantity * dictionary[laptop_id]["Price"]
                purchased_items = [laptop_id, laptop_quantity, total_price]
                invalid_laptop_quantity = False
                return purchased_items

        except:
            print("Pls enter valid number (dont not enter characters other then number)!!")
            
            
        



    

 # Functions to sell laptop to the customers
 
# Function to get valid laptop id
def laptop_ID(dictionary):
    """The following function prompts the user to input a laptop_id """
    valid_laptop_id = True
    while valid_laptop_id:
        try:
            laptop_id = int(input("Please provide the ID of the laptop you want to sell: "))
            if dictionary[laptop_id]["Quantity"] <= 0:
                print("This laptop is currently out of stock!")
                print("PLZ enter  other  laptop id:")
            
            else:
                valid_laptop_id = False
                return laptop_id
                

        except:
            print("Pls enter valid laptop ID :)")
            
    print("\n")
    
# Function to get  valid 
def laptop_Quantity(dictionary,laptop_id):
    """ The following function prompts the user to input the valid  laptop Quantity and return laptop quantity """
    valid_laptop_quantity = False
    while valid_laptop_quantity == False:
        try:
            laptop_quantity = int(input("How many laptops do you want to buy ?  "))
            laptop_quantity_available = dictionary[laptop_id]["Quantity"] 
            if laptop_quantity_available < laptop_quantity or laptop_quantity<=0:
                print("Please select valid number of laptops")
            else:
                valid_laptop_quantity = True
                return laptop_quantity

        except:
                print("Please enter only numbers !!!!!!!!")

def user_purchased_details(laptop_id, laptop_quantity, dictionary):
    
    """This function updates the laptop dictionary and returns the user purchased items"""
    laptop_quantity_available = dictionary[laptop_id]["Quantity"]
    dictionary[laptop_id]["Quantity"] = laptop_quantity_available - laptop_quantity
    total_price = laptop_quantity * dictionary[laptop_id]["Price"]
    user_purchased_items = [laptop_id, laptop_quantity, total_price]
    
    return user_purchased_items
    
    
    
           
            
            
    


    
    
    
    
