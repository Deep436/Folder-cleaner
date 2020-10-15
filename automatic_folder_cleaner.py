## Clear the clutter

import os

def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print("Folder created successfully.......")
    else:
        print(f"{folder} already exits ?\nTry using other name...? ")

def Move(foldername, files):
    for file in files:
        os.replace(file, f'{foldername}/{file}')

create('Media')
create('Images')
create('Documents')
create('Others')


files = os.listdir()
files.remove('automatic_folder_cleaner.py')
# print(files)

image_extension = ['.png','.jpg','.jpeg']
images =[file for file in files if os.path.splitext(file)[1].lower() in image_extension] 
# print(images)

Doc_extension = ['.txt','.docx','.doc','.pdf']
docs = [file for file in files if os.path.splitext(file)[1].lower() in Doc_extension]
# print(docs)

media_extension = ['.mp4', '.mp3','.fiv']
medias = [file for file in files if os.path.splitext(file)[1].lower() in media_extension]
# print(medias)

others = []
for file in files:
    exc = os.path.splitext(file)[1].lower()
    if  exc not in image_extension and exc not in Doc_extension and exc not in media_extension and os.path.isfile(file):
        others.append(file)
# print(others)

Move('Documents', docs)
Move('Images',images )
Move('Media', medias)
Move('Others',others )

# print("\n\t\t\t\tWelcome to Data manager\nOptions available are ---------- :\n\t\t1.) For creating folder ? press f \n\t\t2.)For moving file to a existing folder ? press m")   
# data = input("Enter your choise : ")
# if data == 'f':
#     folder_name = input("Enter folder name : ")
#     create(folder_name)
# elif data == 'm':
#     folder_name = input("Enter the folder name where you want to move : ")
#     folder_name = folder_name.title()
#     print(folder_name)
#     files = input("\nAvailble files are ...\n1.) Images\n2.) Documents\n3.) Medias\n4.)Others\n Enter the file name you want to move :  ")
#     print(files)
#     Move(folder_name, files)
# else:
#     print('Invaild Input')