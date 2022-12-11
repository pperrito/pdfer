# PDFer
A PDF utility and little more.

## Features
- Convert PDF to Word
- Convert PDF to set of images
- Convert images to PDF
- Convert Word to PDF

## Tech
PDFer uses a number of open source projects to work properly:
- [pdf2image] - A python module that wraps the pdftoppm utility to convert PDF to PIL Image object
- [docx2pdf] - Convert docx to pdf on Windows or macOS directly using Microsoft Word
- [pdf2docx] - Open source Python library converting pdf to docx
- [img2pdf] - Lossless conversion of raster images to PDF

And of course PDFer itself is open source with a [public repository][pdfer] on GitHub.
 
   [pdfer]: <https://github.com/student12m11ga1k/pdfer>
   [docx2pdf]: <https://github.com/AlJohri/docx2pdf>
   [img2pdf]: <https://gitlab.mister-muffin.de/josch/img2pdf>
   [pdf2docx]: <https://github.com/dothinking/pdf2docx>
   [pdf2image]: <https://github.com/Belval/pdf2image>