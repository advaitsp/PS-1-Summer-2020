import sys

class Contact_Details:

    def __init__(self,name,number,address):

        self.name=name
        self.number=number
        self.address=address

phone_dir={}

try:
     phone_book=open("phonebook.txt",'r',encoding='utf-8')

     for line in phone_book:

        #print(line)

        s=list(line.split(","))

        #print(s[0])

        Detail1=Contact_Details(s[0],s[1],s[2])

        dict_phone[Detail1.name]=Detail1

        #print(Detail1.name)

except:

    print ((sys.exc_info()[0]),"occured")

finally:

    phone_book.close()


flag=0

while(flag==0):

    print("Enter 1 to add contact")

    print("Enter 2 to update contact")

    print("Enter 3 to display contact")

    print("Enter 4 to delete contact")

    print("Enter any other no. to terminate ")

    choice = int(input())

    



    if(choice==1):

        name=input("Enter name ")

        number=input("Enter number ")

        address=input("Enter address ")

        Detail2=Contact_Detail(name,number,address)

        check=0

        if name in dict_phone:

            check=1

        if check==0:

            try:

                phone_book=open("phonebook.txt",'a+',encoding='utf-8')

                phone_book.write("{},{},{}\n".format(name,number,address))

                dict_phone[name]=Detail2

            except:

                print ((sys.exc_info()[0]),"occured")

            else:

                print("Contact succesfully added")

            finally:

               phone_book.close()

        else:

            print("Name already exists")

            print()

    



    elif(choice==2):

        name=input("Enter name ")

        number=input("Enter number ")

        address=input("Enter address ")

        check=0