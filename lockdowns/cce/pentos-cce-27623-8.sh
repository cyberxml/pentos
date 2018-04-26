DIRS="/bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin"
for dirPath in $DIRS; do
	find $dirPath -type f -exec chown root '{}' \;
done
