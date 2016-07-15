import pdfkit

def htmlToPDF(url):

    pdfkit.from_url(url, "Document.pdf")

if __name__ == "__main__":

    url = input("Enter the url of the html page ")

    htmlToPDF(url)