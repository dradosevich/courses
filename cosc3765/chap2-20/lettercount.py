#Danny Radosevich
#Fall 2019 Security Exam 1
#Statistically determining a cipher solution
#yes I know its shoddy
Dict = {}
keys = [21,22,23,24,25]
freq ={
0:0.07984,
1:0.01511,
2:0.02504,
3:0.04260,
4:0.12452,
5:0.02262,
6:0.02013,
7:0.06384,
8:0.07000,
9:0.00131,
10:0.00741,
11:0.03961,
12:0.02629,
13:0.06879,
14:0.07691,
15:0.01741,
16:0.00107,
17:0.05912,
18:0.06333,
19:0.09058,
20:0.02844,
21:0.01056,
22:0.02304,
23:0.00159,
24:0.02028,
25:0.00057
}
alph={
'A':0,
'B':1,
'C':2,
'D':3,
'E':4,
'F':5,
'G':6,
'H':7,
'I':8,
'J':9,
'K':10,
'L':11,
'M':12,
'N':13,
'O':14,
'P':15,
'Q':16,
'R':17,
'S':18,
'T':19,
'U':20,
'V':21,
'W':22,
'X':23,
'Y':24,
'Z':25
}
#keys = [1,2,3,4,5]
def mod(num):
    return num%26
def p(num):
    return freq[num]

text = "TEBKFKQEBZLROPBLCERJXKBSBKQP"
txt =""
for char in text:
    if char in Dict:
        Dict[char]+=1
    else:
        Dict[char]=1
print(Dict)
#determine the percentages
for i in Dict:
    txt+= "\item "+(str(i)+" "+str(Dict[i]/28.0))+"\n"

print(txt)
txt=""
# show the actual fractions
for i in Dict:
    txt+= "\item "+(str(i)+" "+str(Dict[i]))+"/28"+"\n"
print(txt)
txt=""
temp = 0
#apply the table to determin the most probable solution
for i in keys:
    for j in Dict:
        #print(alph[j])
        temp += (Dict[j]/28.0)*p(mod(alph[j]-i))
    print("\item"+str(i)+ " " + str(temp))
    temp = 0
