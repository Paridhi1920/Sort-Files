import os
import shutil

folders = {
    'Videos':['.mp4'],
    'Audios':['.mp3'],
    'Images':['.jpg','.png'],
    'PDFs':['.pdf'],
    'Excel':['.xlsx','.xls','.xl'],
    'Docs':['.doc','.docx','.docs'],
    'Ppt':['.ppt','.pptx'],
}

def create_move(ext,file_name):
    find = False
    for folder_name in folders :
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name)) 
            find = True  
            break
    if find !=True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,other_name))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))


directory = input("Enter the location / path : ")
other_name = input("Enter the folder name for Unknown Files : ")
all_files = os.listdir(directory)
length = len(all_files)
ddone = 1


for i in all_files:
    if os.path.isfile(os.path.join(directory,i)) == True:
        create_move(i.split(".")[-1],i)
    print("Done !!")  

    