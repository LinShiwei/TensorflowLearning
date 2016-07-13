import gzip
import shutil


#Example of how to GZIP conpress an exitstin file:
with open('testImage36.txt','rb') as f_in,gzip.open('testImage36.txt.gz', 'wb') as f_out:
	shutil.copyfileobj(f_in, f_out)

with open('testImageLabel.txt','rb') as f_in,gzip.open('testImageLabel.txt.gz', 'wb') as f_out:
	shutil.copyfileobj(f_in, f_out)
with open('trainImage36.txt','rb') as f_in,gzip.open('trainImage36.txt.gz', 'wb') as f_out:
	shutil.copyfileobj(f_in, f_out)
with open('trainImageLabel.txt','rb') as f_in,gzip.open('trainImageLabel.txt.gz', 'wb') as f_out:
	shutil.copyfileobj(f_in, f_out)
