Summary:	Raw Digital Photo Decoder
Summary(pl):	Dekoder zdj�� cyfrowych w formacie raw
Name:		dcraw
Version:	20040726
Release:	1
License:	Free
Group:		Applications
Source0:	http://www.cybercom.net/~dcoffin/dcraw/%{name}.c
# NoSource0-md5:	682bc23c18aa1147688b768638b5792f
Source1:	http://www.cybercom.net/~dcoffin/dcraw/%{name}.1
# NoSource1-md5:	fc4318e37efa0160df55ad301258404d
URL:		http://www.cybercom.net/~dcoffin/dcraw/
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dcraw is a program that decodes any raw image from digital cameras and
produces better-quality output than the tools provided by the camera
vendor.

%description -l pl
dcraw jest programem, kt�ry dekoduje zdj�cia z aparat�w cyfrowych
zapisanych w formacie raw i produkuje lepszy jako�ciowo wynik ni�
narz�dzia, kt�re s� dostarczane przez producent�w aparat�w.

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
