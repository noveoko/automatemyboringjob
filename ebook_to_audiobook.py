from gtts import gTTS
import PyPDF2
import glob
import sys


def pdf_to_audio_book(DIR):

    for book in glob.glob(f"{DIR}*.pdf"):

        print(f"Processing book {book}")
        first_page = 0
        title = book.split("/")[-1].replace(".pdf", "")
        clean = title.replace("_", " ")

        pdf_File = open(f'{DIR}{title}.pdf', 'rb')

        pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
        count = pdf_Reader.numPages
        TextList = []

        for i in range(first_page, count):
            try:
                print(f"Processing page {i} or {count}")
                page = pdf_Reader.getPage(i)
                TextList.append(page.extractText())
            except:
                pass

        TextString = " ".join(TextList)
        language = 'en'
        myobj = gTTS(text=TextString, lang=language, slow=False)
        print(f"Saving the book: {clean}")
        myobj.save(f"ai_books/{title}.mp3")


if __name__ == "__main__":
    try:
        PATH = sys.argv[1]
        pdf_to_audio_book(PATH)
    except Exception as e:
        PATH = input("Path to Book Pdfs:")
        if PATH:
            pdf_to_audio_book(PATH)
        else:
            print("Please provide a valid path")
