
import numpy as np

def generate_fragments(datagram_size, mtu):
	''' 
	genera una matriz donde de acuerdo a un tamaño de datagrama y a un MTU se determinan los fragmentos representados
	por las filas de la matriz y las columnas corresponden a:
	1. Longitud	total	del	fragmento
	2. Flags	(3	bits)
	3. Offset	en	binario	(13	bits)
	4. Offset	en	decimal
	5. Los	cuatro	dígitos	hexadecimales	que	representan	los	16	bits
	'''
	
	

	datagram_size = int(datagram_size)
	mtu = int(mtu)

	# Validación verifica que los datos sean mayores a 0
	# if datagram_size < 21 or (mtu < 28 or (mtu - 20) % 8 != 0):
	#	return 

	if datagram_size < 21 or mtu < 21:
		return 

	table = []
	queued_bytes = datagram_size
	offset = 0
	# Mientras los datos del datagrama que aun no hayan sido "enviados" en fragmentos de
	# tamaño equivalente al mtu sean mas grandes que a (mtu - 20) el seguirá iterando
	while queued_bytes > mtu :
		#Tamaño del fragmento
		fragment_len = mtu
		# Bytes sin enviar 
		queued_bytes = queued_bytes - mtu + 20
		#offset en decimal
		decimal_offset = int(offset / 8)
		# Desplazamiento en binario en cadenas de 13 bits
		binary_offset = "{0:b}".format(decimal_offset)
		binary_offset = ('0000000000000%s' % binary_offset)[-13:]
		# flags y offset en su valor hexadecimal
		hex_digits = hex(int('001%s' % binary_offset, 2))
		# se construye la fila
		row = [fragment_len, 0, 0, 1, binary_offset, decimal_offset,  hex_digits]
		table.append(row)
		#Se agrega el desplazamiento para la proxima iteración
		offset += mtu - 20

	if queued_bytes:

		fragment_len = queued_bytes
		decimal_offset = int(offset / 8)
		binary_offset = "{0:b}".format(decimal_offset)
		binary_offset = ('0000000000000%s' % binary_offset)[-13:]
		hex_digits = hex(int('000%s' % binary_offset, 2))
		row = [fragment_len, 0, 0, 0, binary_offset, decimal_offset, hex_digits]
		table.append(row)
	return (np.array(table)).astype('str')


if __name__ == '__main__':
	datagram_size = 3508
	mtu = 1500
	generate_fragments(datagram_size, mtu)
	

