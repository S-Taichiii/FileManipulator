import sys
import os

class Command:
    @staticmethod
    def reverse(contents: str):
        return contents[::-1]
    
    @staticmethod
    def copy(contents: str):
        return contents
    
    @staticmethod
    def duplicate_contents(contents: str, n: str):
        return contents * int(n)
    
    @staticmethod
    def replace_string(contents: str, needle: str, newString: str):
        return contents.replace(needle, newString)
    
def main():
    # Get the commandline arguments
    argv = sys.argv

    # Judge validation of the arguments
    if not validArgv(argv):
        print('Try again!!')
        sys.exit()

    # manipulate file
    manipulate_file(argv)

    print('Done!!')
    sys.exit()

def validArgv(argv):
    """The function to judge commandline arguments valid"""
    # length of argv must be 4 or 5
    if len(argv) != 4 and len(argv) != 5:
        print('Your intt is wrong.')
        return False
    
    commandList = ['reverse', 'copy', 'duplicate_contents', 'replace_string']
    command = argv[1]

    # Does inputPath exist?
    if not os.path.isfile(argv[2]):
        print('The input path is not found or is not file')
        return False
    
    # Is command valid
    if command not in commandList:
        print('Your input is wrong')
        return False
    elif command == 'reverse' or command == 'copy':
        outputPath = argv[3]

        if len(argv)  != 4:
            print('Your input is wtong.')
            return False
        # Does outputPath exist?
        elif not os.path.isfile(outputPath):
            print('The output file is not found or is not file')
            return False
    elif command == 'duplicate_contents':
        cnt = argv[3]

        if len(argv) != 4:
            print('Your input is wrong')
            return False
        else:
            # Is n number?
            try:
                cnt = int(cnt)
            except ValueError:
                print('Duplicate number must be num')
                return False
    else:
        if len(argv) != 5:
            print('Your input is wrong')
            return False
    
    return True
        
def manipulate_file(argv):
    command = argv[1]
    inputPath = argv[2]
    contents = ''

    if command == 'reverse':
        outputPath = argv[3]

        with open(inputPath, 'r') as f:
            contents = f.read()
        with open(outputPath, 'w') as f:
            f.write(Command.reverse(contents))
    elif command == 'copy':
        outputPath = argv[3]

        with open(inputPath, 'r') as f:
            contents = f.read()
        with open(outputPath, 'w') as f:
            f.write(Command.copy(contents))
    elif command == 'duplicate_contents':
        cnt = argv[3]

        with open(inputPath, 'r') as f:
            contents = f.read()
        with open(inputPath, 'w') as f:
            f.write(Command.duplicate_contents(contents, cnt))
    elif command == 'replace_string':
        needle = argv[3]
        newString = argv[4]

        with open(inputPath, 'r') as f:
            contents = f.read()
        with open(inputPath, 'w') as f:
            f.write(Command.replace_string(contents, needle, newString))

if __name__ == '__main__':
    main()