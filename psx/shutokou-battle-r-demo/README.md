These patch instructions are for the *Shutokou Battle R Highlight-Ban* demo disc. You'll need an image of the disc that matches [this one](http://redump.org/disc/33688/) to do the patching.

The __Releases__ page on this repository has an XDelta patch that can be applied with [Delta Patcher](https://github.com/marco-calautti/DeltaPatcher/releases):
* Original file: `Shutokou Battle R (Japan) (Demo) (Track 1).bin`
* XDelta patch: `shutokou-battle-r-demo-extended.xdelta`

To patch manually, follow the instructions below.

Extract the file `OVERLAY/ETC.BIN` from the disc image using [CDMage](https://archive.org/details/CDmage):
* Open the `Shutokou Battle R (Japan) (Demo).cue` file in CDMage.
* Select Session 1 > Track 1 > OVERLAY.
* Right-click on `ETC.BIN` and select `Extract file...`.
* Choose a location to save the file.
 
Open the extracted `ETC.BIN` file and make these modifications in your hex editor of choice:
* Offset `71b0`: change `04 00 02 92` to `03 00 02 34`.
* Offset `141d0`: change `06 00 40 10` to `00 00 00 00`.
* Offset `189dc`: change `0c 00 40 14` to `00 00 00 00`
* Offset `19b10`: change `2b 00 40 14` to `00 00 00 00`.

After making the changes, use CDMage to  swap in your modified `ETC.BIN`:
* Right-click on the `ETC.BIN` file and select `Import file...`.
* Choose the path of your modified file.

