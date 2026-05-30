# numbers = []

# count = int(input("How many numbers do you want to enter: "))

# for i in range(count):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# def add(numbers):
#     return sum(numbers)

# def subtract(numbers):
#     result = numbers[0]

#     for i in numbers[1:]:
#         result -= i

#     return result

# def multiply(numbers):
#     result = 1

#     for i in numbers:
#         result *= i

#     return result

# def divide(numbers):
#     result = numbers[0]

#     for i in numbers[1:]:

#         if i == 0:
#             return "Zero Division Error"

#         result /= i

#     return result

# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     print("Result:", add(numbers))

# elif choice == 2:
#     print("Result:", subtract(numbers))

# elif choice == 3:
#     print("Result:", multiply(numbers))

# elif choice == 4:
#     print("Result:", divide(numbers))

# else:
#     print("Invalid choice")



# numbers = []

# num =  int(input("how many numbers want do enter in calculator : "))

# for i in range(num) :
#     new_num =  int(input("Enter your number : "))
#     numbers.append(new_num)



# def add(numbers) :
#     return sum(numbers)


# def subtract(numbers) :
#     result =  numbers[0]

#     for i in numbers[1: ] :
#         result = result - i
#     return result


# def multiply(numbers) :
#     result =  1

#     for i in numbers :
#         result = result * i
#     return result

# def division(numbers) :
#     result = numbers[0]

#     for i in numbers[1 : ] :
#         if i == 0 :
#             return f"zero divison error occured!"
#         else :
#             result  = result / i
#     return result



# print("1.Add")
# print("2.subtract")
# print("3.Multiply")
# print("4.Divide")

# choice = int(input("Enter your operation number : "))

# if choice == 1 :
#     print("Addition : ",add(numbers) )
# elif choice == 2 :
#     print("Subtract : ",subtract(numbers))
# elif choice == 3 :
#     print("Multiply : ",multiply(numbers))
# elif choice == 4 :
#     print("Division : ",division(numbers))
# else :
#     print(f"Invalid numbers,please try again later!")

# data = {"website": "Google", "url": "https://google.com"}

# # File me data SAVE karne ke liye (dump)
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)

# # File se data READ karne ke liye (load)
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data["website"]) # Output: Google

# data = {
#     "website" : "google",
#     "url" : "https://google.com"
# 

# with open("data.json","w") as file :
#     result = json.dump(data,file,indent= 10)

# with open("data.json","r") as file :
#     result =  json.load(file)
#     print(result["website"])


# import os
# import json

# # File ka naam jahan data save hoga
# FILE_NAME = "contacts.json"

# def load_contacts():
#     """File se data read karne ke liye function"""
#     # Pehle check karte hain ki kya file sach me computer me exist karti hai
#     if not os.path.exists(FILE_NAME):
#         return [] # Agar file nahi hai, to khali list return karo
    
#     try:
#         with open(FILE_NAME, "r") as file:
#             # File se JSON data read karke Python list me badalna
#             return json.load(file)
#     except json.JSONDecodeError:
#         # Agar file khali hai ya corrupted hai, to khali list return karo
#         return []

# def save_contacts(contacts_list):
#     """File me data write (save) karne ke liye function"""
#     with open(FILE_NAME, "w") as file:
#         # Python list ko JSON format me file me write karna
#         json.dump(contacts_list, file, indent=4)
#     print("🎉 Contact successfully save ho gaya!")

# def show_contacts(contacts_list):
#     """Saare contacts screen par dikhane ke liye function"""
#     if not contacts_list:
#         print("\n📭 Contact Book khali hai!")
#         return
        
#     print("\n--- 📞 AAPKE CONTACTS ---")
#     for index, person in enumerate(contacts_list, start=1):
#         print(f"{index}. Naam: {person['name']} | Phone: {person['phone']}")

# # ---- MAIN PROGRAM LOOP ----
# def main():
#     # Program shuru hote hi purana data load karo (READ OPERATION)
#     contacts = load_contacts()
    
#     while True:
#         print("\n======= MENU =======")
#         print("1. Saare Contacts Dekhein (Read)")
#         print("2. Naya Contact Add Karein (Write)")
#         print("3. Program Band Karein")
        
#         choice = input("Apna option chunein (1/2/3): ")
        
#         if choice == "1":
#             show_contacts(contacts)
            
#         elif choice == "2":
#             name = input("Naam likhein: ")
#             phone = input("Phone number likhein: ")
            
#             # Naya contact ek dictionary ke roop me banaya
#             new_contact = {"name": name, "phone": phone}
            
#             # List me add kiya
#             contacts.append(new_contact)
            
#             # File me permanent save kiya (WRITE OPERATION)
#             save_contacts(contacts)
            
#         elif choice == "3":
#             print("👋 Bye Bye! Application band ho rahi hai.")
#             break
#         else:
#             print("❌ Galat option! Kripya 1, 2 ya 3 hi chunein.")

# # Program ko run karne ke liye
# if __name__ == "__main__":
#     main()



# import os 
# import json

# FILE_LIST = 'contact.json'

# def save_contacts(contact_list) :
#  with open(FILE_LIST,"w") as file:
#   json.dump(contact_list,file,indent= 10)

#  print(f"\n your contact is sucessfully saved on here!")


# def read_contact() :
#     if not os.path.exists(FILE_LIST) :
#         return []
    
#     try :
#        with open(FILE_LIST,"r")  as file :
#           return json.load(file)
#     except json.JSONDecodeError :
#        return []


# def show_contact(contact_list) :
#    if not contact_list :
#       return f"your contact book in empty!"
    
#    print(f"\nyour contact on below it : \n")
#    for index,person in enumerate(contact_list,start=1) :
#       print(f"{index}. person : {person["name"]} | contact : {person["contact"]} \n")


# def serach_contacts(contact_list) :
#    if not contact_list : 
#       return f"I have not contact for search ! "
   
#    search = input("Enter your search name : ").lower()
#    found = False

#    for person in contact_list :
#       if search in person["name"].lower() :
#         print(f"your search qurey is found out : {person["name"]} | phone : {person["contact"]}" )
#         found = True
    
#    if not found :
#       print(f"sorry,I can not found out your search ! ")

# def main() :
#    contacts = read_contact()

#    while True :
#         print(f"1. you can read your contact log ! ")
#         print(f"2. you can write your contact log ! ")
#         print(f"3. you can exit this from contact log ! ")
#         print(f"4. you can search  your name ! ")

#         choice = int(input("Enter your number : "))

#         if choice == 1 :
#             show_contact(contacts)

#         elif choice == 2 :
#             name = input("Enter your name : ")
#             contact =  int(input("enter your nubmer : "))

#             new_contacts =  {"name" : name, "contact" : contact}

#             contacts.append(new_contacts)

#             save_contacts(contacts)

#         elif choice == 3 :
#            print(f"your application is close on that point!")
#            break

#         elif choice == 4 :
#            serach_contacts(contacts)
#         else :
#            print(f"please,enter a proper nubmer according to order !")



# if __name__ == "__main__" :
#       main()

# import os
# import json

# FILE_NAME = "contacts.json"

# def save_contacts(contact_list):
#     with open(FILE_NAME, "w") as file:
#         json.dump(contact_list, file, indent=4) # indent=4 se file saaf dikhti hai
#     print("your contacts is saved successfully!")

# def read_contacts():
#     if not os.path.exists(FILE_NAME):
#         return []
#     try:
#         with open(FILE_NAME, "r") as file:
#             return json.load(file)
#     except json.JSONDecodeError:
#         return []

# def show_contact(contact_list):
#     # Agar list khali hai toh yahan se return ho jao
#     if not contact_list:
#         print("Your contact book is empty!")
#         return 

#     print("\n--- Contact List ---")
#     for index, person in enumerate(contact_list, start=1):
#         # Yahan single quotes (') use kiye hain keys ke liye
#         print(f"{index}. person : {person['name']} | phone : {person['phone']}")
#     print("--------------------")

# def search_contacts(contact_list):
#     if not contact_list:
#         print("I have no contact book!")
#         return 
   
#     search = input("Enter your search name : ").lower()
#     found = False

#     for person in contact_list:
#         if search in person["name"].lower():
#             # Yahan bhi single quotes (') use kiye hain
#             print(f"Found -> Name: {person['name']} | phone : {person['phone']}")
#             found = True
      
#     # Ab ye IF statement loop ke BAHAR hai
#     if not found:
#         print("No match found in your contact book!")

# def main():
#     contacts = read_contacts()

#     while True:
#         print("\n1. Read your contact book!")
#         print("2. Write your contact book!")
#         print("3. Search your name in contact book!")
#         print("4. Exit from inside your contact book!")
        
#         choice = input("Enter your choice: ") # int() hata diya taaki agar koi galat word likhe toh crash na ho

#         if choice == "1":
#             show_contact(contacts)
      
#         elif choice == "2":
#             name = input("Enter your name : ")
#             # Phone ko string rakhna safe hai taaki zero (0) se suru hone wale number kharab na hon
#             phone = input("Enter your phone number : ") 

#             new_contacts = {"name": name, "phone": phone}
#             contacts.append(new_contacts)
#             save_contacts(contacts)

#         elif choice == "3":
#             search_contacts(contacts)
      
#         elif choice == "4":
#             print("You have exited from this contact book!")
#             break

#         else:
#             print("Please enter a proper number according to order!")

# if __name__ == "__main__":
#     main()

import re


# text = "hello palent"


# pattern = r"hello|palents"

# result = re.findall(pattern,text)

# print(result)

import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x)


# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())

# import re

# def check_phone():
#     print("\n--- 📞 PHONE NUMBER VALIDATION ---")
#     user_phone = input("Apna phone number enter karein (Format: XXXXX-XXXXX):\n> ").strip()
    
#     phone_pattern = r"^\d{5}-\d{5}$" 
#     # Yahan ^ aur $ ka matlab hai ki poori string isi format mein honi chahiye
    
#     if re.match(phone_pattern, user_phone):
#         print("✅ Valid Phone Number! Yeh bilkul sahi format hai.")
#     else:
#         print("❌ Invalid Phone Number! Kripya 5 digits, fir hyphen (-), fir 5 digits likhein.")

# def check_email():
#     print("\n--- ✉️ EMAIL VALIDATION ---")
#     user_email = input("Apna Email ID enter karein:\n> ").strip()
    
#     email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
#     if re.match(email_pattern, user_email):
#         print(f"✅ Valid Email! '{user_email}' ek sahi email address hai.")
#     else:
#         print("❌ Invalid Email! Kripya sahi format use karein (e.g., name@example.com).")

# def check_date():
#     print("\n--- 📅 DATE FORMAT CONVERTER ---")
#     user_date = input("Koi bhi date enter karein (Format: DD/MM/YYYY):\n> ").strip()
    
#     date_pattern = r"^(\d{2})/(\d{2})/(\d{4})$"
    
#     if re.match(date_pattern, user_date):
#         # Agar format sahi hai, toh use '-' mein convert kar rahe hain
#         converted_date = re.sub(date_pattern, r"\1-\2-\3", user_date)
#         print(f"✅ Valid Date! Aapki date ka naya format hai: {converted_date}")
#     else:
#         print("❌ Invalid Date Format! Kripya '/' ka use karein (e.g., 25/05/2026).")

# # --- Main Program Menu ---
# while True:
#     print("\n=========================================")
#     print("      REGEX VALIDATION & EXTRACTOR       ")
#     print("=========================================")
#     print("1. Phone Number Check Karein")
#     print("2. Email ID Check Karein")
#     print("3. Date Format Convert Karein")
#     print("4. Program Se Bahar Niklein (Exit)")
    
#     choice = input("\nApna option chunein (1-4): ").strip()
    
#     if choice == "1":
#         check_phone()
#     elif choice == "2":
#         check_email()
#     elif choice == "3":
#         check_date()
#     elif choice == "4":
#         print("\nThank you! Program band ho raha hai. 👋")
#         break
#     else:
#         print("\n⚠️ Galt option! Kripya 1, 2, 3 ya 4 mein se hi chunein.")
    
#     print("\n" + "-"*40)

# import re

# def phone_number() :

#     print(f"-----phone-Validator-----")
#     user_input =  input("Enter your phone number on here!  : ").strip()
    
#     phone_pattern = r"^\d{5}-\d{5}$"

#     if re.match(phone_pattern,user_input)  :
#         print(f"your phone is validation is correct on here : {user_input}")
#     else :
#         print(f"your validation is wrong on here : {user_input} you follow : (e.g : 93270-63241)")



# def email_valid() :
#     print(f"----Email validator---------")

#     user_input =  input("Enter your Email on here : ").strip()

#     email_pattern = r"^[a-zA-Z0-9.+-_%]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"


#     if re.match(email_pattern,user_input) :
#         print(f"your email pattern is validation is correct on here : {user_input}")
    
#     else :
#         print(f"your email validation is wrong try, again later : ")



# def date_valid() :
#     print(f"----Date validataion--------")

#     user_input =  input("Enter your data on here : ").strip()

#     date_pattern = r"^(\d{2})/(\d{2})/(\d{4})$"

#     if re.sub(date_pattern,r"\1-\2-\3",user_input) :
#         print(f"your crediantials is corret on here : {user_input}")
#     else :
#         print(f"your data format is wrong on here :(e.g : 20-12-2024) ")


# while True :

#     print(f"==================================")
#     print(f"=====Regex validation on here : =======")
#     print(f"1.phone number validation : ")
#     print(f"2.Email validation : ")
#     print(f"3.date validation : ")
#     print(f"4.Exit this program : ")
#     print(f"==================================")

#     choice =  input("Enter your choice : (e.g : 1,2,3,4)").strip()

#     if choice == "1" :
#         phone_number()
#     elif choice == "2" :
#         email_valid()
#     elif choice == "3" :
#         date_valid() 
#     elif choice == "4" :
#         print(f"your program is closed on here : ")
#         break
#     else :
#         print(f"please choose correct nubmer ,try again later : ")



