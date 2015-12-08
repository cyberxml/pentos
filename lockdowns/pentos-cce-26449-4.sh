for part in `mount -t ext4 | awk '{print $3}'`
do 
	echo ${part}
	sed -i -e "s@ $part \+ext4 \+defaults@ $part  ext4  defaults,nodev@" /etc/fstab
done
