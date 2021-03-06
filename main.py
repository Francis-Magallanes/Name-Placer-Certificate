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

            #remove the front space in the given name if there is
            if ' ' == name_split[1][0]:
                name_split[1].replace(" ", "", 1)

            #remove the last space in the given name if there is
            if name_split[1][len(name_split[1])- 1] == ' ':
                name_split[1] = name_split[1][:len(name_split[1]) - 1]

            new_names.append(name_split[1] + " " + name_split[0])
        else:
            new_names.append(name)
    
    return new_names
        
    
    
def main():
    
    #adjust this according to where the csv file of the names located
    filepath_csv = "assets/Sci-Py Registration.csv"

    #this will get the names from the csv file
    #Note: Duplicates will be removed
    with open(filepath_csv, newline='') as csv_file:
        csv_file_data = csv.DictReader(csv_file)

        #adjust the key of the row so that the name will be retrieved
        names = [ row["Name (Last Name, First Name, Middle Initial)"] for row in csv_file_data]
    
    
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

    print("Process Started")

    for name in names:

        with Image.open(filepath_certificate) as certificate_img:
            
            Process_OneName(certificate_img, name, placement_coordinate)

            #adjust this accordingly where the modified photo will be saved
            certificate_img.save("assets/Saved Test Photos/" + name + " Certificate.png")
   
    print("Finished!!!")

if (__name__ == "__main__"):
    main()