stuff= list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))

class PartyAnimal:
   x= 0
   name= ''
   def __init__(self, nam):
       self.name= nam
       print(self.name, 'constructed')

   def party(self) :
     self.x= self.x + 1
     print(self.name, 'party count', self.x)
     
     def __del__(self):
        print('I am Destructed', self.x)

s= PartyAnimal('Sally')
j= PartyAnimal('Jim')

s.party()
j.party()
s.party()