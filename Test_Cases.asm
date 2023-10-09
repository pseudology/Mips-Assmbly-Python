Parctically anything that has a syntax error, one way or another. Examples can be:
addm $5, $5, $3
add $5, $xx, $2
Harder ones can be:
addi $4, $2, $3
slt $2, $3, 5
add $8, $9, $10
add $19, $16, $17
sub $8, $9, $10
or $8, $9, $10
addi $8, $9, 5
addi $19, $16, -10
ori $8, $9, 5
lui $t0, 0xFFFF
add xx ,xx , xx
lbu $s1, 2($s0)
lw $t4, -4($t0)
#	hw1.asm 
# 
# Start of the text segment: 
.text
.globl __start 
main:# execution starts here 
la $a0, msg1		# load address of msg1 into register $a0
addi $v0, $zero, 4      # put 4 in $v0	
syscall# because $v0 is 4, this command prints the characters in address $a0 to the console.

addi $v0, $zero, 5	
syscall# because $v0 is 5, this command reads an integer from the console 
	# value read from keyboard is returned in register $v0 
	# in other words, whatever you type on the console will end up in $v0 
	# debug the code and see it for yourself



add $s0, $zero, $v0	# move $v0 to $s0 
	# This step is not necessary, but I like to do it, because typically $v0 is used for other purposes

la $t9, MyArray		# $t9 = beginning of MyArray 
	# The data segment is at the bottom of this program. Check it out. MyArray is just a bunch of integers in decimal and hex


######################################### Your work starts here ##############################################################
# write your code here 
# 	MyArray[i+2] = MyArray[i]+MyArray[i+1]
#   	where $s0 = i
#   	where MyArray = $t9
# I would be referring MyArray as a since it is convenient to comment
# Please excuse me for that
sll $s0,$s0,2 		# multiply i by 4 since mpis requires adresses at multiples of 4
add $t9,$t9,$s0 	# add s0 to t9 in order to move t9 from a[0] to a[i]
lw $t0,0($t9)		# load a[i] to t0
addi $t9,4# move t9 from a[i] to a[i+1]
lw $t1,0($t9)		# load a[i+1] to t1
addi $t9,4# Move t9 from a[i+1] to a[i+2]
add $t1,$t1,$t0		# add t0 and t1 (a[i] + a[i+1]) to t1
sw $t1,0($t9)		# store t1 to t9(a[i+2])
# The objective required for the assignment has been completed

######################################### Your work ends here ##############################################################

###### printing the result to console 
la $a0, MyArray		# load address of msg2 into register 
li $v0, 4 
syscall# make a syscall to print msg2 in console window 
li $v0, 1# system call code for printing an integer 
lw $a0, 0($t9)		# move integer to be printed (value of MyArray[i+2]) into $a0
syscall		 	# call operating system to perform print 
li $v0, 10 
syscall# exit the program via syscall	

# Start of the data segment 
.data 
msg1:	.asciiz	 "Enter an integer between 0 and 7: " 
msg2:	.asciiz	"The computed result is: " 
MyArray:	.word 5, 0xabcd, 215, 0x12, 55, 12, 0x12, 2, 7, 4 
#end of hw1.asm