import os

class User:
   def __init__(self):
      self.name = ""
      self.address = {
         "street": "",
         "city" : "",
         "state": "",
         "country": "",
         "zipCode": ""
      }
      self.phone = ""

   def getInputs(self):
      self.name = input("Enter your name: ")

      print("Enter your address:\n")
      self.address["street"] = input("Street: ")
      self.address["city"] = input("City: ")
      self.address["state"] = input("State: ")
      self.address["country"] = input("Country: ")
      self.address["zipCode"] = input("Zip code: ")

      print()
      self.phone = input("Enter your phone number: ")

class File:
   def __init__(self):
      self.path = ""
      self.name = ""
      self.delimiter = ","

   def getInputs(self):
      isDir = False
      while not isDir:
         self.path = input("Where would you like to save the file? ")

         isDir = os.path.isdir(self.path)
         if(not isDir):
            print(f"\"%s\" is not a valid directory." % (self.path))

      self.name = input("What is the name of the file? ")      

   def write(self, user):
      try:
         with open(self.path + "\\" + self.name, 'w') as myFile:
            myFile.write(self.formatLine("name",
               "street",
               "city",
               "state",
               "country",
               "zipCode",
               "phone"))

            myFile.write(self.formatLine(user.name,
               user.address["street"],
               user.address["city"],
               user.address["state"],
               user.address["country"],
               user.address["zipCode"],
               user.phone))
      except:
         print(f"There was an error writing the file at: \"%s\\%s\"." % (self.path, self.name))

   def read(self):
      try:
         with open(self.path + "\\" + self.name, 'r') as myFile:
            for line in myFile:
               print(line.rstrip())
      except:
         print(f"There was an error reading the file at: \"%s\\%s\"." % (self.path, self.name))

   def formatLine(self, name, street, city, state, country, zipCode, phone):
      line = ("\"{name}\""
               + self.delimiter
               + "\"{street}\""
               + self.delimiter
               + "\"{city}\""
               + self.delimiter
               + "\"{state}\""
               + self.delimiter
               + "\"{country}\""
               + self.delimiter
               + "\"{zipCode}\""
               + self.delimiter
               + "\"{phone}\""
               +"\n"
            )
      
      return line.format(name=name, street=street, city=city, state=state, country=country, zipCode=zipCode, phone=phone)

def main():
   user = User()
   dirFile = File()

   dirFile.getInputs()
   user.getInputs()

   dirFile.write(user)
   dirFile.read()

main()