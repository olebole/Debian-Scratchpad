AstroConda programs for potential inclusion in Debian
===================================================


The list is taken from the
[AstroConda](http://astroconda.readthedocs.io)
package list. Packages that are already in Debian are in **bold**, packages
that will (for various reasons) not go into Debian are in *italic*. The other
may be packaging candidates.


| Package              | Description |
| -------------------- | ----------- |
| | |
| | **HST/JWST specific packages** |
| [acstools](http://acstools.readthedocs.io/) | Python Tools for ACS (Advanced Camera for Surveys) Data |
| [wfpc2tools](http://www.stsci.edu/resources/software_hardware/stsci_python) | Tools for use with the Wide Field and Planetary Camera 2 |
| [calcos](https://github.com/spacetelescope/calcos) | Calibration for HST/COS |
| [hstcal](https://github.com/spacetelescope/hstcal) | Calibration for HST/WFC3, HST/ACS, and HST/STIS |
| [nictools](https://github.com/spacetelescope/nictools) | Tools for HST/NICMOS |
| [jwst-lib](ssh://git@bitbucket.org/stsci_ssb/jwst.git) | James Webb Space Telescope library |
| [jwst-pipeline](http://ssb.stsci.edu/doc/jwst_dev/jwst_pipeline.pipeline.doc.user_guide.doc/html/index.html) | James Webb Space Telescope pipeline |
| [jwst-tools](ssh://git@bitbucket.org/stsci_ssb/jwst.git) | James Webb Space Telescope tools |
| [wfc3tools](http://ssb.stsci.edu/doc/stsci_python_2.15.1/wfc3tools.doc/html/index.html) | Tools for the Hubble Space Telescope Wide Field Camera 3 |
| [reftools](http://www.stsci.edu/institute/software_hardware/pyraf/stsci_python) | Tools for HST reference files |
| [stistools](http://www.stsci.edu/institute/software_hardware/pyraf/stsci_python) | Tools for working with STIS data |
| [costools](http://www.stsci.edu/institute/software_hardware) | Tools for working with COS data |
| [crds](http://www.stsci.edu/hst/observatory/crds/) | Calibration Reference Data System |
| | |
| | **STSci specific packages** |
| [*stsci.sphere*](http://ssb.stsci.edu/doc/stsci_python_x/stsci.sphere.doc/html/user.html) | STScI's spherical geometry astropy package (*Package is outdated and replaced by Scipy*) |
| [*stsci.skypac*](https://github.com/spacetelescope/stsci.skypac) | Sky matching for image mosaic (*Package is outdated and replaced by Scipy*) |
| [*stsci.convolve*](https://github.com/spacetelescope/stsci.convolve) | Subset of SciPy functionality for convolving (*Package is outdated and replaced by Scipy*) |
| [**stsci.distutils**](https://packages.debian.org/sid/python-stsci.distutils) | Python packaging utilities for STScI's packages |
| [*stsci.image*](https://github.com/spacetelescope/stsci.image) | Image array manipulation functions (*Package is outdated and replaced by Scipy*) |
| [*stsci.imagemanip*](https://github.com/spacetelescope/stsci.imagemanip) | STScI general image manipulation tools (*Package is outdated and replaced by Scipy*) |
| [*stsci.imagestats*](https://github.com/spacetelescope/stsci.imagestats) | Compute various useful statistical values for array objects (*Package is outdated and replaced by Scipy*) |
| [*stsci.ndimage*](https://github.com/spacetelescope/stsci.ndimage) | Fork of scipy.ndimage (*Package is outdated and replaced by Scipy*) |
| [*stsci.numdisplay*](http://stsdas.stsci.edu/numdisplay) | Visualize numpy array objects (*Package is outdated. Use pyds9 instead.*) |
| [*stsci.stimage*](https://github.com/spacetelescope/stsci.stimage) | Various functions for performing processing of images (*Package is outdated and replaced by Scipy*) |
| [**stsci.tools**](https://github.com/spacetelescope/stsci.tools) | STScI utility functions |
| [asv](http://asv.readthedocs.io/) | Simple Python benchmarking tool with web-based reporting |
| [cube-tools](https://github.com/spacetelescope/cube-tools) | Data analysis package for cubes |
| [fitsblender](http://ssb.stsci.edu/doc/stsci_python_dev/fitsblender.doc/html/index.html) | FITS header merging from multiple images. |
| [stwcs](https://github.com/spacetelescope/stwcs) | WCS based distortion models and coordinate transformation |
| [specview](https://github.com/spacetelescope/specview) | Java spectrum visualization, manipulation, and fitting |
| [stginga](https://github.com/spacetelescope/stginga) | Ginga products specific to STScI data analysis |
| | |
| | **Astronomy packages** |
| [**pyregion**](https://packages.debian.org/sid/python-pyregion) | Python module to parse ds9 region files |
| [**asdf**](https://packages.debian.org/sid/python-asdf) | Python library for the Advanced Scientific Data Format |
| [asdf-standard](http://asdf-standard.readthedocs.io/) | Advanced Scientific Data Format documentation |
| [astrolib.coords](http://ssb.stsci.edu/doc/stsci_python_dev/astrolib.coords.doc/html/index.html) | Astronomical coordinates & angular separations |
| [**photutils**](https://packages.debian.org/sid/python-photutils) | Astropy affiliated package for image photometry |
| [**pyds9**](https://packages.debian.org/sid/python-pyds9) | Python connection to SAOimage DS9 via XPA |
| [**xpa**](https://packages.debian.org/sid/libxpa-dev) | Provides seamless communication between many kinds of Unix programs |
| [**cfitsio**](https://packages.debian.org/sid/libcfitsio-dev) | Library for I/O with FITS format data files |
| [**ds9**](https://packages.debian.org/sid/saods9) | Image display tool for astronomy |
| [**wcstools**](https://packages.debian.org/sid/wcstools) | For setting and using the world coordinate systems (WCS) in the headers of the most common astronomical image formats |
| [**pysynphot**](https://packages.debian.org/sid/python-pysynphot) | Python Synthetic Photometry Utilities |
| [**pywcs**](https://packages.debian.org/sid/python-pywcs) | Set of routines for handling the FITS WCS standard |
| [**pyraf**](https://github.com/spacetelescope/pyraf) | Python replacement for IRAF cl from STScI |
| [**iraf**](http://iraf.noao.edu) | NOAO Image Reduction and Analysis Facility |
| [**ginga**](https://github.com/ejeschke/ginga) | The Ginga astronomical FITS file viewer |
| [**astropy**](https://packages.debian.org/sid/python-astropy) | Core functionality for performing astrophysics with Python |
| [**imexam**](http://imexam.readthedocs.io) | Simple image examination, and plotting, with similar functionality to IRAF's imexamine |
| [**gwcs**](http://gwcs.readthedocs.io/) | Tools for managing the WCS in a general way |
| [astroimtools](http://astroimtools.readthedocs.io) | Astronomical Image Convenience Tools |
| [drizzlepac](http://drizzlepac.stsci.edu/) | Align and combine HST images |
| | |
| | **Science packages** |
| [**numpy**](https://packages.debian.org/sid/python-numpy) | Numerical Python adds a fast array facility to the Python language |
| [**scipy**](https://packages.debian.org/sid/python-scipy) | Scientific tools for Python |
| [**pyfftw**](https://packages.debian.org/sid/python-pyfftw) | Pythonic wrapper around FFTW |
| [poppy](https://github.com/mperrin/poppy) | Physical Optics Propagation in Python |
| [webbpsf](http://www.stsci.edu/jwst/software/webbpsf/) | WebbPSF: Simulated PSF for the James Webb Space Telescope |
| [**fftw**](https://packages.debian.org/sid/libfftw3-dev) | Library for computing Fast Fourier Transforms |
| [htc-utils](http://bitbucket.org/jhunkeler/htc_utils) | Homebrew set of HTCondor wrappers |
| | |
| | **Other packages** |
| [**appdirs**](https://packages.debian.org/sid/python-appdirs) | Determining appropriate platform-specific dirs |
| [**d2to1**](https://packages.debian.org/sid/python-d2to1) | Python support for distutils2-like setup.cfg files as package metadata |
| [recon](http://github.com/jhunkeler/recon) | Release control for git |
| [**pytools**](https://packages.debian.org/sid/python-pytools) | A collection of tools for Python |
| [purge-path](http://bitbucket.org/jhunkeler/purge_path) | Small PATH manipulator |
| [**shunit2**](https://packages.debian.org/sid/shunit2) | Unit test framework for Bourne based shell scripts |
