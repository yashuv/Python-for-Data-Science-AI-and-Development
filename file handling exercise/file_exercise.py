# Exercise
# Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
# Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.

from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee = ('yes', 'no')


# generate some informations in files

def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015, 2020)) + '-' + \
                str(rnd(1, 12))+'-'+str(rnd(1, 25))
            writefile.write(data.format(
                rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020)) + '-' + \
                str(rnd(1, 12))+'-'+str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))


genFiles(memReg, exReg)


'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function removes all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''


def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as readfile:
        with open(exMem, 'a+') as appendfile:
            header = readfile.readline()
            list_of_lines = readfile.readlines()
            readfile.seek(0)
            readfile.write(header)
            for line in list_of_lines:
                if 'yes' in line:
                    readfile.write(line)
                    # print(line)   # just to check if works
                else:
                    appendfile.write(line)

            readfile.truncate()


memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg, exReg)

# same as cleanFiles() function above, just different indent.
# def cleanFiles_(currentMem, exMem):
#   with open(currentMem, 'r+') as readfile:
#     header = readfile.readline()
#     list_of_lines = readfile.readlines()
#     readfile.seek(0)
#     readfile.write(header)
#     for line in list_of_lines:
#       if 'yes' in line:
#         readfile.write(line)
#         print(line)
#     readfile.truncate()

#   with open(exMem, 'a+') as appendfile:
#     for line in list_of_lines:
#       if 'no' in line:
#         appendfile.write(line)


# The code below is to help you view the files after cleaning above.
headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())


# sample data
# Membership No  Date Joined  Active
#     44014      2020-6-12    no
#     89670      2017-9-23    yes
#     45860      2017-1-19    no
#     77252      2017-9-3     no
#     75242      2020-11-5    no
#     89655      2018-8-6     no
#     49878      2020-5-1     no
#     65044      2019-12-24   no
#     19725      2015-4-5     no
#     22818      2017-5-4     no
#     41366      2018-8-10    yes
#     38772      2019-11-13   yes
#     55186      2019-8-15    yes
#     17742      2019-1-23    no
#     81492      2019-11-6    yes
#     79966      2020-2-18    no
#     95802      2016-9-8     no
#     28483      2017-9-2     yes
#     47500      2018-12-12   no
#     50210      2015-6-15    yes
