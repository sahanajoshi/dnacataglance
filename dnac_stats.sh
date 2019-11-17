SN=$(sudo dmidecode -s system-serial-number)
appliance=$(more /sys/devices/virtual/dmi/id/product_name)
services_down=$(magctl appstack status | grep 0/)
member_list=$(etcdctl member list)

echo "***************************************************************************************************************************************************"
printf "\n"
echo "DNAC Stats"
printf "\n"
echo Kernel and OS:
uname -a
printf "\n"
echo Serial number: $SN
echo Appliance: $appliance
echo Services Down: $services_down
printf "\n"

echo Cluster members:
echo $member_list
printf "\n"

echo Cluster health:
etcdctl cluster-health
printf "\n"

echo Packages installed:
maglev package status
printf "\n"

echo Network Interfaces:
ip a | grep enp
printf "\n"

echo ISE-PxGrid disconnect messages today:
printf "\n"

date=$(date +"%Y-%m-%d")
magctl service logs -r identity-manager-pxgrid-service | egrep 'Disconnect|ERROR' | grep $date 
printf "\n"

echo ISE-ERS/PAN disconnect/issues today:
magctl service logs -r network-design-service | egrep 'UNTRUSTED|ERROR' | grep $date
printf "\n"
echo "***************************************************************************************************************************************************"
