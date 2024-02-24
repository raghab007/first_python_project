def update_stock(dictionary):
    """This function updates the file named as laptop.txt by updating the laptop stock.."""
    file = open("laptop.txt", "w")
    for values in dictionary.values():
        for key, value in values.items():
            if key == "Price":
                value = str(value)
                value = "$" + value
                file.write(str(value))
                file.write(",")
                file.write("")
            elif key == "Graphics":
                file.write(str(value))
            else:
                file.write(str(value))
                file.write(",")
                file.write("")
        file.write("\n")
    file.close()

def generate_bill_sell(user_name,bill_name,contact_number,user_purchased_details,laptop_dictionary,grand_total,date):
    """This function generates unique bill while selling laptop to the customer """
    
    file = open(user_name+bill_name, "w")
    file.write("\t\t\t Pokhrel Laptop store(Apple authorized store) ")
    file.write("\n")
    file.write("\t\t\t\t _____Laptop Bill_____")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t Sandhikharka, Arghakhanchi\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t Phone Number:981234561\n")
    file.write("\n")
    file.write("Purchase Date: ")
    file.write(date)
    file.write("\n")
    file.write("==============================================\n")
    file.write("\t\tUser Purchase details\n")
    file.write("==============================================\n")
    file.write("\n")

    file.write("user name:" + (user_name))
    file.write("\n")
    file.write("Phone Number:" + contact_number),
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Item Name\t\t\tQuantity\t\t\tLaptop Price\t\t\ttotal price")
    file.write("------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    for i in user_purchased_details:
        file.write(laptop_dictionary[i[0]]["Name"])
        file.write("\t\t\t")
        file.write(str(i[1]))
        file.write("\t")
        file.write("\t\t\t"+"$   " + str(laptop_dictionary[i[0]]["Price"]))
        file.write("*")
        file.write(str(i[1]))
        file.write("\t\t\t")
        file.write("$")
        file.write(str(laptop_dictionary[i[0]]["Price"]*i[1]))
        file.write("\n")
    file.write("\nThe total price is:")
    file.write("$" + str(grand_total))
    file.write("\n")

    file.write("**************************************************")
    
def generate_bill_buy(distributor,bill_name , company_phone, purchased_details , laptop_dictionary, total_price, total_price_with_vat,date):
    """This function generates bill in the text file"""
    file = open(distributor + bill_name, "w")
    file.write("\t\t\t Pokhrel Laptop store(Authorized store) ")
    file.write("\n")
    file.write("\t\t\t\t _____Laptop Bill_______")
    file.write("\n")
    file.write("\t\t  Sandhikharka, Kathmandu\n")
    file.write("\t\t  Contact Number:981234561\n")
    file.write("\n")
    file.write("\t\tDate_of_purchase: "+date)
    file.write("\n")
    file.write("=====================================================================\n")
    file.write("\t\t\t\t\tLaptop Purchase details\n")
    file.write("=====================================================================\n")
    file.write("\n")

    file.write("Distributor Name" + (distributor))
    file.write("\n")
    file.write("Phone Number:" + company_phone),
    file.write("\n")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Item Name\t\t\tQuantity\t\tLaptop Price\t\t\ttotal price")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------")
    file.write("\n")
    
    for i in purchased_details:
        file.write(laptop_dictionary[i[0]]["Name"])
        file.write("\t\t"+str(i[1]))
        file.write( "\t\t\t\t")
        file.write("$" +str(laptop_dictionary[i[0]]["Price"]))
        file.write("\t\t\t")
        file.write("\t$")
        file.write(str(laptop_dictionary[i[0]]["Price"]*i[1]))
        file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("The total price without vat :")
    file.write("$"+str(total_price))
    file.write("\n")
    file.write("\nThe total price with 13% vat:")
    file.write("$" + str(total_price_with_vat))
    file.write("\n")
       

    file.write("-----------------------------------------------------------------------------------------------------")
    file.close()
    
    
