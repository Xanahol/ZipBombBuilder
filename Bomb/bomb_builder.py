import shutil
from zipfile import ZipFile
import os
import zipfile
import trigger as Trigger
import sys

myLocalDirectory = r'D:\Bomb'

def writeOnLine(st):
    sys.stdout.write(st)
    sys.stdout.flush()


def explosionCleanupCrew(amount):
    writeOnLine("[")
    for i in range(amount):
        for a in range(10):
            os.remove('{}\Bomb{}'.format(myLocalDirectory, i) +
                      r'\t' + 'est {}.txt'.format(a))
        os.rmdir('{}\Bomb{}'.format(myLocalDirectory, i))
        writeOnLine("#")
    os.remove('test.txt')
    os.remove('bomb.zip')
    writeOnLine("]")


def build(a):
    size = 10**a
    f = open("test.txt", "w+")
    print("\nWriting Files...")
    writeOnLine("[")
    for i in range(0, size):
        f.write("This Statement should be repeated a lot of times and compressed")

    for i in range(10):
        original = '{}'.format(myLocalDirectory) + r'\test.txt'
        target = '{}'.format(myLocalDirectory) + \
            r'\test '+"{}".format(i)+'.txt'
        shutil.copyfile(original, target)
        writeOnLine("#")
    writeOnLine("]")
    print("\n\(^o^)/   - Done\n")

    print("Engineering Bomb...")
    writeOnLine("[")
    for i in range(10):
        zipObj = ZipFile('Bomb.zip'.format(i), 'w')
        writeOnLine("#")
        for i in range(10):
            zipObj.write('test {}.txt'.format(i))
    writeOnLine("]")
    print("\n\(^o^)/   - Done\n")

    print("Cleaning up your mess...")
    for i in range(10):
        os.remove("test {}.txt".format(i))

    print("\(^o^)/   - !The Bomb is ready!\n-----------------------------------------------")


def buildTheBomb():
    input("\n\n-----------------------------------------------\n(⌐■_■)\n\n- !WELCOME!\nTo Noëls magical Zip Bomb Simulation. My name is Al and I'll help you on your mildly suicidal mission of building a bomb on your local machine!\n-----------------------------------------------\nHit Enter when you're ready...")
    bombSize = int(input("\nᕕ(⌐■_■)ᕗ  \n\n- Before We make our bomb, I need to know what size it's gonna take. A bigger bomb needs more time to generate and won't open fast but it'll take up a lot of space faster, while a smaller bomb is generated fast and with enaugh triggers it can become really harmful. So, How big should our bomb be? On a scale from 1 to 10? (I recommend using 4)\n"))
    build(bombSize)
    descision = input("\n<(^_^)>   \nWould you like me to trigger the Bomb? (y/n)\n")
    if descision == "y":
        trigger = int(
            input("\nHow many times would you like to trigger it? (to abort use ctrl+C)\n"))
        Trigger.triggerBombXTimes(trigger)
        pass
    else:
        trigger = 0
        pass
    

    cleanupDescision = input(
        "\n<(^_^)>   \nWould you like me to clean up your mess? (y/n)\n")
    if cleanupDescision == "y":
        print("\nヽ(｀Д´)ﾉ  \nCleanup crew: GO, GO, Go!")
        explosionCleanupCrew(trigger)
        pass
    else:
        pass

    buildTheBomb()
