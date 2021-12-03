import requests
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-y', '-year', help="Which year's input to download", required=True)
	parser.add_argument('-d', '-day', help="Which day's input to download", required=True)
	
	return parser.parse_args()


def get_cookie():
	with open("cookie.txt", "r") as authfile:
		cookie = authfile.read()
	return cookie


def get_input(url, cookie):
	r = requests.get(url, cookies=cookie)
	return r.content


def save_to_file(filepath, data):
	with open(filepath, "w") as input_file:
		input_file.write(data)


def main(args):
	print("Downloading...")

	url = "https://adventofcode.com/{}/day/{}/input".format(args['y'], args['d'])
	cookie = get_cookie()
	session_cookie = {"session": cookie}
	
	data = get_input(url, session_cookie).decode('utf-8')

	dest_filepath = "{}/Day{}/input.txt".format(args['y'], args['d'])
	save_to_file(dest_filepath, data)

	print(data)
	print("Download Complete!")

	# create empty file for test data
	test_filepath = "{}/Day{}/test_input.txt".format(args['y'], args['d'])
	save_to_file(test_filepath, "")
	print("\nEmpty Test File Created!")


if __name__ == "__main__":
	args = parse_args()
	main(vars(args))
