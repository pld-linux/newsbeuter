# TODO: optflags
Summary:	Newsbeuter - an RSS feed reader for the text console
Summary(hu.UTF-8):	Newsbeuter - egy RSS hírolvasó szöveges terminálra
Summary(pl.UTF-8):	Newsbeuter - czytnik RSS dla terminala tekstowego
Name:		newsbeuter
Version:	1.3
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.newsbeuter.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	7246e37ed0067ab55803be4b1d144c50
URL:		http://www.newsbeuter.org/
BuildRequires:	gettext-devel
BuildRequires:	libmrss-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	sqlite3-devel
BuildRequires:	stfl-devel >=0.19
BuildRequires:  stfl-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	_sysconfdir	%{_sysconfdir}/X11}

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
%{__make} \
	prefix=%{_prefix} \
	docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/podbeuter
%{_mandir}/man1/%{name}*
%{_mandir}/man1/podbeuter*
