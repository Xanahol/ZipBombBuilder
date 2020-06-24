r'''


PUZZLETEIL 1
------------------------------------------------------------------
writeOnLine("[")
    for i in range(10):
        zipObj = ZipFile('Bomb.zip'.format(i), 'w')
        writeOnLine("#")
        for i in range(10):
            zipObj.write('test {}.txt'.format(i))
    writeOnLine("]")
------------------------------------------------------------------
BOMB_BUILDER3


PUZZLETEIL 2
------------------------------------------------------------------
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
------------------------------------------------------------------
BOMB_BUILDER1


PUZZLETEIL 3
------------------------------------------------------------------
os.chdir(myDirectory)
        for item in os.listdir(myDirectory):
            if item.endswith(extension):
                file_name = os.path.abspath(item)
                zip_ref = zipfile.ZipFile(file_name)
                zip_ref.extractall("{}\Bomb{}".format(myDirectory, i))
                zip_ref.close()
                subprocess.Popen(r'explorer /select,' +
                                 "{}\Bomb{}".format(myDirectory, i) + r'\test 0.txt')
------------------------------------------------------------------
TRIGGER


PUZZLETEIL 4
------------------------------------------------------------------
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
------------------------------------------------------------------
BOMB_BUILDER2



'''
