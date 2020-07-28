import requests
import sys

def test_internet():
	test_url = 'https://cxd.cisco.com/home'
	response = None
	print("Checking internet connectivity.")
	try:
		response = requests.get(test_url, verify=False)
	except Exception as e:
		print("Unable to connect to internet. Make sure you have connectivity, and you have set the Proxy and DNS entries. \nError: " + str(e))
	if  response is not None and response.status_code == 401:
		# If we are receiving a 401 response from the server, connection is OK
		print("Internet check successful. Proceeding")
		return True
	else:
		print("Make sure the DNAC has access to internet, and correct HTTPS proxy settings are entered, if any")
		return False


def accept_SR_token_file_input(file_path='/data/rca/'):
	sr_number = raw_input("Enter the SR number of the case: ")
	token  = raw_input("Enter the CXD token of the case: ")
	file_name = raw_input("Enter the  filename to be uploaded: ")
        receiver_mail_id = raw_input("Enter the mail ID to which the notification has to be sent to once upload is completed: ")
	
	f_ = open("/tmp/rca_load.txt", "w+")
	f_.write(sr_number + '\n')
	f_.write(token + '\n')
	f_.write(file_name + '\n')
	f_.write(file_path + '\n')
        f_.write(receiver_mail_id + '\n')
	# upload_file_cxd_token(sr_number, token, file_name,default_file_path)
	f_.close()


if(test_internet()):
        file_path = raw_input("\nIf uploading any file other than RCA, then enter the file path, e.g, /tmp/ : ")
        if len(file_path) == 0:
	        accept_SR_token_file_input()
        else:
                accept_SR_token_file_input(file_path)
else:
	print("Issue with connectivity to internet, please fix and re-try")
