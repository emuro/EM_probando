"""from
https://www.programiz.com/python-programming/directory
"""
import os


dir=os.getcwd()
print(dir)

dir=os.getcwdb()
print(dir)

os.chdir('/tmp')
dir=os.getcwd()
print(dir)

files=os.listdir()
print(files)

f=open("/tmp/em_tomates_verdes_fritos.txt", "w")
f.close()
f=open("em_otro_mas__tomates_verdes_fritos.txt", "w")
f.close()
files=os.listdir()
print(files)

os.rename("em_otro_mas__tomates_verdes_fritos.txt", "em_tomates_verdes_fritos2.txt")
files=os.listdir()
print(files)

os.remove("em_tomates_verdes_fritos2.txt")
files=os.listdir()
print(files)

os.rmdir("test_em") #shutil::rmtree
files=os.listdir()
print(files)