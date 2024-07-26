import sys

# Gather our code in a main() function
def main():

    f = open("r.0.0.mca", "rb")
    try:
        byte = f.read(1) # reads one byte from the file and prints it to the screen
        while byte != "": # when the byte is not null
            print (byte, end='') # print byte and remove the carriage return
            
            byte = f.read(1)
    finally:
        f.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()