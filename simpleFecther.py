from urllib.request import urlopen
httpRequest = urlopen("http://sixty-north.com/c/t.txt")
data =  []
for item in httpRequest:
    line_words = item.decode("utf8").split()
    for word in line_words:
        data.append(word)
httpRequest.close()

print(data)