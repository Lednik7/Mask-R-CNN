#pip install ImageHash
import imagehash as m
import os

# Sample/jpg/
dir = input("Path: ")

ask = (input("Delete copies?: ")).replace(" ", "").lower() #Yes or No || 1 or 0

path = os.path.join(os.getcwd(), dir)

original = []
copy = []

try:
    for filename in os.listdir(path):
        path2 = os.path.join(path, filename)
        hash = m.dhash(Image.open(path2))
        if hash in original:
            copy.append(filename)
            if ask == "yes" or 1:
                os.remove(path2)
        else:
            original.append(hash)
        
    print("Number of originals: " + str(len(original)))
    print("Number of copies: " + str(len(copy)))
            
except FileNotFoundError:
    print("Wrong way")
