PREFIX ?= /usr/local
DEST=$(DESTDIR)$(PREFIX)/share/pyqmloscilloscope
QML=qml/qmloscilloscope

.PHONY: all test clean install
all: ;

clean: ;

test: all
	./main.py

install: all
	install -d $(DEST)/$(QML)
	install -m 644 $(QML)/main.qml $(DEST)/$(QML)
	install -m 644 $(QML)/ControlPanel.qml $(DEST)/$(QML)
	install -m 644 $(QML)/ScopeView.qml $(DEST)/$(QML)
	install -m 644 $(QML)/MultiButton.qml $(DEST)/$(QML)
	install -m 644 datasource.py $(DEST)
	install -m 644 __init__.py $(DEST)
	install -m 755 main.py $(DEST)
