#First string
firstString = "Python is awesome!"

#Second String
secondString = "PyThOn iS aWeSoMe!"

if(firstString.upper() == secondString.upper()):
    print("The strings are same.")
else:
    print("The strings are not same.")
print("------------------------------")

#Substring function
message = "Hello World!"
print(message[2:5]) # 2.ci indeksten 5 e kadar yaz!
newMessage = message[:4] #Bastan itibaren o indise kadar verir
print(newMessage)
print("------------------------------")

#len function
print(len(message)) #13 karater
print("------------------------------")
newMessage2 = message[len(message)-1:len(message)]
print(newMessage2)
print("------------------------------")

#Lower Upper
print(message.upper())
print(message.lower())
print("------------------------------")

#Replace
print(message.replace("W","K"))
print(message)
print("------------------------------")

#Split ve Strip
info = "   Hi I'm Bartu Bozkurt and I'm 21 years old!".strip()
print(info.split())
print("Yaşı = " +  info.split(" ")[6])
print("Adı = " +  info.split(" ")[2])

#input
name = input("Adınız?")
sayi1 = input("Sayı 1 =?")
sayi2 = input("Sayı 2 =?")
print(int(sayi1)+int(sayi2))