import os 

def main(): 

    for count, filename in enumerate(os.listdir("alif")): 
        dst ="alif_" + str(count) + ".jpg"
        src ='alif\\'+ filename 
        dst ='alif\\'+ dst 

        os.rename(src, dst) 

if __name__ == '__main__': 
    main() 

# Folder
# --alif
# -changeName.py