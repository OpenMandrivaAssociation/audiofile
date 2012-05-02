%define	major 1
%define	libname %mklibname %{name} %{major}
%define	libnamedev %mklibname %{name} -d

Summary:	Library to handle various audio file formats
Name:		audiofile
Version:	0.3.4
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/audiofile/%{name}-%{version}.tar.xz
URL:		http://www.68k.org/~michael/audiofile/
BuildRequires:  alsa-lib-devel

%description
The Silicon Graphics Audio File Library provides a uniform programming 
interface to standard digital audio file formats.

Currently supported sound file formats include AIFF/AIFF-C, WAVE, and
NeXT/Sun .snd/.au. Supported compression formats are currently G.711 
mu-law and A-law. 
Used by the esound daemon.

%package -n	%{libname}
Summary:	Main library for audiofile 
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with audiofile.

%package -n	%{libnamedev}
Summary:	Includes and other files to develop audiofile applications
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	audiofile-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n	%{libnamedev}
Libraries, include files and other resources you can use to develop audiofile
applications.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
    --enable-largefile \
    --disable-static
%make CXX="g++ -w"

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc COPYING README
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libaudiofile.so.%{major}*

%files -n %{libnamedev}
%doc COPYING README ACKNOWLEDGEMENTS TODO NEWS NOTES ChangeLog docs
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_mandir/man3/*
