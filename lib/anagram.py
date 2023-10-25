# your code goes here!
class Anagram:
    def __init__(self, mword):
        self.setMyWord(mword);

    def setMyWord(self, mword):
        if (mword == None or len(mword) < 1 or type(mword) != str):
            print("the word must be a non-empty string!");
        else: self._word = mword;

    def getMyWord(self): return self._word;

    word = property(getMyWord, setMyWord);

    def getLetterCountForLetter(self, letter, mword):
        if (letter == None or mword == None or len(mword) < 1): return 0;
        if (len(letter) == 1): pass;
        else: raise Exception("letter must be only one character long!");
        cnt = 0;
        for mletr in mword:
            if (mletr == letter): cnt += 1;
        return cnt;

    def getUniqueLetters(self, mword):
        if (mword == None or len(mword) < 1): return [];
        elif (len(mword) < 2): return [mword[0]];
        else: return list(set(mword));

    def getLetterCountPerLetter(self, ultrs, mword):
        return [self.getLetterCountForLetter(letter, mword) for letter in ultrs];

    def match(self, words):
        #print(f"words = {words}");
        if (words == None or len(words) < 1): return [];
        else:
            uletsinwrd = self.getUniqueLetters(self.word);
            letcntperltrwrd = self.getLetterCountPerLetter(uletsinwrd, self.word);
            #print(self.word);
            #print(uletsinwrd);
            #print(letcntperltrwrd);
            mtchs = [];
            for cword in words:
                if (len(cword) == len(self.word)):
                    #for it to be an anagram:
                    #it must have the same number of each letter
                    #the words must be the same length
                    uletsincwrd = self.getUniqueLetters(cword);
                    letcntperltrcwrd = self.getLetterCountPerLetter(uletsincwrd, cword);
                    #print(cword);
                    #print(uletsincwrd);
                    #print(letcntperltrcwrd);
                    ismatch = True;
                    for i in range(len(uletsinwrd)):
                        ltrwrdfnd = False;
                        for k in range(len(uletsincwrd)):
                            if (uletsinwrd[i] == uletsincwrd[k]):
                                ltrwrdfnd = True;
                                if (letcntperltrwrd[i] == letcntperltrcwrd[k]): pass;
                                else: ltrwrdfnd = False;
                                break;
                        if (ltrwrdfnd): pass;
                        else:
                            ismatch = False;
                            break;
                    if (ismatch): mtchs.append(cword);
                else: pass;
            return mtchs;

#ana = Anagram("bananas");
#print(ana.getUniqueLetters(ana.word));#[b, a, n, s]
#print(ana.getLetterCountForLetter('b', ana.word));#1
#print(ana.getLetterCountForLetter('a', ana.word));#3
#print(ana.getLetterCountForLetter('n', ana.word));#2
#print(ana.getLetterCountForLetter('s', ana.word));#1
#print(ana.match(["something", "stupid", "sananba", "sanbana"]));
#print(ana.match(["something", "stupid", "no", "match"]));


