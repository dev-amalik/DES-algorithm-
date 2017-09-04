

PlainText = '02468aceeca86420'
Key = '0f1571c947d9e859'

#convert binary to Hex
def binToHex(CT):
    CT_hex = ''
    for i in range(0,64,4):
        bits = CT[i:i+4]
        h = hex(int(bits,2))
        CT_hex += h[-1:]
    return CT_hex

#convert hex to binary 
def hexToBinToString( ins ):
    return bin(int(ins, 16))[2:].zfill(64)

#format bits to chunks of 'num' bits
def formatStringBin(ins, num=4):
    return ' '.join(ins[i:i+num] for i in range(0, 64, num))

#performs permutation on input using mat
def permute(input,mat):
    ar = []
    for i,bit in enumerate(mat):
        ar.append(input[bit-1])
    l = list(map(str, ar))
    o = str("".join(map(str,l))  ) 
    return o
#Permuted Choice 1
def pc1(ins):
    CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    
    return permute(ins,CP_1)

#Performs Left Circular Shift
def lcs(ins):
    firstpart, secondpart = ins[:28], ins[28:]
    a = firstpart[0]
    b = firstpart[1:]
    b += a
    a = secondpart[0]
    c = secondpart[1:]
    c += a
    b += c
    return b

#Permuted Choice 2
def pc2(ins):
    CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]
    return permute(ins,CP_2)


#Performs Initial Permutation
def inP(ins):
    PI =  [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
    return permute(ins,PI)

#Performs Expansion Permutation
def eP(ins):
    E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]
    return permute(ins,E)

#Splits 64 bits into two 32 bit chunks
def split(ins):
    firstpart, secondpart = ins[:32], ins[32:]
    return firstpart,secondpart

#Performs Xor
def xorWa(ins1,ins2):
      return  bin(int(ins1,2)^int(ins2,2))[2:]

#Applies Substitution  
def sBox(ins):
    S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]
    ar = []
    index = 0
    for i in range(0,47,6):
        
        a = ins[i:i+6]
        b = a[0]+a[5]
        row = int(b,2)
        d = a[1:5]
        col = int(d,2)
        ar.append(bin(S_BOX[index][row][col])[2:].zfill(4))
        index += 1
        
    l2 = list(map(str, ar))
    o2 = str("".join(map(str,l2)))
        
    return o2

#Performs Permutation
def pP(ins):
    P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]
    
    
    return permute(ins,P)

#Performs Inverse Initial Permutation.
def IP_inv(ins):
    PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
    return permute(ins,PI_1)

nD = 75



#Key Generation   
print('Key Generation')
print('')
print('')


key =  hexToBinToString(Key)
print('Key',formatStringBin(key,8))
print('-'*nD)
print('PC1',formatStringBin(pc1(key),7))
print('-'*nD)
lc = pc1(key)
keys=[]
#Generate all keys and appends each to 'keys[]' list. 
for i in range(16):
    print('K',i+1)
    if i <2:
        lc = lcs(lc)
        keys.append(pc2(lc))
        print('LCS:',formatStringBin(lc,7))
        print('-'*nD)
        print('K ',i+1,":",formatStringBin(pc2(lc),8))
    elif i < 8:
        lc = lcs(lcs(lc))
        keys.append(pc2(lc))
        print('LCS:',formatStringBin(lc,7))
        print('-'*nD)
        print('K ',i+1,":",formatStringBin(pc2(lc),8))

    elif i == 8:
        lc = lcs(lc)
        keys.append(pc2(lc))
        print('LCS:',formatStringBin(lc,7))
        print('-'*nD)
        print('K ',i+1,":",formatStringBin(pc2(lc),8))
    elif i <15:
        lc = lcs(lcs(lc))
        keys.append(pc2(lc))
        print('LCS:',formatStringBin(lc,7))
        print('-'*nD)
        print('K',i+1,":",formatStringBin(pc2(lc),8))
    elif i == 15:
        lc = lcs(lc)
        keys.append(pc2(lc))
        print('LCS:',formatStringBin(lc,7))
        print('-'*nD)
        print('K',i+1,":",formatStringBin(pc2(lc),8))
  
    print('-'*nD)
    print('_'*nD)
    print('◆'*nD)

    
#Round Generation    
print('')
print('')
print('')
print('Round Generation')
print('')
print('')

print('PT   :',formatStringBin(hexToBinToString(PlainText),8))
print('__________________________________________________________')
pt = hexToBinToString(PlainText)
print('IP   :',formatStringBin(inP(pt),8))   
print('__________________________________________________________')

l= inP(pt)
rhs = split(l)[1]
lhs = split(l)[0]

#Generates Lhs and Rhs of all rounds using keys in keys[] 
for z in range(16):
    print('ROUND',z+1)
    ep = eP(rhs)
    xr = xorWa(ep,keys[z]).zfill(48)
    sb = sBox(xr)
    p = pP(sb)
    xr2 = xorWa(p,lhs).zfill(32)

    print('eP:',formatStringBin(eP(rhs),6))
    print('_'*nD)
    print('ep xor K',z+1,':',formatStringBin(xr,6))
    print('_'*nD)
    print('Sbox :',formatStringBin(sBox(xr),8))
    print('_'*nD)
    print('P:',formatStringBin(p,8))
    print('_'*nD)
    print('LHS xor P:',formatStringBin(xr2,8))
    print('_'*nD)
    lhs = rhs
    #print('lhs mute: ',formatStringBin(lhs,8))
    #print('__________________________________________________________')
    rhs = xr2
    #print('rhs mute: ',formatStringBin(rhs,8))
    #print('_'*nD)
    print('◆'*nD)

vl = rhs+lhs
CT = IP_inv(vl)
print('32 bit Swap:',formatStringBin(vl,8))
print('_'*nD)
print('IP:',formatStringBin(CT,8))
print('_'*nD)
print('Cipher Text:',binToHex(CT))




