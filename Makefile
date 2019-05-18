PREFIX ?= /usr/local
DEST=$(DESTDIR)$(PREFIX)/share/pyqmloscilloscope
PYRCC5 ?= pyrcc5
BUILDDIR ?= .

.PHONY: all test clean distclean install
all: qrc_resources.py

qrc_%.py: %.qrc $(wildcard qml/**/*)
	$(PYRCC5) $< >$(BUILDDIR)/$@

test: all
	./main.py

clean: ;
distclean: clean
	rm -f qrc_*.py

install: all
	install -d $(DEST)
	install -m 644 $(BUILDDIR)/qrc_resources.py $(DEST)
	install -m 644 datasource.py $(DEST)
	install -m 644 __init__.py $(DEST)
	install -m 755 main.py $(DEST)
