Scisoft programs for potential inclusion in Debian
===================================================

[Scisoft-8.0](http://www.eso.org/sci/software/scisoft/Scisoft-contents.html)

Data Analysis Systems
---------------------

| Package              | Description |
| -------------------- | ----------- |
| *IRAF*               | IRAF is hard to package for Debian (in fact for any distribution) because of its old architecture. It  also contains various routines from Numerical Recipes which are illegal to distribute. |
| *IRAF/ctio*          | Utilities from CTIO |
| *IRAF/mxtools*       | Utilities from NOAO including QDPHOT |
| *IRAF/guiapps*       | Graphical applications for IRAF |
| *IRAF/xdimsum*       | Enhanced IR data reduction and mosaicing software |
| *IRAF/color*         | Utilities for creating colour images |
| *IRAF/fitsutil*      | FITS utilities |
| *IRAF/mscred*        | Mosaic camera CCD reduction tasks from NOAO |
| *IRAF/esowfi*        |  |
| *IRAF/rvsao*         | Spectral Radial Velocity package from CfAi |
| *IRAF/stecf*         | Utilities from ST-ECF, including polarimetry reduction and spectral restoration packages |
| *IRAF/STSDAS/TABLES* | HST data analysis and tables systems |
| *IRAF/ECL*           | Enhanced CL |
| Eclipse              | Includes ISAAC, CONICA, WFI, Lua and ADONIS add-ons |
| **ESO-MIDAS**        | available in Debian |
| *PyMidas*            | PyMidas is outdated and no longer maintained. Does not support Python 2.7 or 3.x. |
| **IDL**              | Interactive Data Language from RSI. Commercial package, requires license. GDL is in Debian as free replacement.|
| **IDL/Astron**       | Goddard Astron IDL astronomical procedure library. Available in Debian. |
| IDL/StarFinder       | IDL adaptive optics photometry software. Not available anymore. |
| IDL/JHUAPL Library   | IDL procedure collection from Johns Hopkins |
| IDL/ATV              |an interactive display tool for IDL |
| Gildas               | Radio astronomy applications from IRAM |
| Miriad               | Calibration, mapping, deconvolution and image analysis of interferometric data |
| Karma                | Toolkit for interprocess communications, authentication, encryption, graphics display, user interface and manipulating the Karma network data structure. Not maintained any longer.|
| CRUSH                | Data Reduction and Imaging for Bolometer Array |
| CASA                 | Common Astronomy Software Application |
| THELI                | A pipeline for astronomical image data reduction |
| Difmap               | Interactive program for radio synthesis imaging from Caltech |

Image Display Servers
---------------------

| Package              | Description |
| -------------------- | ----------- |
| *x11iraf*            | See IRAF |
| *SAOImage*           | The original, needs 8bit Xserver; Outdated; use saods9 |
| **DS9**              | Latest display server from SAO. Available in Debian. |
| **XPA**              | Messaging system from SAO. Used by DS9. Available in Debian |
| **Skycat**           | ESO image display tool with catalogue and image server access. Available in Debian |
| **fv**               | Available in Debian |
| QFitsView            | FITS file viewer |
| Gaia                 | Graphical Astronomy and Image Analysis Tool |


Graphics Software
-----------------

| Package              | Description |
| -------------------- | ----------- |
| *SM*                 | SuperMongo. Not free. |
| **PGPLOT**           | Available in Debian (non-free) |
| **gnuplot**          | Command-line driven interactive function plotting utility. Available in Debian |
| **Grace**            | 2D WYSIWYG plotting tool. Available in Debian. |
| **ggobi**            | Data visualisation in 3D. Available in Debian. |
| **Matplotlib**       | Python 2D plotting library. Available in Debian. |
| **PLplot**           | Cross-platform software package for creating scientific plots. Available in Debian. |

Scripting Languages
-------------------

| Package              | Description |
| -------------------- | ----------- |
| **Python**           | General purpose, object orientated, extensible scripting language. Available in Debian |
| *Python/Numeric*     | Not maintained anymore, outdated by numpy |
| **Python/Scientific** | available in Debian |
| **Python/Imaging (PIL)** | Available in Debian |
| **Python/Pmw**       | Available in Debian |
| Python/asciidata     | |
| **Python/binascii**  | Available as part of Python |
| **Python/ipython**   | Available in Debian  |
| **Python/scipy**     | Available in Debian  |
| **Python/Gnuplot**   | Available in Debian  |
| Python/ppgplot       | |
| **Python/biggles**   | Available in Debian  |
| **Python/pygame**    | Available in Debian  |
| Python/cStringIO & cPickle | |
| **Python/wx**        | wxPython. Available in Debian. |
| *Python/PyRAF*       | Python replacement for IRAF cl from STScI. See IRAF.
| **Python/PyFITS**    | Python FITS package from STScI. Available in Debian.
| Python/PyDrizzle     | Drizzling software |
| Python/MultiDrizzle  | Automatic image combination drizzling software |
| **Python/NumPy**     | Python package for scientific computing. Available in Debian.
| **Java**             | Java runtime environment and JDK. Available in Debian.
| DPUser               | Interactive language for handling numbers, strings, and matrices

Scientific Libraries
--------------------

| Package              | Description |
| -------------------- | ----------- |
| **GSL**              | The GNU Scientific Library. Available in Debian. |
| *DISLIN*             | Scientific Data Plotting software. Not DFGS-free |
| **CFITSIO**          | FITS File Subroutine Library. Available in Debian. |
| **LAPACK**           | Linear Algebra Subroutine Library. Available in Debian. |
| **Atlas**            | Another Linear Algebra Library. Available in Debian. |
| **FFTW**             | Fast Fourier Transform library. Available in Debian. |
| **plotutils**        | GNU plotting utilities. Available in Debian. |
| **JPype**            | Java to Python integration. Available in Debian. |
| **Funtools**         | "Minimal buy-in" FITS library and utility package. Available in Debian. |

Miscellaneous Utilities
-----------------------

| Package              | Description |
| -------------------- | ----------- |
| **wcstools**         | World Coordinate System software tools and library from Doug Mink at SAO. Available in Debian. |
| **Astromatic**       | Available in Debian |
| **Astromatic/SExtractor** | Available in Debian |
| **Astromatic/SWarp** | Available in Debian |
| **Astromatic/SCAMP** | Available in Debian |
| Astromatic/EyE       |  |
| **Astromatic/MissFits** | Available in Debian |
| **Astromatic/STIFF** | Available in Debian |
| Astromatic/Stuff     |  |
| **Astromatic/WeightWatcher** | Available in Debian |
| Tiny Tim             | HST point-spread function simulation software |
| *Xephem*             | Planetarium and ephemeris software. Not DFSG-Free. |
| dss/dss2             | Digitized Sky Survey image extraction software |
| *DAOPhot*            | Stellar Photometry and related packages from Peter Stetson at DAO/HIA. Not DFSG-Free. |
| **fitsverify**       | FITS format checker. Available in Debian. |
| **fitscut**          | Image cutout and conversion utility. Available in Debian. |
| **fpack/funpack**    | FITS file compression utilities. Available in Debian. |
| Cloudy               | Plasma simulation and spectral synthesis code |
| HyperZ               | Photometric Redshift Code |
| **graphviz**         | Graphical Visualisation Software. Available in Debian. |

Virtual Observatory Tools
-------------------------

| Package              | Description |
| -------------------- | ----------- |
| Aladin               | Aladin Sky Atlas |
| VOspec               | tool for handling Virtual Observatory compliant Spectra |
| VOplot               | VOTable plotting tool |
| Plastic              | PLatform for AStronomical Tool InterConnection |
| Specview             | |
| Splat                | Spectral Analysis Tool |
| Stilts               | Starlink Tables Infrastructure Library Tool Set |
| TOPCAT               | Tool for OPerations on Catalogues And Tables |
| VirGO                | Visual Browser for the ESO Science Archive Facility |
