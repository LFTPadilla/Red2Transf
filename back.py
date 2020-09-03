
import numpy as np

def generate_fragments(datagram_size, mtu):

	datagram_size = int(datagram_size)
	mtu = int(mtu)
	table = []
	queued_bits = datagram_size
	offset = 0
	while queued_bits > mtu :

		fragment_len = mtu
		queued_bits = queued_bits - mtu + 20 
		binary_offset = "{0:b}".format(int(offset / 8))
		binary_offset = ('0000000000000%s' % binary_offset)[-13:]
		
		hex_digits = hex(int('001%s' % binary_offset, 2))
		row = [fragment_len, 0, 0, 1, binary_offset, offset,  hex_digits]
		table.append(row)
		offset += mtu - 20

	if queued_bits:

		fragment_len = queued_bits
		binary_offset = "{0:b}".format(int(offset / 8))
		binary_offset = ('0000000000000%s' % binary_offset)[-13:]
		hex_digits = hex(int('000%s' % binary_offset, 2))
		row = [fragment_len, 0, 0, 0, binary_offset, offset, hex_digits]
		table.append(row)
	return (np.array(table)).astype('str')


if __name__ == '__main__':
	datagram_size = 3508
	mtu = 1500
	generate_fragments(datagram_size, mtu)
	

