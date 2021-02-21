#FINAL PROJECT FOR RECIPE : 
MYLIST("KABAKTATLISI, PASTA, FRIEDFRIES")
 
#KABAK TATLISI RECIPE
              Class KabakTatlisi():      
               def __init__(self, pumpkin, sugar, cut, cook, pot):
      self.pumpkin = pumpkin
      self.sugar = sugar
      self.cut = cut
      self.cook = cook
      self.pot = pot  
      
    def cut(self):
        print(self.cut)
    def put(self):
        print(self.pumkin),(self.pot)
    def adding(self):
        print(self.sugar)
    def cook(self):
        print(self.cook)
    
    def showInfo(self):
      
      print("{} the {} properly".format(self.cut),(self.pumpkin))
      print("put the sliced {} in a {}".format(self.pumpkin),(self.pot))       
      print("Add a glass of the {}".format(self.sugar))  
      print("Rest it over a night".)
      print("After a night".)
      print("Take the {} and {} for an hour".(self.pumpkin),(self.cook))
      print("Yummy Yummy in my Tummy!".)   
              
      Kabaktatlisi.showInfo()   
              
      Cut the pumpkin properly        
      Put the sliced pumpkin in a pot        
      Add a glass of the sugar        
      Rest it over a night        
      After a night        
      Take the pan and cook for an hour       
      "Yummy Yummy in my Tummy!"       
          
#PASTA RECIPE
  Class Pasta():
  
  def __init__(self, water, salt, cook, pasta, souce):
    self.water = water
    self.salt = salt
    self.cook = cook
    self.pasta = pasta
    self.souce = souce
  
    def put(self):
        print(self.water)
    def adding(self):
        print(self.salt)
    def adding(self):
        print(self.pasta)
    def cook(self):
        print(self.cook)
    def adding(self):
        print(self.souce)    
   
  def showInfo(self):
        print(A liter {} is {} added in ".format(self.water))
        print("After, we add some {}".format(self.salt))
        print("Add the {} in ".format(self.pasta))
        print("{} the {} for 10 mins".format(self.cook),(self.pasta))    
        #importing the time module
        import time
        #wait for 10 minutes
        time.sleep(10)
        print("filter the pasta.")
        print("Add some {} top".format(self.souce))
        print ("Bon Apetit!".)
        pasta.showInfo()
        
        A liter water is added
        After, we add some salt
        Add the pasta in
        Cook the pasta for 10 mins     
        Filter the pasta.
        Add some souce top.
        Bon Apetit!
              
  #FRIEDFRIES RECIPE
              
        Class Friedfries():
           def __init__(self, oil, potatoes, salt, slice, wash, cut, pot, cook):
    self.oil = oil
    self.potatoes = potatoes
    self.cook = cook
    self.salt = salt
    self.slice = slice
    self.wash = wash
    self.cut = cut
    self.pot = pot
    def wash(self):
        print(self.potatoes)
    def slice(self):
       print(self.slice)       
    def cut(self): 
         print(self.cut)
    def adding(self):
        add(self.oil)
    def cook(self):
        print(self.cook)
    def adding(self):
        print(self.salt) 
              
    def showInfo(self):
              
        print("{} the {} nicely".format(self.wash),(self.potatoes))
        print("{} the {}".format(self.slice),(self.potatoes))
        print("{} the {}".format(self.cut),(self.potatoes))
        print("Add some {} in the {}".format(self.oil),(self.pot))
        print("{} for 15 mins".format(self.cook))
        print("Add some {}".format(self.salt)
        print("Bon Apetit!.")
      
      Friedfries.showInfo()
              
      Wash the potatoes nicely
      Slice the potatoes
      Cut the potatoes
      Add some oil in the pot
      Cook for 15 mins
      Add some salt
      Bon Apetit!        
              
    
