#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v10
# autospec commit: 5905be9
#
Name     : pypi-mkdocs_get_deps
Version  : 0.2.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/98/f5/ed29cd50067784976f25ed0ed6fcd3c2ce9eb90650aa3b2796ddf7b6870b/mkdocs_get_deps-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/f5/ed29cd50067784976f25ed0ed6fcd3c2ce9eb90650aa3b2796ddf7b6870b/mkdocs_get_deps-0.2.0.tar.gz
Summary  : MkDocs extension that lists all dependencies according to a mkdocs.yml file
Group    : Development/Tools
License  : MIT
Requires: pypi-mkdocs_get_deps-bin = %{version}-%{release}
Requires: pypi-mkdocs_get_deps-license = %{version}-%{release}
Requires: pypi-mkdocs_get_deps-python = %{version}-%{release}
Requires: pypi-mkdocs_get_deps-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# mkdocs-get-deps
**An extra command for [MkDocs][] that infers required PyPI packages from `plugins` in mkdocs.yml.**

%package bin
Summary: bin components for the pypi-mkdocs_get_deps package.
Group: Binaries
Requires: pypi-mkdocs_get_deps-license = %{version}-%{release}

%description bin
bin components for the pypi-mkdocs_get_deps package.


%package license
Summary: license components for the pypi-mkdocs_get_deps package.
Group: Default

%description license
license components for the pypi-mkdocs_get_deps package.


%package python
Summary: python components for the pypi-mkdocs_get_deps package.
Group: Default
Requires: pypi-mkdocs_get_deps-python3 = %{version}-%{release}

%description python
python components for the pypi-mkdocs_get_deps package.


%package python3
Summary: python3 components for the pypi-mkdocs_get_deps package.
Group: Default
Requires: python3-core
Provides: pypi(mkdocs_get_deps)
Requires: pypi(mergedeep)
Requires: pypi(platformdirs)
Requires: pypi(pyyaml)

%description python3
python3 components for the pypi-mkdocs_get_deps package.


%prep
%setup -q -n mkdocs_get_deps-0.2.0
cd %{_builddir}/mkdocs_get_deps-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713794245
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mkdocs_get_deps
cp %{_builddir}/mkdocs_get_deps-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-mkdocs_get_deps/7e1ff5b0f79c688017a0a219169159e6a58e6859 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mkdocs-get-deps

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mkdocs_get_deps/7e1ff5b0f79c688017a0a219169159e6a58e6859

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
