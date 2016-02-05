Scisoft programs for potential inclusion in Debian
===================================================


The list is taken from the [Scisoft-8.0](http://www.eso.org/sci/software/scisoft/Scisoft-contents.html)
package list. Packages that are already in Debian are in **bold**, packages
that will (for various reasons) not go into Debian are in *italic*. The other
may be packaging candidates.


| Package              | Description |
| -------------------- | ----------- |
| | **Data Analysis Systems** |
| [*IRAF*](http://iraf.noao.edu/) | Image Reduction and Analysis Facility (*IRAF is hard to package for Debian (in fact for any distribution) because of its old architecture. It  also contains various routines from Numerical Recipes which are illegal to distribute.*) |
| [*IRAF/ctio*](http://www.stecf.org/scripts/irafhelp?ctio) | Utilities from CTIO (*Depends on IRAF*) |
| [*IRAF/mxtools*](http://www.noao.edu/noao/staff/mighell/mxtools/) | Utilities from NOAO including QDPHOT (*Depends on IRAF*) |
| [*IRAF/guiapps*](http://www.stecf.org/iraf/web/projects/guiapps/) | Graphical applications for IRAF (*Depends on IRAF*) |
| *IRAF/xdimsum* | Enhanced IR data reduction and mosaicing software (*Depends on IRAF*) |
| [*IRAF/color*](http://www.stecf.org/scripts/irafhelp?color) | Utilities for creating colour images (*Depends on IRAF*) |
| [*IRAF/fitsutil*](http://www.stecf.org/scripts/irafhelp?fitsutil) | FITS utilities (*Depends on IRAF*) |
| [*IRAF/mscred*](http://www.stecf.org/scripts/irafref?mscred) | Mosaic camera CCD reduction tasks from NOAO (*Depends on IRAF*) |
| *IRAF/esowfi* |  (*Depends on IRAF*) |
| [*IRAF/rvsao*](http://tdc-www.harvard.edu/iraf/rvsao/rvsao.html) | Spectral Radial Velocity package from CfAi (*Depends on IRAF*) |
| [*IRAF/stecf*](http://www.stecf.org/software/stecf-iraf/) | Utilities from ST-ECF, including polarimetry reduction and spectral restoration packages (*Depends on IRAF*) |
| [*IRAF/STSDAS/TABLES*](http://www.stsci.edu/resources/software_hardware/stsdas) | HST data analysis and tables systems (*Depends on IRAF*) |
| [*IRAF/ECL*](http://iraf.noao.edu/iraf/web/new_stuff/ecl_beta.html) | Enhanced CL (*Depends on IRAF*) |
| [Eclipse](http://www.eso.org/sci/software/eclipse/) | Includes ISAAC, CONICA, WFI, Lua and ADONIS add-ons |
| [**ESO-MIDAS**](https://packages.debian.org/sid/eso-midas) | European Southern Observatory Munich Image Data Analysis System |
| [*PyMidas*](http://www.eso.org/sampo/pymidas) | Python interface for ESO-MIDAS (*PyMidas is outdated and no longer maintained. Does not support Python 2.7 or 3.x.*) |
| [**IDL**](https://packages.debian.org/sid/gnudatalanguage) | Interactive Data Language from RSI. |
| [**IDL/Astron**](https://packages.debian.org/sid/gdl-astrolib) | Goddard Astron IDL astronomical procedure library. |
| [IDL/StarFinder](http://www.bo.astro.it/StarFinder/) | IDL adaptive optics photometry software. |
| [IDL/JHUAPL](http://fermi.jhuapl.edu/s1r/idl/s1rlib/local_idl.html) | IDL procedure collection from Johns Hopkins |
| [IDL/ATV](http://www.astro.caltech.edu/~barth/atv/) | interactive display tool for IDL |
| [Gildas](http://iram.fr/IRAMFR/GILDAS/) | Radio astronomy applications from IRAM |
| [Miriad](http://bima.astro.umd.edu/miriad/) | Calibration, mapping, deconvolution and image analysis of interferometric data |
| [Karma](http://www.atnf.csiro.au/computing/software/karma/) | Toolkit for interprocess communications, authentication, encryption, graphics display, user interface and manipulating the Karma network data structure. |
| [CRUSH](http://www.submm.caltech.edu/~sharc/crush/) | Data Reduction and Imaging for Bolometer Array |
| [CASA](http://casa.nrao.edu/) | Common Astronomy Software Application |
| [THELI](http://www.astro.uni-bonn.de/~theli/) | A pipeline for astronomical image data reduction |
| [Difmap](http://www.cv.nrao.edu/adass/adassVI/shepherdm.html) | Interactive program for radio synthesis imaging from Caltech |
| | **Image Display Servers** |
| [*x11iraf*](http://www.openastro.com/osx/x11iraf-info.html) | Graphical tools to work with IRAF (*Depends on IRAF*) |
| [*SAOImage*](http://tdc-www.harvard.edu/software/saoimage.html) | The original, needs 8bit Xserver (*Outdated; use saods9*) |
| [**DS9**](https://packages.debian.org/sid/saods9) | Latest display server from SAO |
| [**XPA**](https://packages.debian.org/sid/xpa-tools) | Messaging system from SAO. Used by DS9. |
| [**Skycat**](https://packages.debian.org/sid/skycat) | ESO image display tool with catalogue and image server access. |
| [**fv**](https://packages.debian.org/sid/ftools-fv) | Tool for viewing and editing FITS format files |
| [QFitsView](http://www.mpe.mpg.de/~ott/QFitsView/index.html) | FITS file viewer |
| [Gaia](http://star-www.dur.ac.uk/~pdraper/gaia/gaia.html) | Graphical Astronomy and Image Analysis Tool |
| | **Graphics Software** |
| [*SM*](http://www.astro.princeton.edu/~rhl/sm/) | SuperMongo. (*Not free.*) |
| [**PGPLOT**](https://packages.debian.org/sid/pgplot5) | large subroutine library for plotting scientific data |
| [**gnuplot**](https://packages.debian.org/sid/gnuplot) | Command-line driven interactive function plotting utility |
| [**Grace**](https://packages.debian.org/sid/grace) | 2D WYSIWYG plotting tool |
| [**ggobi**](https://packages.debian.org/sid/ggobi) | Data visualisation in 3D. |
| [**Matplotlib**](https://packages.debian.org/sid/ggobi) | Python 2D plotting library. |
| [**PLplot**](https://packages.debian.org/sid/libplplot-dev) | Cross-platform software package for creating scientific plots |
| | **Scripting Languages** |
| [**Python**](https://packages.debian.org/sid/python) | General purpose, object orientated, extensible scripting language. |
| [*Python/Numeric*](http://sourceforge.net/projects/numpy/files/Old%20Numeric/) | Python module for high-performance, numeric computing (*Not maintained anymore, outdated by numpy*) |
| [**Python/Scientific**](https://packages.debian.org/sid/python-scientific) | Python modules useful for scientific computing |
| [**Python/Imaging (PIL)**](https://packages.debian.org/sid/python-pil) | Python Imaging Library (Pillow fork) |
| [**Python/Pmw**](https://packages.debian.org/sid/python-pmw) | Pmw -- Python MegaWidgets |
| [Python/asciidata](http://www.stecf.org/software/PYTHONtools/astroasciidata/) | Python module to handle ASCII tables |
| [**Python/binascii**](https://packages.debian.org/sid/python) | interactive high-level object-oriented language (default version) |
| [**Python/ipython**](https://packages.debian.org/sid/ipython) | enhanced interactive Python shell |
| [**Python/scipy**](https://packages.debian.org/sid/python-scipy) | scientific tools for Python |
| [**Python/Gnuplot**](https://packages.debian.org/sid/python-gnuplot) | Python interface to the gnuplot plotting program |
| [Python/ppgplot](https://github.com/npat-efault/ppgplot) | Pythonic Interface to PGPLOT |
| [**Python/biggles**](https://packages.debian.org/sid/python-pyggles) | Scientific plotting package for Python |
| [**Python/pygame**](https://packages.debian.org/sid/python-pygame) | SDL bindings for games development in Python |
| [**Python/cStringIO**](https://packages.debian.org/sid/python) | interactive high-level object-oriented language (default version) |
| [**Python/cPickle**](https://packages.debian.org/sid/python) | interactive high-level object-oriented language (default version) |
| [**Python/wx**](https://packages.debian.org/sid/python-wxgtk3.0) | Python interface to the wxWidgets Cross-platform C++ GUI toolkit |
| [STScI_Python](http://www.stsci.edu/resources/software_hardware/pyraf/stsci_python) | STScI Python packages |
| [*Python/PyRAF*](http://www.stsci.edu/resources/software_hardware/pyraf) | Python replacement for IRAF cl from STScI (*Depends on IRAF*) |
| [**Python/PyFITS**](https://packages.debian.org/sid/python-pyfits) | Python FITS package from STScI |
| [Python/PyDrizzle](http://www.stsci.edu/resources/software_hardware/pydrizzle) | Drizzling software |
| [Python/MultiDrizzle](http://stsdas.stsci.edu/pydrizzle/multidrizzle/) | Automatic image combination drizzling software |
| [**Python/NumPy**](https://packages.debian.org/sid/python-numpy) | Python package for scientific computing |
| [**Java**](https://packages.debian.org/sid/openjdk-9-jdk) | Java runtime environment and JDK |
| [DPUser](http://www.mpe.mpg.de/~ott/dpuser/index.html) | Interactive language for handling numbers, strings, and matrices |
| | **Scientific Libraries** |
| [**GSL**](https://packages.debian.org/sid/libgsl-dev) | The GNU Scientific Library |
| [*DISLIN*](http://www.linmpi.mpg.de/dislin/) | Scientific Data Plotting software. (*Not DFSG-free*) |
| [**CFITSIO**](https://packages.debian.org/sid/libcfitsio-dev) | FITS File Subroutine Library |
| [**LAPACK**](https://packages.debian.org/sid/liblapack-dev) | Linear Algebra Subroutine Library |
| [**Atlas**](https://packages.debian.org/sid/libatlas-dev) | Another Linear Algebra Library |
| [**FFTW**](https://packages.debian.org/sid/libfftw3-dev) | Fast Fourier Transform library |
| [**plotutils**](https://packages.debian.org/sid/plotutils) | GNU plotting utilities |
| [**JPype**](https://packages.debian.org/sid/python-jpype) | Java to Python integration |
| [**Funtools**](https://packages.debian.org/sid/funtools) | 'Minimal buy-in' FITS library and utility package |
| | **Miscellaneous Utilities** |
| [**wcstools**](https://packages.debian.org/sid/wcstools) | World Coordinate System software tools and library from Doug Mink at SAO |
| [**Astromatic**](https://packages.debian.org/sid/astromatic) | Astronomical pipeline software collection |
| [**Astromatic/SExtractor**](https://packages.debian.org/sid/sextractor) | Source extractor for astronomical images |
| [**Astromatic/SWarp**](https://packages.debian.org/sid/swarp) | Resample and co-add together FITS images |
| [**Astromatic/SCAMP**](https://packages.debian.org/sid/scamp) | Compute astrometric and photometric solutions |
| [Astromatic/EyE](http://www.astromatic.net/software/eye) | Enhance Your Extraction |
| [**Astromatic/MissFits**](https://packages.debian.org/sid/missfits) | Basic maintenance and packaging tasks on FITS files |
| [**Astromatic/STIFF**](https://packages.debian.org/sid/stiff) | convert scientific FITS images to the TIFF format |
| [Astromatic/Stuff](http://www.astromatic.net/software/stuff) | Simulate 'perfect' astronomical catalogues |
| [**Astromatic/WeightWatcher**](https://packages.debian.org/sid/weightwatcher) | Combine maps and polygon data for astronomical image processing |
| [Tiny Tim](http://www.stsci.edu/software/tinytim/tinytim.html) | HST point-spread function simulation software |
| [*Xephem*](http://www.clearskyinstitute.com/xephem/) | Planetarium and ephemeris software (*Not DFSG-Free.*) |
| [*dss/dss2*](http://archive.eso.org/dss/eso-dss.html) | Digitized Sky Survey image extraction software (*Probably not DFSG-Free*) |
| [*DAOPhot*](http://www.star.bris.ac.uk/~mbt/daophot/) | Stellar Photometry and related packages from Peter Stetson at DAO/HIA (*Not DFSG-Free.*) |
| [**fitsverify**](https://packages.debian.org/sid/fitsverify) | FITS format checker |
| [**fitscut**](https://packages.debian.org/sid/fitscut) | Image cutout and conversion utility |
| [**fpack/funpack**](https://packages.debian.org/sid/libcfitsio-bin) | FITS file compression utilities |
| [Cloudy](http://www.nublado.org/) | Plasma simulation and spectral synthesis code |
| [HyperZ](http://webast.ast.obs-mip.fr/hyperz/) | Photometric Redshift Code |
| [**graphviz**](https://packages.debian.org/sid/graphviz) | Graphical Visualisation Software |
| | **Virtual Observatory Tools** |
| [Aladin](http://aladin.u-strasbg.fr/) | Aladin Sky Atlas |
| [VOspec](http://esavo.esa.int/vospec/) | tool for handling Virtual Observatory compliant Spectra |
| [VOplot](http://vo.iucaa.ernet.in/~voi/voplot.htm) | VOTable plotting tool |
| [Plastic](http://plastic.sourceforge.net/) | PLatform for AStronomical Tool InterConnection |
| [Specview](http://www.stsci.edu/resources/software_hardware/specview) | 1-D spectral visualization and analysis of astronomical spectrograms |
| [Splat](http://star-www.dur.ac.uk/~pdraper/splat/splat-vo/) | Spectral Analysis Tool |
| [Stilts](http://www.star.bris.ac.uk/~mbt/stilts/) | Starlink Tables Infrastructure Library Tool Set |
| [TOPCAT](http://www.star.bristol.ac.uk/~mbt/topcat/) | Tool for OPerations on Catalogues And Tables |
| [VirGO](http://archive.eso.org/cms/tools-documentation/visual-archive-browser) | Visual Browser for the ESO Science Archive Facility |
