BOOM = boom
DOOM2 = bootstrap
WADOUT = castle.wad

normal:
	$(MAKE) -C bootstrap
	$(MAKE) -C graphics
	$(MAKE) -C lumps
	$(MAKE) -C patches
	$(MAKE) -C sprites
	$(RM) $(WADOUT)
	deutex -doom2 $(DOOM2) -make config/wadinfo.txt $(WADOUT)

run: $(DOOM2)/doom2.wad $(WADOUT)
	$(BOOM) -file $(WADOUT) -warp 01

textures:
	deutex -doom2 $(DOOM2) -make config/textures.wadinfo textures.wad

clean:
	$(MAKE) -C bootstrap clean
	$(MAKE) -C graphics clean
	$(MAKE) -C lumps clean
	$(MAKE) -C patches clean
	$(MAKE) -C sprites clean
	$(RM) $(WADOUT)
