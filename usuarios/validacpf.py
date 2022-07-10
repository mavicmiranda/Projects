CPF = "05455039490"
ocpf = CPF
print(ocpf)
fatiacpf = CPF[:9]
print(fatiacpf)

soma =0 
for chave, multiplicador in enumerate(range(len(fatiacpf)+1, 1, -1 )):
    print((fatiacpf[chave]),'*' ,multiplicador)
    soma += int(fatiacpf[chave])* multiplicador
    print(soma)

resto = 11 -(soma%11)
resto = resto if resto <=9 else 0
print(resto)

fatiacpf2 = fatiacpf + str(resto)

soma2 =0 
for chave, multiplicador in enumerate(range(len(fatiacpf2)+1, 1, -1 )):
    print((fatiacpf2[chave]),'*' ,multiplicador)
    soma2 += int(fatiacpf2[chave])* multiplicador
    print(soma2)

resto2 = 11 -(soma2%11)
resto2 = resto2 if resto2 <=9 else 0
print(resto2)

validacpf = fatiacpf + str(resto) 

print(validacpf)
    
if fatiacpf + str(resto) +str(resto2) != ocpf :
    print("cpf invalido")
else:
    print("cpf valido")
