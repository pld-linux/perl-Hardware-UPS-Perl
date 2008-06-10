#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Hardware
%define		pnam	UPS-Perl
Summary:	Hardware::UPS-Perl - module and scripts to deal with an UPS
Summary(pl.UTF-8):	Hardware::UPS-Perl - moduł i skrypty do obsługi UPS-ów
Name:		perl-Hardware-UPS-Perl
Version:	0.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/perl-%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	397e23b51242033d61dc964acf70aada
URL:		http://search.cpan.org/dist/perl-Hardware-UPS-Perl
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(splice)

%description
Hardware::UPS-Perl - module and scripts to deal with an UPS.

%description -l pl.UTF-8
Hardware::UPS-Perl - moduł i skrypty do obsługi UPS-ów.

%prep
%setup -q -n perl-%{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Hardware
%{perl_vendorlib}/Hardware/*.pm
%{_mandir}/man3/*
