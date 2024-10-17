Summary:	Logical Disk Manager (Dynamic Disk) Tool
Name:		linux-ldm
Version:	0.0.8
%define	docver	0.2
Release:	%mkrel 5
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://prdownloads.sf.net/linux-ntfs/%name-%version.tar.bz2
Source1:	http://prdownloads.sf.net/linux-ntfs/ldmdoc-%{docver}.tar.bz2
URL:		https://linux-ntfs.sf.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%_tmppath/%name-%version

%description
Utility to dump or get information about LDM partitions (Windows
2000/XP "dynamic disks").

Contains LDM documentation.

%prep
%setup -q -a1

%build
%make -C ldmutil
mv -f ldmutil/README README.ldmutil

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install test/ldminfo ldmutil/ldmutil $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* ldmdoc
%attr(755,root,root) %{_bindir}/*
