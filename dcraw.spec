Summary:	Raw Digital Photo Decoder
Summary(pl):	Dekoder zdjêæ cyfrowych w formacie raw
Name:		dcraw
Version:	20040307
Release:	0.1
License:	Free
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/%{name}.c
# NoSource0-md5:	31154dba3111be5798818f62d3bdfd10
Source1:	http://www.cybercom.net/~dcoffin/dcraw/%{name}.1
# NoSource1-md5:	fc4318e37efa0160df55ad301258404d
URL:		http://www.cybercom.net/~dcoffin/dcraw/
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
%{__cc} %{rpmldflags} -o dcraw %{rpmcflags} dcraw.c -lm

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
