# lines_seen = set() # holds lines already seen
# outfile = open("modorigin.csv", "w")
# for line in open("origin.csv", "r"):
#     if line not in lines_seen: # not a duplicate
#         outfile.write(line)
#         lines_seen.add(line)
# outfile.close()

lines_seen = set() # holds lines already seen
outfile = open("moddestination.csv", "w")
for line in open("realdestination.csv", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()