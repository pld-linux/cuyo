Summary:	Cuyo - a Tetris clone
Summary(pl):	Cuyo - klon Tetrisa
Name:		cuyo
Version:	1.7.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e87f7a31df451fd5a674124b656e91fe
Patch0:		%{name}-make.patch
Patch1:		%{name}-no_pedantic.patch
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
rm -f missing
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
for i in src/*.moc.cpp; do
	rm -f $i;
	moc ${i%.moc.cpp}.h > $i
done
%{__make}

%install
#Could somebody help me to force automake using DESTDIR? //pascalek
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/pics,%{_mandir}/man6}

cp src/%{name} $RPM_BUILD_ROOT%{_bindir}
cp data/*.ld $RPM_BUILD_ROOT%{_datadir}/%{name}
cp data/pics/* $RPM_BUILD_ROOT%{_datadir}/%{name}/pics
cp docs/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

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
