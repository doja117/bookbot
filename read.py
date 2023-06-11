with open('./book.txt') as f:
    mydict={}
    file_content=f.read().lower()
    words=file_content.split()
    for word in words:
        for char in word:
            if char in mydict:
                mydict[char]+=1
            else:
                mydict[char]=1
    list=[]
    for chars in mydict:
        list.append(chars)

    list.sort()

    for char in list:
        print(f"The {char} character was found {mydict[char]} times")