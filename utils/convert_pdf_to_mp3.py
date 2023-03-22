from pypdf import PdfReader
from gtts import gTTS
import os

def save_pdf_file_as_txt(pdfname):
    reader = PdfReader(pdfname)
    filename = pdfname.split('.')[0]+".txt"
    file = open(filename,"w",encoding="utf-8")
    total_pages = len(reader.pages)
    print(total_pages)
    for page_num in range(total_pages):
        page = reader.pages[page_num]
        try:
            text = page.extract_text()
            # text_to_write = text.encode("utf-8")
            file.write(text)
            print("Written to File Page number = ",page_num)
        except UnicodeEncodeError as e:
            print(e)
            print(f"Text on page number {page_num} cannot be encoded. Try again later...")

def save_txt_file_as_mp3(filename):
    print(f"Converting {filename} to mp3")
    try:
        text = open(filename,"r",encoding="utf-8").read()
        audio = gTTS(text=text, lang="en", slow=False)
        new_file_name = filename.split(".")[0]+".mp3"
        audio.save(new_file_name)
    except Exception as e:
        print(e)

def play_music(filename):
    os.system(f"start {filename}")
