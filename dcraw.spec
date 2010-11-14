# TODO:
# - gimp plugin ?

Summary:	Raw Digital Photo Decoder
Summary(pl.UTF-8):	Dekoder zdjęć cyfrowych w formacie raw
Name:		dcraw
Version:	9.05
Release:	1
Epoch:		1
License:	Free + GPL v2+ (for some parts of code)
Group:		Applications/Graphics
Source0:	http://www.cybercom.net/~dcoffin/dcraw/archive/%{name}-%{version}.tar.gz
# Source0-md5:	b06ad99909ede5f1a129fa4b53d32e04
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
Dcraw jest programem, który dekoduje zapisane w formacie surowym (raw)
zdjęcia z aparatów cyfrowych i tworzy z nich pliki w formacie PPM 
(Portable Pixel Map - przenośna mapa pikseli).

%prep
%setup -q -n %{name}
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .

%build
%{__cc} %{rpmldflags} -o dcraw/dcraw %{rpmcflags} -Wall -DLOCALEDIR=\"%{_datadir}/locale/\" dcraw/dcraw.c -lm -ljpeg -llcms
%{__cc} %{rpmldflags} -o clean_crw %{rpmcflags} -Wall clean_crw.c
%{__cc} %{rpmldflags} -o fujiturn %{rpmcflags} -Wall fujiturn.c -D_16BIT
%{__cc} %{rpmldflags} -o fuji_green %{rpmcflags} -Wall fuji_green.c -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dcraw/dcraw clean_crw fujiturn fuji_green $RPM_BUILD_ROOT%{_bindir}
install dcraw.1 $RPM_BUILD_ROOT%{_mandir}/man1

for lpo in dcraw_*.po ; do
	bname=$(basename $lpo .po)
	lang=${bname#dcraw_}
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	msgfmt -o $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/dcraw.mo $lpo
done
for lman in dcraw_*.1 ; do
	bname=$(basename $lman .1)
	lang=${bname#dcraw_}
	install -d $RPM_BUILD_ROOT%{_mandir}/$lang/man1
	cp -p $lman $RPM_BUILD_ROOT%{_mandir}/$lang/man1/dcraw.1
done
	
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcraw
%attr(755,root,root) %{_bindir}/clean_crw
%attr(755,root,root) %{_bindir}/fujiturn
%attr(755,root,root) %{_bindir}/fuji_green
%{_mandir}/man1/dcraw.1*
%lang(ca) %{_mandir}/ca/man1/dcraw.1*
%lang(cs) %{_mandir}/cs/man1/dcraw.1*
%lang(cs) %{_mandir}/da/man1/dcraw.1*
%lang(de) %{_mandir}/de/man1/dcraw.1*
%lang(eo) %{_mandir}/eo/man1/dcraw.1*
%lang(es) %{_mandir}/es/man1/dcraw.1*
%lang(fr) %{_mandir}/fr/man1/dcraw.1*
%lang(hu) %{_mandir}/hu/man1/dcraw.1*
%lang(it) %{_mandir}/it/man1/dcraw.1*
%lang(pl) %{_mandir}/pl/man1/dcraw.1*
%lang(pt) %{_mandir}/pt/man1/dcraw.1*
%lang(ru) %{_mandir}/ru/man1/dcraw.1*
%lang(sv) %{_mandir}/sv/man1/dcraw.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/dcraw.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/dcraw.1*
