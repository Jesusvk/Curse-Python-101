ft = open('uno.txt','r')

def op_file(tex):
	cadena = ""
	for line in ft:
		cadena += line
	return cadena			
def rempla(tex):
	for a in tex:
		
tx = op_file(ft)