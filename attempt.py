import os
import shutil
import scripts.parse_pdfs as pp

tidy_path = "data/tidy"
json_path = "data/json"

#delete current ones
shutil.rmtree(tidy_path)
shutil.rmtree(json_path)

#make directories again
os.mkdir(tidy_path)
os.mkdir(json_path)

#json attempt things
pdfs = os.listdir("pdfs")
print(pdfs)
#pp.parse_pdf_python_attempt(pdfs)


