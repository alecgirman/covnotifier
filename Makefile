COPY=cp -v
REMOVE=rm -v
PREFIX=/usr/local/bin

install:
	# copy to binary directory and remove .py extension
	$(COPY) covdaily.sh $(PREFIX)/covdaily
	$(COPY) covwatcher.py $(PREFIX)/covnotifier
	
	# make executable
	chmod +x $(PREFIX)/covdaily $(PREFIX)/covnotifier

uninstall:
	$(REMOVE) $(PREFIX)/covdaily
	$(REMOVE) $(PREFIX)/covnotifier
