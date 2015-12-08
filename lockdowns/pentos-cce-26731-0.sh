for pkg in `rpm -qa`
do
	rpm --setperms ${pkg}
done
