import pdfplumber
import fitz



doc = fitz.open("tinkoff.pdf")
text = {}
with fitz.open("tinkoff.pdf") as f:
    for num, page in enumerate(doc.pages()):
        text[num] = page.get_text()
print(len(text))
    


