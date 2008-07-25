Summary:	Newsbeuter is an RSS feed reader for the text console.
Name:		newsbeuter
Version:	0.9.1
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://synflood.at/newsbeuter/%{name}-%{version}.tar.gz
# Source0-md5:	58f688dd305ed46d3a837897ff04c049
URL:		http://synflood.at/newsbeuter.html
BuildRequires:	sqlite3-devel
BuildRequires:	libmrss-devel
BuildRequires:	ncurses-devel
BuildRequires:	gettext-devel
BuildRequires:	gcc-c++
BuildRequires:	stfl-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	_sysconfdir	%{_sysconfdir}/X11}
%define _myprefix /usr
%define _mydocdir %{_prefix}/share/doc/%{name}-%{version}
%description
Newsbeuter is an RSS feedreader. Newsbeuter is designed to be used 
on text terminals on Unix or Unix-like systems.

%prep
%setup -q
#%patch0 -p1

%build

%{__make} prefix=%{_myprefix} docdir=%{_mydocdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install prefix=$RPM_BUILD_ROOT%{_myprefix}\
	docdir=$RPM_BUILD_ROOT%{_mydocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README 
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/podbeuter
%{_mandir}/man1/%{name}*
%{_mandir}/man1/podbeuter*
