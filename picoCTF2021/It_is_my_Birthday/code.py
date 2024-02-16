#!/usr/bin/env python3

# import hashlib
# from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
from requests import Request, Session
import os
from html import unescape


# def create_pdf(file_path, content):
#     with open(file_path, "wb") as pdf_file:
#         pdf_canvas = canvas.Canvas(pdf_file)
#         pdf_canvas.drawString(100, 700, content)
#         pdf_canvas.save()


# def calculate_md5(file_path):
#     md5_hash = hashlib.md5()
#     with open(file_path, "rb") as file:
#         for chunk in iter(lambda: file.read(4096), b""):
#             md5_hash.update(chunk)
#     return md5_hash.hexdigest()


# We generate a file of the form:
"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#

diff = '''<one of 2 collision blocks>'''
same = '''<first of the 2 collision blocks>'''

if (same == diff):
    print "good"

else:
    print "evil"
"""
# Example usage:
pdf_path1 = "collision1.pdf"
pdf_path2 = "collision2.pdf"
content = "This is some content for the PDF."

# Create two different PDFs with the same MD5 hash
# create_pdf(pdf_path1, content)
# create_pdf(pdf_path2, content)

# md5_checksum1 = calculate_md5(pdf_path1)
# md5_checksum2 = calculate_md5(pdf_path2)

# print(f"MD5 checksum of {pdf_path1}: {md5_checksum1}")
# print(f"MD5 checksum of {pdf_path2}: {md5_checksum2}")

# if md5_checksum1 == md5_checksum2:
#     print("Collision successfully created.")
# else:
#     print("No collision.")


url = 'http://mercury.picoctf.net:20277/index.php'

s = Session()

# res = s.get(url)

# print(res.text)

path_file_colli = './fastcoll'

pdf_path1 = os.path.join(path_file_colli, "msg1.pdf")
pdf_path2 = os.path.join(path_file_colli, "msg2.pdf")

multiple_files = [('file1', ('msg1.pdf', open(pdf_path1, 'rb'), 'application/pdf')),
                  ('file2', ('msg2.pdf', open(pdf_path2, 'rb'), 'application/pdf'))]

req = Request('POST', url, files=multiple_files, data={'submit': 'upload'})

prepped = s.prepare_request(req)


headers = prepped.headers

content = prepped.body

# print(prepped.method+' '+prepped.url+' ')
# print(headers, '\n')
# print(content)

res = s.send(prepped)

response = res.text
html_code = response

# Parse the HTML code with BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Find all PHP code within the HTML
php_code_elements = soup.find_all('span', style='color: #FF8000')

# Concatenate the PHP code elements
php_code = ''.join(element.get_text() for element in php_code_elements)

# Save the PHP code to a new PHP file
with open('output.php', 'w+') as file:
    file.write('<?php\n\n' + php_code + '\n\n?>')
