def get_chars_after(s,key,n):
    s = open("data/alicetxt.txt")
    g = s.find(key)
    if g == -1:
        return ""
    else:
        return s[g:n:]
    
def word_count(s, key):
    s = open("data/alicetxt.txt")
    g = s.readlines()
    n = 0
    count = 0
    while n < len(g):
        if g[n] == key:
            count += 1
        n += 1
    return count

def get_words_after(s,key,n):
    s = open("data/alicetxt.txt")
    g = s.split(' ')
    word = s.find(key)
    if word == -1:
        return ""
    else:
        return g[word:n:]
    
def get_chapter(s,chapter):
    s = open("data/alicetxt.txt")
    if chapter == "I":
        chapterFind = "Chapter I"
        chapterEnd = "Chapter II"
        chapterNum = 1
    if chapter == "II":
        chapterFind = "Chapter II"
        chapterEnd = "Chapter III"
        chapterNum = 2
    if chapter == "III":
        chapterFind = "Chapter III"
        chapterEnd = "Chapter IV"
        chapterNum = 3
    if chapter == "IV":
        chapterFind = "Chapter IV"
        chapterEnd = "Chapter V"
        chapterNum = 4
    if chapter == "V":
        chapterFind = "Chapter V"
        chapterEnd = "Chapter VI"
        chapterNum = 5
    if chapter == "VI":
        chapterFind = "Chapter VI"
        chapterEnd = "Chapter VII"
        chapterNum = 6
    if chapter == "VII":
        chapterFind = "Chapter VII"
        chapterEnd = "Chapter VIII"
        chapterNum = 7
    if chapter == "VIII":
        chapterFind = "Chapter VIII"
        chapterEnd = "Chapter IX"
        chapterNum = 8
    if chapter == "IX":
        chapterFind = "Chapter IX"
        chapterEnd = "Chapter X"
        chapterNum = 9
    if chapter == "X":
        chapterFind = "Chapter X"
        chapterEnd = "Chapter XI"
        chapterNum = 10
    if chapter == "XI":
        chapterFind = "Chapter XI"
        chapterEnd = "Chapter XII"
        chapterNum = 11
    if chapter == "XII":
        chapterFind = "Chapter XII"
        chapterEnd = "Chapter XIII"
        chapterNum = 12
    if chapter == "XIII":
        chapterFind = "Chapter XIII"
        chapterEnd = " THE END "
        chapterNum = 13
    n = s.find(chapterFind)
    m = s.find(chapterEnd)
    return s[n:m:]
