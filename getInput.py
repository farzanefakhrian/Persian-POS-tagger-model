# -*- coding: utf-8 -*-

f = open("test.conll", "r", encoding="utf8" )
inputfile=open("input.txt","w+", encoding="utf8")

for line in f:
        if line.strip() :
                inputword = line.split()[1]
                inputfile.write(inputword)
                inputfile.write(" ")
                
               
                
        else:
              inputfile.write("\n") 
	#else:
                
                
                #if (inputword=='.') :
                #    inputfile.write("\n")    
                #else :
                #        inputfile.write(" ")
                
                
                
                
	
inputfile.close()
