# assumes user is root
# assumes no spaces in dirs in path
for i in ` echo $PATH | sed 's/:/ /g'`
do
	chmod g-w ${i}
	chmod o-w ${i}
done
