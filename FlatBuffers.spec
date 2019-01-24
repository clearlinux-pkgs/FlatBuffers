#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : FlatBuffers
Version  : 1.9.0
Release  : 3
URL      : https://github.com/google/flatbuffers/archive/v1.9.0.tar.gz
Source0  : https://github.com/google/flatbuffers/archive/v1.9.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: FlatBuffers-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
Patch1: werror.patch

%description
![logo](http://google.github.io/flatbuffers/fpl_logo_small.png) FlatBuffers
===========

%package dev
Summary: dev components for the FlatBuffers package.
Group: Development
Provides: FlatBuffers-devel

%description dev
dev components for the FlatBuffers package.


%package license
Summary: license components for the FlatBuffers package.
Group: Default

%description license
license components for the FlatBuffers package.


%prep
%setup -q -n flatbuffers-1.9.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534631774
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build ; make test ; popd

%install
export SOURCE_DATE_EPOCH=1534631774
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/FlatBuffers
cp LICENSE.txt %{buildroot}/usr/share/doc/FlatBuffers/LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

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

%files license
%defattr(-,root,root,-)
/usr/share/doc/FlatBuffers/LICENSE.txt
