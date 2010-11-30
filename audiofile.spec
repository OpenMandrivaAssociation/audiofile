%define	name	audiofile
%define	version	0.2.7
%define	release	%mkrel 2
%define	lib_major 0
%define	lib_name %mklibname %{name} %{lib_major}

Summary:	Library to handle various audio file formats
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
# (fc) 0.2.3-3mdk don't add -L/usr/lib to ldflags
Patch0:		audiofile-0.2.6-libdir.patch
# the debian patches comes from audiofile_0.2.6-8.diff.gz
Patch4:		10_pack_real_char3.dpatch
Patch8:		10_sfinfo_no_options.dpatch
Patch12:	10_include_audiofile_in_af_vfs.dpatch
Patch13:	10_pkgconfig_privlibs.dpatch
Patch14:	10_float_size_calculation_fix.dpatch
URL:		http://www.68k.org/~michael/audiofile/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

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
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc COPYING README ACKNOWLEDGEMENTS TODO NEWS NOTES ChangeLog docs
%{_bindir}/audiofile-config
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*


