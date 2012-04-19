This packages up a virtualenv to be deployed to another machine.  It
assumes that the packages will be deployed onto a system with the same
architecture and operating system.

## Backends

### zip

This backend examines your virtualenv for any .so files and packages
up your virtualenv with any linked dependacies for the .so

    root@host-0 ~$ package-virtualenv -b zip path-to-virtualenv out.zip

Warning, this zip file has system libraries so make sure you unzip
with the -n option to avoid overwriting existing files.


     root@host-1 ~$ unzip -n out.zip


### rpm-spec

The backend generates a RPM spec that can be used with "rpmbuild -ba"
to generate an RPM.

    $ package-virtualenv -b rpm-spec path-to-virtualenv out.spec	
    $ rpmbuild -ba out.spec

Warning, rpm-spec is currently not working correctly