import requests, sys, argparse, os
from termcolor import colored

def GetArgs():
    parser = argparse.ArgumentParser(description="DIRECTORY FINDER")
    parser.add_argument("-l","--link",metavar="LINK",action="store",type=str,help="Link for find dorectory")
    parser.add_argument("-d","--directory")
    return parser.parse_args()

def Help():
    title = "DIRECTORY FINDER"
    print("""
########################################################\n""" + 
f"#{title:_^54}#" + """
#  -h/--help    HELP    show help and exit             #
#  -l/--link    LINK    input link to find             #
#______________________________________________________#
#  made by @example                                    #
########################################################
""")

status = 0
fstatus = False
foundDir = []
dirs = []

try:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        Help()
        exit()
except IndexError:
    print(colored("[!]","red"),"Missing arguments")
    exit()

arguments = GetArgs()
if arguments.link:
    LINK  = arguments.link
else:
    print(colored("[!]"),"Link not defind")
    exit()

try:Directory = [line.strip() for line in open("Dirs.txt","r").readlines()]
except FileNotFoundError as error:
    print(colored("[!]","red"),"Missing directory file")
    exit()


if LINK == "" or None:
    print(colored("[!]","red"),"Missing the link")
    exit()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if "http" or "https" in LINK:LINK =  (LINK + "/")
if "http://" or "https//" in LINK:LINK = (LINK + "/")
else:LINK = "http://" + LINK + "/"

if "result.txt" in os.listdir(os.getcwd()):fstatus = True
file = open("result.txt","a")
if fstatus == True:file.write("\n")
for dir in Directory:
    rslt = requests.get(LINK + dir)
    if rslt.status_code != 200:continue
    if dir in dirs:continue
    print(colored("[+]","green"),f"{dir} found")
    dirs.append(dir)
    foundDir.append(LINK + dir)
    status+=1

print(foundDir)

try:file.writelines("\n".join(foundDir))
except TypeError:pass
except Exception:pass

print(colored("[*]","magenta"),"status...")
print(f"{status} directories found")
input("Back To Menu (Press Enter...)")