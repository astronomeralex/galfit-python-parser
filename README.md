# Galfit Python Parser
A few python classes to parse through galfit output fits files to retrieve fit information. This code relies on AstroPy for fits io.

Feel free to issue pull requests or issues if there are more features you'd like to see. Also feel free to email me.

The code contains two classes, `GalfitResult` and `GalfitComponent`. The input to `GalfitResult` is a string that is the name of the Galfit output file you'd like to open. The class then opens the file, and each component of the Galfit result is stored in a `GalfitComponent` object. The attributes of the `GalfitComponent` class are the same names as the Galfit keywords in the fits header. The input into Galfit is saved in `GalfitComponent` object as attributes that start with "input_".
