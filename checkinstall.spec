Summary:	CheckInstall installations tracker
Summary(pl):	Proste narzêdzie do tworzenia i zarzadzania pakietami (.tgz, .rpm, .deb)
Name:		checkinstall
Version:	1.5.1
Release:	2
License:	GPL
Group:		Development
Requires:	bash
Requires:	installwatch >= 0.6.3
Source0:	http://asic-linux.com.mx/~izto/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CheckInstall keeps track of all the files created or modified by your
installation script ("make install" "make install_modules", "setup",
etc), builds a standard binary package and installs it in your system
giving you the ability to uninstall it with your distribution's
standard package management utilities.

%description -l pl
Program do ¶ledzenia modyfikacji robionych przez skrypty instalacyjne
("make install", "setup", itp), potrafi zbudowaæ standartow± paczkê i
zainstalowaæ j± w twoim systemie z mo¿liwo¶ci± odinstalowania jej
narzêdziami dostêpnymi w twojej dystrybucji (obsluguje rpm, deb, tgz). 

%prep
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT%{_prefix}/{bin,sbin,lib/checkinstall} -p

sed -e "s|#\!/bin/sh|#\!/bin/bash|" < checkinstall > foo
sed -e "s|/usr/local|%{_prefix}|" < foo > checkinstall

install {checkinstall,makepak} $RPM_BUILD_ROOT%{_sbindir}
install checkinstallrc 	$RPM_BUILD_ROOT%{_libdir}/checkinstall
gzip -9nfr doc-pak/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc-pak
%attr(755,root,root) %{_sbindir}/checkinstall
%attr(755,root,root) %{_sbindir}/makepak
%config %{_libdir}/checkinstall/checkinstallrc
