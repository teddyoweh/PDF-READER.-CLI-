# importing required modules
import PyPDF2
import tqdm
from tqdm import *
import huepy 
from huepy import yellow
from huepy import white 
from huepy import *
from gtts import gTTS 
from playsound import playsound
def pdf_to_audio():
    language = 'en'
    
    filetr = input('Enter file to read: ')
    try: open(filetr)
    except: pdf_to_audio()
    else: pass
    filestr = filetr.strip('.pdf')
    pdfFileObj = open(filetr, 'rb')
    filetxt = '{}_text.txt'.format(filestr)
    filewr = open(filetxt,'w', encoding="utf-8")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    doc = ''
    print(yellow('[~]Extracting text from {}'.format(filestr)))
    for i in tqdm(range(int(pdfReader.numPages)+1)):
        
        ii = i-1
        
        pageObj = pdfReader.getPage(ii)
        textdata = pageObj.extractText()
        textdata = str(textdata)
        doc += textdata
        filewr.write(textdata)

    print(white('[+] Done Extracting Text From {}'.format(filestr)))
    
    doc = str(doc)
  
    print(white('[+] Done Write {} PDF Content to {}'.format(filestr, filetxt)))
    pdfFileObj.close()
    
    mscss = '{}_audio.mp3'.format(filestr)
    filetrad = open(filetxt,'r', encoding="utf-8").read()
    speech = gTTS(text = filetrad, lang = language, slow = False)
    filetrall =open(filetxt,'r', encoding="utf-8").readlines()
    print(yellow('[~] Saving {} Text To {}'.format(filestr, mscss)))
      
        
        
        

    
    speech.save(mscss)
    print(yellow('[+] Saved {} Text To {}'.format(filestr, mscss)))
if __name__ == '__main__': 
    pdf_to_audio()