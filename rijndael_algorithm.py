import numpy as np
import random

def sub_byte(x):
    S_box = [
        0x63,0x7c ,0x77 ,0x7b ,0xf2 ,0x6b ,0x6f ,0xc5 ,0x30 ,0x01 ,0x67 ,0x2b ,0xfe ,0xd7 ,0xab ,0x76,
        0xca ,0x82 ,0xc9 ,0x7d ,0xfa ,0x59 ,0x47 ,0xf0 ,0xad ,0xd4 ,0xa2 ,0xaf ,0x9c ,0xa4 ,0x72 ,0xc0,
        0xb7 ,0xfd ,0x93 ,0x26 ,0x36 ,0x3f ,0xf7 ,0xcc ,0x34 ,0xa5 ,0xe5 ,0xf1 ,0x71 ,0xd8 ,0x31 ,0x15,
        0x04 ,0xc7 ,0x23 ,0xc3 ,0x18 ,0x96 ,0x05 ,0x9a ,0x07 ,0x12 ,0x80 ,0xe2 ,0xeb ,0x27 ,0xb2 ,0x75,
        0x09 ,0x83 ,0x2c ,0x1a ,0x1b ,0x6e ,0x5a ,0xa0 ,0x52 ,0x3b ,0xd6 ,0xb3 ,0x29 ,0xe3 ,0x2f ,0x84,
        0x53 ,0xd1 ,0x00 ,0xed ,0x20 ,0xfc ,0xb1 ,0x5b ,0x6a ,0xcb ,0xbe ,0x39 ,0x4a ,0x4c ,0x58 ,0xcf,
        0xd0 ,0xef ,0xaa ,0xfb ,0x43 ,0x4d ,0x33 ,0x85 ,0x45 ,0xf9 ,0x02 ,0x7f ,0x50 ,0x3c ,0x9f ,0xa8,
        0x51 ,0xa3 ,0x40 ,0x8f ,0x92 ,0x9d ,0x38 ,0xf5 ,0xbc ,0xb6 ,0xda ,0x21 ,0x10 ,0xff ,0xf3 ,0xd2,
        0xcd ,0x0c ,0x13 ,0xec ,0x5f ,0x97 ,0x44 ,0x17 ,0xc4 ,0xa7 ,0x7e ,0x3d ,0x64 ,0x5d ,0x19 ,0x73,
        0x60 ,0x81 ,0x4f ,0xdc ,0x22 ,0x2a ,0x90 ,0x88 ,0x46 ,0xee ,0xb8 ,0x14 ,0xde ,0x5e ,0x0b ,0xdb,
        0xe0 ,0x32 ,0x3a ,0x0a ,0x49 ,0x06 ,0x24 ,0x5c ,0xc2 ,0xd3 ,0xac ,0x62 ,0x91 ,0x95 ,0xe4 ,0x79,
        0xe7 ,0xc8 ,0x37 ,0x6d ,0x8d ,0xd5 ,0x4e ,0xa9 ,0x6c ,0x56 ,0xf4 ,0xea ,0x65 ,0x7a ,0xae ,0x08,
        0xba ,0x78 ,0x25 ,0x2e ,0x1c ,0xa6 ,0xb4 ,0xc6 ,0xe8 ,0xdd ,0x74 ,0x1f ,0x4b ,0xbd ,0x8b ,0x8a,
        0x70 ,0x3e ,0xb5 ,0x66 ,0x48 ,0x03 ,0xf6 ,0x0e ,0x61 ,0x35 ,0x57 ,0xb9 ,0x86 ,0xc1 ,0x1d ,0x9e,
        0xe1 ,0xf8 ,0x98 ,0x11 ,0x69 ,0xd9 ,0x8e ,0x94 ,0x9b ,0x1e ,0x87 ,0xe9 ,0xce ,0x55 ,0x28 ,0xdf,
        0x8c ,0xa1 ,0x89 ,0x0d ,0xbf ,0xe6 ,0x42 ,0x68 ,0x41 ,0x99 ,0x2d ,0x0f ,0xb0 ,0x54 ,0xbb ,0x16
    ]
    
    return S_box[x]

def mixColumns(column):


    newCol = [0,0,0,0]
    a = int(column[0],16)
    b = int(column[1],16)
    c = int(column[2],16)
    d = int(column[3],16)
    #print(a)

    newCol[0] = np.uint8(a*2) ^ 27 if (a/128 > 1) else np.uint8(a*2) 
    newCol[0] = newCol[0] ^ np.uint8(b*2) ^ 27 ^ b if (b/128 > 1) else newCol[0] ^ np.uint8(b*2) ^ b
    newCol[0] = hex(newCol[0] ^ c ^ d)

    newCol[1] = np.uint8(b*2) ^ 27 if (b/128 > 1) else np.uint8(b*2) 
    newCol[1] = newCol[1] ^ np.uint8(c*2) ^ 27 ^ c if (c/128 > 1) else newCol[1] ^ np.uint8(c*2) ^ c
    newCol[1] = hex(newCol[1] ^ d ^ a)

    newCol[2] = np.uint8(c*2) ^ 27 if (c/128 > 1) else np.uint8(c*2) 
    newCol[2] = newCol[2] ^ np.uint8(d*2) ^ 27 ^ d if (d/128 > 1) else newCol[2] ^ np.uint8(d*2) ^ d
    newCol[2] = hex(newCol[2] ^ a ^ b)

    newCol[3] = np.uint8(d*2) ^ 27 if (d/128 > 1) else np.uint8(d*2) 
    newCol[3] = newCol[3] ^ np.uint8(a*2) ^ 27 ^ a if (a/128 > 1) else newCol[3] ^ np.uint8(a*2) ^ a
    newCol[3] = hex(newCol[3] ^ b ^ c)

    
    return(newCol)

def main():

    input_message = input("Enter a message to be encrypted: ")

    #-------------- Convert message into hex --------------#
    input_message_hex = ""
    for char in input_message:
        input_message_hex = input_message_hex + format(ord(char),'x')
    
    print("\nMessage in hex: %s" % input_message_hex)

    #Pad 0s to get blocks of 16 bytes
    if(len(input_message_hex) % 32 != 0):
        for i in range(0,32-len(input_message_hex)%32):
            input_message_hex = input_message_hex + "0"

    #-------------- Generate Cipher Key --------------#
    cipher_key_matrix = []
    for i in range(0,16):
        cipher_key_matrix.append('%s%s' % (str(format(random.randint(0,15),'x')), str(format(random.randint(0,15),'x'))))
    #cipher_key_matrix = ['2b','28','ab','09','7e','ae','f7','cf','15','d2','15','4f','16','a6','88','3c']

    #Convert cipher key into a colxrow matrix to make operations easier
    cipher_key = ''.join(cipher_key_matrix)
    cipher_key_matrix = np.array(cipher_key_matrix)
    cipher_key_matrix = cipher_key_matrix.reshape(4,4)
    cipher_key_matrix = cipher_key_matrix.transpose()
    print("Cipher Key: %s" % cipher_key)
    
    #-------------- Generate Cipher Key Schedule --------------#
    key_schedule = []
    Rcon = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36]

    key_schedule.append(cipher_key_matrix) #Round 0
    for round in range(1,11):
        round_key = np.zeros((4,4), 'U10')
        #Apply last column rotation
        round_key[3] = key_schedule[round-1][3]
        round_key[3] = np.roll(round_key[3],3)
        #Sub bytes
        for i in range(0,4):
            round_key[3][i] = sub_byte(x=int(round_key[3][i],16))

        #XOR round key's first value with Rcon
        round_key[3][0] = int(round_key[3][0]) ^ int(Rcon[round-1])
            
        #XOR round key column with previous round key's first column
        for j in range(0,4):
            round_key[3][j] = hex(int(round_key[3][j]) ^ int(key_schedule[round-1][0][j],16))
        round_key[0] = round_key[3]
        for ii in range(1,4):
            for jj in range(0,4):
                round_key[ii][jj] = hex(int(round_key[ii-1][jj],16) ^ int(key_schedule[round-1][ii][jj],16))
        key_schedule.append(round_key)

    #-------------- break hex message into blocks of 16 bytes --------------#
    hex_message = []
    encrpyted_message_string = ""
    for i in range(1,len(input_message_hex)+1,2):
        hex_message.append("%s%s" % (input_message_hex[i-1], input_message_hex[i]))
        if (i%32==31):
            hex_message = np.array(hex_message, 'U10')
            hex_message = hex_message.reshape((4,4))
            
            #hex_message = np.array(['32','88','31','e0','43','5a','31','37','f6','30','98','07','a8','8d','a2','34'], 'U10')
            #hex_message = hex_message.reshape((4,4))

            #-------------- Encrpyt the message through 10 rounds of encrpytion --------------#
            encrpyted_message = hex_message.transpose()
            for round in range(0,11):
                if (round > 0):
                    encrpyted_message = encrpyted_message.transpose()
                    #Sub byte
                    for i in range(0,4):
                        for j in range(0,4):
                            encrpyted_message[i][j] = format((sub_byte(int(encrpyted_message[i][j],16))),'x')
                    #Shift rows
                    for i in range(1,4):
                        encrpyted_message[i] = np.roll(encrpyted_message[i],i*-1)

                    #Mix columns and XOR with round key
                    encrpyted_message = encrpyted_message.transpose()
                    for jj in range(0,4):  
                        if (round !=10):          
                            encrpyted_message[jj] = mixColumns(encrpyted_message[jj])
                        for ii in range(0,4):
                            encrpyted_message[jj][ii] = hex(int(encrpyted_message[jj][ii],16) ^ int(key_schedule[round][jj][ii],16))
                #XOR Round Key only 
                else:
                    for jj in range(0,4): 
                        for ii in range(0,4):
                            encrpyted_message[jj][ii] = hex(int(encrpyted_message[jj][ii],16) ^ int(key_schedule[round][jj][ii],16))

                #print("\n------------ Finished Round %d of Encrpytion Process ------------" % round)
                #print(key_schedule[round].transpose())
                #print(encrpyted_message.transpose())


            #-------------- Print out encrpyted message --------------#
            encrpyted_message = encrpyted_message.reshape((1,16))
            
            for i in range(0,16):
                encrpyted_message_string = encrpyted_message_string + chr(int(encrpyted_message[0][i],16))
            hex_message = []

    print("\nEncrpyted message: \n %s" % encrpyted_message_string)
    
    
if __name__ == "__main__":
    main()