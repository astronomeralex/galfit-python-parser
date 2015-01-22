#
# This module will read in the galfit best fit values and uncertainties
#

from astropy.io import fits

class GalfitResults(object):
    """
    This class stores galfit results information
    Currently only does one component
    """
    def __init__(self, galfit_fits_file):
        """
        init method for GalfitResults. Take in a string that is the name
        of the galfit output fits file
        """
        hdulist = fits.open(galfit_fits_file)
        #now some checks to make sure the file is what we are expecting
        assert len(hdulist) == 4
        galfitmodel = hdulist[2]
        galfitheader = galfitmodel.header
        galfit_in_comments = False
        for i in galfitheader['COMMENTS']:
            galfit_in_comments = galfit_in_comments or "GALFIT" in i
        assert True == galfit_in_comments
        assert "COMP_1" in galfitheader
        #now we've convinced ourselves that this is probably a galfit file
        
        self.galfit_fits_file = galfit_fits_file
        self.fitsheader = galfitheader
        #read in the input parameters
        self.input_initfile = galfitheader['INITFILE']
        self.input_datain = galfitheader["DATAIN"]
        self.input_sigma = galfitheader["SIGMA"]
        self.input_psf = galfitheader["PSF"]
        self.input_constrnt = galfitheader["CONSTRNT"]
        self.input_mask = galfitheader["MASK"]
        self.input_fitsect = galfitheader["FITSECT"]
        self.input_convbox = galfitheader["CONVBOX"]
        self.input_magzpt = galfitheader["MAGZPT"]
        
        #read in the chi-square value
        self.chisq = galfitheader["CHISQ"]
        self.ndof = galfitheader["NDOF"]
        self.nfree = galfitheader["NFREE"]
        self.reduced_chisq = galfitheader["CHI2NU"]
        
        #find the number of components
        num_components = 1 #already verified above
        while True:
            if "COMP_" + str(num_components + 1) in galfitheader:
                num_components = num_components + 1
            else:
                break
        self.num_components = num_components
        
        headerkeys = [i for i in galfitheader.keys()]
        
        
        