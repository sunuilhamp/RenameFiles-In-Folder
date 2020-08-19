import os 

def main(): 
    folder = input("Masukkan nama folder sekaligus file: ")

    for count, filename in enumerate(os.listdir(folder)): 
        dst = folder + "_" + str(count) + ".jpg"
        src = folder + '\\' + filename 
        dst = folder + '\\' + dst 

        os.rename(src, dst) 

if __name__ == '__main__': 
    main() 

# Folder
# --alif
# -changeName.py