%define		iw_version	0.6.1
Summary:	CheckInstall installations tracker, version 1.4.1
Summary(pl):	Proste narzÍdzie do tworzenia i zarzadzania pakietami (.tgz, .rpm, .deb)
Name:		checkinstall
Version:	1.5.0
Release:	1
License:	GPL
Group:		Development
Group(de):	Entwicklung
Group(es):	Desarrollo
Group(pl):	Programowanie
Group(pt_BR):	Desenvolvimento
Group(ru):	Ú¡⁄“¡¬œ‘À¡
Group(uk):	Úœ⁄“œ¬À¡
Source0:	http://asic-linux.com.mx/~izto/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CheckInstall keeps track of all the files created or modified by your
installation script ("make install" "make install_modules", "setup",
etc), builds a standard binary package and installs it in your system
giving you the ability to uninstall it with your distribution's
standard package management utilities.

%description -l pl
Program do ∂ledzenia modyfikacji robionych przez skrypty instalacyjne
("make install", "setup", itp), potrafi zbudowaÊ standartow± paczkÍ i
zainstalowaÊ j± w twoim systemie z moøliwo∂ci± odinstalowania jej
narzÍdziami dostÍpnymi w twojej dystrybucji (obsluguje rpm, deb, tgz). 

%prep
%setup -q 

%build
%{__make} CC="gcc %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT%{_prefix}/{bin,sbin,lib/checkinstall} -p

install {checkinstall,makepak} $RPM_BUILD_ROOT%{_sbindir}
install checkinstallrc 	$RPM_BUILD_ROOT%{_libdir}/checkinstall
install installwatch-%{iw_version}/installwatch $RPM_BUILD_ROOT%{_bindir}
install installwatch-%{iw_version}/installwatch.so $RPM_BUILD_ROOT%{_libdir}
gzip -9nfr doc-pak/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/*
%doc doc-pak
