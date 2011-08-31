Summary:	Newsbeuter - an RSS feed reader for the text console
Summary(hu.UTF-8):	Newsbeuter - egy RSS hírolvasó szöveges terminálra
Summary(pl.UTF-8):	Newsbeuter - czytnik RSS dla terminala tekstowego
Name:		newsbeuter
Version:	2.4
Release:	2
License:	MIT/X
Group:		Applications/Networking
Source0:	http://www.newsbeuter.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	67fd0d44a55e10ed1ba15b197262a35f
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

%build
CXXFLAGS="%{rpmcxxflags}" %{__make} \
	CXX="%{__cxx}" \
	REALLDFLAGS="%{rpmldflags}" \
	prefix=%{_prefix} \
	docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/es{_ES,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/zh{,_CN}
install AUTHORS README TODO $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install doc/*.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install doc/xhtml/*.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/podbeuter
%{_mandir}/man1/%{name}*
%{_mandir}/man1/podbeuter*
