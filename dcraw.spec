# TODO:
# - gimp plugin
#
Summary:	Raw Digital Photo Decoder
Summary(pl.UTF-8):	Dekoder zdjęć cyfrowych w formacie raw
Name:		dcraw
Version:	8.74
Epoch:		1
Release:	0.2
License:	Free + GPL (for some parts of code)
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/archive/%{name}-%{version}.tar.gz
# Source0-md5:	c7db9ea7c7574f2c39ee24c5ae2f2565
####Source0:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
#Source1:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.1# NoSource1-md5:	cecee38561cef4cf83726b38da8fd85d
Source2:	http://www.cybercom.net/~dcoffin/dcraw/clean_crw.c
# NoSource2-md5:	37b386fef86eef8768965e91ea0be9e6
Source3:	http://www.cybercom.net/~dcoffin/dcraw/fujiturn.c
# NoSource3-md5:	bc4a56184a338f6c181b19535ba328a0
Source4:	http://www.cybercom.net/~dcoffin/dcraw/fuji_green.c
# NoSource4-md5:	25c05a032d3eaf094b30b5b85feca78f
URL:		http://www.cybercom.net/~dcoffin/dcraw/
BuildRequires:	gettext-devel
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
#%setup -qcT
%setup -q -n %{name}
#cp %{SOURCE0} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .

%build
#FIXME
#%{__cc} %{rpmldflags} -o dcraw %{rpmcflags} -Wall -DLOCALEDIR="%{_datadir}/locale/" dcraw.c -lm -ljpeg -llcms
#%{__cc} %{rpmldflags} -o clean_crw %{rpmcflags} -Wall -DLOCALEDIR="%{_datadir}/locale/" clean_crw.c
#%{__cc} %{rpmldflags} -o fujiturn %{rpmcflags} -Wall -DLOCALEDIR="%{_datadir}/locale/" fujiturn.c -D_16BIT
#%{__cc} %{rpmldflags} -o fuji_green %{rpmcflags} -Wall -DLOCALEDIR="%{_datadir}/locale/" fuji_green.c -lm
%{__cc} %{rpmldflags} -o dcraw %{rpmcflags} -Wall dcraw.c -lm -ljpeg -llcms
%{__cc} %{rpmldflags} -o clean_crw %{rpmcflags} -Wall clean_crw.c
%{__cc} %{rpmldflags} -o fujiturn %{rpmcflags} -Wall fujiturn.c -D_16BIT
%{__cc} %{rpmldflags} -o fuji_green %{rpmcflags} -Wall fuji_green.c -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dcraw clean_crw fujiturn fuji_green $RPM_BUILD_ROOT%{_bindir}

# Some fancy way for making this list automagically is needed, maybe:
for lang in eo ru fr it de pt es zh_TW zh_CN nl pl hu; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$lang/man1
	cp dcraw_$lang.1 $RPM_BUILD_ROOT%{_mandir}/$lang/man1/dcraw.1
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	msgfmt -o $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/dcraw.mo dcraw_$lang.po
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
