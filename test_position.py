'''
This python file is also for showing the coordinates where the name will be placed in the
certificate.
'''
from PIL import Image, ImageDraw


#change the filepath to where the template for the certificate can be found
filepath_certificate = "assets/Sci-Py Certificate Template.png"
certificate = Image.open(filepath_certificate)

width, height = certificate.size

#change this to your desire point where the name will be placed
placement_coordinate = (width/2, height/2) 

certificate_drawer = ImageDraw.Draw(certificate)
certificate_drawer.point([placement_coordinate], fill = (255,0,0))

#Note that a point is already drawn in the picture. However, it is very small
#Try to zoom in based on the coordinate placed unitl you see a red dot
certificate.show()