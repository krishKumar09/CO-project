register = {
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "fp": "01000",
    "s0": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",
    "s2": "10010",
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",
    "t3": "11100",
    "t4": "11101",
    "t5": "11110",
    "t6": "11111",
    "x0": "00000",
    "x1": "00001",
    "x2": "00010",
    "x3": "00011",
    "x4": "00100",
    "x5": "00101",
    "x6": "00110",
    "x7": "00111",
    "x8": "01000",
    "x9": "01001",
    "x10": "01010",
    "x11": "01011",
    "x12": "01100",
    "x13": "01101",
    "x14": "01110",
    "x15": "01111",
    "x16": "10000",
    "x17": "10001",
    "x18": "10010",
    "x19": "10011",
    "x20": "10100",
    "x21": "10101",
    "x22": "10110",
    "x23": "10111",
    "x24": "11000",
    "x25": "11001",
    "x26": "11010",
    "x27": "11011",
    "x28": "11100",
    "x29": "11101",
    "x30": "11110",
    "x31": "11111",

}


opcode = {
    "add": "0110011",
    "sub": "0110011",
    "sll": "0110011",
    "slt": "0110011",
    "sltu": "0110011",
    "xor": "0110011",
    "srl": "0110011",
    "or": "0110011",
    "and": "0110011",
    "lw": "0000011",
    "addi": "0010011",
    "sltiu": "0010011",
    "jalr": "1100111",
    "beq": "1100011",
    "bne": "1100011",
    "blt": "1100011",
    "bge": "1100011",
    "bltu": "1100011",
    "bgeu": "1100011",
    "lui": "0110111",
    "auipc": "0010111",
    "sw": "0100011",
    "jal": "1101111"
}

def binary(dec):
    bin_list = ['0'] * 12
    i = 11
    n = abs(dec)

    while n > 0:
        bin_list[i] = str(n % 2)
        n = n // 2
        i -= 1

    if dec < 0:
        j = 11
        while j >= 0:
            if bin_list[j] == '0':
                j -= 1
            else:
                break

        k = j - 1
        while k >= 0:
            if bin_list[k] == '0':
                bin_list[k] = '1'
            else:
                bin_list[k] = '0'
            k -= 1

    return ''.join(bin_list)

def Binarytodecimal(dec):
    bin_list = ['0'] * 20
    i = 19
    n = abs(dec)

    while n > 0:
        bin_list[i] = str(n % 2)
        n = n // 2
        i -= 1

    if dec < 0:
        j = 19
        while j >= 0:
            if bin_list[j] == '0':
                j -= 1
            else:
                break

        k = j - 1
        while k >= 0:
            if bin_list[k] == '0':
                bin_list[k] = '1'
            else:
                bin_list[k] = '0'
            k -= 1

    return ''.join(bin_list)

def add(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "000"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def sub(instruct):
    s = "0100000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "000"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s


def sll(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "001"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def slt(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "010"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def sltu(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "011"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def xor(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "100"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def srl(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "101"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def Or(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "110"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def And(instruct):
    s = "0000000"
    s += register[instruct[3]]
    s += register[instruct[2]]
    s += "111"
    s += register[instruct[1]]
    s += opcode[instruct[0]]
    return s

def lw(instruct):
    s = binary(int(instruct[2]))
    s += register[instruct[3]]
    s += "010"
    s += register[instruct[1]]
    s += "0000011"
    return s

def addi(instruct):
    s = binary(int(instruct[3]))
    s += register[instruct[2]]
    s += "000"
    s += register[instruct[1]]
    s += "0010011"
    return s

def sltiu(instruct):
    s = binary(int(instruct[3]))
    s += register[instruct[2]]
    s += "011"
    s += register[instruct[1]]
    s += "0010011"
    return s

def jalr(instruct):
    s = binary(int(instruct[3]))
    s += register[instruct[2]]
    s += "000"
    s += register[instruct[1]]
    s += "1100111"
    return s

def sw(instruct):
    k = binary(int(instruct[2]))
    s = k[:7]
    s += register[instruct[1]]
    s += register[instruct[3]]
    s += "010"
    s += k[7:]
    s += "0100011"
    return s

def beq(instruct):
    k = binary(int(instruct[3]))
    s = k[:7]
    s += register[instruct[2]]
    s += register[instruct[1]]
    s += "000"
    s += k[7:]
    s += "1100011"
    return s

def bne(instruct):
    k = binary(int(instruct[3]))
    s = k[:7]
    s += register[instruct[2]]
    s += register[instruct[1]]
    s += "001"
    s += k[7:]
    s += "1100011"
    return s

def blt(instruct):
    k = binary(int(instruct[3]))
    s = k[:7]
    s += register[instruct[2]]
    s += register[instruct[1]]
    s += "100"
    s += k[7:]
    s += "1100011"
    return s

def bge(instruct):
    k = binary(int(instruct[3]))
    s = k[:7]
    s += register[instruct[2]]
    s += register[instruct[1]]
    s += "101"
    s += k[7:]
    s += "1100011"
    return s

def bltu(instruct):
    k = binary(int(instruct[3]))
    s = k[:7]
    s += register[instruct[2]]
    s += register[instruct[1]]
    s += "110"
    s += k[7:]
    s += "1100011"
    return s

def bgeu(instruct):
    k = binary(int(instruct[3]))
    s = k[:7]
    s += register[instruct[2]]
    s += register[instruct[1]]
    s += "111"
    s += k[7:]
    s += "1100011"
    return s

def lui(instruct):
    s=""
    if int(instruct[2])>=0:
        s="0"*20
    else:
        s="1"*20
    s += register[instruct[1]]
    s += "0110111"
    return s

def auipc(instruct):
    s =""
    if int(instruct[2])>=0:
        s="0"*20
    else:
        s="1"*20
    s += register[instruct[1]]
    s += "0010111"
    return s

def jal(instruct):
    k = Binarytodecimal(int(instruct[2]))
    s = k[-12:-1]
    s += k[0:9]
    s += register[instruct[1]]
    s += "1101111"
    return s

def instruct(s):
    i = 0
    t = []
    k = ""
    while i < len(s):
        if s[i] in " ,()":
            if k:
                t.append(k)
                k = ""
        else:
            k += s[i]
        i += 1
    if k:
        t.append(k)
    return t

def fileWork(filename):
    f = open(filename, 'r')
    v = f.readlines()
    t = []
    for i in range(len(v)):
        k = v[i]
        m = k[:-1]
        t.append(m)
    return t

def fileGenerate(list,filename):
    t = "New folder\ " + filename
    f = open(f"{t}","a")
    for i in range(len(list)):
        f.write(list[i])
        f.write("\n")



def final(filename):
   global instruct
   q = []
   instructions = fileWork(filename)
   leng=len(instructions)
   for a in range(leng):
          c = instruct(instructions[a])
          if c[0]== 'add':
              q.append(add(c))
          elif c[0]=='sub':
              q.append(sub(c))
          elif c[0]=='sll':
              q.append(sll(c))
          elif c[0]=='slt':
              q.append(slt(c))
          elif c[0]=='sltu':
              q.append(sltu(c))
          elif c[0]=='xor':
              q.append(xor(c))
          elif c[0]=='srl':
              q.append(srl(c))
          elif c[0]=='and':
              q.append(And(c))
          elif c[0]=='or':
              q.append(Or(c))
          elif c[0]=='lw':
              q.append(lw(c))
          elif c[0]=='addi':
              q.append(addi(c))
          elif c[0]=='sltiu':
              q.append(sltiu(c))
          elif c[0]=='jalr':
              q.append(jalr(c))
          elif c[0]=='sw':
              q.append(sw(c))
          elif c[0]=='beq':
              q.append(beq(c))
          elif c[0]=='bne':
              q.append(bne(c))
          elif c[0]=='blt':
              q.append(blt(c))
          elif c[0]=='bge':
              q.append(bge(c))
          elif c[0]=='bltu':
              q.append(bltu(c))
          elif c[0]=='bgeu':
              q.append(bgeu(c))
          elif c[0]=='bge':
              q.append(bge(c))
          elif c[0]=='lui':
              q.append(lui(c))
          elif c[0]=='auipc':
              q.append(auipc(c))
          elif c[0]=='jal':
              q.append(jal(c))
          else:
              q.append("Invalid")
   fileGenerate(q,filename)

krish = input()
final(krish)





