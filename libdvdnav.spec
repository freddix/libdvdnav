Summary:	DVD menu support library
Name:		libdvdnav
Version:	5.0.1
Release:	1
License:	GPL
Group:		Libraries
#
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.xz
# Source0-md5:	19a9e91198c957a9c0fc85122556f99a
URL:		http://dvdnav.mplayerhq.hu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel >= 5.0.0
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVD menu support library.

%package devel
Summary:	Development files for libdvdnav
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdvdread-devel >= 5.0.0

%description devel
Development files for libdvdnav.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/dvdnav
%{_pkgconfigdir}/*.pc

