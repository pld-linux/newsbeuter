Summary:	Newsbeuter - an RSS feed reader for the text console
Summary(hu.UTF-8):	Newsbeuter - egy RSS hírolvasó szöveges terminálra
Summary(pl.UTF-8):	Newsbeuter - czytnik RSS dla terminala tekstowego
Name:		newsbeuter
Version:	2.9
Release:	4
License:	MIT/X
Group:		Applications/Networking
#Source0Download: https://www.newsbeuter.org/download.html
Source0:	https://www.newsbeuter.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	9cf332dc7e591023147bda7add430835
Patch0:		%{name}-json_c.patch
URL:		https://www.newsbeuter.org/
BuildRequires:	curl-devel
BuildRequires:	gettext-tools
BuildRequires:	json-c-devel >= 0.11
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libxml2-devel >= 2
BuildRequires:	ncurses-devel >= 6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	stfl-devel >= 0.21-4
Requires:	json-c >= 0.11
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
%patch -P0 -p1

%{__sed} -i "s@ncursesw5@ncursesw6@g" config.sh

%build
CXXFLAGS="%{rpmcxxflags}" \
%{__make} \
	CXX="%{__cxx}" \
	REALLDFLAGS="%{rpmldflags}" \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/zh{,_CN}
# less up-to-date version of es
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/es_ES

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README TODO doc/*.txt doc/xhtml/*.html doc/example-config
%attr(755,root,root) %{_bindir}/newsbeuter
%attr(755,root,root) %{_bindir}/podbeuter
%{_mandir}/man1/newsbeuter.1*
%{_mandir}/man1/podbeuter.1*
