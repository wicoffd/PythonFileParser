import sys

# Gather our code in a main() function
def main():
    
   

    f = open("r.0.0.mca", "rb")
    with open("file_copy.txt", "wb") as binary_file: # open or create a new file named file_copy
        try:
            byte = f.read(1) # reads one byte from the file and prints it to the screen
            while byte != "": # when the byte is not null
                #print (byte, end='') # print byte and remove the carriage return
                    # Write bytes to file
                binary_file.write(byte)
                byte = f.read(1)
        finally:
            f.close() # closes the file
            binary_file.close() # closes the file copy
            print("exit")
            sys.exit(0)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()