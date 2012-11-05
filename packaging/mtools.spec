Name:           mtools
#BuildRequires:  xorg-x11
#BuildRequires:  xorg-x11-devel
Version:        4.0.17
Release:        0
License:        GPL-3.0+
Summary:        Access Files on an MS-DOS File System
Url:            http://mtools.linux.lu/
Group:          System/Filesystems
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-conf.diff
Patch1:         %{name}-%{version}-autoconf.diff
Patch3:         %{name}-%{version}-aliasing.diff
Patch4:         %{name}-%{version}-fat-bits.diff
Patch5:         %{name}-%{version}-prototypes.diff
BuildRequires:  autoconf
#BuildRequires:  libpng
BuildRequires:  makeinfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mtools allows uncomplicated access to an MS-DOS file system on disk
without mounting it. It includes commands for working with MS-DOS
files: mdir, mcd, mcopy, and mformat.

XDF support for OS/2 is also provided.

%package doc
License:        GPL-3.0+ and GFDL-1.3
Summary:        Access Files on an MS-DOS File System
Group:          System/Filesystems
Requires:       %{name} = %{version}

%description doc
Mtools allows uncomplicated access to an MS-DOS file system on disk
without mounting it. It includes commands for working with MS-DOS
files: mdir, mcd, mcopy, and mformat.

XDF support for OS/2 is also provided.

%prep
%setup -q
%patch0
%patch1
%patch3
%patch4
%patch5

%build
autoconf --force
export CC=gcc
export INSTALL_PROGRAM="install"
%configure \
    --includedir=/usr/src/linux/include

%install
install -d -m 755 %{buildroot}%{_sysconfdir}
%make_install
cp -p mtools.conf %{buildroot}%{_sysconfdir}

rm -rf %{buildroot}%{_mandir}/man?*/f*
rm -rf %{buildroot}%{_bindir}/f*

%docs_package

%files
%defattr(-,root,root)
%config %{_sysconfdir}/mtools.conf
%{_bindir}/*


%changelog
