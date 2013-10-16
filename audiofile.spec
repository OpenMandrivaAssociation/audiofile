%define	url_ver %(echo %{version}|cut -d. -f1,2)

%define	major 1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Library to handle various audio file formats
Name:		audiofile
Version:	0.3.6
Release:	3
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://www.68k.org/~michael/audiofile/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/audiofile/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(flac)

%description
The Silicon Graphics Audio File Library provides a uniform programming
interface to standard digital audio file formats.

Currently supported sound file formats include AIFF/AIFF-C, WAVE, and
NeXT/Sun .snd/.au. Supported compression formats are currently G.711
mu-law and A-law.

Used by the esound daemon.

%files
%doc COPYING README
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_mandir}/man1/*

#------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Main library for audiofile 
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with audiofile.

%files -n %{libname}
%{_libdir}/libaudiofile.so.%{major}*

#------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Includes and other files to develop audiofile applications
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}audiofile0-devel < 0.3.4

%description -n	%{devname}
Libraries, include files and other resources you can use to develop audiofile
applications.

%files -n %{devname}
%doc COPYING README ACKNOWLEDGEMENTS TODO NEWS NOTES ChangeLog docs
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

#------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--enable-largefile \
	--disable-static

%make CXX="%{__cxx} -w"

%install
%makeinstall_std

