from PIL import Image, ImageDraw, ImageFont

#this will handle the processing of one certificate
#it will return an edited Image object
def Process_OneName(certificate_img: Image, name:str, position:tuple):
    
    certificate_drawer = ImageDraw.Draw(certificate_img)

    #load the neccesary font. Change this according to your desired font and size
    #Note: This font is clear sans bold
    font = ImageFont.truetype(font = "assets/ClearSans-Bold.ttf", size = 85)

    certificate_drawer.text(position, name, fill = "black", font=font, anchor="ms")

   

    
def main():
    
    #change the filepath to where the template for the certificate can be found
    filepath_certificate = "assets/Sci-Py Certificate Template.png"
    certificate_img = Image.open(filepath_certificate)

    width_img, height_img = certificate_img.size

    #change this to your desire point where the name will be placed
    #you can use the test_position.py to determine your desired point
    placement_coordinate = (width_img/2, (height_img/2) - 30) 

    Process_OneName(certificate_img, "Francis John N. Magallanes", placement_coordinate)

    certificate_img.show()
    
  
    
    pass

if (__name__ == "__main__"):
    main()