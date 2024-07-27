f = open("poem.txt")
content = f.read()

if "Twinkle" in content :
  print("Twinkle is present")
else :
  print("Twinkle is not present")

f.close()

s = "My name is Muaaz"
f = open("old.txt", "w")
f.write(s)
f.close()

import os 
current_file_name = 'old.txt'
new_file_name = 'python.txt'

os.rename(current_file_name, new_file_name)
