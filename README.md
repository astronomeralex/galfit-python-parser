# Galfit Python Parser
A few python classes to parse through galfit output fits files to retrieve fit information. This code relies on AstroPy for fits io.

Feel free to issue pull requests or issues if there are more features you'd like to see. Also feel free to email me.

The code contains two classes, `GalfitResult` and `GalfitComponent`. The input to `GalfitResult` is a string that is the name of the Galfit output file you'd like to open. The class then opens the file, and each component of the Galfit result is stored in a `GalfitComponent` object. The attributes of the `GalfitComponent` class are the same names as the Galfit keywords in the fits header. The input into Galfit is saved in `GalfitComponent` object as attributes that start with "input_".

For example, let's say you have the output fits file from galfit called `42_output.fits`. The software knows to look into the third fits HDU for the information; the software also checks a few things to verify that the file its opening is a Galfit output file.  To get the Galfit results, use `galfitres = galfit_parser.GalfitResult("42_output.fits")`. `galfitres` is a `GalfitResult` object which contains one or more `GalfitComponent` objects, as well as information about the inputs. To access component 1, for example, use `galfitres.COMP_1`. The attributes for `galfitres.COMP_1` are named using the same string, lowercase, as in the fits header. You can also see all the attributes of the object using `dir(galfitres)` or `dir(galfitres.COMP_1)`. 
