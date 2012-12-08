%define	major 1
%define	libname %mklibname %{name} %{major}
%define	libnamedev %mklibname %{name} -d

Summary:	Library to handle various audio file formats
Name:		audiofile
Version:	0.3.4
Release:	3
License:	LGPLv2+
Group:		System/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/audiofile/%{name}-%{version}.tar.xz
URL:		http://www.68k.org/~michael/audiofile/
BuildRequires:	pkgconfig(alsa)

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
Obsoletes:	%{_lib}audiofile0-devel < 0.3.4

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
%makeinstall_std

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
%{_mandir}/man3/*


%changelog
* Wed May 02 2012 Götz Waschk <waschk@mandriva.org> 0.3.4-1
+ Revision: 794977
- update build deps
- update to new version 0.3.4

* Thu Jan 12 2012 Götz Waschk <waschk@mandriva.org> 0.3.3-1
+ Revision: 760264
- new version
- new major
- drop patch

* Tue Dec 06 2011 Zé <ze@mandriva.org> 0.3.2-2
+ Revision: 738407
- forgot to remove .la files
- clean defattr, BR, clean section and mkrel
- clean static and .la files
- move doc from lib package
- requires and provides
- rename no longer needed

* Wed Nov 30 2011 Götz Waschk <waschk@mandriva.org> 0.3.2-1
+ Revision: 735539
- fix linking
- update to new version 0.3.2

* Sun Sep 18 2011 Götz Waschk <waschk@mandriva.org> 0.3.1-1
+ Revision: 700226
- xz tarball
- new version
- update file list

* Fri Sep 16 2011 Götz Waschk <waschk@mandriva.org> 0.3.0-1
+ Revision: 699965
- new version
- new source URL
- drop patches
- update file list
- fix build

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-3
+ Revision: 662890
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-2mdv2011.0
+ Revision: 603479
- rebuild

* Wed Apr 28 2010 Götz Waschk <waschk@mandriva.org> 0.2.7-1mdv2010.1
+ Revision: 540157
- new version
- drop old patches
- update license

* Wed Jan 13 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.6-15mdv2010.1
+ Revision: 490980
- synch debian patches from audiofile_0.2.6-8.diff.gz

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2.6-14mdv2010.0
+ Revision: 413125
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.2.6-13mdv2009.1
+ Revision: 350135
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.2.6-12mdv2009.0
+ Revision: 220468
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 18 2007 Frederic Crozat <fcrozat@mandriva.com> 0.2.6-10mdv2008.0
+ Revision: 89524
- Rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags


* Wed Feb 28 2007 Götz Waschk <waschk@mandriva.org> 0.2.6-8mdv2007.0
+ Revision: 126864
- rebuild for pkgconfig provides

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 0.2.6-7mdv2007.1
+ Revision: 108676
- Import audiofile

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 0.2.6-7mdv2007.1
- unpack patches

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 0.2.6-6mdk
- rebuild for sparc

* Tue Jan 24 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.6-5mdk
- fix underquoted calls (P1 from fedora)
- %%mkrel
- cosmetics

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.2.6-4mdk
- Rebuild

* Thu Feb 24 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.2.6-3mdk
- cleanup patch0 (libdir) to make audiofile-config arch-independent

* Fri Apr 23 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.2.6-2mdk
- Fix package URL (no longer SGI)

* Fri Apr 23 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.6-1mdk
- fix source URL
- New release 0.2.6

