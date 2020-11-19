import os 

def main(): 
    folders = [ 'aien', 'alif', 'ba', 'ta', 'dal', 'dhod', 'dzal',
                'dzho', 'fa', 'ghoin', 'ha', 'ha\'', 'hamzah', 'jiem',
                'kaf', 'kho', 'lam', 'lamalief', 'miem', 'nun', 'qof',
                'ro', 'shod', 'sien', 'syien', 'ta', 'tho', 'tsa', 
                'wawu', 'ya', 'zain']
    #folder = input("Masukkan nama folder sekaligus file: ")
    for folder in folders:
        for count, filename in enumerate(os.listdir(folder)): 
            try:
                dst = folder + "_" + str(count) + ".jpg"
                # dst = 'eka' + "_" + str(count) + ".jpg"
                src = folder + '\\' + filename 
                dst = folder + '\\' +  dst

                os.rename(src, dst) 
            except:
                print("File Sudah Ada")

if __name__ == '__main__': 
    main() 

# Folder
# --alif
# -changeName.py