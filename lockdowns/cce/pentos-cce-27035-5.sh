gconftool-2 --direct \
	--config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory \
	--type bool \
	--set /apps/nautilus/preferences/media_automount false
gconftool-2 --direct \
	--config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory \
	--type bool \
	--set /apps/nautilus/preferences/media_autorun_never true
