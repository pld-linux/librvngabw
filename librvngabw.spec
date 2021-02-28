#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Library for generating documents in AbiWord (ABW) format
Summary(pl.UTF-8):	Biblioteka do generowania dokumentów w formacie AbiWorda (ABW)
Name:		librvngabw
Version:	0.0.2
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/librvngabw/%{name}-%{version}.tar.xz
# Source0-md5:	a7bb0b7d0bebf4e7a1cdcc15cf79936a
URL:		http://librvngabw.sourceforge.net/
BuildRequires:	doxygen
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librvngabw is a library for generating documents in AbiWord (ABW)
format. It provides generator implementations for text document
interfaces supported by librevenge.

%description -l pl.UTF-8
librvngabw to biblioteka do generowania dokumentów w formacie AbiWorda
(ABW). Zawiera implementacje generatorów dla interfejsów dokumentów
tekstowych obsługiwanych przez librevenge.

%package devel
Summary:	Header files for librvngabw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki librvngabw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for librvngabw library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki librvngabw.

%package static
Summary:	Static librvngabw library
Summary(pl.UTF-8):	Statyczna biblioteka librvngabw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librvngabw library.

%description static -l pl.UTF-8
Statyczna biblioteka librvngabw.

%package apidocs
Summary:	librvngabw API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki librvngabw
Group:		Documentation
BuildArch:	noarch

%description apidocs
librvngabw API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki librvngabw.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules \
	--disable-werror
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librvngabw-*.la
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/librvngabw

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/librvngabw-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librvngabw-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librvngabw-0.0.so
%{_includedir}/librvngabw-0.0
%{_pkgconfigdir}/librvngabw-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/librvngabw-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*
