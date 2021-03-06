#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : FlatBuffers
Version  : 1.11.0
Release  : 4
URL      : https://github.com/google/flatbuffers/archive/v1.11.0/flatbuffers-1.11.0.tar.gz
Source0  : https://github.com/google/flatbuffers/archive/v1.11.0/flatbuffers-1.11.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: FlatBuffers-bin = %{version}-%{release}
Requires: FlatBuffers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
Patch1: werror.patch

%description
![logo](http://google.github.io/flatbuffers/fpl_logo_small.png) FlatBuffers
===========

%package bin
Summary: bin components for the FlatBuffers package.
Group: Binaries
Requires: FlatBuffers-license = %{version}-%{release}

%description bin
bin components for the FlatBuffers package.


%package dev
Summary: dev components for the FlatBuffers package.
Group: Development
Requires: FlatBuffers-bin = %{version}-%{release}
Provides: FlatBuffers-devel = %{version}-%{release}
Requires: FlatBuffers = %{version}-%{release}

%description dev
dev components for the FlatBuffers package.


%package license
Summary: license components for the FlatBuffers package.
Group: Default

%description license
license components for the FlatBuffers package.


%prep
%setup -q -n flatbuffers-1.11.0
cd %{_builddir}/flatbuffers-1.11.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579044075
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1579044075
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/FlatBuffers
cp %{_builddir}/flatbuffers-1.11.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/FlatBuffers/89e4939e88f1e7ff29e52604a9d65a762c062d1d
cp %{_builddir}/flatbuffers-1.11.0/dart/LICENSE %{buildroot}/usr/share/package-licenses/FlatBuffers/964f6fc24f3d1216a2482a8f26cf7618e99d8a05
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flatc

%files dev
%defattr(-,root,root,-)
/usr/include/flatbuffers/base.h
/usr/include/flatbuffers/code_generators.h
/usr/include/flatbuffers/flatbuffers.h
/usr/include/flatbuffers/flatc.h
/usr/include/flatbuffers/flexbuffers.h
/usr/include/flatbuffers/grpc.h
/usr/include/flatbuffers/hash.h
/usr/include/flatbuffers/idl.h
/usr/include/flatbuffers/minireflect.h
/usr/include/flatbuffers/reflection.h
/usr/include/flatbuffers/reflection_generated.h
/usr/include/flatbuffers/registry.h
/usr/include/flatbuffers/stl_emulation.h
/usr/include/flatbuffers/util.h
/usr/lib64/cmake/flatbuffers/FlatbuffersConfig.cmake
/usr/lib64/cmake/flatbuffers/FlatbuffersConfigVersion.cmake
/usr/lib64/cmake/flatbuffers/FlatbuffersTargets-relwithdebinfo.cmake
/usr/lib64/cmake/flatbuffers/FlatbuffersTargets.cmake
/usr/lib64/cmake/flatbuffers/FlatcTargets-relwithdebinfo.cmake
/usr/lib64/cmake/flatbuffers/FlatcTargets.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/FlatBuffers/89e4939e88f1e7ff29e52604a9d65a762c062d1d
/usr/share/package-licenses/FlatBuffers/964f6fc24f3d1216a2482a8f26cf7618e99d8a05
