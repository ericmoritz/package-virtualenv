This packages up a virtualenv to be deployed to /opt/virtualenvs.  It
is rudimentary but it works.

It assumes that the packages will be deployed onto a system with the
same architecture

## Backends

### zip

This backend examines your virtualenv for any .so files and packages
up your virtualenv with any linked dependacies for the .so


### rpm-spec

The backend generates a RPM spec that can be used with "rpmbuild -ba"
to generate an RPM.

