import os
import time
import platform as pf


# data
notPermissioned = ('Android/data', 'Android/obb')
sys = pf.system()
init = ''
rem = '/storage/emulated/0/'
fNum = allNum = 0
empty = []
startTime = 0
RED = '\033[1;31;40m'
WHITE = '\033[0;38;48m'
rmPre= lambda s: s.replace(rem,'')


# Clears Screen
def cls():
    if sys == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Check The given directory and sub directories
def checkDir(path, rem):
    global fNum, allNum
    try:
    	for item in os.listdir(path):
            item = os.path.join(path, item)
            allNum += 1
            if os.path.isdir(item) and not item.endswith(notPermissioned) :
                print(rmPre(item))
                fNum += 1
                if not os.listdir(item):
                    empty.append(rmPre(item))
                else:
                    checkDir(item, rem)
                    checkBack(item,rem)
    except:
            pass
            
                                  
# Check the pervious directory
def checkBack(path,rem):
	if all(rmPre(os.path.join(path,item)) in empty for item in os.listdir(path)):
		empty.append(rmPre(path.replace(rem,'')))
		

# Starts again if error or wrong input
def startAgain(show):
    cls()
    print(show, '\n')
    start()


# Show Empty Folders removed
def showEmptyFolders():
    print('\nEmpty Folders:')
    if len(empty) != 0:
        emptyMax = len(max(empty))
    for i in range(len(empty)):
        item = empty[i]
        print(f'{i+1}) {item}{RED}-----Removed!!!{WHITE}')


# Delete
def delete():
	for e in empty:
	   try:
	   	os.rmdir(init+e)
	   except:
	   	pass
    		

# Start
def start():
    global init, startTime
    option = input(
        f'{WHITE}Clear the empty folders:\n\
1. Clear the empty folders in curent path\n\
2. Clear the empty folder in given path by user\n\
Enter your option: ')
    print()
    if option == '1':
        path = os.getcwd()
    elif option == '2':
        path = input('Enter path to scan and delete empty folders: ')
        if sys == 'Linux':
            init = rem
        if not os.path.exists(init+path):
            startAgain('The Path does not exit.\nTry again')
            return
        elif sys == 'Windows' and path.endswith('\\') and path.endswith('//'):
            path += '\\'
    else:
        startAgain('Wrong Option')
        return
    startTime = time.time()
    
    checkDir(init + path, rem)
    
    cls()
    showEmptyFolders()

    s = lambda num: "s" if num > 1 else ""
    pad = lambda num: ' ' * \
        (len(str(max(len(empty), fNum, allNum))) - len(str(num)) + 1)

    showNums = lambda pad, n, pr: print('\n', n, pad(n), pr, sep='', end='')
    showNums(pad, len(empty), f'Empty folder{s(len(empty))} Deleted!')
    showNums(pad, fNum, f'Total folder{s(fNum)} Scanned.')
    showNums(pad, allNum, f'Total file{s(allNum)} and folder{s(allNum)}')
    #delete()


# Run
cls()
start()
_ = input(
    f'\n[Took {round(time.time()-startTime,2)}s in executing] \n\t\tPress Enter to Exit.')