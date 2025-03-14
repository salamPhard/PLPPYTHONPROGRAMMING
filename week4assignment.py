def readfromfile(file):
    try:
    #open first file for reading
        with open(file, 'r') as initialfile:
            data = initialfile.read() #read the file
            #print(data)
    except FileNotFoundError:
        print("File not found")
    initialfile.close()
    return data

def modify_content(file):
    #Writing a modified version of the file
    original_file = readfromfile(file)
    modified_data = original_file.upper()
    return modified_data


def write_new_file(file, new_created_file):
    try:
        #Writing the modified version
        with open(new_created_file, 'w') as modified_data:
            new_file = modified_data.write(file + " I AM NOW MODIFIED AND WRITTEN TO FILE")
            print("File written and modified successfully")
    except FileExistsError:
        print("File already exist")
        modified_data.close()
        
    return new_file



readfromfile('welcome.txt')
new_file = modify_content('welcome.txt')
write_new_file(new_file, 'finaltext.txt')