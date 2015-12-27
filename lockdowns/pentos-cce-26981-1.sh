for i in `ls -d1 /home/* | grep -v "lost+found"`
do
	chmod g-w ${i}
	chmod o-rwx ${i}
done
