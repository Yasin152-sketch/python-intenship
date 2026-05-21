# com =  45 + 56j
# print("Real number  : ",com.real)
# print("Imaginary nubmer :",com.imag)


# x = 10
# y = 20
# print(complex(x,y))

# a = 2 + 10j
# b = 8 + 50j
# print(a + b)
# print(a * b)
# large_num =  1_000_000
# small_num = 2
# print(large_num * small_num)


# distance =  1.5 * 10**8
# print(distance)

# n = 10
# print(n.bit_length())
# print(n.bit_count())

# n =  5.5
# b = 2.0
# print(b.is_integer())

# b = 0.75
# print(b.as_integer_ratio())

# f = 10.53
# num =  f.hex()
# print(num)
# print(float.fromhex(num))

# print(num.upper())
# print(num.strip())
# print(num.replace("o", "12"))
# print(num.split())
# print(num.startswith("h"))
# print(num.endswith("e"))
# print(num.find("h"))
# num = "hello world! "
# print(id(num))
# sum =  num + "how are you?"
# print(sum)
# print(id(sum))


# print(id(first))
# first.append("orange")
# print(first)
# sum = [12,45,78]
# print(id(sum))
# sum.append(100)
# print(sum)
# phone = first.extend(sum)
# # print(phone)
# num =  [12,3,45,78]
# print(id(num))
# first =  ["appple","banana"]
# cam =  num.extend(first)
# print(cam)
# print(type(cam))
# print(num)
# print(id(num))

# num = [12,3,5,4,7,89]
# print(num)
# num.sort()
# print(num)
# num.insert(2,"yasin shaikh!")
# print(num)
# num.pop()
# num.reverse()
# print(num)
# print(num.count(5))

# mouse = {1,2,3,4,2}
# print(type(mouse))
# mouse.add(10)
# mouse.add(20)
# print(mouse)

# mouse.update([30,50,40])
# print(mouse)
# # mouse.remove(200)
# mouse.discard(200)
# print(mouse)

# mouse.pop()
# print(mouse)

# mouse.clear()
# print(mouse)

# mouse = {1,2,3,4,5}
# print(mouse)

# mouse.add(10)
# mouse.update([10,20,30,40,50])

# print(mouse)

# mouse.remove(20)
# print(mouse)

# mouse.discard(200)
# print(mouse)
# mouse.pop()
# print(mouse)

# mouse.clear()
# print(mouse)

# 1. String: Page URL Slug aur Title
page_slug = "how-to-learn-python-2026"

# 2. Int & Float: Web Analytics
page_views = 1500
load_time_sec = 0.45 

# 3. Complex: SVG Graphics calculation
# Web development mein complex numbers CSS transitions ya 
# SVG animations ke coordinates calculate karne ke liye use hote hain.
animation_vector = 5 + 3j 

# 4. List: Navigation Menu (Mutable)
nav_links = ["Home", "About", "Blog", "Contact"]

# 5. Tuple: Database Connection Config (Immutable)
# Ye sensitive info hai jo runtime par change nahi honi chahiye.
db_config = ("127.0.0.1", 5432, "admin_db")

# 6. Set: Unique User Tags
# Ek post par multiple tags ho sakte hain par unique hone chahiye.
post_tags = {"coding", "webdev", "python", "webdev"} # 'webdev' duplicate remove ho jayega

# 7. Dictionary: JSON Response Header
# Web APIs hamesha dict (JSON) format mein data bhejti hain.
api_response = {
    "status": 200,
    "content_type": "application/json",
    "server": "Nginx/1.24"
}

# 8. Range: Pagination logic
# Page numbers 1 se 10 tak generate karne ke liye.
pagination = range(1, 11)

# 9. Bool: User Authentication Status
is_logged_in = True

# --- WEB MEDIA HANDLING (Advanced Binary Section) ---

# 10. Bytes: Raw Image Data (Avatar)
# Web server par image upload bytes format mein aati hai.
raw_image = b"\xff\xd8\xff\xe0\x00\x10JFIF" # Fake JPEG header

# 11. Bytearray: Live Image Watermarking
# Maanlo humein image metadata mein website ka naam add karna hai.
image_buffer = bytearray(raw_image)
image_buffer.extend(b"-WEB-APP-2026") # In-place modification

# 12. Memoryview: High-Speed Image Slicing
# Image ke bade data ko bina copy kiye process karna (Performance optimization).
mv = memoryview(image_buffer)
preview_chunk = mv[0:4] # Pehle 4 bytes ka view lena

# --- Backend Execution Logic ---

print(f"--- WEB SERVER STATUS: {'ONLINE' if is_logged_in else 'OFFLINE'} ---")
print(f"Endpoint: /{page_slug} | Load Time: {load_time_sec}s")
print(f"Database: Connecting to {db_config[0]} port {db_config[1]}...")
print(f"API Response Header: {api_response}")
print(f"Active Tags: {', '.join(post_tags)}")

# Memoryview check
print(f"Image Header Preview (Hex): {preview_chunk.hex()}") 