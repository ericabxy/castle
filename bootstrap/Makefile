# Build a fake IWAD to bootstrap deutex

IWAD=doom2.wad

$(IWAD): playpal/playpal-base.lmp
	./bootstrap < $< > $@

clean:
	$(RM) $(IWAD)

.PHONY: clean
