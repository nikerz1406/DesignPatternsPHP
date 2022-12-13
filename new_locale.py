import os
import re
from pathlib import Path

def removeFile(name) :
    path = Path(name)
    if  path.is_file() :
        os.remove(name)
def createFolder(path) : 
    is_exist = os.path.exists(path)
    if is_exist == False :
        os.mkdir(path)
def createFile(input,output,locale):
    command = f'pybabel init -o {output} -i {input} -l {locale}'
    os.system(command)
def getPOfile(file):
    if(len(file) == 0) :
        return None
    i = 0
    while i < len(file):
        if re.search('\.po$',file[i],flags=re.IGNORECASE) :
            return file[i]
        i +=1
    return None
def createFilePo(new_lang,old_lang):
    dir = "./locale/"+old_lang+"/"
    total_file = 0
    for root,dirs,file in os.walk(dir):
        path = root.replace('\\','/')
        path = re.sub(f"\/{old_lang}\/",f"/{new_lang}/",path)
        createFolder(path)
        po = getPOfile(file)
        if po is not None :
            sub_dir = root.replace('\\','/')
            input = f'{sub_dir}/{po}'
            sub_dir = re.sub(f"\/{old_lang}\/",f"/{new_lang}/",sub_dir)
            output = f'{sub_dir}/{po}'
            try :
                removeFile(output)
                createFile(input,output,new_lang)
                total_file += 1
            except :
                continue
            
    print(f"=========================\nTotal file:{total_file}")

locale = "vi"
template = "de"
createFilePo(locale,template)
