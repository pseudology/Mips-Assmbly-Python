add $8, $9, $10     #-> 012a4020
add $19, $16, $17   #-> 02119820    
sub $8, $9, $10     #-> 012a4022  
or $8, $9, $10      #-> 012a4025  
addi $8, $9, 5      #-> 21280005  
addi $19, $16, -10  #-> 2213fff6  
ori $8, $9, 5       #-> 35280005  
lui $t0, 0xFFFF     #-> 3c08ffff
Invalid Instruction: #This line will give an error since no instruction present on this line.
Parctically anything that has a syntax error, one way or another. Examples can be:
#This line and the one above will give an error since no instruction present on this line.
addi $234, $3, 5    #Invalid Instruction so wont compile
addm $5, $5, $3     #Invalid Instruction so wont compile
add $5, $xx, $2     #Invalid Instruction so wont compile
Harder ones can be:     #Similar explaination to line 9,10 and 11
addi $4, $2, $3     #Invalid Instruction so wont compile
slt $2, $3, 5       #Invalid Instruction so wont compile