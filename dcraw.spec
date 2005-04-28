Summary:	Raw Digital Photo Decoder
Summary(pl):	Dekoder zdjêæ cyfrowych w formacie raw
Name:		dcraw
Version:	20050428
Release:	1
License:	Free
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
# NoSource0-md5:	2fc0584127c3746debba941273f8b417
Source1:	http://www.cybercom.net/~dcoffin/dcraw/dcraw.1
# NoSource1-md5:	0edfe10acf69c93724e271646ae79df5
URL:		http://www.cybercom.net/~dcoffin/dcraw/
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dcraw is a program that decodes any raw image from digital cameras and
produces better-quality output than the tools provided by the camera
vendor.

%description -l pl
dcraw jest programem, który dekoduje zdjêcia z aparatów cyfrowych
zapisanych w formacie raw i produkuje lepszy jako¶ciowo wynik ni¿
narzêdzia, które s± dostarczane przez producentów aparatów.

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
