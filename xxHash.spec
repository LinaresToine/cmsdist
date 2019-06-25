### RPM external xxHash 0.7.0
## INITENV SETV XXHASH_SOURCE %{source0}
## INITENV SETV XXHASH_STRIP_PREFIX %{source_prefix}

%define source_prefix %{n}-%{realversion}
Source: https://github.com/Cyan4973/xxHash/archive/v%{realversion}.tar.gz

BuildRequires: gmake cmake

%prep
%setup -n %{source_prefix}

%build

cmake cmake_unofficial \
 -DCMAKE_INSTALL_PREFIX:PATH=%{i}

make %{makeprocesses}

%install

make install

