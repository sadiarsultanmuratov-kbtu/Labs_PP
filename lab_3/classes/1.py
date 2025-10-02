class string:
    def getstring(self):
        self.sentence=input("Sentense:")
    def printstring(self):
        print("With upper case:"+ self.sentence.upper())
        
mystring=string()
mystring.getstring()
mystring.printstring()