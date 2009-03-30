# TODO:
# - gimp plugin
#
Summary:	Raw Digital Photo Decoder
Summary(pl.UTF-8):	Dekoder zdjęć cyfrowych w formacie raw
Name:		dcraw
Version:	8.93
Epoch:		1
Release:	1
License:	Free + GPL (for some parts of code)
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/archive/%{name}-%{version}.tar.gz
# Source0-md5:	1ca10ba4be66962f976163c294e58579
Source1:	http://www.cybercom.net/~dcoffin/dcraw/clean_crw.c
# NoSource1-md5:	37b386fef86eef8768965e91ea0be9e6
Source2:	http://www.cybercom.net/~dcoffin/dcraw/fujiturn.c
# NoSource2-md5:	10e468e0eed5e772fb09f3b2590696f1
Source3:	http://www.cybercom.net/~dcoffin/dcraw/fuji_green.c
# NoSource3-md5:	e801331242f2acf805c0ce00f609fe8c
URL:		http://www.cybercom.net/~dcoffin/dcraw/
BuildRequires:	gettext-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
Requires:	FHS > 2.3-18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dcraw is a program that decodes any raw image from digital cameras and
produces portable pixel map (PPM).

%description -l pl.UTF-8
Dcraw jest programem, który dekoduje zdjęcia z aparatów cyfrowych
zapisanych w formacie raw i produkuje przenośną mapę pikseli (PPM).

%prep
%setup -q -n %{name}
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .

%build
%{__cc} %{rpmldflags} -o dcraw %{rpmcflags} -Wall -DLOCALEDIR=\"%{_datadir}/locale/\" dcraw.c -lm -ljpeg -llcms
%{__cc} %{rpmldflags} -o clean_crw %{rpmcflags} -Wall clean_crw.c
%{__cc} %{rpmldflags} -o fujiturn %{rpmcflags} -Wall fujiturn.c -D_16BIT
%{__cc} %{rpmldflags} -o fuji_green %{rpmcflags} -Wall fuji_green.c -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dcraw clean_crw fujiturn fuji_green $RPM_BUILD_ROOT%{_bindir}
install dcraw.1 $RPM_BUILD_ROOT%{_mandir}/man1

# Some fancy way for making this list automagically is needed, maybe:
for lang in ca cs de eo es fr hu it pl pt ru sv zh_TW ; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$lang/man1
	cp dcraw_$lang.1 $RPM_BUILD_ROOT%{_mandir}/$lang/man1/dcraw.1
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	msgfmt -o $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/dcraw.mo dcraw_$lang.po
done

# For this language there is only manual:
for lang in zh_CN; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$lang/man1
	cp dcraw_$lang.1 $RPM_BUILD_ROOT%{_mandir}/$lang/man1/dcraw.1
done
# For this language there is only translation:
for lang in nl; do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	msgfmt -o $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/dcraw.mo dcraw_$lang.po
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(ca) %{_mandir}/ca/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(eo) %{_mandir}/eo/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(pt) %{_mandir}/pt/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(sv) %{_mandir}/sv/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
%lang(zh_TW) %{_mandir}/zh_TW/man1/*
