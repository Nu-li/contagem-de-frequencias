arquivo = #[seu arquivo aqui]

file = open(arquivo, 'r')
lines = file.readlines()
seq = []

for line in lines: # lê o arquivo e manda pra variável seq só o que não começa com '>'
    if line.find('>') != 0:
        seq.append(line)

seqDict = {}

for sequencia in seq:#monta um dicionário com chave = sequência/valor = frequência  
    count = seq.count(sequencia)
    seqDict[sequencia] = count/#[insira o valor base da frequência]
#print(seqDict)
print(seqDict.values())

selctList = []
aux = "" #variável auxiliar

for sequ, frequ in seqDict.items():#monta uma lista a partir do dicionário apenas com as sequências selecionadas
    if aux != sequ:
        if frequ > 0.01:
            selctList.append(sequ)
    aux = sequ
print(selctList)