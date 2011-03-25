Summary:	C++ wrappers for GooCanvas library
Summary(pl.UTF-8):	Interfejsy C++ dla biblioteki GooCanvas
Name:		goocanvasmm
Version:	0.15.4
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goocanvasmm/0.15/%{name}-%{version}.tar.bz2
# Source0-md5:	cf462e8d2f36f4e02387eb094773b3e9
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.9
BuildRequires:	doxygen
BuildRequires:	glibmm-devel >= 2.14.2
BuildRequires:	goocanvas-devel >= 0.15
BuildRequires:	gtkmm-devel >= 2.22.0
BuildRequires:	mm-common >= 0.7.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	goocanvas >= 0.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for GooCanvas library.

%description -l pl.UTF-8
Interfejsy C++ dla biblioteki GooCanvas.

%package devel
Summary:	Header files for goocanvasmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki goocanvasmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	goocanvas-devel >= 0.15
Requires:	gtkmm-devel >= 2.22.0

%description devel
Header files for goocanvasmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki goocanvasmm.

%package static
Summary:	Static goocanvasmm library
Summary(pl.UTF-8):	Statyczna biblioteka goocanvasmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static goocanvasmm library.

%description static -l pl.UTF-8
Statyczna biblioteka goocanvasmm.

%package apidocs
Summary:	goocanvasmm API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki goocanvasmm
Group:		Documentation

%description apidocs
API documentation for goocanvasmm library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki goocanvasmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgoocanvasmm-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoocanvasmm-1.0.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoocanvasmm-1.0.so
%{_libdir}/goocanvasmm-1.0
%{_includedir}/goocanvasmm-1.0
%{_pkgconfigdir}/goocanvasmm-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgoocanvasmm-1.0.a

%files apidocs
%defattr(644,root,root,755)
# it can't be compressed
%{_docdir}/goocanvasmm-1.0
%{_datadir}/devhelp/books/goocanvasmm-1.0
