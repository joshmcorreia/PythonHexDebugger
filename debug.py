import argparse
import sys

def main():
	parser = argparse.ArgumentParser(description='Python hex debugger')
	parser.add_argument('-i', "--input", required=True, help="The input string to be debugged. Can either be in decimal or hex.")
	parser.add_argument('-d', "--decimal", help="If toggled on then the input string is expected to be in decimal.", action='store_true')
	args = parser.parse_args()

	if not args.decimal:
		hex_input = args.input.replace(" ", "")
		if (len(hex_input) % 2 != 0):
			print("ERROR: Input hex has an odd number of characters. Please use an even number of characters.")
			sys.exit(1)
		num_char_in_hex_byte = 2 # each byte in hex is 2 characters wide
		hex_input_list = [hex_input[i:i+num_char_in_hex_byte] for i in range(0, len(hex_input), num_char_in_hex_byte)]
		hex_input_list_reversed = hex_input_list.copy()
		hex_input_list_reversed.reverse()

		hex_input_little_endian_string = "".join(hex_input_list_reversed)
		hex_input_big_endian_string = "".join(hex_input_list)

		hex_as_decimal_little_endian = int(hex_input_little_endian_string, 16)
		hex_as_decimal_big_endian = int(hex_input_big_endian_string, 16)
		print(f"Little endian decimal unsigned: {hex_as_decimal_little_endian}")
		print(f"Big endian decimal unsigned:    {hex_as_decimal_big_endian}")

		# TODO: Add two's-complement, seen in Java

	else:
		decimal_input = args.input
		decimal_input = decimal_input.replace(",", "") # support input decimals having commas, ex: 1,000 becomes 1000
		print("Decimal is not currently supported.")
		sys.exit(1)

if __name__ == "__main__":
	main()
