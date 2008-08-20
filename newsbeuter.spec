# TODO: optflags
Summary:	Newsbeuter - an RSS feed reader for the text console
Summary(pl.UTF-8):	Newsbeuter - czytnik RSS dla terminala tekstowego
Name:		newsbeuter
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.newsbeuter.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	3521c20b3540b62c414d9e10b48c95ed
URL:		http://www.newsbeuter.org/
BuildRequires:	gettext-devel
BuildRequires:	libmrss-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	sqlite3-devel
BuildRequires:	stfl-devel >=0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	_sysconfdir	%{_sysconfdir}/X11}

%description
Newsbeuter is an RSS feedreader. Newsbeuter is designed to be used 
on text terminals on Unix or Unix-like systems.

%description -l pl.UTF-8
Newsbeuter to czytnik RSS przeznaczony do używania na terminalach
tekstowych w systemach uniksowych.

%prep
%setup -q

%build
%{__make} \
	prefix=%{_prefix} \
	docdir=%{_defaultdocdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	docdir=$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README 
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/podbeuter
%{_mandir}/man1/%{name}*
%{_mandir}/man1/podbeuter*
