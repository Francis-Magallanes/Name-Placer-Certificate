from PIL import Image, ImageDraw, ImageFont
import csv

#this will handle the processing of one certificate
#it will return an edited Image object
def Process_OneName(certificate_img: Image, name:str, position:tuple):
    
    certificate_drawer = ImageDraw.Draw(certificate_img)

    #load the neccesary font. Change this according to your desired font and size
    #Note: This font is clear sans bold
    font = ImageFont.truetype(font = "assets/ClearSans-Bold.ttf", size = 85)

    certificate_drawer.text(position, name, fill = "black", font=font, anchor="ms")


#this function will convert the name of "Last Name, Given Name" to
# "Given Name last Name"
def Lastnamefirst_to_Givennamefirst(names:list) -> list:

    new_names = []
    for name in names:

        if ',' in name:
            name_split = name.split(",")

            #remove the front space in the given if there is
            if ' ' == name_split[1][0]:
                name_split[1].replace(" ", "", 1)
        
    
    
def main():
    
    #adjust this according to where the csv file of the names located
    filepath_csv = "assets/Sci-Py Registration.csv"

    #this will get the names from the csv file
    with open(filepath_csv, newline='') as csv_file:
        csv_file_data = csv.DictReader(csv_file)

        #adjust this so that the name will be retrieved based on the header  of the row names
        names = csv_file_data["Name (Last Name, First Name, Middle Initial)"] 
    
    #remove this if the format of the name follows "Given Name Last Name"
    names = Lastnamefirst_to_Givennamefirst(names)

    #change the filepath to where the template for the certificate can be found
    filepath_certificate = "assets/Sci-Py Certificate Template.png"
    
    #this is for getting the width and height of certificate template
    #remove/ignore this, if not needed
    with  Image.open(filepath_certificate) as cert_img:
        width_img, height_img = cert_img.size
     
    #change this to your desire point where the name will be placed
    #you can use the test_position.py to determine your desired point
    placement_coordinate = (width_img/2, (height_img/2) - 30) 


    Process_OneName(certificate_img, "Francis John N. Magallanes", placement_coordinate)

    certificate_img.show()
    
  
    
    pass

if (__name__ == "__main__"):
    main()