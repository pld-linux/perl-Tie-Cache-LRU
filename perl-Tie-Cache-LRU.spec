%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Cache-LRU
Summary:	Tie::Cache-LRU Perl module - A Least-Recently Used cache
Summary(cs):	Modul Tie::Cache-LRU pro Perl
Summary(da):	Perlmodul Tie::Cache-LRU
Summary(de):	Tie::Cache-LRU Perl Modul
Summary(es):	Módulo de Perl Tie::Cache-LRU
Summary(fr):	Module Perl Tie::Cache-LRU
Summary(it):	Modulo di Perl Tie::Cache-LRU
Summary(ja):	Tie::Cache-LRU Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Tie::Cache-LRU ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Tie::Cache-LRU
Summary(pl):	Modu³ perla Tie::Cache-LRU - buforowanie "ostatnio u¿ywanych"
Summary(pt_BR):	Módulo Perl Tie::Cache-LRU
Summary(pt):	Módulo de Perl Tie::Cache-LRU
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Tie::Cache-LRU
Summary(sv):	Tie::Cache-LRU Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Tie::Cache-LRU
Summary(zh_CN):	Tie::Cache-LRU Perl Ä£¿é
Name:		perl-Tie-Cache-LRU
Version:	0.21
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_sitelib}/Tie/Cache
%{perl_sitelib}/Tie/Cache/LRU
%{perl_sitelib}/Tie/Cache/LRU.pm
%{_mandir}/man3/*
