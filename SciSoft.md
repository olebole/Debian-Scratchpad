SciSoft programs for potential inclusion in Debian
===================================================


The list is taken from the
[SciSoft](http://www.eso.org/sci/software/scisoft)
package list. Packages that are already in Debian are in **bold**, packages
that will (for various reasons) not go into Debian are in *italic*. The other
may be packaging candidates.


| Package              | Description |
| -------------------- | ----------- |
| | |
| | **Data Analysis Systems** |
| [*iraf*](http://iraf.noao.edu/) | Image Reduction and Analysis Facility (*IRAF is hard to package for Debian (in fact for any distribution) because of its old architecture. It  also contains various routines from Numerical Recipes which are illegal to distribute.*) |
| [*iraf-ctio*](http://www.stecf.org/scripts/irafhelp?ctio) | Utilities from CTIO (*Depends on IRAF*) |
| [*iraf-mxtools*](http://www.noao.edu/noao/staff/mighell/mxtools/) | Utilities from NOAO including QDPHOT (*Depends on IRAF*) |
| [*iraf-guiapps*](http://www.stecf.org/iraf/web/projects/guiapps/) | Graphical applications for IRAF (*Depends on IRAF*) |
| *iraf-xdimsum* | Enhanced IR data reduction and mosaicing software (*Depends on IRAF*) |
| [*iraf-color*](http://www.stecf.org/scripts/irafhelp?color) | Utilities for creating colour images (*Depends on IRAF*) |
| [*iraf-fitsutil*](http://www.stecf.org/scripts/irafhelp?fitsutil) | FITS utilities (*Depends on IRAF*) |
| [*iraf-mscred*](http://www.stecf.org/scripts/irafref?mscred) | Mosaic camera CCD reduction tasks from NOAO (*Depends on IRAF*) |
| *iraf-esowfi* | ESO WFI Mosaic reduction package (*Depends on IRAF*) |
| [*iraf-rvsao*](http://tdc-www.harvard.edu/iraf/rvsao/rvsao.html) | Spectral Radial Velocity package from CfAi (*Depends on IRAF*) |
| [*iraf-stecf*](http://www.stecf.org/software/stecf-iraf/) | Utilities from ST-ECF (*Depends on IRAF*) |
| [*iraf-stsdas-tables*](http://www.stsci.edu/resources/software_hardware/stsdas) | HST data analysis and tables systems (*Depends on IRAF*) |
| [*iraf-ecl*](http://iraf.noao.edu/iraf/web/new_stuff/ecl_beta.html) | Enhanced CL (*Depends on IRAF*) |
| [eso-eclipse](http://www.eso.org/sci/software/eclipse/) | C Library for an Image Processing Software Environment |
| [**eso-midas**](https://packages.debian.org/sid/eso-midas) | European Southern Observatory Munich Image Data Analysis System |
| [*pymidas*](http://www.eso.org/sampo/pymidas) | Python interface for ESO-MIDAS (*PyMidas is outdated and no longer maintained. Does not support Python 2.7 or 3.x.*) |
| [**idl**](https://packages.debian.org/sid/gnudatalanguage) | Interactive Data Language from RSI. |
| [**idl-astron**](https://packages.debian.org/sid/gdl-astrolib) | Goddard Astron IDL astronomical procedure library. |
| [idl-starfinder](http://www.bo.astro.it/StarFinder/) | IDL adaptive optics photometry software. |
| [idl-jhuapl](http://fermi.jhuapl.edu/s1r/idl/s1rlib/local_idl.html) | IDL procedure collection from Johns Hopkins |
| [idl-atv](http://www.astro.caltech.edu/~barth/atv/) | interactive display tool for IDL |
| [gildas](http://iram.fr/IRAMFR/GILDAS/) | Radio astronomy applications from IRAM |
| [miriad](http://bima.astro.umd.edu/miriad/) | Calibration, mapping, deconvolution and image analysis of interferometric data |
| [karma](http://www.atnf.csiro.au/computing/software/karma/) | Toolkit for IPC, authentication, graphics display etc. |
| [crush](http://www.submm.caltech.edu/~sharc/crush/) | Data Reduction and Imaging for Bolometer Array |
| [casa](http://casa.nrao.edu/) | Common Astronomy Software Application |
| [theli](http://www.astro.uni-bonn.de/theli/) | A pipeline for astronomical image data reduction |
| [difmap](http://www.cv.nrao.edu/adass/adassVI/shepherdm.html) | Interactive program for radio synthesis imaging from Caltech |
| | |
| | **Image Display Servers** |
| [*x11iraf*](http://www.openastro.com/osx/x11iraf-info.html) | Graphical tools to work with IRAF (*Depends on IRAF*) |
| [*saoimage*](http://tdc-www.harvard.edu/software/saoimage.html) | The original, needs 8bit Xserver (*Outdated; use saods9*) |
| [**ds9**](https://packages.debian.org/sid/saods9) | Latest display server from SAO |
| [**xpa**](https://packages.debian.org/sid/xpa-tools) | Messaging system from SAO. Used by DS9. |
| [**skycat**](https://packages.debian.org/sid/skycat) | ESO image display tool with catalogue and image server access. |
| [**fv**](https://packages.debian.org/sid/ftools-fv) | Tool for viewing and editing FITS format files |
| [**qfitsview**](https://packages.debian.org/sid/qfitsview) | FITS file viewer |
| [gaia](http://star-www.dur.ac.uk/~pdraper/gaia/gaia.html) | Graphical Astronomy and Image Analysis Tool |
| | |
| | **Graphics Software** |
| [*supermongo*](http://www.astro.princeton.edu/~rhl/sm/) | SuperMongo. (*Not free.*) |
| [**pgplot**](https://packages.debian.org/sid/pgplot5) | large subroutine library for plotting scientific data |
| [**gnuplot**](https://packages.debian.org/sid/gnuplot) | Command-line driven interactive function plotting utility |
| [**grace**](https://packages.debian.org/sid/grace) | 2D WYSIWYG plotting tool |
| [**ggobi**](https://packages.debian.org/sid/ggobi) | Data visualisation in 3D. |
| [**matplotlib**](https://packages.debian.org/sid/python-matplotlib) | Python 2D plotting library. |
| [**plplot**](https://packages.debian.org/sid/libplplot-dev) | Cross-platform software package for creating scientific plots |
| | |
| | **Scripting Languages** |
| [*python-numeric*](http://sourceforge.net/projects/numpy/files/Old%20Numeric/) | Python module for high-performance, numeric computing (*Not maintained anymore, outdated by numpy*) |
| [**python-scientific**](https://packages.debian.org/sid/python-scientific) | Python modules useful for scientific computing (*Not maintained anymore, outdated by scipy*) |
| [**python-imaging (pil)**](https://packages.debian.org/sid/python-pil) | Python Imaging Library (Pillow fork) |
| [**python-pmw**](https://packages.debian.org/sid/python-pmw) | Pmw -- Python MegaWidgets |
| [python-asciidata](http://www.stecf.org/software/PYTHONtools/astroasciidata/) | Python module to handle ASCII tables |
| [**python-ipython**](https://packages.debian.org/sid/ipython) | enhanced interactive Python shell |
| [**python-scipy**](https://packages.debian.org/sid/python-scipy) | scientific tools for Python |
| [**python-gnuplot**](https://packages.debian.org/sid/python-gnuplot) | Python interface to the gnuplot plotting program |
| [python-ppgplot](https://github.com/npat-efault/ppgplot) | Pythonic Interface to PGPLOT |
| [**python-biggles**](https://packages.debian.org/sid/python-pybiggles) | Scientific plotting package for Python |
| [**python-pygame**](https://packages.debian.org/sid/python-pygame) | SDL bindings for games development in Python |
| [**python-wx**](https://packages.debian.org/sid/python-wxgtk3.0) | Python interface to the wxWidgets Cross-platform C++ GUI toolkit |
| [stsci-python](http://www.stsci.edu/resources/software_hardware/pyraf/stsci_python) | STScI Python packages |
| [*python-pyraf*](http://www.stsci.edu/resources/software_hardware/pyraf) | Python replacement for IRAF cl from STScI (*Depends on IRAF*) |
| [**python-pyfits**](https://packages.debian.org/sid/python-pyfits) | Python FITS package from STScI |
| [python-pydrizzle](http://www.stsci.edu/resources/software_hardware/pydrizzle) | Drizzling software |
| [python-multidrizzle](http://stsdas.stsci.edu/multidrizzle/) | Automatic image combination drizzling software |
| [**python-numpy**](https://packages.debian.org/sid/python-numpy) | Python package for scientific computing |
| [**dpuser**](https://packages.debian.org/sid/dpuser) | Interactive language for handling numbers, strings, and matrices |
| | |
| | **Scientific Libraries** |
| [**gsl**](https://packages.debian.org/sid/libgsl-dev) | The GNU Scientific Library |
| [*dislin*](http://www.mps.mpg.de/1389229/dislin) | Scientific Data Plotting software. (*Not DFSG-free*) |
| [**cfitsio**](https://packages.debian.org/sid/libcfitsio-dev) | FITS File Subroutine Library |
| [**lapack**](https://packages.debian.org/sid/liblapack-dev) | Linear Algebra Subroutine Library |
| [**atlas**](https://packages.debian.org/sid/libatlas-dev) | Another Linear Algebra Library |
| [**fftw**](https://packages.debian.org/sid/libfftw3-dev) | Fast Fourier Transform library |
| [**plotutils**](https://packages.debian.org/sid/plotutils) | GNU plotting utilities |
| [**jpype**](https://packages.debian.org/sid/python-jpype) | Java to Python integration |
| [**funtools**](https://packages.debian.org/sid/funtools) | 'Minimal buy-in' FITS library and utility package |
| | |
| | **Miscellaneous Utilities** |
| [**wcstools**](https://packages.debian.org/sid/wcstools) | World Coordinate System software tools and library from Doug Mink at SAO |
| [**astromatic**](https://packages.debian.org/sid/astromatic) | Astronomical pipeline software collection |
| [**astromatic-sextractor**](https://packages.debian.org/sid/sextractor) | Source extractor for astronomical images |
| [**astromatic-swarp**](https://packages.debian.org/sid/swarp) | Resample and co-add together FITS images |
| [**astromatic-scamp**](https://packages.debian.org/sid/scamp) | Compute astrometric and photometric solutions |
| [astromatic-eye](http://www.astromatic.net/software/eye) | Enhance Your Extraction |
| [**astromatic-missfits**](https://packages.debian.org/sid/missfits) | Basic maintenance and packaging tasks on FITS files |
| [**astromatic-stiff**](https://packages.debian.org/sid/stiff) | convert scientific FITS images to the TIFF format |
| [astromatic-stuff](http://www.astromatic.net/software/stuff) | Simulate 'perfect' astronomical catalogues |
| [**astromatic-weightwatcher**](https://packages.debian.org/sid/weightwatcher) | Combine maps and polygon data for astronomical image processing |
| [*tiny-tim*](http://www.stsci.edu/software/tinytim/tinytim.html) | HST point-spread function simulation software (*Unknown, unspecified license*) |
| [*xephem*](http://www.clearskyinstitute.com/xephem/) | Planetarium and ephemeris software (*Not DFSG-Free.*) |
| [*dss-dss2*](http://archive.eso.org/cms/tools-documentation/the-eso-st-ecf-digitized-sky-survey-application.html) | Digitized Sky Survey image extraction software (*Probably not DFSG-Free*) |
| [*daophot*](http://www.star.bris.ac.uk/~mbt/daophot/) | Stellar Photometry and related packages from Peter Stetson at DAO/HIA (*Not DFSG-Free.*) |
| [**fitsverify**](https://packages.debian.org/sid/fitsverify) | FITS format checker |
| [**fitscut**](https://packages.debian.org/sid/fitscut) | Image cutout and conversion utility |
| [**fpack-funpack**](https://packages.debian.org/sid/libcfitsio-bin) | FITS file compression utilities |
| [cloudy](http://www.nublado.org/) | Plasma simulation and spectral synthesis code |
| [hyperz](http://webast.ast.obs-mip.fr/hyperz/) | Photometric Redshift Code |
| [**graphviz**](https://packages.debian.org/sid/graphviz) | Graphical Visualisation Software |
| | |
| | **Virtual Observatory Tools** |
| [aladin](http://aladin.u-strasbg.fr/) | Aladin Sky Atlas |
| [vospec](http://esavo.esa.int/vospec/) | tool for handling Virtual Observatory compliant Spectra |
| [voplot](http://vo.iucaa.ernet.in/~voi/voplot.htm) | VOTable plotting tool |
| [plastic](http://plastic.sourceforge.net/) | PLatform for AStronomical Tool InterConnection |
| [specview](http://www.stsci.edu/resources/software_hardware/specview) | 1-D spectral visualization and analysis of astronomical spectrograms |
| [**splat**](https://packages.debian.org/sid/splat) | Spectral Analysis Tool |
| [stilts](http://www.star.bris.ac.uk/~mbt/stilts/) | Starlink Tables Infrastructure Library Tool Set |
| [topcat](http://www.star.bristol.ac.uk/~mbt/topcat/) | Tool for OPerations on Catalogues And Tables |
| [virgo](http://archive.eso.org/cms/tools-documentation/visual-archive-browser) | Visual Browser for the ESO Science Archive Facility |
