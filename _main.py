import requests
import sys

def test_internet():
	test_url = 'https://www.google.com'
	response = None
	print("Checking internet connectivity.")
	try:
		response = requests.get(test_url)
	except Exception as e:
		print("Unable to connect to internet. Make sure you have connectivity, and you have set the Proxy and DNS entries. \nError: " + str(e))
	if  response is not None and response.status_code == 200:
		print("Internet check successful. Proceeding")
		return True
	else:
		print("Make sure the DNAC has access to internet, and correct HTTPS proxy settings are entered, if any")
		return False


def accept_SR_token_file_input():
	sr_number = raw_input("Enter the SR number of the case: ")
	token  = raw_input("Enter the CXD token of the case: ")
	file_name = raw_input("Enter the rca file to be uploaded: ")

	default_file_path = '/data/rca/'
	
	f_ = open("/tmp/rca_load.txt", "w+")
	f_.write(sr_number + '\n')
	f_.write(token + '\n')
	f_.write(file_name + '\n')
	f_.write(default_file_path + '\n')
	# upload_file_cxd_token(sr_number, token, file_name,default_file_path)
	f_.close()


if(test_internet()):
	accept_SR_token_file_input()
else:
	print("Issue with connectivity to internet, please fix and re-try")
