import sys
def printarguments():
    arguments = sys.argv[1:]
    #check number of arguments
    num_arguments = len(arguments)
     
    output = ""
    
    #conditional statements
    if num_arguments == 0:
        output += "0 argument{}.\n".format('s' if num_arguments != 1 else '')
    else:
        output += "{} argument{}:\n".format(num_arguments, 's' if num_arguments != 1 else '')

        # Construct string for each argument with its position
    for i, arg in enumerate(arguments, 1):
         output += "{}: {}\n".format(i, arg)
    return output.strip()   
if __name__== '__main__':

     result = printarguments()
     if result:
        print(result)