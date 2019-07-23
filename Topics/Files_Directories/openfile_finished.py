


# Open a file, read, and print. Read (r) is assumed
# file = open('userdata.csv', 'r')
# print(file.read())
# file.close()

# Read a bufferd sized
# file = open('userdata.csv', 'r')
# string_64 = file.read(64)
# print("Size: " + str(len(string_64)) + "\nLine: " + string_64)
# file.close()

# Read one line only
# file = open('userdata.csv', 'r')
# print(file.readline())
# file.close()

# Looping over the file object
# file = open('userdata.csv', 'r')

# for line in file:
#     print(line)

# file_as_list = list(file)
# for line in file_as_list:
#     print(line)

# Open a file for read and write
# file = open('userdata.csv', 'r+')
# file.write('rv1732,ramon,vivanco,m,september 15 1987,broncos,41,quarterback,nissan_stadium,/bin/ksh\n')
# file.write('m1022,surina,moats,f,june 9 1993,bears,80,running_back,arrowhead_stadium,/bin/ksh\n')
# file.write('hb1684,holli,bekker,f,march 12 1998,eagles,92,long_snapper,dignity_health_sports_park,/bin/bash\n')
# file.close()

# Remove line from file
file = open('userdata.csv', 'r+')
delete_string = 'rv1732,ramon,vivanco,m,september 15 1987,broncos,41,quarterback,nissan_stadium,/bin/ksh' + "\n"
for index, line in enumerate(file, start=0):
    print(line)
    if line ==  delete_string:
        print(file.tell())
        print(len(delete_string))
        



        


# Read a file as binary mode


# Open using the with statement
# NOTE:  The advantage is that the file is properly closed after its suite finishes
# with open('userdata.csv') as f:
#     read_data = f.read()
# print(f.closed)


if __name__ == "__main__":
    pass