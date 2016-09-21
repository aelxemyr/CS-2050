def int_count(filename):
    count = 0
    file = open(filename, "r")
    for line in file:
        count += 1
    return count
    
def bucket_count(list):
    count = {}
    i = 1
    for bucket in list:
        size = len(bucket)
        count[i] = size
        i += 1
    return count
    
def hashList(numberOfBuckets, filename):
    hashList = []
    for i in range(numberOfBuckets):
        hashList.append([])
    file = open(filename, "r")
    for line in file:
        n = int(line)
        k = int(line) % numberOfBuckets
        hashList[k].append(n)
    return hashList
        
def print_results(filename, hashList):
    print("Input File: ", filename)
    print("Number of Integers: ", int_count(filename))
    print("Bucket Size: (Varies)")
    print("Distribution of Integers in Buckets:", bucket_count(hashList))
        
def main(numberOfBuckets, filename):
    hashed = hashList(numberOfBuckets, filename)
    print_results(filename, hashed)