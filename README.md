# DNA-C At A Glance

## Table of Contents

  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Removal / Cleanup](#removal--cleanup)
  - [Features](#features)
    - [Upload RCA](#upload-rca)
    - [Basic Health Check](#basic-health-check)
  - [Appendix](#appendix)
    - [Obtain CXD Token](#obtain-cxd-token)

## Introduction

_DNA-C at a glance_ is a project that is aimed at users of the Cisco DNA-C Appliance for troubleshooting, auditing, etc. on Cisco DNA-C CLI.

## Installation

**Prerequisites:** Access to `github.com:443` from the DNA-C Appliance.

1. Goto home directory: `cd`
1. Clone this repository to the DNA-C Appliance: `git clone https://github.com/sahanajoshi/dnacataglance.git`
1. Verify download: `ls dnacataglance`

## Removal / Cleanup

1. Goto home directory: `cd`
1. Delete install directory: `rm -rf dnacataglance`


## Features

### Upload RCA

**Prerequisites:** Access to `cxd.cisco.com:443` from the DNA-C Appliance.

1. Goto directory where scripts were downloaded: `cd ~/dnacataglance`
2. Run `./upload_rca.sh`
3. Follow the prompts. (Refer Appendix: Obtain CXD Token)
4. The upload process runs in the background. So the SSH session to the DNA-C can be closed after initiating upload. To confirm upload success, run `cat nohup.out`

### What to expect when you run the script?
![Image of DNAC-CLI](https://github.com/sahanajoshi/dnacataglance/blob/master/DNAC-CLI1.png)
![Image of mycase portal](https://github.com/sahanajoshi/dnacataglance/blob/master/DNAC-CLI2.png)

##### Notes
* **Completion codes**

| Code | Reason               | Resolution                   |
| ---- | -------------------- | ---------------------------- |
| 401  | Unauthorized Request | Check SR number or CXD token |
| 201  | Successful Upload    | -                            |

* RCA files are large in size (~300-400 MB) and will take sometime for upload to complete depending on your bandwidth availability.

* Other logs/files can also be uploaded to the case. To do this, enter the file path and filename when prompted. For example, if you have to upload `/tmp/log_file.log`, enter `/tmp/` for the path, and `log_file.log` for the filename.

### Basic Health Check

1. Goto directory where scripts were downloaded: `cd ~/dnacataglance`
2. Run `.dnac_stats.sh`
3. Follow the prompts. Enter the maglev/admin passwords when prompted.

## Appendix
### Obtain CXD Token

CXD token is generated by Cisco Support Case Manager for every SR (Service Request) opened with Cisco and can be obtained in the following ways.
* [https://mycase.cloudapps.cisco.com](https://mycase.cloudapps.cisco.com) > Case > Attachments > Generate Token.
* In the initial automatic email sent out when a new SR is created.
* Cisco TAC engineer will be able to provide the CXD token.

### Where can the customer see the CXD Token?
![Image of mycase portal](https://github.com/sahanajoshi/dnacataglance/blob/master/DNAC-CLI3.png)

For detailed instructions on setting up the scripts and other requirements, refer the Deployment Guide in this repository.
