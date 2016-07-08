import gzip
import numpy

def _read32(bytestream):
	dt = numpy.dtype(numpy.uint32).newbyteorder('>')
	return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]
with gzip.open('testReadFile.txt.gz', 'rb') as bytestream:
	magic = _read32(bytestream)
	print(magic)
	num = _read32(bytestream)
	print(num)
