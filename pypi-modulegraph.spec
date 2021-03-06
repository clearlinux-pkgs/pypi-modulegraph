#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-modulegraph
Version  : 0.19.2
Release  : 4
URL      : https://files.pythonhosted.org/packages/0d/93/17013896ecedeb0fa0fbfdf9dcd31217c24d428f4a27726c550a32b77065/modulegraph-0.19.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/93/17013896ecedeb0fa0fbfdf9dcd31217c24d428f4a27726c550a32b77065/modulegraph-0.19.2.tar.gz
Summary  : Python module dependency analysis tool
Group    : Development/Tools
License  : MIT
Requires: pypi-modulegraph-bin = %{version}-%{release}
Requires: pypi-modulegraph-license = %{version}-%{release}
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
Requires: pypi-modulegraph-license = %{version}-%{release}

%description bin
bin components for the pypi-modulegraph package.


%package license
Summary: license components for the pypi-modulegraph package.
Group: Default

%description license
license components for the pypi-modulegraph package.


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
pushd ..
cp -a modulegraph-0.19.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656393854
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
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-modulegraph
cp %{_builddir}/modulegraph-0.19.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-modulegraph/2a5f8746735c45cf862a2c4037afc53d6a4ec81d
cp %{_builddir}/modulegraph-0.19.2/doc/license.rst %{buildroot}/usr/share/package-licenses/pypi-modulegraph/f7c8530285650877d9b3d44075329c6dbf5de742
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/modulegraph

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-modulegraph/2a5f8746735c45cf862a2c4037afc53d6a4ec81d
/usr/share/package-licenses/pypi-modulegraph/f7c8530285650877d9b3d44075329c6dbf5de742

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
