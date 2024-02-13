print('############ Task 1 ###############\n\n')

Letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Function for calculating the correlation of frequency
def Correlation_of_Frequency(chipher_text):

    character_frequency = {i: chipher_text.count(i) for i in set(chipher_text)}
    character_frequency = dict(sorted(character_frequency.items(), key=lambda item: item[1], reverse=True))
    if ' ' in character_frequency:
        character_frequency.pop(' ')
    
    n = len(chipher_text)-chipher_text.count(' ')
    
    for i in character_frequency:
        character_frequency[i] = round(character_frequency[i]/n,3)
    
    P = {0:.08, 1:.015, 2:.03, 3:.04,
         4:.13, 5:.02, 6:.015, 7:.06,
         8:.065, 9:.005, 10:.005, 11:.035,
         12:.03, 13:.07, 14:.08, 15:.02,
         16:.002, 17:.065, 18:.06, 19:.09,
         20:.03, 21:.01, 22:.015, 23:.005,
         24:.02, 25:.002}
    
    # Now we will compute the correlation of frequency for each 26 possible keys
    correlation_values = []
    for i in range(26):
        phi_i = 0
        for j in character_frequency:
            phi_i += character_frequency[j] * P[((26+Letter.find(j)-i)%26)]
        correlation_values.append([i,phi_i])
    
    correlation_values.sort(key = lambda x: x[1], reverse=True)

    # We will consider only the first 5 highest values
    return correlation_values[:5]


############### TASK 01 ###############
chipher_text = 'IT STY XYZRGQJ TAJW XTRJYMNSL GJMNSI DTZ'
# Function to find the corresponding plain text
def Break_Ceaser_Chiper(chipher_text):

    print(Correlation_of_Frequency(chipher_text))
    keys = [i[0] for i in Correlation_of_Frequency(chipher_text)]
    
    for key in keys:
        
        plain_text = ""

        for each_char in chipher_text:

            if each_char in Letter:
                pos = Letter.find(each_char)
                new_pos = (pos - key) % 26
                new_character = Letter[new_pos]
                plain_text += new_character
            else:
                plain_text += each_char

    
        print('For the key = ',str(key)+',','Plain Text =',plain_text)

Break_Ceaser_Chiper(chipher_text)

# After runing the above code, the following lines were generattted.
# For the key =  5, Plain Text = DO NOT STUMBLE OVER SOMETHING BEHIND YOU
# For the key =  15, Plain Text = TE DEJ IJKCRBU ELUH IECUJXYDW RUXYDT OEK
# For the key =  6, Plain Text = CN MNS RSTLAKD NUDQ RNLDSGHMF ADGHMC XNT
# For the key =  21, Plain Text = NY XYD CDEWLVO YFOB CYWODRSXQ LORSXN IYE
# For the key =  4, Plain Text = EP OPU TUVNCMF PWFS TPNFUIJOH CFIJOE ZPV



print('\n\n\n\n############ Task 2 ###############\n\n')

############### TASK 02 ###############

def Index_of_Coincidence(chipher_text):
    character_frequency = {i: chipher_text.count(i) for i in set(chipher_text)}
    Fi = 0
    for i in character_frequency:
        if i==' ':
            continue
        Fi += character_frequency[i]*(character_frequency[i]-1)
    
    n = len(chipher_text)-chipher_text.count(' ')

    return round(Fi/(n*(n-1)),3)

chipher_text = 'UPRCW IHSGY OXQJR IMXTW AXVEB DREGJ AFNIS EECAG SSBZR TVEZU RJCXT OGPCY OOACS EDBGF ZIFUB KVMZU FXCAD CAXGS FVNKM SGOCG FIOWN KSXTS ZNVIZ HUVME DSEZU LFMBL PIXWR MSPUS FJCCA IRMSR FINCZ CXSNI BXAHE LGXZC BESFG HLFIV ESYWO RPGBD SXUAR JUSAR GYWRS GSRZP MDNIH WAPRK HIDHU ZBKEQ NETEX ZGFUI FVRI'
print('Index of Coincidence for the chipher text is',Index_of_Coincidence(chipher_text))
# The IOC for the chipher text is 0.043. So, the key length is slightly
# above 5. Let's assume it's 6.

key_len = 6

# Now we will split the alphabets into 6 tiles of boxes

new_block_chipher_text = []
i = 0
while(True):
    if i>=len(chipher_text):
        break
    block = ''
    for j in range(i,len(chipher_text)):
        if len(block)==key_len:
            new_block_chipher_text.append(block)
            i=j
            break
        if chipher_text[j]==' ':
            i=j+1
            continue
        else:
            block+=chipher_text[j]
            i=j+1
    
    if i==len(chipher_text) and block:
            new_block_chipher_text.append(block)
            break
    
key_wise_letter_entry = ['','','','','','']
for i in new_block_chipher_text:
    for j in range(len(i)):
        key_wise_letter_entry[j]+=i[j]
    
    
# print(new_block_chipher_text)
# print((len(new_block_chipher_text)-1)*6 + len(new_block_chipher_text[-1]))
# print(len(chipher_text)-chipher_text.count(' '))
# for i in range(len(key_wise_letter_entry)):
#     print('Alphabet',i+1,':',key_wise_letter_entry[i],end='\n')


for i in key_wise_letter_entry:
    Break_Ceaser_Chiper(i)
    print('\n\n\n')

# IVEHPOSPNHCRTNRTUCHNRTLIOTLONUSDIOGAORSLT
# BEVIPROLGAANGGOHAIETEYIEUUETOTESMDSPBTCLH
# ETENEANEETNTOSNAPAMHROESEAAROYLOETFAEHATE
# LHRGNRPCSYLOTGGTPTWEIUVSVLRUNOFMSHARTINOR
# IAYHSEEHOOELHOSYREHYGBEOELNSEUAEGILTTNFG
# ETTAFAOATUAEIWOOETEAHELYNYTTBRNTONLSEGAE

