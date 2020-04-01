import requests
from datetime import datetime as dt
import smtplib

def upload_file_cxd_token(sr_number, cxd_token, filename, filepath, receiver_mail_id):
        url = 'https://cxd.cisco.com/home/'
        username = sr_number
        password = cxd_token
        auth = requests.auth.HTTPBasicAuth(username, password)

        try:
                f = open(filepath + filename, 'rb')
        except Exception as e:
                print("Unable to open file. Error: " + str(e))

        try:
                r = requests.put(url + filename, f, auth=auth, verify=False)
        except Exception as e:
                print("Unable to upload file. Error: " + str(e))
        r.close()
        f.close()
	print(dt.now().strftime('%Y-%m-%d %H:%M:%S') + ":  Attempting to upload")

        server = smtplib.SMTP('mail.cisco.com')
        
        if r.status_code == 201:
		print(dt.now().strftime('%Y-%m-%d %H:%M:%S') + ":  File Uploaded Successfully")
                message = 'Subject: File Upload Successful\n\n'
                message += 'File {} successfully uploaded to SR {}'.format(filename, sr_number)
                server.sendmail('team-dr-dnac@cisco.com', [receiver_mail_id], message)
        elif r.status_code == 401:
                print(dt.now().strftime('%Y-%m-%d %H:%M:%S') + ":  Unauthorized request, please make sure your SR number and CXD token are correct")
                message = 'Subject: Unable to upload file {} to SR {}\n\nRun cat /home/maglev/dnacataglance/nohup.out for more information'.format(filename, sr_number)
                server.sendmail('team-dr-dnac@cisco.com', [receiver_mail_id], message)

def fetch_rca_data():
	f_ = open("/tmp/rca_load.txt", "r")
	list_ = f_.readlines()

	print(list_[0].rstrip('\n'))	
	upload_file_cxd_token(list_[0].rstrip('\n'), list_[1].rstrip('\n'), list_[2].rstrip('\n'), list_[3].rstrip('\n'), list_[4].rstrip('\n'))
	f_.close()

fetch_rca_data()
