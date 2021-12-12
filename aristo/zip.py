import zipfile
import color
from color import *

def zipfile():
	print(""+C+"Files have to be in the same directory - Include .zip or .txt")
	zipfilename = input(''+T+'' + color.UNDERLINE + 'Zip file>' + color.END)
	dictionary = input(''+T+'' + color.UNDERLINE + 'Dictionary file>' + color.END)
	print(""+G+"[*] "+W+"Cracking...")
	password = None
	zip_file = zipfilename
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
				pass
	print(""+G+"[!] "+W+"Password found: " + password)
