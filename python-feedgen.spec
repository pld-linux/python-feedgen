#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Feedgenerator
Summary(pl.UTF-8):	Generator kanałów informacyjnych (feedów)
Name:		python-feedgen
Version:	0.9.0
Release:	3
License:	BSD or LGPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/feedgen/
Source0:	https://files.pythonhosted.org/packages/source/f/feedgen/feedgen-%{version}.tar.gz
# Source0-md5:	9b5be451a164135d6b3fc91a6edcd8ed
URL:		https://pypi.org/project/feedgen/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can be used to generate web feeds in both ATOM and RSS
format. It has support for extensions. Included is for example an
extension to produce Podcasts.

%description -l pl.UTF-8
Ten moduł służy do generowania kanałów informacyjnych WWW, zarówno w
formacie ATOM, jak i RSS. Ma obsługę rozszerzeń; dołączone jest
przykładowe rozszerzenie do tworzenia Podcastów.

%package -n python3-feedgen
Summary:	Feedgenerator
Summary(pl.UTF-8):	Generator kanałów informacyjnych (feedów)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-feedgen
This module can be used to generate web feeds in both ATOM and RSS
format. It has support for extensions. Included is for example an
extension to produce Podcasts.

%description -n python3-feedgen -l pl.UTF-8
Ten moduł służy do generowania kanałów informacyjnych WWW, zarówno w
formacie ATOM, jak i RSS. Ma obsługę rozszerzeń; dołączone jest
przykładowe rozszerzenie do tworzenia Podcastów.

%package apidocs
Summary:	API documentation for Python feedgen module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona feedgen
Group:		Documentation

%description apidocs
API documentation for Python feedgen module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona feedgen.

%prep
%setup -q -n feedgen-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc license.bsd readme.rst
%{py_sitescriptdir}/feedgen
%{py_sitescriptdir}/feedgen-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-feedgen
%defattr(644,root,root,755)
%doc license.bsd readme.rst
%{py3_sitescriptdir}/feedgen
%{py3_sitescriptdir}/feedgen-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/html/*
%endif
