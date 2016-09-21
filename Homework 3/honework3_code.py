# Bennett Alex Myers
# CS 2050 - Homework 3
# 5 March 2016

main = "__main__" == __name__

class hashList:
    
    # Create a new hashList object with the specified number of buckets
    # The list itself is composed of a list of lists
    def __init__(self, numberOfBuckets):
        self.numberOfBuckets = numberOfBuckets
        self.bucketArray = []
        for i in range(numberOfBuckets):
            self.bucketArray.append([])

    # Return the number of buckets in this list    
    def getNumberOfBuckets(self):
        return self.numberOfBuckets
    
    # Return the list itself
    def getBucketArray(self):
        return self.bucketArray
            
    # Apply the hashing algorithm to index integers into buckets
    def hashIt(self, intArray):
        for n in intArray:
            k = n % self.numberOfBuckets
            self.bucketArray[k].append(n)
            
    # Return a dictionary which details the number of integers in each bucket
    def bucketCount(self):
        count = {}
        i = 1
        for bucket in self.bucketArray:
            size = len(bucket)
            count[i] = size
            i += 1
        return count
    
    # Return the total number of integers stored
    def intCount(self):
        count = 0
        for bucket in self.bucketArray:
            for n in bucket:
                count += 1
        return count
        
class fileIO:
    
    # Produce a list of integers from a text file of integers
    def fileToIntArray(self, filename):
        file = open(filename, "r")
        intArray = []
        for line in file:
            try:
                intArray.append(int(line))
            except ValueError:
                write("errorlog.txt", str("Value error has occured for: " + line))
        return intArray
    
    # Write (append) to a specified file
    def write(self, filename, line):
        file = open(filename, "a")
        file.write(line + "\n")
        
class engine:
    
    # Create a new hashing engine with a specified output file and fileIO object
    # Write header for output file
    def __init__(self, outputFileName):
        self.outputFile = outputFileName
        self.io = fileIO()
        self.io.write(self.outputFile, "Bennett Alex Myers")
        self.io.write(self.outputFile, "CS 2050 - Homework 3\n")
        self.io.write(self.outputFile, "HASHING ALGORITHM RESULTS:\n")      
        
    # Create a new hashList with a specified number of buckets and assign the 
    # integers in the input file to that list through the hashing algorithm.
    # Record the results of processing the input file to the output file.
    def processFile(self, filename, numberOfBuckets):
        hList = hashList(numberOfBuckets)
        intArray = self.io.fileToIntArray(filename)
        hList.hashIt(intArray)
        self.io.write(self.outputFile, self.resultsToString(filename, hList))
        
    # Return a string with the output specified in the assignment    
    def resultsToString(self, filename, hList):
        r = "Input File: " + filename
        r += "\nNumber of Integers: " + str(hList.intCount())
        r += "\nBucket Size Varies"
        r += "\nDistribution of Integers:\n"
        r += self.dictToString(hList.bucketCount())
        return r
    
    # Utility function for listing the items in a dictionary in a sensible way
    def dictToString(self, d):
        s = ""
        for x,y in d.items():
            s += "    Bucket " + str(x) + ": " + str(y) + "\n"
        return s
        
if main:
    
    # **********Main Program********** 
    
    # Hashing trials will be executed with bucket numbers of 10, 20, and 30
    bucketNumbers = [10, 20, 30]
    
    # Files to be processed
    fileList = ["hw3a.txt", "hw3b.txt", "hw3c.txt"]
    
    # Instantiate new engine object
    e = engine("hw3_results.txt")
    
    # Run hashing algorithm for different numbers of buckets for each input file
    for n in bucketNumbers:
        for file in fileList:
            e.processFile(file, n)
