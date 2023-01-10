print ("====== program menentukan max ======")
print("")

bil1 = int(input("masukan bilangan 1 : "))
bil2 = int(input("masukan bilangan 2 : "))
bil3 = int(input("masukan bilangan 3 : "))

if bil1 >= bil2 >= bil3 :
    print("bilangan yang paling besar adalah", bil1)
elif bil1 <= bil2 >= bil3 :
    print("bilangan yang paling besar adalah", bil2)
elif bil1 <= bil2 <= bil3 :
    print("bilangan yang paling besar adalah", bil3)
