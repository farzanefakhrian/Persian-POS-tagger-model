# -*- coding: utf-8 -*-

oc = open("outCheck.txt", "r", encoding="utf8" )
of = open("outFinal.txt","r", encoding="utf8")

error = 0.0
correct = 0.0


for c in oc:
    for f in of:
        if c != f :
            error+=1
        else :
            correct +=1
        #next(of)
        break

full=error+correct
accuracy = (correct/full)*100


print (accuracy)
