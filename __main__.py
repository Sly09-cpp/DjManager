import DjManager
import os, sys
import argparse

def scan(file_path):
    res = ''
    
    try:
        file = open(file_path, "r")
        for line in file:
            res = print(line.strip())
        file.close()
    except OSError:
        print("Something went wrong.")
    
    return res

def main():
    # Configure arguments for the script executable
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--Scan", help="Scan .token file for token value in same directory level as executable.", nargs='?', const=True, default=False)
    parser.add_argument("-f", "--File_Path", help="Pass in a path to a file holding the bot token value.")
    parser.add_argument("-t", "--Token", help="Pass in token directly as value.")
    parser.add_argument("-c", "--Cookies_Path", help="Cookies file path to use to avoid Youtube bot detection when extracting URL information.")
    args = parser.parse_args()

    # Initialize token alias & cookies file path alias
    token = ''
    cookie_file_path = ''

    # Parse argument values
    if args.Scan:
        token = scan("./.token")
    elif args.Token:
        token = str(args.Token)
    elif args.File_Path:
        token = scan(str(args.File_Path))
    
    if args.Cookies_Path:
        cookie_file_path = str(args.Cookies_Path)

    # Finally, get instance of DJ manager and run
    manager = DjManager(token, cookie_file_path)

if __name__ == "__main__":
    main()