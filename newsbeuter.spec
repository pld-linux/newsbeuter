Summary:	Newsbeuter is an RSS feed reader for the text console.
Name:		newsbeuter
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.newsbeuter.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	3521c20b3540b62c414d9e10b48c95ed
URL:		http://www.newsbeuter.org
BuildRequires:	sqlite3-devel
BuildRequires:	libmrss-devel
BuildRequires:	ncurses-devel
BuildRequires:	gettext-devel
BuildRequires:	gcc-c++
BuildRequires:	stfl-devel >=0.19
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
