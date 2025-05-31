File=open("txt5.txt","w")
File.write("Hello this is a write method")
File.close()

File=open("txt5.txt","a")
File.write("\nThis is append method")
File.close()