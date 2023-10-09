def output():                                            #function to make txt file
    final= (name + '.txt').replace(".asm.txt",".txt")    #replacing .asm.txt with .txt
    temp_f = open(final, 'w')
    for i in range(len(ans)):                            #For loop to write answers in txt file
        temp_f.write(input_final[i]+" " * (40-len(input_final[i])) +" ---->"+ans[i]+'\n')
        
    line_count=len(input_final)
    success=line_count-failed
    temp_f.write("----------------------------------------------"+'\n')
    temp_f.write("END OF PARSING"+'\n')
    temp_f.write("----------------------------------------------"+'\n')
    temp_f.write("Total Instructions: "+ str(line_count)+'\n')
    temp_f.write("Total Instructions Succesfully  Parsed : "+ str(success)+'\n')
    temp_f.write("Total Instructions Failed : "+ str(failed)+'\n')

    temp_f.close()

def parser():

    opdict = {
        "add": "0000000 100000",                         #copy pasted opcode dictionary to my input cleaner so that i can check whether the instruction is valid
        "addi": "001000",
        "addiu": "001001",
        "addu": "000000 100001",
        "and": "000000 100100",
        "andi": "00100",
        "j": "000010",
        "jal": "000011",
        "jr": "000000 001000",
        "lbu": "100100",
        "lhu": "100101",
        "ll": "110000",
        "lui": "001111",
        "lw": "100011",
        "nor": "000000 00111",
        "or": "000000 100101",
        "ori": "001101",
        "slt": "000000 101010",
        "slti": "001010",
        "sltiu": "001011",
        "sltu": "000000 101011",
        "sll": "000000 000000",
        "srl": "000000 000010",
        "sb": "101000",
        "sc": "111000",
        "sh": "101001",
        "sw": "101011",
        "sub": "000000 100010",
        "subu": "000000 100011",
        }
    
    
    
    name = input("Enter file name : ")
    file = open(name, 'r')
    content = file.read()
    file.close()

    content = content.splitlines()            #splitting the lines of .asm file
    
    input_final = []

    i = 0

    for i in range(len(content)):
        if len(content[i]) == 0:              #removing blank lines
            pass

        else:
            if str(content[i][:3]) in opdict:   #checks if strings with 3 letters are present in opcode dictionary(add etc)

                input_final.append((content[i])) #checks if strings with 2 letters are present in opcode dictionary(la lw etc)
            elif content[i][:2] in opdict:
                input_final.append((content[i]))
            elif content[i][:1] in opdict:
                input_final.append((content[i]))
            else:
                pass
    
                
                 

    for i in range(len(input_final)):
        temp = input_final[i]         #assigning temp variable 

        for x in range(len(temp)):
            if temp[x] == '#':    #removing comments
                input_final[i] = temp[0:x:]

        else:
            pass
    return name,input_final


def opcodes(op):      #dicitonary for opcode
    
    opdict = {
        "add": "000000 100000",
        "addi": "001000",
        "addiu": "001001",
        "addu": "000000 100001",
        "and": "000000 100100",
        "andi": "00100",
        "beq": "000100",
        "bne": "000101",
        "j": "000010",
        "jal": "000011",
        "jr": "000000 001000",
        "lbu": "100100",
        "lhu": "100101",
        "ll": "110000",
        "lui": "001111",
        "lw": "100011",
        "nor": "000000 00111",
        "or": "000000 100101",
        "ori": "001101",
        "slt": "000000 101010",
        "slti": "001010",
        "sltiu": "001011",
        "sltu": "000000 101011",
        "sll": "000000 000000",
        "srl": "000000 000010",
        "sb": "101000",
        "sc": "111000",
        "sh": "101001",
        "sw": "101011",
        "sub": "000000 100010",
        "subu": "000000 100011",
    }
    if op in opdict:
        return opdict[op]

    else:
        print("Invalid code")
        

    print(opcode)


def registers(reg):   #dictionary for registers
    
    regdict = {
        "zero": 0,
        "0": 0,
        "at": 1,
        "v0": 2,
        "v1": 3,
        "a0": 4,
        "a1": 5,
        "a2": 6,
        "a3": 7,
        "t0": 8,
        "t1": 9,
        "t2": 10,
        "t3": 11,
        "t4": 12,
        "t5": 13,
        "t6": 14,
        "t7": 15,
        "s0": 16,
        "s1": 17,
        "s2": 18,
        "s3": 19,
        "s4": 20,
        "s5": 21,
        "s6": 22,
        "s7": 23,
        "t8": 24,
        "t9": 25,
        "k0": 26,
        "k1": 27,
        "gp": 28,
        "sp": 29,
        "fp": 30,
        "ra": 31,
    }

    if reg in regdict and reg != '$zero':
        binary.append(bin(regdict[reg]).replace("0b", ""))        #if register exists directly converts to binary
        return binary
    elif reg.isdigit() :
          
        binary.append(bin(int(reg)).replace("0b", ""))           #if its a digit then checks if -ve if true then appends 2s complement
        print('isidigt')
    elif reg[0]=='-':
        binary.append(twosComplement(int(reg), 16))
    elif reg == '$zero':
        binary.append('0000')
    elif reg[0:2]=='0x':
        binary.append('hex')
        pass
    else:
        print("Invalid code")
    return binary



def twosComplement(value, bitLength):     #function to convert to twos complement
    return (bin(value & (2 ** bitLength - 1)).replace('0b', '')).zfill(bitLength) 


# end of 2nd function
def Answer(hex_imm):

    print(binary)
    hex_split = [(binary_f[i:i + 4]) for i in range(0, len(binary_f), 4)]# splitting binary into groups of 4
    print("curr",hex_split)


    print(binary)

    for i in range(0, len(hex_split)):
        n = str(hex_split[i])
        z = bth(n)                                                             # calling function to convert to hex
        hex_split[i] = str(z)

    print('hex_split',hex_split)
    if hex_imm==1:
        print("flag 1")
        hex_split[len(hex_split)-1]=result[3].replace("0x","")
    elif hex_imm==2:
        print("flag 2")
        print(result[2])
        hex_split[len(hex_split)-1]=result[2].replace("0x","")
        print("hex_split",hex_split)
    else:
        pass




    hex_split = ''.join(map(str, hex_split))
    hex_split = '0x' + hex_split                                           #adding 0x

    print("Instruction parsed: ", i)
    ans.append(hex_split)
    print(ans)
    return ans


def bth(val):
    
    hexdict = {                           #dictionary for binary to hex
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    if val in hexdict:
        z = hexdict[val]
        return z

    else:
        print("invalid")


def bit_check(): 
                    #function to check if bit value is satisfied for rs rt rd imm
    
    hex_imm=0
    num2 = []
    num3 = []

    i_signed = ['addi', 'lhu', 'll', 'lui', 'slti']
    r_type = ['add', 'addu', 'and', 'nor', 'or', 'sub', 'subu', 'slt']
    shift_type = ['sll', 'srl']
    i_unsign = ['addiu', 'andi', 'ori', 'sltiu']
    offset_sign = ['lw', 'sb', 'sc', 'sh', 'sw']
    off_unsign = ['lbu']

    if result[0] in i_signed:
        print(binary)

        if len(result) == 3:
            rs = binary[1]
            imm = result[2]
            rt = '00000'
        else:
            print("MY")
            rs = binary[1]

            rt = binary[2]

            imm = result[3]

        if len(rt) < 5 and rt !='00000':
            binary[1] = rt.zfill(5)
        elif imm[0:2] == '0x':
            binary[1]=rt
        elif rt=='00000':
            binary.append(rt)
            print('qppend',binary)
        else:
            binary[1] = rt
        

        if len(rs) < 5:
            binary[2] = rs.zfill(5)
        else:
            binary[2] = rs


        num = []
        hex_imm=0
        
        if len(result) == 4:
            print("reched 4")
            
            if len(binary[3]) < 16:
                if imm[0:2] == '0x':
                    binary[3] = '0000'
                    print(binary)
                    hex_imm = 1
                    return hex_imm
                else:
                    x=twosComplement(int(imm), 16)
                    binary[3]=x
            else:
                x = twosComplement(int(imm), 16)
                binary[3] = x


        elif len(result) == 3:
            if len(binary[2]) < 16:
                if imm[0:2] == '0x':
                    binary.append('0000')
                    hex_imm = 2
                    return hex_imm
                else:
                    x = twosComplement(int(imm), 16)
                    binary[2] = x
            else:
                x = twosComplement(int(imm), 16)
                binary[2] = x

        else:
            pass
        print(binary)

    elif result[0] in offset_sign:

     
        rs = binary[1]
        rt = binary[3]
        imm = result[2]

        print('here')
        print(rs)
        print(imm)
        print(rt)
        if len(rs) < 5:
            binary[2]=rs.zfill(5)
        else:
            binary[2] = rs

        if len(rt) < 5:
            binary[1]=rt.zfill(5)
        else:
            binary[1] = rt

        num = []
        
        if len(binary) == 4 and len(binary[3]) < 16:
            x = twosComplement(int(imm), 16)
            binary[3] = x
        elif len(binary) == 3 and len(binary[2]) < 16:
            x = twosComplement(int(imm), 16)
            binary[2] = x
        else:
            x = twosComplement(int(imm), 16)
            binary[3] = x
        print(binary)
    
    elif result[0] in r_type:
        rs = binary[2]
        rt = binary[3]
        rd = binary[1]
        shamt = '0'

        if len(rs) < 5:
            binary[1] = rs.zfill(5)

        else:
            binary[1] = rs

        if len(rt) < 5:
            binary[2] = rt.zfill(5)

        else:
            binary[2] = rt
       
        if len(rd) < 5:
            binary[3]=rd.zfill(5)
        else:
            binary[3] = rd
        num = []

        if shamt == '0':
            binary.append('00000')


        else:
            x = 5 - len(shamt)

            for i in range(0, x):
                num.append('0')
            num.append(shamt)
            print(num)

            num = ''.join(map(str, num))
            print('shamt is ', num)
            x = num
            binary.append(x)

        if len(funct) < 6:

            x = 6 - len(funct)

            for i in range(0, x):
                num.append('0')
            num.append(funct)

            num = ''.join(map(str, num))

            x = num
            binary.append(funct)

        else:

            binary.append(funct)

        print(binary)

    elif result[0] in shift_type:

        rs = '00000'

        rt = binary[2]

        rd = binary[1]
        
        shamt = binary[3]

        print(rd)
        print('rs is ', rs)
        print(rt)

        if len(rs) < 5:
            binary[1]=rs.zfill(5)
        else:

            binary[1] = rs

        if len(rt) < 5:
           binary[2] = rt.zfill(5)
        else:
            binary[2] = rt
        if len(rd) < 5:
            binary[3] = rd.zfill(5)
        else:
            binary[3] = rd

        num = []

        if len(shamt) < 5:
            x = 5 - len(shamt)

            for i in range(0, x):
                num.append('0')
            num.append(shamt)
            print(num)

            num = ''.join(map(str, num))
            print('shamt is ', num)
            x = num
            binary.append(x)


        else:
            binary.append(shamt)

        if len(funct) < 6:

            x = 6 - len(funct)

            for i in range(0, x):
                num.append('0')
            num.append(funct)
            print(num)

            num = ''.join(map(str, num))
            print(x)
            x = num
            binary.append(x)

        else:
            print("else")
            binary.append(funct)

        print(binary)

    elif result[0] in off_unsign:
        imm = binary[2]
        rs = binary[3]
        rt = binary[1]
        print('here')
        print(rs)
        print(imm)
        print(rt)
        if len(rs) < 5:
            binary[1] = rs.zfill(5)
        else:
            binary[1] = rs

        if len(rt) < 5:
           binary[2] = rt.zfill(5)
        else:
            binary[2] = rt

        num = []
        if len(imm) < 16 and imm != '0':

            binary[3] = imm.zfill(16)
        elif imm == '0':
            binary[3] =imm.zfill(15)
        else:
            pass

    else:
        print(binary)

        if len(binary) == 3:
            rs = binary[1]
            imm = binary[2]
            rt = '00000'
        else:
            rs = binary[1]

            rt = binary[2]

            imm = binary[3]

        if len(rs) < 5:
            binary[2] = rs.zfill(5)
        else:
            binary[2] = rs
        if len(rt) < 5:
            binary[1] = rt.zfill(5)
        elif len(binary) == 3:
            binary.append(rt)
        else:
            binary[1] = rt
        num = []
        if len(imm) < 16 and imm != '0':
            binary[3] = imm.zfill(16)
        elif imm == '0':
            binary[3] = imm.zfill(15)
        else:
            pass


# main

   
    
ans = []
failed=0
r_type = ['add', 'addu', 'and', 'nor', 'or', 'sub', 'subu', 'slt']
shift_type = ['sll', 'srl']
i_unsigned = ['addi', 'lhu', 'll', 'lui', 'slti']

name,input_final=parser()

for i in range(len(input_final)):
    try:
        line = input_final[i]
        
        binary = []
        i = 0
        line = line.replace("(", " ,")
        line = line.replace(")", " ")
        line=line.replace("$" , " ")
        mysplit = [x.strip() for x in line.split(',')]
        print(mysplit)
        result = mysplit[0].split()

        for i in range(1, len(mysplit)):
                result.append(mysplit[i])

        print(result)
        if result[0] == 'add' or 'addu' or 'and' or 'nor' or 'or' or 'sub' or 'subu' or 'slt' or 'sll' or 'srl': #Checks If its r type then splits the opcode for function
            opcode = opcodes(result[0])
            buffer_function = opcode.split(" ")
            print(buffer_function)
            opcode = buffer_function[0]
            if len(buffer_function) == 2:
                funct = buffer_function[1]
            else:
                pass
            binary.append(opcode)



        else:
            opcode=opcodes(result[0])
            binary.append(opcode)

        for i in range(1, len(result)):   #looping all registers to find binary value
            binary = registers(result[i])

        hex_imm = bit_check()             #checking if all bits are satisfied for rs rt rd etc and if immediate is HEX then it will raise a flag for hex_imm
        

        binary_f = ''.join(map(str, binary))
        print(binary_f)


        ans= Answer(hex_imm)

        for i in range(len(ans)):
            print(ans[i])
         #function to append to text file
      
    except:
        Failed_case=[]
        print("INVALID INSTRUCTION")
        ans.append("{} : COULDNT PARSE INSTRUCTION / INVALID INSTRUCTION ".format(line))
        failed=failed+1
        pass
output()

