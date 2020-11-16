myfile = open("function.txt",'w+')

def wrote(text,file):
    myfile.writelines(text)

wrote("hii My name is namrata",myfile)

wrote("\nI am a student",myfile)
