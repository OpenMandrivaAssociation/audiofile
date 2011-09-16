%define	name	audiofile
%define	version	0.3.0
%define	release	%mkrel 1
%define	lib_major 0
%define	lib_name %mklibname %{name} %{lib_major}

Summary:	Library to handle various audio file formats
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
Source0:	http://www.68k.org/~michael/audiofile/%{name}-%{version}.tar.gz
URL:		http://www.68k.org/~michael/audiofile/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  alsa-lib-devel

%description
The Silicon Graphics Audio File Library provides a uniform programming 
interface to standard digital audio file formats.

Currently supported sound file formats include AIFF/AIFF-C, WAVE, and
NeXT/Sun .snd/.au. Supported compression formats are currently G.711 
mu-law and A-law. 
Used by the esound daemon.

%package -n	%{lib_name}
Summary:	Main library for audiofile 
Group:		System/Libraries

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with audiofile.

%package -n	%{lib_name}-devel
Summary:	Includes and other files to develop audiofile applications
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	lib%{name}-devel = %{version}
Provides:	audiofile-devel = %{version}
Obsoletes:	audiofile-devel

%description -n	%{lib_name}-devel
Libraries, include files and other resources you can use to develop audiofile
applications.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --enable-largefile
%make CXX="g++ -w"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING README
%{_bindir}/sfconvert
%{_bindir}/sfinfo

%files -n %{lib_name}
%defattr(-, root, root)
%doc COPYING README
%{_libdir}/libaudiofile.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc COPYING README ACKNOWLEDGEMENTS TODO NEWS NOTES ChangeLog docs
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_mandir/man3/*
%_mandir/mant/*

