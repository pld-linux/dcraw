Summary:	Raw Digital Photo Decoder
Summary(pl):	Dekoder zdjêæ cyfrowych w formacie raw
Name:		dcraw
Version:	20051106
Release:	1
License:	Free + GPL (for some parts of code)
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
# NoSource0-md5:	9db410a5c542f75dabd47f1df13170b2
Source1:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.1
# NoSource1-md5:	9c091d19e6c4cc2d42b1b5624caf9dc5
URL:		http://www.cybercom.net/~dcoffin/dcraw/
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dcraw is a program that decodes any raw image from digital cameras and
produces portable pixel map (PPM).

%description -l pl
Dcraw jest programem, który dekoduje zdjêcia z aparatów cyfrowych
zapisanych w formacie raw i produkuje przeno¶n± mapê pikseli (PPM).

%prep
%setup -qcT
cp %{SOURCE0} .

%build
%{__cc} %{rpmldflags} -o dcraw %{rpmcflags} dcraw.c -lm -ljpeg -llcms

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dcraw $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
