import argparse
import sys

def main():
	parser = argparse.ArgumentParser(description='Python hex debugger')
	parser.add_argument('-i', "--input", required=True, help="The input string to be debugged. Can either be in decimal or hex.")
	parser.add_argument('-d', "--decimal", help="If toggled on then the input string is expected to be in decimal.", action='store_true')
	args = parser.parse_args()

	if not args.decimal:
		hex_input = args.input
		hex_input_list = hex_input.split(" ")
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
