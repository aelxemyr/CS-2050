def average(list):
    sum = 0
    for n in list:
        sum += int(n)
    return sum / len(list)

isbnBookMap = {}
bookRatingMap = {}
bookfile = open("BX-Books.csv")

for line in bookfile:
    linelist = line.split("\"")
    isbnBookMap[linelist[1]] = str(linelist[3] + " by " + linelist[5])
    
for isbn,book in isbnBookMap.items():
    bookRatingMap[book] = []
    
ratingsfile = open("BX-Book-Ratings.csv")

for line in ratingsfile:
    try:
        linelist = line.split("\"")
        book = isbnBookMap[linelist[3]]
        if (linelist[5] != '0'):
            bookRatingMap[book].append(linelist[5])
    except KeyError:
        pass
    
file = open("bookdump.txt","a")
file2 = open("over100ratingsbooklist.txt","a")
file2.write("Books With More Than 100 Ratings\n\n")
n = 0
for book,ratings in bookRatingMap.items():
    if (len(ratings) > 100):
        n += 1
        file.write(book + " : " + str(ratings) + "\n")
        file2.write(book + "\n" + "Average Rating: " + str(average(ratings)) + "\n" + "Number of Ratings: " + str(len(ratings)) + "\n\n")
    
file2.write("Number of Books: " + str(n))
file.close()
file2.close()

