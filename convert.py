import PyPDF2

filename = input("Enter File Path: ")
try:
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        page_obj = pdf_reader.getPage(0)
        text = page_obj.extractText()
        with open('output.txt', 'w') as f:
            f.write(text)
    print("PDF data has been successfully converted to text and saved as 'output.txt'.")
except Exception as e:
    print("Error: Could not read the PDF file.")
