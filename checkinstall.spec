Summary:	CheckInstall installations tracker
Summary(pl.UTF-8):	Proste narzędzie do tworzenia i zarządzania pakietami (.tgz, .rpm, .deb)
Name:		checkinstall
Version:	1.6.1
Release:	1
License:	GPL v2
Group:		Base/Utilities
Source0:	http://asic-linux.com.mx/~izto/checkinstall/files/source/%{name}-%{version}.tgz
# Source0-md5:	1ae49645d6d16efac79ac67b84bfb419
URL:		http://asic-linux.com.mx/~izto/checkinstall/
BuildRequires:	sed >= 4.0
Requires:	bash
Requires:	installwatch >= 0.6.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CheckInstall keeps track of all the files created or modified by your
installation script ("make install" "make install_modules", "setup",
etc), builds a standard binary package and installs it in your system
giving you the ability to uninstall it with your distribution's
standard package management utilities.

%description -l pl.UTF-8
Program do śledzenia modyfikacji robionych przez skrypty instalacyjne
("make install", "setup", itp), potrafi zbudować standardową paczkę i
zainstalować ją w twoim systemie z możliwością odinstalowania jej
narzędziami dostępnymi w twojej dystrybucji (obsługuje rpm, deb, tgz).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}

%{__sed} -i "s|#\!/bin/sh|#\!/bin/bash|" checkinstall
%{__sed} -i "s|/usr/local|%{_prefix}|" checkinstall{,rc-dist}
%{__sed} -i "s|/usr/lib/checkinstall/checkinstallrc|%{_sysconfdir}/checkinstallrc|g" checkinstall

install checkinstall makepak $RPM_BUILD_ROOT%{_sbindir}
install checkinstallrc-dist $RPM_BUILD_ROOT%{_sysconfdir}/checkinstallrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS Changelog FAQ NLS_SUPPORT README RELNOTES TODO
%attr(755,root,root) %{_sbindir}/checkinstall
%attr(755,root,root) %{_sbindir}/makepak
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/checkinstallrc
