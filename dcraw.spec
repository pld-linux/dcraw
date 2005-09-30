Summary:	Raw Digital Photo Decoder
Summary(pl):	Dekoder zdjêæ cyfrowych w formacie raw
Name:		dcraw
Version:	20050925
Release:	1
License:	Free + GPL (for some parts of code)
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
# NoSource0-md5:	77ed8b203478b774b18f319a48e1c482
Source1:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.1
# NoSource1-md5:	fc808b590e4d8430eb5c726d43b4b0e9
URL:		http://www.cybercom.net/~dcoffin/dcraw/
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
%{__cc} %{rpmldflags} -o dcraw %{rpmcflags} dcraw.c -lm -ljpeg

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
