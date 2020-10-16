### ASCII TEXT GENERATOR - PYTHON

    Ascii Text Generator, it will help you to add beatufull banners to your scripts

![demo](https://i.ibb.co/yYFFpkm/1.png)

### HOW TO USE : 

### INSTALL REQS

    pip install BeautifulSoup4 requests wheel
  
    python setup.py bdist_wheel
    
    pip install -e .
	
    import asciiText
    

#### GET LIST OF AVAILABLE FONTS
	
    asciiText.listFonts(exemple=True,text="TestText")
    

 - exemple : If True it will list all the fonts including exemples if False it will list only the font id  
 
 ###  GENERATE ASCII ART FROM A TEXT
 ![asciigenerator](https://i.ibb.co/0ZnhGff/2.png)

    asciiText.getAscii(text="TextText",font="broadway")

![colorascii](https://i.ibb.co/YBXG36v/color.png)

    asciiText.getAsciiColor(text="JoeVenner",font="broadway",color="green")


### FOR API CALL

 1. LIST FONTS http://artii.herokuapp.com/fonts_list
 2. GENERATE ASCII TEXT http://artii.herokuapp.com/make?text=ASCII+art&font=trek


### TO ADD

 - [ ] Add as python Module
 - [ ] Use it in Offline mode
