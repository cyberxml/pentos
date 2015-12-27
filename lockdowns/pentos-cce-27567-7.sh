# a bit heavy-handed
sed -i -e 's/^exec.*/exec /usr/bin/logger -p security.info "Control-Alt-Delete pressed"/' /etc/init/control-alt-delete.conf
