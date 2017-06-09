# -*- coding: utf-8 -*-

fo = open("output.txt", "r", encoding="utf8" )
outFin=open("outFinal.txt","w+", encoding="utf8")
fc = open("test.conll", "r", encoding="utf8" )
outTest=open("outCheck.txt","w+", encoding="utf8")

next(fo)
next(fo)
for line in fo:
        if line.strip() :
                words = line.split()
                for word in words:
                    outFin.write(word+"\n")
                
                
outFin.close()

for line in fc:
        if line.strip() :
                word = line.split()[1]
                tag=line.split()[4]
                outTest.write(word + "_" + tag + "\n")
                
outTest.close()
