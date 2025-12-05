DOOM2 = bootstrap
WADOUT = castle.wad

normal:
	$(MAKE) -C bootstrap
	$(MAKE) -C graphics
	$(MAKE) -C levels
	$(MAKE) -C lumps
	$(MAKE) -C sprites
	$(RM) $(WADOUT)
	deutex -doom2 $(DOOM2) -make config/wadinfo.txt $(WADOUT)

run: $(DOOM2)/doom2.wad $(WADOUT)
	boom -file $(WADOUT) -warp 01

clean:
	$(MAKE) -C bootstrap clean
	$(MAKE) -C graphics clean
	$(MAKE) -C levels clean
	$(MAKE) -C lumps clean
	$(MAKE) -C sprites clean
	$(RM) $(WADOUT)
