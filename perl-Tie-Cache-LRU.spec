#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Cache-LRU
Summary:	Tie::Cache-LRU Perl module - a Least-Recently Used cache
Summary(pl):	Modu³ Perla Tie::Cache-LRU - buforowanie "ostatnio u¿ywanych"
Name:		perl-Tie-Cache-LRU
Version:	0.21
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	114890d5a3c1ecf6f51d743086c5372f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-Virtual
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

%description -l pl
Tie::Cache-LRU - jest to implementacja buforowania "ostatnio
u¿ywanych" (least-recently used - LRU), buforuj±ca w pamiêci RAM.

Cache LRU jest podobny do u¿ywanego przez przegl±darki WWW. Nowe
elementy s± umieszczane na szczycie cache'u. Gdy graniczny rozmiar
cache zostanie przekroczony, wyrzucane s± z niego elementy znajduj±ce
siê na dole. Sztuczka polega na tym, ¿e gdy wystêpuje --dostêp-- do
elementu, jest on przenoszony na szczyt. W wyniku tego wszystkie
elementy, do których dostêp nastêpuje czêsto, maj± tendencjê do
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
