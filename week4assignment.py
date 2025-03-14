try:
    #open first file for reading
    with open('welcome.txt', 'r') as file:
        data = file.read() #read the file

    #Writing a modified version of the file
    with open('myNewText.txt', 'w') as file2:
        edit_data = file2.write(data + " now I am adding a modified version")

    #Reading the modified version
    with open('myNewText.txt', 'r') as modified_data:
        print(modified_data.read())

#Handle the errors
except FileNotFoundError:
    print("File not found. please check the filename")
except Exception as e:
    print(f"error occurred: {e}")

finally:
    file.close()
    file2.close()
    modified_data.close()