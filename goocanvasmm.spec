Summary:	C++ wrappers for GooCanvas library
Summary(pl.UTF-8):	Interfejsy C++ dla GooCanvas library
Name:		goocanvasmm
Version:	0.13.0
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goocanvasmm/0.13/%{name}-%{version}.tar.bz2
# Source0-md5:	c25c567f95af4619b0af0124251b3c39
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	glibmm-devel >= 2.14.2
BuildRequires:	goocanvas-devel >= 0.13
BuildRequires:	gtkmm-devel >= 2.12.0
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
Requires:	goocanvas-devel >= 0.13
Requires:	gtkmm-devel >= 2.12.0

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
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-apidocs-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# build API documentation
cd docs/reference/
doxygen
cp html/* $RPM_BUILD_ROOT%{_docdir}/%{name}-apidocs-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgoocanvasmm-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoocanvasmm-0.1.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoocanvasmm-0.1.so
%{_libdir}/libgoocanvasmm-0.1.la
%{_libdir}/goocanvasmm-0.1
%{_includedir}/goocanvasmm-0.1
%{_pkgconfigdir}/goocanvasmm-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgoocanvasmm-0.1.a

%files apidocs
%defattr(644,root,root,755)
# it can't be compressed
%{_docdir}/%{name}-apidocs-%{version}
