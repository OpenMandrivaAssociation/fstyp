%define name   fstyp
%define version 0.1
%define release %mkrel 7

Name: %name
Version: %version
Release: %release
Summary: A filesystem type identifier
Source: http://mkp.net/fstyp/%{name}-0.1.tar.gz
URL:    https://mkp.net/fstyp
Group:  File tools 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL

%description
Utility to heuristically determine filesystem type of a partition.

%prep
%setup -q
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/sbin
make install DESTDIR=$RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/fstyp
%{_mandir}/man8/fstyp.*

