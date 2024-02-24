# Importing all the required modules in the program !
import datetime
from read import *
from write import *
from operations import *



date = str(datetime.datetime.now())
date = date[0:10]

# Removing all the characters other than number in the bill_name
bill_name = str(datetime.datetime.now())
bill_name = bill_name.replace("-", "")
bill_name = bill_name.replace(" ", "")
bill_name = bill_name.replace(":", "")
bill_name = bill_name.replace(".", "")



# Creating dictionary , reading file and updating dictionary
laptop_dictionary = {}
#This read file functions reads all the data of from the text file and stores in dictionary
read_file(laptop_dictionary)
loop = True

#printing store  name
print("========================================================================\n")
print("************************************************************************\n")
print("")
print("Hello welcome to   Islington Laptop Store, Hope you are doing good (:")
print("")
print("************************************************************************\n")
print("========================================================================\n")

while loop == True:
    # Reading text file named laptop.txt and displaying all the available laptops
    print(
        "=================================================================================================================="
    )
    print(
        "S.N.\tLaptop Name\t\tCompany Name\tPrice\t\tQuantity\t Processor\t\tGraphics Card"
    )
    print(
        "================================================================================================================="
    )

    file = open("laptop.txt", "r")
    a = 1
    for line in file:
        print(a, "\t" + line.replace(",", "\t\t"))
        a = a + 1
    print(
        "***************************************************************************************************************"
    )
    file.close()
    print("\n")
# Prompting the user to input the following options !!
    you_want = input(
        """______________________________________________________________________
               * Given below are some of the options for you to carry out needed operations.
               * ____________________________________________________________________________
               * \n
               * press 1 to sale the laptop to the customer.
               * Press 2 to purchase from manufacture.
               * Press 3 to exit from the system.
               * \n
        **************************************************************************************
                        """
    )
    # If User selects "1" then this block will be executed !!
    if you_want == "1":

        # Calling the laptop_ID function and storing the returned value i.e valid laptop id in the variable
        laptop_id = laptop_ID(laptop_dictionary)
        # Calling laptop_Quantity function to get the laptop quantity 
        laptop_quantity = laptop_Quantity(laptop_dictionary,laptop_id)

        # All the purchased items will be stored in purchased_items list
        purchased_items = []
        purchased_items.append(user_purchased_details(laptop_id,laptop_quantity,laptop_dictionary))
        update_stock(laptop_dictionary)
        want_to_buy_other = input("Do you want to buy other laptops yes/no ").lower()
        while want_to_buy_other  == "yes":
            laptop_id = laptop_ID(laptop_dictionary)
            laptop_quantity = laptop_Quantity(laptop_dictionary, laptop_id)
            purchased_items.append(user_purchased_details(laptop_id,laptop_quantity,laptop_dictionary))
            update_stock(laptop_dictionary)
            want_to_buy_other= input("Do you want to buy other laptops yes/no ").lower()
            if want_to_buy_other != "yes":
                want_to_buy_other= "no"
                
        want_to_ship = input("DO YOU WANT TO YOUR LAPTOP TO BE SHIPPED? (yes/no) ").lower()
        
        # Asking the user about the shiiping 
        shipping_cost = 0
        grand_total = 0
        if want_to_ship == "yes":
            location = input("Are you from kathmandu  ?(yes/no) ").lower()
            location = location.lower()
            if location == "yes":
                shipping_cost = 250
                grand_total = grand_total + shipping_cost
                
                print("Your product will be shipped in your location! ")
            elif location == "no":
                    shipping_cost = 500
                    grand_total = grand_total + shipping_cost
                    print("Your product will be delivered in some time !!")

        elif want_to_ship =="no":
                shipping_cost = 0
                print("Please visit our shop to take your product")
                
            

       

        total = 0

        for i in purchased_items:
            total = total + i[2]

        

        grand_total = total + grand_total
        
            

        contact_number = input("Enter your contact number: ")
        user_name = input("Enter your name: ")

        # prining the bill in the terminal
        print("\n")
        print("\t\t\t Islington Laptop store( authorized Laptop store)")
        print("\n")
        print("\t\t\t\t _____Laptop Bill_____")
        print("\n")
        print("\t\t  New Baneshwar, Kathmandu")

        print("\t\t  Phone Number:981234561")
        print("\n")
        print(f"Date :{date }") 
        print("\t\t\t\tUser Purchased details")
        print("\n")
        print("--------------------------------------------------------------------")
        print(f"\tUser Name: {user_name}")
        
        print(f"\tPhone Number: {contact_number}")
        print("---------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------------------------------------------")
        print("Item Name\t\tTotal Quantity\t\tLaptop Price\t\t TotalPrice")
        print("--------------------------------------------------------------------------------------------------------")
        # Printing all the details of laptop bought by the customer in the screen..
        for i in purchased_items:
            print(
                
                laptop_dictionary[i[0]]["Name"],
                "\t\t",
                i[1],
                "\t\t\t","$",
                laptop_dictionary[i[0]]["Price"],"*",i[1],
                "\t\t",
              "    $",int(laptop_dictionary[i[0]]["Price"])*int(i[1])
            )
        print("\n")
        print("\t")
        print("*********************************")
        if shipping_cost > 0:
            print(f"The shipping cost is: ${shipping_cost}")
        print(f"The total price is: {grand_total}$")
        
        print("**********************************")
        print("\n")
        print("a")
        # Calling generate bill function to generate bill by creating unique text file
        generate_bill_sell(user_name,bill_name,contact_number,purchased_items,laptop_dictionary,grand_total,date)
        
        # Asking the user if he wants to exit from the system or not. 
        want_to_exit = input("DO you want to exit from our system:(Y/N): ").lower()
        if want_to_exit =="y":
            loop = False

       
                
    # If user selects 2 the following block of code will be executed 
    elif you_want == "2":
        distributor = input("From which distributor do you want to buy laptop: ")
        company_phone = input("Distributor phone number ?")
        laptop_id = laptop_id_buy(laptop_dictionary)
        laptop_quantity = laptop_quantity_buy(laptop_dictionary,laptop_id)
        purchased_details = []
        purchased_details.append(laptop_quantity)
        update_stock(laptop_dictionary)
        want_to_buy_again = input("DO you want to buy again(Y/N").lower()
       
       # Asking if company wants to buy other laptops 
        while want_to_buy_again == "y":
            laptop_id = laptop_id_buy(laptop_dictionary)
            laptop_quantity = laptop_quantity_buy(laptop_dictionary,laptop_id)
            purchased_details.append(laptop_quantity)
            update_stock(laptop_dictionary)
            want_to_buy_again = input("Do you want to buy again(y/n? ").lower()
        vat = 13
        total_price = 0
        for i in purchased_details:
            total_price = total_price + i[2]
        total_price_with_vat = total_price + total_price * (vat/100)  


        

        #printing laptop bill on the screen
        
        print("\t\t\t Islington Laptop store(Apple authorized store) ")
        print("\n")
        print("\t\t\t\t _____Laptop Bill_____")
        print("\n")
        print("\t\t  New Baneshwar, Kathmandu")
        print("\t\t  Phone Number:981234561")
        print(f"\t\t  Date of Purchase: {date}")
        print("\n")
        print("========================================================")
        print("\t\tLaptop Purchase details")
        print("=========================================================")
        print("")
        print("Distributor Name" + (distributor))
        print("Phone Number:" + company_phone)
        print("\n")
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("Item Name\t\t\t\t\tQuantity\t\t\tLaptop Price\t\t\tTotal Price")
        print("----------------------------------------------------------------------------------------------------------------------------")
        for i in purchased_details:
            print(
                laptop_dictionary[i[0]]["Name"]+"\t\t\t",
            "\t\t",
            str(i[1]),
            "\t\t\t\t",
            "$" + str(laptop_dictionary[i[0]]["Price"]),
            "\t\t\t\t"
            "$"+str(laptop_dictionary[i[0]]["Price"]*i[1])
            )
        
        print("-----------------------------------------------------------------------------------------------------------------------------")    
        print("\n")
        print("The total price without vat :"+"$"+str(total_price))
        print("\nThe total price with 13% vat:"+"$"+str(total_price_with_vat))
        
        print("\n")

        print("------------------------------------------------------------------------------------------------------------------------------")



        #creating unique laptop bill

        generate_bill_buy(distributor,bill_name , company_phone, purchased_details , laptop_dictionary, total_price, total_price_with_vat,date)

        want_to_exit = input("Do you want to exit from the system(y/n)")
        if want_to_exit =="y":
            loop= False
        
        

    elif you_want == "3":
        loop = False
        print("Thank you for visiting us. See you soon")
        print("\n")
        print("We are ready  for any time if you need any help !")
    
