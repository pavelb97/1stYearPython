##### ////// fileLabsheet.py - First lab working with files \\\\\ #####
"""
Working on CS1117 labsheet - Working with files.

Basic file principles covered:
    - Opening & closing file pipes
    - Basic data processing

"""

filehandle = "city_day_time.txt"
inputfile = open(filehandle, "r")

k = []
i = 0

for line in inputfile.readlines():
    line = line.strip("\n").split("\t")
    for word in line:
        if ":" in word:
            word = word.replace(":", "")
            line[-1] = word
            k.append(line)
    i += 1

print(k)
inputfile.close()
