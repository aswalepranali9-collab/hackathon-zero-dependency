import os, shutil

def organize_files(folder):
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        ext = ext[1:]
        if ext:
            new_folder = os.path.join(folder, ext)
            os.makedirs(new_folder, exist_ok=True)
            shutil.move(os.path.join(folder, filename), os.path.join(new_folder, filename))

def menu():
    print("1. Organize Files")
    print("2. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        folder = input("Enter folder path: ")
        organize_files(folder)
    else:
        print("Goodbye!")

def main():
    print("Welcome to Hackathon Project")
    menu()   # इथे menu call करायचं आहे

if __name__ == "__main__":
    main()

