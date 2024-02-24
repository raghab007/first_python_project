def read_file(d):
    """This functions reads the text file named laptop.txt and updates the dictionary with  key  as numbers and values as dictionaries having laptop information"""
    file = open("laptop.txt", "r")
    d1 = 1
    for line in file:
        line = line.replace("\n", "")
        line = line.replace("\t", "")
        laptop = line.split(",")
        lap_dict = {
            "Name": laptop[0],
            "Company": laptop[1],
            "Price": int(laptop[2].replace("$", "")),
            "Quantity": int(laptop[3]),
            "Processor": laptop[4],
            "Graphics": laptop[5],
        }
        d.update({d1: lap_dict})
        d1 = d1 + 1
    file.close()
