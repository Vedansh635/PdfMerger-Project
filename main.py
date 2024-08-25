def merger(path, mergedpdfname):
    from PyPDF2 import PdfMerger
    import os
    merger = PdfMerger()
    for pdf in os.listdir(path):
        if pdf.endswith('.pdf'):  # only consider pdf files
            merger.append(os.path.join(path, pdf))

    merger.write(f"{path}\\{mergedpdfname}.pdf")

    merger.close()

path = input('Enter path in which pdfs are located: ')
pdfname = input('Enter name you want to give to merged pdf: ')

merger(path, pdfname)

