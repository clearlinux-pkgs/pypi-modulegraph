#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-modulegraph
Version  : 0.19.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/0d/93/17013896ecedeb0fa0fbfdf9dcd31217c24d428f4a27726c550a32b77065/modulegraph-0.19.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/93/17013896ecedeb0fa0fbfdf9dcd31217c24d428f4a27726c550a32b77065/modulegraph-0.19.2.tar.gz
Summary  : Python module dependency analysis tool
Group    : Development/Tools
License  : MIT
Requires: pypi-modulegraph-bin = %{version}-%{release}
Requires: pypi-modulegraph-python = %{version}-%{release}
Requires: pypi-modulegraph-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(altgraph)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
modulegraph
===========
modulegraph determines a dependency graph between Python modules primarily
by bytecode analysis for import statements.

%package bin
Summary: bin components for the pypi-modulegraph package.
Group: Binaries

%description bin
bin components for the pypi-modulegraph package.


%package python
Summary: python components for the pypi-modulegraph package.
Group: Default
Requires: pypi-modulegraph-python3 = %{version}-%{release}

%description python
python components for the pypi-modulegraph package.


%package python3
Summary: python3 components for the pypi-modulegraph package.
Group: Default
Requires: python3-core
Provides: pypi(modulegraph)
Requires: pypi(altgraph)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-modulegraph package.


%prep
%setup -q -n modulegraph-0.19.2
cd %{_builddir}/modulegraph-0.19.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652687948
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/modulegraph

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
