Summary:	Cuyo - a Tetris clone
Summary(pl):	Cuyo - klon Tetrisa
Name:		cuyo
Version:	1.8.5
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/cuyo/%{name}-%{version}.tar.gz
# Source0-md5:	9c250217ab90baeb993a238b9b98f63f
Patch0:		%{name}-make.patch
Patch1:		%{name}-qt.patch
URL:		http://www.karimmi.de/cuyo/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cuyo is an interesting Tetris clone.

%description -l pl
Cuyo to ciekawy klon Tetrisa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	QTDIR=%{_prefix}
for i in src/{cuyo,prefs,punktefeld,spielfeld,startatdlg,tastenbtn,sound}.h; do
	moc $i > ${i%.h}.moc.cpp
done
%{__make} \
	CPPFLAGS=-I/usr/include/qt \
	%{!?debug:CXXDBGFLAGS="-DQT_NO_DEBUG -DQT_NO_CHECK %{rpmcflags}"} \
	%{?debug:CXXDBGFLAGS="%{debugcflags}"}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gamesdir=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ld
%dir %{_datadir}/%{name}/pics
%{_datadir}/%{name}/pics/*
%{_mandir}/man6/*
