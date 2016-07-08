import gzip
import shutil

#Example of how to read a compressed file:
with gzip.open('testReadFile.txt.gz', 'rb') as f:
	file_content = f.read()
	print(file_content)

#Example of how to create a compressed GZIP file:
content = "Lots of content here"
with gzip.open('testWriteFile.txt.gz', 'wb') as f:
	f.write(content)

#Example of how to GZIP conpress an exitstin file:
with open('testFile.txt','rb') as f_in,gzip.open('testFile.txt.gz', 'wb') as f_out:
	shutil.copyfileobj(f_in, f_out)
