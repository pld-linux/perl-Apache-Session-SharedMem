#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Session-SharedMem
Summary:	Apache::Session::Store::SharedMem - Store persistent data in shared memory
Summary(pl):	Apache::Session::Store::SharedMem - Przechowuj trwa�e dane w pami�ci dzielonej
Name:		perl-Apache-Session-SharedMem
Version:	0.41
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	74284d41fb3373d628ddb42fd3ee613b
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Apache-Session
BuildRequires:	perl-IPC-Cache
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apache::Session extension module that stores the session
data in Shared memory (so, does exactly what it says on the tin then)
using IPC::Cache (and hence IPC::ShareLite).

%description -l pl
To jest rozszerzenie Apache::Session, przechowuj�ce dane sesyjne w pami�ci
dzielonej (czyli robi dok�adnie to, co ma napisane na puszce), przy u�yciu
IPC::Cache (a wi�c IPC::ShareLite).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -wle 'WriteMakefile(NAME=>"Apache::Session::SharedMEM")' \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Apache/Session/*.pm
%{perl_vendorlib}/Apache/Session/Store/*.pm
%{_mandir}/man3/*
