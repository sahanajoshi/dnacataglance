To upload the RCA, simply run the bash script:
        ./upload_rca.sh
Follow the prompts, and enter the relevant information.
The upload status can be seen in the nohup.out file generated. To see this, run
        cat nohup.out

Other logs/ files can also be uploaded to the case. To do this, please enter the file path and filename when prompted. 
For example, if you have to upload /tmp/log_file.log, enter /tmp/ for the path, and log_file.log for the filename. 

To see the stats of the DNAC, run the bash script:
        ./dnac_stats.sh
Follow the prompts, and enter the maglev/ admin passwords when prompted.

For detailed instructions on setting up the scripts and other requirements, please refer to the Deplyment Guide in this repository.
