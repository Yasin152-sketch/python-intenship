# name = b'yasin shaikh'

# print(name.hex())
# print(name.decode())

# print(bin(120))


# name = b'hello world'
# print(name)
# print(name.decode())
# print(name.hex())
# print(name.find(b'worlds'))


# name = b'yasin'
# print(name)
# print(bytes(name))
# print(id(name))
# print(name.hex())
# print(name.decode())
# print(name.find(b's'))
# print(name.replace(b's',b'x'))
# print(id(name))
# print(name.count(b'y'))

# print(name.split(b's'))
# print(name.startswith(b'ya'))
# print(name.endswith(b'n'))
# print(id(name))


# name = bytearray(b'yasin shaikh')
# print(name)
# print(id(name))
# print(name.hex())
# print(name.decode())
# print(name.find(b'shaikh'))

# name.append(120)
# print(name)
# print(id(name))
# name.extend(b'software developer')
# print(name)

# name = bytearray(b'laptop')
# print(name.reverse())
# print(name)
# print(name.hex())
# print(name.decode())

# name.replace(b'top',b'phone')
# print(name)

# print(name.count(b'p'))
# print(name)

# phone = bytearray(b'name:id:email')
# phone.split(b'|')
# print(phone)

# clock = bytearray(b'clock')
# print(clock)

# clock.reverse()
# print(clock)


# sofa = bytearray(b'|')

# result = sofa.join([b'hello',b'world'])
# print(result)


# a = ["apple","banana"]
# print(id(a))
# b = ["grape","orange"]
# print(id(b))
# x =  a
# print(id(x))
# print(x)

# print( a is b)
# print(a is x)

# print(a == b)


# a = int("10")
# b = float("3")
# print(a)
# print(b)

# if num < num2 : print("num is greater than num2")
# print("num is 10 value") if num == 10 else print("num2 is value is 20")

# bigger =  num if num == 10 else num2
# print(bigger,"num is 10")

# value = 0

# if value  >= 20 :
#     print("this is valid statement!")
# elif value == 0 :
#     pass
# else  :
#     print('last statment!')



# value = 5
# match value :
#     case 1 :
#         print("monday")
#     case 2 : 
#         print("Tuesday")
#     case 3 :
#         print("Wednesday")
#     case 4 :
#         print("Thursday")
#     case _ :
#         print("defaul value is on here!")
            
# # User se input lena
# name = input("Apna naam batayein: ")
# maths = int(input("Maths ke marks: "))
# science = int(input("Science ke marks: "))
# english = int(input("English ke marks: "))

# # 1. Operators ka use (Arithmetic Operators)
# total_marks = maths + science + english
# percentage = (total_marks / 300) * 100

# print(f"\n--- {name} ka Result ---")
# print(f"Total Marks: {total_marks}/300")
# print(f"Percentage: {percentage:.2f}%")

# # 2. If-Else ka use (Comparison & Logical Operators)
# if percentage >= 90:
#     grade = "A"
# elif percentage >= 75:
#     grade = "B"
# elif percentage >= 50:
#     grade = "C"
# elif percentage >= 33:
#     grade = "D"
# else:
#     grade = "F"

# # Validation check
# if maths < 0 or science < 0 or english < 0:
#     print("Error: Marks negative nahi ho sakte!")
# else:
#     # 3. Match-Case ka use (Python 3.10+)
#     match grade:
#         case "A":
#             reward = "Naya Smartphone! 📱"
#         case "B":
#             reward = "Ek nayi Watch! ⌚"
#         case "C":
#             reward = "Ek nayi Book! 📚"
#         case "D":
#             reward = "Thoda aur mehnat karo! 💪"
#         case "F":
#             reward = "Agli baar sahi se padhna... 🤐"
#         case _:
#             reward = "Invalid Grade"

#     print(f"Aapka Grade: {grade}")
#     print(f"Aapka Reward: {reward}")


# name =  input("Enter your name : ")
# maths = int(input("Enter your maths marks : "))
# science = int(input("Enter your science marks : "))
# English = int(input("Enter your English   marks : "))

# total_marks = maths +  science +  English
# percentage =  (total_marks / 300) * 100

# print(f"\n -----{name}------------")
# print(f"total marks is : {total_marks}")
# print(f"percentage  : {percentage:.2f}%")

# if percentage >= 90 :
#     grade = 'A'
# elif percentage >= 75 : 
#     grade = 'B'
# elif percentage >= 60 :
#     grade = 'C'
# elif percentage >= 45 :
#         grade = 'D'
# else :
#       grade = "invalid grade,try again!"

# if maths < 0 or science < 0 or English < 0 :
#         print("Error : you not put negative number in it!")
# else :
#     match grade :
#         case "A" :
#                 reward = "you earn 1 lacs!"
#         case "B" :
#                 reward = "your can 50k upto"
#         case "c" :
#                 reward = "your can phone upto"
#         case "D" :
#                 reward = "None work hard on this"
#         case _ :
#                 reward = "invalid grade,try again!"

# print(f"you obtain grade is : {grade}")
# print(f"you earn reward  is : {reward}")

# 1. Data Types Definition
# store_name = "Apna Bazar"          # Tuple (Location)
# stock = {"Apple": 10, "Milk": 5}   # Dictionary

# print(f"--- Welcome to {store_name} ---")

# # 2. Project Logic using Loop, Range, and Match
# def manage_store():
#     # Range based loop (Simulating 3 customers)
#     for customer_id in range(1, 4):
#         print(f"\nServing Customer #{customer_id}")
        
#         action = input("Kya karna chahte hain? (view / add / exit): ").lower()

#         # 3. Match-Case (Modern Python 3.10+ feature)
#         match action:
#             case "view":
#                 print("Current Stock:")
#                 for item, qty in stock.items():
#                     print(f"- {item}: {qty} units")
            
#             case "add":
#                 item_name = input("Item ka naam: ")
#                 if item_name in stock:
#                     stock.item_name.append(1)
#                 else:
#                     stock[item_name] = 1
#                 print(f"{item_name} update ho gaya!")
                
#             case "exit":
#                 print("Store closing...")
#                 break
                
#             case _:
#                 print("Invalid option! Dubara try karein.")

# manage_store()


# store_name = "instamart"
# stock = {"apple" : 10,"cherry" :10}

# print(f"\n--------{store_name}-------")

# def shopping() :
#     for custormer_id in range(1,4) :
#         print(f"custormer_id : {custormer_id}")
#         action = input("what do you want to do : (view / add / exit)").lower()

#         match action :
#             case "view" :
#                 print("current items list out : ")
#                 for qty,item in stock.items() :
#                     print(f"{qty} - {item} units ")
            
#             case "add" : 
#                 item_name = input("Enter your new item name : ")
#                 if item_name in stock :
#                     stock.item_name.append(1)
#                     print(f"new item added : {item_name}")
#                 else : 
#                     stock[item_name] = 1
#                     print(item_name,"item name updated on here!")
            
#             case "exit" :
#                 print("the mall is closing.... ")
#                 break
#             case _ :
#                 print("invalid option is selected,try again!")

# shopping()

# def messge() :
#     print("this is message you passed on here!")

# messge()

# def phone() :
#     return "this is phone on here!"

# laptop =  phone()
# print(laptop)

# def items(x,y) :
#     return x + y

# laptop = items(5,15)
# print(laptop)

# def Items():
#     return ["one","two","three"]

# new_items = Items()
# print(new_items[0])
# print(new_items[1])
# print(new_items[2])

# def Items():
#     return (10,20)

# x, y  =  Items() 
# print(x)
# print(y)

# def phone(name,lname) :
#     print(f"your name is  : {name}")
#     print(f"and your breed is  : {lname} and first name : {name}")


# phone(name = "junior",lname="german shephared")

# def Items(*val) :
#     print(f'your first value is  : {val[2]}')
#     print(f"all values of items : {val}")
#     print(f"type of *args is : {type(val)}")

# Items("yasin","farhan","shabbir")

# def Student_Data(**data) :
#     print(f"all data show me  : {list(data.items())}")
#     print(f"your data first row show me  : {list(data.items())[0]}")
#     print(f"type of this fucntion is  : {type(data)}")

# Student_Data(name="yasin" , age = 20,school = "the new age high school")


# def second(**name) :
#     print(f"your name is  : {name["first"]}")
#     print(f"your second name is  : {name["second"]}")
#     print(f'all data is : {name}')
#     print(f"the type of is : {type(name)}")

# second(first= "shaikh",second = "nasrin shaikh")

# def test(title,*first,**second) :
#     print(f"your title is  : {title}")
#     print(f"postional argusements : {first}")
#     print(f"keyword arguements : {second}")

# test("check it : ","yasin","farhan",age = 20 ,address = "india")


# def add_nubmers(a,b,c) :
#     print(f"a : {a}, b : {b} , c : {c}")
#     return a + b+ c 

# my_list = [10,20,30]
# result =  add_nubmers(*my_list)
# print(result)

# def introduce(name,age,city) :
#     print(f"your name is  : {name} and age is  : {age}  and city is  : {city}")

# user_info = {
#     "name" : "yasin",
#     "age" : 20,
#     "city" : "ahemdabad"
# }

# introduce(**user_info)

# def super_fucn(a,b,c,d) :
#     print(a,b,c,d)

# pos_args = (1,2)
# key_args = {"c" : 10, "d" : 20}

# super_fucn(*pos_args,**key_args)


# def phone(title,*post_args,**key_args) :
#     print(f"title  : {title}")
#     print(f"postinal arguments : {post_args}")
#     print(f"keyword arguements : {key_args}")

# phone("define which things do : ","yasin shiakh",address = "juhapura")

# def phone(fname,lname) :
#     print(f"your first name : {fname}")
#     print(f"your last name : {lname}")

# result = {"fname" : "yasin", "lname" : "shaikh"}
# phone(*result)

# 1. Function to calculate total price using *args (Unlimited items)
# def calculate_total(*prices):
#     return sum(prices)

# # 2. Function to apply discount using Default Argument
# def apply_discount(total_amount, discount_percentage=10):
#     discount = (total_amount * discount_percentage) / 100
#     return total_amount - discount

# # 3. Function to print bill using Unpacking and Keyword Arguments
# def generate_bill(name, final_amount, **details):
#     print("\n--- GROCERY BILL ---")
#     print(f"Customer Name: {name}")
#     print(f"Final Payable: ₹{final_amount}")
    
#     print("Additional Info:")
#     for key, value in details.items():
#         print(f"- {key}: {value}")
#     print("--------------------")

# # --- Logic Starts Here ---

# # Step 1: Customer ne items kharide
# item_prices = [150, 45, 300, 120]

# # Step 2: Total nikalne ke liye list ko Unpack (*) karke bheja
# total = calculate_total(*item_prices)

# # Step 3: Discount apply kiya (Default 10% chalega agar hum kuch na dein)
# payable_price = apply_discount(total,20)

# # Step 4: Bill generate kiya (Keyword arguments ke saath)
# customer_info = {"Payment_Mode": "UPI", "Store_Location": "Ahmedabad", "Date": "2026-05-15"}
# generate_bill("Yasin", payable_price, **customer_info)


# def calculate_total(*price) :
#     return sum(price)

# def discount_value(total,discount_percentage = 10) :
#     discount = (total * discount_percentage) / 100
#     return total -  discount
# def genrate_bill(name,total_amount,**details) :
#     print(f"\n-----grocery store: -----")
#     print(f"customer name is  : {name}")
#     print(f"your total amount : {total_amount}")
#     print(f"Addtional details below it : ")

#     for key,value in details.items() :
#         print(f"{key} : {value}")

# customer_info = {"payment mode": "UPI", "store_location":"ahemdbad","Date" : "20-12-25"}
# items_price = [10,20,30,85,65,250,350]
# amount = calculate_total(*items_price)
# payble_bill = discount_value(amount,35)
# genrate_bill("yasin",payble_bill,**customer_info)

# # 1. Total Calculate karne wala function
# def calculate_total(*prices):
#     return sum(prices)

# # 2. Discount apply karne wala function
# def apply_discount(total_amount, discount_percentage=10):
#     discount = (total_amount * discount_percentage) / 100
#     return total_amount - discount

# # 3. NAYA FUNCTION: GST calculate karne ke liye
# def apply_gst(amount, gst_rate=18):
#     gst_amount = (amount * gst_rate) / 100
#     final_price = amount + gst_amount
#     return final_price, gst_amount # Hum dono cheezein return kar rahe hain

# # 4. Bill print karne wala function
# def generate_bill(name, total, discount_amt, gst_amt, final_payable, **details):
#     print("\n" + "="*30)
#     print("      RELIANCE FRESH - AHMEDABAD")
#     print("="*30)
#     print(f"Customer: {name}")
#     print(f"Total Items Price: ₹{total}")
#     print(f"Discount Applied : -₹{discount_amt}")
#     print(f"GST (18%)        : +₹{gst_amt}")
#     print("-" * 30)
#     print(f"FINAL BILL       : ₹{final_payable}")
#     print("-" * 30)
    
#     for key, value in details.items():
#         print(f"{key}: {value}")
#     print("="*30)

# # --- Logic Starts Here ---

# prices = [500, 200, 300] # Total 1000
# total = calculate_total(*prices)

# # Discount ke baad ka price (Net Price)
# discounted_price = apply_discount(total, 10) 
# discount_amt = total - discounted_price

# # GST apply kiya discounted price par
# final_price, gst_value = apply_gst(discounted_price)

# # Bill generate kiya
# generate_bill("Yasin", total, discount_amt, gst_value, final_price, Mode="Cash", Counter="F1")

# def calculate_total(*price) :
#     return sum(price)

# def discount_apply(total,discount_percentage = 10) :
#     discount = (total * discount_percentage) / 100 
#     return total -  discount

# def genrate_bill(name,total,discout_amt,gst_amt,payable_amt,**details) :
#     print(f"\n {"=" * 30}")
#     print(f"your name is : {name}")
#     print(f"your total is  : {total}")
#     print(f"your discoutn amount : {discout_amt}")
#     print(f"your gst amount is : {gst_amt}")
#     print(f"your payble amount : {payable_amt}")
#     print(f"Additional detials : ")
#     for keys,value in details.items() :
#         print(f"{keys} : {value}")


# genrate_bill("yasin",250,10,18,180 ,payment = "UPI",counter = "F1")
# print(calculate_total(10,20,30,40))

# # --- Purane Functions ---
# def calculate_total(*prices):
#     return sum(prices)

# def apply_discount(total_amount, discount_percentage=10):
#     discount = (total_amount * discount_percentage) / 100
#     return total_amount - discount

# def apply_gst(amount, gst_rate=18):
#     gst_amount = (amount * gst_rate) / 100
#     return amount + gst_amount, gst_amount

# def generate_bill(name, total, discount_amt, gst_amt, final_payable):
#     print("\n" + "="*30)
#     print(f"Customer: {name}")
#     print(f"Total: ₹{total} | Discount: -₹{discount_amt} | GST: +₹{gst_amt}")
#     print(f"FINAL PAYABLE: ₹{final_payable}")
#     print("="*30)

# # --- NEW: User Input Handling ---
# def main():
#     customer_name = input("Customer ka naam bataiye: ")
#     item_prices = []

#     print(f"\nHello {customer_name}, items ke prices enter karein.")
#     print("(Sare prices likhne ke baad 'q' dabayein bill nikalne ke liye)")

#     while True:
#         entry = input("Price: ")
        
#         if entry.lower() == 'q':
#             break
        
#         try:
#             p = float(entry)
#             if p < 0:
#                 print("Price minus mein nahi ho sakta!")
#                 continue
#             item_prices.append(p)
#         except ValueError:
#             print("Invalid! Sirf number ya 'q' likhein.")

#     # Agar list khali nahi hai, tabhi bill banayein
#     if item_prices:
#         total = calculate_total(*item_prices)
#         discounted = apply_discount(total)
#         final, tax = apply_gst(discounted)
        
#         # Bill print karna
#         generate_bill(customer_name, total, total-discounted, tax, final)
#     else:
#         print("Koi item add nahi kiya gaya.")

# # Program Start
# main()

# def calculate_total(*price) :
#     return sum(price)

# def discount_amount(total,discount_percentage = 10) :
#     discount =  (total * discount_percentage) / 100
#     return  total -  discount

# def gst_amt(total,gst_amt = 18) :
#     gst_rate = (total *  gst_amt) / 100
#     return total +  gst_rate, gst_rate 

# def generate_bill(name,total,discount_amt,gst_amt,paynable_amt) :
#     print(f"your name : {name}")
#     print(f"your total amount : {total:.2f}")
#     print(f"discount after amount : {discount_amt:.2f}")
#     print(f"gst applied after amount : {gst_amt:.2f}")
#     print(f"final payable price : {paynable_amt:.2f}")

# def main() :
#     customer_name = input("Enter your name : ")
#     item_price = []
#     print(f"your name is {customer_name},Enter your price : ")
#     print(f"you want to exit from program ,enter press a q key!")
    
#     while True :
#         entry =  input("Enter your item price : ")
#         if entry.lower() == "q" :
#             break
#         try :
#             p = float(entry) 
#             if p < 0 :
#                 print("you cannot assign value in minus !")
#                 continue
#             item_price.append(p)
#         except ValueError : 
#             print("your cannot enter a any character in it!")

#     if item_price :
#         total =  calculate_total(*item_price)
#         discounted=   discount_amount(total)
#         final,tax =  gst_amt(discounted)

#         generate_bill(customer_name,total,total -  discounted,tax,final)
#     else : 
#         print("your are not added items in cart!")

# main()

# x = "global scope!"
# def phone(name) :
#     age = 20
#     print(f"your name : {name}")
#     print(f"your age is  : {age}")

# phone("yasin")

# def laptop() :
#     print(x)

# laptop()

# def outer() :
#     x = "hello world on here!"
#     def innner() :
#         print(x)

#     innner()

# outer()


# count = 0 
# def calculate() :
#     global count 
#     count += 1

# print(f"first count : {count}")
# calculate()
# print(f"second calculate  : {count}")


# def outer() :
#     x = "Hello world" 
#     def inner() :
#         print(x)
#     inner()
# outer()



# x =  "global vairble!"

# def outer() :
#     x = "greetings" 
#     print(x)
#     def inner() :
#         print(x,"inner function")
#     inner()
#     print("outside inner fucntion!",x)
# outer()
# print("your varible is outside outer!",x)

# def outer() :
#     counter = 0
#     def inner() : 
#         nonlocal  counter
#         counter += 1
#         print(f"inner coutner : {counter}")
#     inner()
# outer()

# # 1. Decorator function define kiya
# def my_decorator(func):
#     def wrapper():
#         print("--- Function chalne se PEHLE ka kaam ---")
#         func()  # Yahan aapka original function run ho raha hai
#         print("--- Function chalne ke BAAD ka kaam ---")
#     return wrapper

# # 2. Decorator ko use karne ke liye '@' symbol ka use hota hai
# @my_decorator
# def say_hello():
#     print("Hello World! 🚀")
# say_hello()

# 3. Function ko call kiya


# def my_decorator(func) :
#     func()

# @my_decorator 
# def say_hello() :
#     print("hello world on here!")

# say_hello()


# def my_decorator(func) :
#     def inner() :
#         print(f"=======================")
#         func()
#         print(f"=======================")
#     return inner

# @my_decorator
# def say_name() :
#     print("yasin shiakh")
# say_name()


# def my_decorator(name) :
#     def inner() :
#         return name().upper()
#     return inner

# @my_decorator
# def change_value() :
#     return "your value is changed on here!"

# @my_decorator
# def my_fuunction() :
#     return "your function is changed on here!"

# print(change_value())
# print(my_fuunction())

# is_logged =  False

# def is_logged_required(func) :
#     def wrapper() :
#         if is_logged == True :
#             func() 
#         else :
#             print("your access is denided :you get a first login in instagram!")
#     return wrapper

# @is_logged_required
# def view_logged():
#     print("you cannot see your photo :")

# @is_logged_required
# def view_profile() :
#     print("you cannot see a profile : ")


# view_logged()
# view_profile()
# print(f"------------------------------------------------")

# is_logged =  True

# view_logged()
# view_profile()

# def my_decorator(func) :
#     def wrapper() :
#         print(f"first statement on here!")
#         func()
#         print(f"second statement on here!")
#     return wrapper

# @my_decorator 
# def say_hello() :
#     print("first greetings....")

# @my_decorator 
# def final_say() :
#     print("final greetings on here!")

# say_hello()
# final_say()

# 1. Decorator jo arguments ko handle kar sakta hai

# def My_decorator(func) :
#     def wrapper(*args,**kwargs) :
#         print(f"log : fucniton is started on here!")
#         print(f"postinal arguments on here : {args}")
#         print(f"keyword arguments on here : {kwargs}")
#         return func(*args,**kwargs)
#     return wrapper

# @My_decorator
# def say_hello(name) :
#     print(f"your name is : {name}")
# say_hello("yasin")

# @My_decorator
# def add_calculate(a,b) :
#     print(f"your add to number is : {a + b}")
# add_calculate(a = 10,b = 20)
# print(f"new keyword on here : ")
# add_calculate(30,b = 786)

# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(1)
# def myfunction():
#   return "Hello Linus"

# print(myfunction())

# def changecase(n) :
#     def My_Decorator(name) :
#         def wrapper() :
#            if n == 1 :
#                 a =  name().upper()
#            else:
#                 a =  name().lower()

#            return a
#         return wrapper
#     return My_Decorator

# @changecase(1) 
# def my_func() :
#    return f"yasin shaikh"

# print(my_func())

# def my_Decorator(n) :
#     def changecase(name) :
#         def wrapper() :
#             print(f"print your statment : ")

#             if n == 1 :
#                 a =  name().upper()
#             else :
#                 a = name().lower()
#             return a
#         return wrapper
#     return changecase

# @my_Decorator(10) 
# def check() :
#     return "farhan shaikh"
# print(check())

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Have a great day!"

# print(myfunction.__doc__)
# print(myfunction())

# def My_decorator(func) :
#     def wrapper():
#         return func().upper()
#     return wrapper

# @My_decorator
# def say_hello() :
#     return f"your name is yasin shaikh!"
# print(say_hello.__name__)
 
# nubmers = [10,20,30,40,50,60]
# sum_two = list(map(lambda x : x * 2 ,nubmers))
# print(sum_two)

# computer_drive = {
#     "Documents" : {
#         "Resume.pdf" : "file",
#         "personal" : {
#             "passport.png" : "file",
#             "Note.txt" : "file",
#         }
#     },
#     "Download" : {
#         "Game_setup" :"file",
#         "Movies" :{
#             "Inception.mp4" : "file"
#         }
#     }
# }

# def find_item(curr_folder, target):
#     # Har item ko check karo, chahe woh file ho ya folder
#     for name, content in curr_folder.items():
#         if name == target:
#             return name
        
#         # Agar yeh ek folder hai, toh iske andar dhoondo
#         if isinstance(content, dict):
#             result = find_item(content, target)
#             if result:
#                 return f"{name} --> {result}"
                
#     return None

# # Ab agar aap "Movies" (folder) dhoondenge:
# print("Path:", find_item(computer_drive, "Movies1"))

# # Agar aap "Inception.mp4" (file) dhoondenge:
# print("Path:", find_item(computer_drive, "Inception.mp4"))
 

# server_logs =[
#     "INFO : sever stared on here!",
#     "WARGING : Mermory usage upto 75%",
#     "ERROR : database connection failed on here!",
#     "ERROR : page not found on here!",
#     "INFO : cache cleared!"
# ]

# def error_scammer(logs) :
#     for line in logs :
#         if "ERROR" in line : 
#             yield line
# scanner =  error_scammer(server_logs)
# print("----ERROR processong starting...------")
# print(next(scanner))
# print(id(scanner))
# print(next(scanner))
# print(id(scanner))

# def count_top(n)  : 
#     count = 1
#     while count <= n :
#         yield count
#         count += 1

# for num  in count_top(10) :
#     print(num)



# def large_value(n) :
#     for i in range(n) :
#         yield i

# next_value = large_value(10)
# print(next(next_value))
# print(next(next_value))
# print(next(next_value))
# print(next(next_value))


# def large_sequence(n) :
#     for i in range (n) :
#         yield i


# gen =  large_sequence(1000)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# list_comp = [x * x for x in range(5)]
# print(list_comp)

# gen_comp = (x * x for x in range(5))
# print(gen_comp)

# print(list(gen_comp))

# My_list = [x * x for x in range(5)]

# print(f"how many memeory save in it : {sys.getsizeof(My_list)} bytes : ")

# def Multifiler() :

#     into = 2 

#     while True :

#         recevied =  yield f"your multiply values : {into}"

#         if recevied is not None  :
#             into =  recevied


# gen =  Multifiler()
# print(next(gen))
# print(gen.send(50))
# print(gen.send(20))

# import time

# # 1. Generator Function: Jo line-by-line file padhega (Hum yahan list se simulate kar rahe hain)
# def log_reader(log_data):
#     print("\n--- Generator Shuru Hua (Lazy Loading) ---")
#     for line in log_data:
#         # Har line ko check karne mein thoda waqt lagta hai (simulation)
#         time.sleep(0.3) 
#         yield line # Ek baar mein sirf EK line bahar bhejega

# # 2. Filter Generator Function: Jo sirf ERROR wali lines ko chunega
# def error_filter(log_stream):
#     for line in log_stream:
#         if "ERROR" in line:
#             yield line # Sirf ERROR wali line ko hi aage bhejega

# # --- MINI PROJECT TESTING ---

# # Hamara dummy server data (Sochiye yeh 1 GB ki file hai)
# server_logs = [
#     "[INFO] 10:00:01 - Server started successfully.",
#     "[INFO] 10:00:05 - User 'rahul' logged in.",
#     "[ERROR] 10:01:20 - Database connection failed!", # <-- Hamein yeh chahiye
#     "[INFO] 10:02:10 - Page rendered in 12ms.",
#     "[WARNING] 10:03:15 - Memory usage above 80%.",
#     "[ERROR] 10:04:50 - User payment failed (Timeout).", # <-- Hamein yeh chahiye
#     "[INFO] 10:05:00 - Backup completed."
# ]

# print("--- Project Shuru Ho Raha Hai ---")

# # Pipeline banana (Abhi tak koi data process nahi hua hai!)
# raw_logs = log_reader(server_logs)
# only_errors = error_filter(raw_logs)

# # Ab hum next() ya for loop se data mangenge, tabhi generator chalega
# print("\nAb hum sirf ERRORs ko print karenge:")
# for error in only_errors:
#     print(f"🚨 ALERT PAYA GAYA: {error}")

# print("\n--- Processing Khatam ---")

# import time

# def log_reader(data) :

#     print(f"\n the generator is stared on here! : ")
#     for line in data :
#         time.sleep(0.3)
#         yield line


# def log_stream(file) :
#     for line in file :
#         if "ERROR"  in line :
#             yield line

# server_logs = [
#     "[INFO] : this is succesfully installed on here!",
#     "[ERROR] : this is error is for you!",
#     "[ERROR] : this is error is for server crush!",
#     "[INFO] : I cound not futher info to related a files"
# ]


# raw_logs =  log_reader(server_logs) 
# new_logs =  log_stream(raw_logs)

# print(f"\n the error are below it : ")

# for error in new_logs :
#     print(f"alert new therth : {error}")


# print(f"your program is terminated!")

# new_logs =  range(0,10,3)
# print(len(new_logs))

# print(list(range(5)))
# print(list(range(5,10)))
# print(list(range(0,10,3)))

# r = range(10)
# print(60 in r)


# My_list = ["apple","banana","cheery","mango"]
# gen =  My_list
# try :
#         print(next(gen))
# except TypeError as e :
#         print(f"Error is  : {e}")


# My_iterator =  iter(My_list)

# print(next(My_iterator))
# print(next(My_iterator))

def greetings(name) :
    return f"your name is {name} shaikh!"

new_value =  "farhan shaikh!"


print(greetings("yasin"))