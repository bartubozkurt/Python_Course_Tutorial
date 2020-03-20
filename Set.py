# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:27:40 2020

@author: Bartu

Listeleri benzerdir.
    En önemli özelliği index siz ve sırasız elemanlardan oluşur.
    Veri tekrarı söz konusu olamaz. Tüm elemanlar eşssizdir.(unique)
    Bu veri yapısı performanslı bir data sağlar 
    Listede olan veriyi değiştiremezsin !"""
    
    
studentsSet = {"Bartu","Ali","Osman","Ahmet"}
print(studentsSet)     #Python bu verileri kendi algoritmasına göre sıralıyor 
                       # Set'in en önemli özelliği budur sırasız ve indexsiz
                       
for student in studentsSet:
    print(student)
                    
print("derin" in studentsSet) #Liste içinde derin var mı küçük büyük harf duyarlı False verir!
print("Bartu" in studentsSet) #Liste içinde Bartu var mı küçük büyük harf duyaarlı True verir!

if "Osman" in studentsSet :
    print("Listede var!")
    
studentsSet.add("Bozkurt")  # Listeye ekleme
print(studentsSet)


studentsSet.update(["John","Bench","Marianna","Tracey"])
print(studentsSet)

print(len(studentsSet))
studentsSet.remove("Osman") #Eleman Siler!
print(len(studentsSet))
x = studentsSet.pop()
print(len(studentsSet))
print(studentsSet)
print(x) #Çıkarılan kişi !

y = studentsSet.pop()
print(y) # Çıkarılan kişi !

print(studentsSet)
print(len(studentsSet))

z = studentsSet.clear()
print(z) # Listeyi sildi !

del studentsSet # Set ten kurtulduk !
# print(studentsSet)  Artık böyle bir Set yok !

studentsSet2 = set("abc")
print(studentsSet2)
