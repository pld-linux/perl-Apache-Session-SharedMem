#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Session-SharedMem
Summary:	Apache::Session::Store::SharedMem - store persistent data in shared memory
Summary(pl):	Apache::Session::Store::SharedMem - przechowywanie trwa³ych dane w pamiêci wspólnej
Name:		perl-Apache-Session-SharedMem
Version:	0.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	880074b9d0703d0db6cd3d5901a7ee6a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
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
To jest rozszerzenie Apache::Session, przechowuj±ce dane sesyjne w pamiêci
dzielonej (czyli robi dok³adnie to, co ma napisane na puszce), przy u¿yciu
IPC::Cache (a wiêc IPC::ShareLite).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -wle 'WriteMakefile(NAME=>"Apache::Session::SharedMEM")' \
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
%{perl_vendorlib}/Apache/Session/*.pm
%{perl_vendorlib}/Apache/Session/Store/*.pm
%{_mandir}/man3/*
