Summary: 	Cuyo - a Tetris clone
Summary(pl):	Cuyo - klon Tetrisa
Name:		cuyo
Version:	1.6.0alpha5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.karimmi.de/%{name}/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Cuyo is an interesting Tetris clone.

%description -l pl
Cuyo to ciekawy klon Tetrisa.

%prep
%setup -q
%patch0 -p1

%build
aclocal -I .
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
#Could somebody help me to force automake using DESTDIR? //pascalek
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/pics
install -d $RPM_BUILD_ROOT/%{_mandir}/man6

cp src/%{name} $RPM_BUILD_ROOT/%{_bindir}
cp data/*.ld $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp data/pics/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/pics
cp docs/%{name}.6 $RPM_BUILD_ROOT/%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS TODO README docs/cual
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ld
%dir %{_datadir}/%{name}/pics
%{_datadir}/%{name}/pics/*
%{_mandir}/man6/*
