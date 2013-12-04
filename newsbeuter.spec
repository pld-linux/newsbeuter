Summary:	Newsbeuter - an RSS feed reader for the text console
Summary(hu.UTF-8):	Newsbeuter - egy RSS hírolvasó szöveges terminálra
Summary(pl.UTF-8):	Newsbeuter - czytnik RSS dla terminala tekstowego
Name:		newsbeuter
Version:	2.7
Release:	2
License:	MIT/X
Group:		Applications/Networking
Source0:	http://www.newsbeuter.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	cc8d43e8957875608d3b77679f437af6
URL:		http://www.newsbeuter.org/
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	stfl-devel >= 0.21-4
Suggests:	wwwbrowser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newsbeuter is an RSS feedreader. Newsbeuter is designed to be used on
text terminals on Unix or Unix-like systems.

%description -l hu.UTF-8
Newsbeuter egy RSS hírolvasó, amely szöveges terminálokon való
használatra készült.

%description -l pl.UTF-8
Newsbeuter to czytnik RSS przeznaczony do używania na terminalach
tekstowych w systemach uniksowych.

%prep
%setup -q
%{__sed} -i "s@ncursesw5@ncursesw6@g" config.sh

%build
CXXFLAGS="%{rpmcxxflags}" %{__make} \
	CXX="%{__cxx}" \
	REALLDFLAGS="%{rpmldflags}" \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/zh{,_CN}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/es_ES
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO doc/*.txt doc/xhtml/*.html doc/example-config
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/podbeuter
%{_mandir}/man1/%{name}*
%{_mandir}/man1/podbeuter*
