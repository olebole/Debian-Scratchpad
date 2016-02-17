Automated backporting
=====================

 * install a virtual machine somewhere
 * install pbuilder, cowbuilder
 * install images from all target releases:
   - Debian stable (jessie)
   - Debian oldstable 
   - Ubuntu Trusty
   - Ubuntu Xenial (when it comes out)
 * install backport script
 * decide which packages to backport; create YML file with them
 * in crontab, regularly for each package:
 
   - check whether package was updated in debian testing; if yes:
   - get source package
   - for each supported backport release:
   
     - create backport source package
     - try to create binary package; if successfull:
     - sign source and binary packages with intermediate keys
     - put source and binary packages into private archive
   - Log all successfull and failed build attempts to a website
  * create a summary report per day with new backports and mail them
  * locally download, sign, and upload new backports
