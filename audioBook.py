import PyDF2
import pyttsx3

book = open(input("enter the book name: "), 'rb')
pageNumber = int(input("enter page number from wich want the system to start reading :"))

pdfReader = PyDF2.PdfFileReader(book)
pages = pdfReader.numPages()
speaker = pyttsx3.init()

for num in range((pageNumber - 1), pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndAwait()
