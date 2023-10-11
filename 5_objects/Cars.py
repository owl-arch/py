from Cars.Bmw import Bmw as myBmw 
from Cars.Audi import Audi
from Cars.Nissan import Nissan


#print(dir(Bmw))
#print(dir(Audi))
#print(dir(Nissan))

ModBMW = myBmw()
ModBMW.outModels()
   
ModAudi = Audi()
ModAudi.outModels()
  
ModNissan = Nissan()
ModNissan.outModels()