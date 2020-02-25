f=open("archivo.txt","w")

f.write("32 espacio \n")
f.write("33 !\n")
f.write("34 '' \n")
f.write("35 # \n")
f.write("36 $ \n")
f.write("37 % \n")
f.write("38 & \n")
f.write("39 ' \n")
f.write("40 ( \n")
f.write("41 ) \n")
f.write("41 * \n")
f.write("43 + \n")
f.write("44 , \n")


f.close()

f=open("archivo.txt","r")
content=f.read()
print(content)
f.close()
