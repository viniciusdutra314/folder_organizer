import os
from shutil import move

arquivos=os.listdir()
arquivos.remove("organizar.py")
tipo_arquivo=[]

for j in arquivos:
    point_place=len(j)-j[::-1].find(".")
    tipo_arquivo.append(j[point_place:])

def cria_se_nao_existe(nome):
    if not os.path.exists(nome):
        os.makedirs(nome)

ja_mudou=False
pastas=[]

def verifica(formatos:list,nome_pasta:str):
    global j, ja_mudou
    if nome_pasta not in pastas: pastas.append(nome_pasta)

    if tipo_arquivo[j] in formatos:
        cria_se_nao_existe(nome_pasta)
        move(arquivos[j],nome_pasta)
        ja_mudou=True

for j in range(len(arquivos)):
    verifica(["pdf"],"PDFs")
    verifica(["csv","xlsx"],"Tabelas")
    verifica(["jpg","png","psd"],"Imagens")
    verifica(["mp4","wmv","avi","mkv"],"Videos")
    verifica(["mp3","ogg","wav","pkf"],"Audios")
    verifica(["zip"],"Zips")
    verifica(["exe","msi","ini"],"Executaveis")
    verifica(["ipynb","py","c","c++","txt","tex"],"Codigos")
    verifica(["prproj"],"Projetos_Pr")
    verifica(["aep"],"Projetos_Ae")
    if ja_mudou==False and arquivos[j] not in pastas: 
        move(arquivos[j],"Outros")
    ja_mudou=False
