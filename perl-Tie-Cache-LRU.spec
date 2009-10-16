#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Cache-LRU
Summary:	Tie::Cache-LRU Perl module - a Least-Recently Used cache
Summary(pl.UTF-8):	Moduł Perla Tie::Cache-LRU - buforowanie "ostatnio używanych"
Name:		perl-Tie-Cache-LRU
Version:	20081023.2116
Release:	1
Epoch:		1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	38053411c06ba8199922111adad4bcef
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Assert
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-Class-Virtual
BuildRequires:	perl-enum
BuildRequires:	perl-Test-Simple >= 0.82
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::Cache-LRU - This is an implementation of a least-recently used
(LRU) cache keeping the cache in RAM.

A LRU cache is similar to the kind of cache used by a web browser. New
items are placed into the top of the cache. When the cache grows past
its size limit, it throws away items off the bottom. The trick is that
whenever an item is -accessed-, it is pulled back to the top. The end
result of all this is that items which are frequently accessed tend to
stay in the cache.

%description -l pl.UTF-8
Tie::Cache-LRU - jest to implementacja buforowania "ostatnio
używanych" (least-recently used - LRU), buforująca w pamięci RAM.

Cache LRU jest podobny do używanego przez przeglądarki WWW. Nowe
elementy są umieszczane na szczycie cache'u. Gdy graniczny rozmiar
cache zostanie przekroczony, wyrzucane są z niego elementy znajdujące
się na dole. Sztuczka polega na tym, że gdy występuje --dostęp-- do
elementu, jest on przenoszony na szczyt. W wyniku tego wszystkie
elementy, do których dostęp następuje często, mają tendencję do
pozostawania w cache'u.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%dir %{perl_vendorlib}/Tie/Cache
%{perl_vendorlib}/Tie/Cache/LRU
%{perl_vendorlib}/Tie/Cache/LRU.pm
%{_mandir}/man3/*
