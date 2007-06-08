# TODO:
# - gimp plugin
#
Summary:	Raw Digital Photo Decoder
Summary(pl.UTF-8):	Dekoder zdjęć cyfrowych w formacie raw
Name:		dcraw
Version:	8.74
Epoch:		1
Release:	1
License:	Free + GPL (for some parts of code)
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
# NoSource0-md5:	bab97be8718fcddfb9beb0fff2438b18
Source1:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.1
# NoSource1-md5:	cecee38561cef4cf83726b38da8fd85d
Source2:	http://www.cybercom.net/~dcoffin/dcraw/clean_crw.c
# NoSource2-md5:	37b386fef86eef8768965e91ea0be9e6
Source3:	http://www.cybercom.net/~dcoffin/dcraw/fujiturn.c
# NoSource3-md5:	10e468e0eed5e772fb09f3b2590696f1
Source4:	http://www.cybercom.net/~dcoffin/dcraw/fuji_green.c
# NoSource4-md5:	e801331242f2acf805c0ce00f609fe8c
URL:		http://www.cybercom.net/~dcoffin/dcraw/
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dcraw is a program that decodes any raw image from digital cameras and
produces portable pixel map (PPM).

%description -l pl.UTF-8
Dcraw jest programem, który dekoduje zdjęcia z aparatów cyfrowych
zapisanych w formacie raw i produkuje przenośną mapę pikseli (PPM).

%prep
%setup -qcT
cp %{SOURCE0} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .

%build
%{__cc} %{rpmldflags} -o dcraw %{rpmcflags} dcraw.c -lm -ljpeg -llcms
%{__cc} %{rpmldflags} -o clean_crw %{rpmcflags} clean_crw.c
%{__cc} %{rpmldflags} -o fujiturn %{rpmcflags} fujiturn.c -D_16BIT
%{__cc} %{rpmldflags} -o fuji_green %{rpmcflags} fuji_green.c -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dcraw clean_crw fujiturn fuji_green $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
