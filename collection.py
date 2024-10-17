#Lela Parks
#Oct 15, 2024

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

for author in authors:
    #print ("The author" + author + "died in" + authors[authors])
   print ( "%s" % author + " died in " + "%s" % authors[author])
   
#Make sure to close the brackets to see that the code will finish

#Too many variables are trying to be compressed into one strand

#Dictonaries have keys and values so make sure you seperate each code into the following functions

#This code has to be re-written. Mainly because the "%s" will want to show the code while the "%d" wants
#to be counted as an intiger.
