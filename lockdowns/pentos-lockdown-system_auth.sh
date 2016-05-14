# this file has numerous changes that are easier to implement
# by swapping out a predefined file

# but ... authconfig will overwrite

if [ -L /etc/pam.d/system-auth ]
then
	rm /etc/pam.d/system-auth
fi

cp -f files/system-auth-local /etc/pam.d/system-auth-local
chmod 644 /etc/pam.d/system-auth-local
chown root:root /etc/pam.d/system-auth-local
ln -s /etc/pam.d/system-auth-local /etc/pam.d/system-auth
