Summary:	CheckInstall installations tracker
Summary(pl):	Proste narzêdzie do tworzenia i zarz±dzania pakietami (.tgz, .rpm, .deb)
Name:		checkinstall
Version:	1.6.0
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://asic-linux.com.mx/~izto/checkinstall/files/source/%{name}-%{version}.tgz
# Source0-md5:	41c1be61199406edf2e3ee92f2007fe5
URL:		http://asic-linux.com.mx/~izto/checkinstall/
BuildRequires:	sed >= 4.0
Requires:	bash
Requires:	installwatch >= 0.6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CheckInstall keeps track of all the files created or modified by your
installation script ("make install" "make install_modules", "setup",
etc), builds a standard binary package and installs it in your system
giving you the ability to uninstall it with your distribution's
standard package management utilities.

%description -l pl
Program do ¶ledzenia modyfikacji robionych przez skrypty instalacyjne
("make install", "setup", itp), potrafi zbudowaæ standardow± paczkê i
zainstalowaæ j± w twoim systemie z mo¿liwo¶ci± odinstalowania jej
narzêdziami dostêpnymi w twojej dystrybucji (obs³uguje rpm, deb, tgz).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/checkinstall}

%{__sed} -i "s|#\!/bin/sh|#\!/bin/bash|" checkinstall
%{__sed} -i "s|/usr/local|%{_prefix}|" checkinstall{,rc-dist}

install {checkinstall,makepak} $RPM_BUILD_ROOT%{_sbindir}
install checkinstallrc-dist $RPM_BUILD_ROOT%{_libdir}/checkinstall/checkinstallrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS Changelog FAQ NLS_SUPPORT README RELNOTES TODO
%attr(755,root,root) %{_sbindir}/checkinstall
%attr(755,root,root) %{_sbindir}/makepak
%config %{_libdir}/checkinstall/checkinstallrc
