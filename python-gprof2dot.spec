%define 	module	gprof2dot
Summary:	Generate a dot graph from the output of several profiles
Summary(pl.UTF-8):	Generowanie grafu dot z wyjścia różnych profilowań
Name:		python-%{module}
Version:	2022.7.29
Release:	1
License:	LGPL v3+
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/g/gprof2dot/%{module}-%{version}.tar.gz
# Source0-md5:	e5cc9688e03be98748901fc513175573
URL:		https://pypi.org/project/gprof2dot/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	graphviz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generate a dot graph from the output of several profiles.

%description -l pl.UTF-8
Generowanie grafu dot z wyjścia różnych profilowań.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/gprof2dot{,-2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755, root,root) %{_bindir}/gprof2dot-2
%{py_sitescriptdir}/gprof2dot.py[co]
%{py_sitescriptdir}/gprof2dot-%{version}-py*.egg-info
