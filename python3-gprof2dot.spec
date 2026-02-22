#
# Conditional build:
%bcond_with	tests	# unit tests (files missing in sdist)

%define 	module	gprof2dot
Summary:	Generate a dot graph from the output of several profiles
Summary(pl.UTF-8):	Generowanie grafu dot z wyjścia różnych profilowań
Name:		python3-%{module}
Version:	2025.4.14
Release:	1
License:	LGPL v3+
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/g/gprof2dot/%{module}-%{version}.tar.gz
# Source0-md5:	6ab489c204d22a5b7b739aaf66f030c4
URL:		https://pypi.org/project/gprof2dot/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests}
BuildRequires:	graphviz
%endif
Requires:	graphviz
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generate a dot graph from the output of several profiles.

%description -l pl.UTF-8
Generowanie grafu dot z wyjścia różnych profilowań.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} tests/test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/gprof2dot{,-3}
ln -sf gprof2dot-3 $RPM_BUILD_ROOT%{_bindir}/gprof2dot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755, root,root) %{_bindir}/gprof2dot-3
%{_bindir}/gprof2dot
%{py3_sitescriptdir}/gprof2dot.py
%{py3_sitescriptdir}/__pycache__/gprof2dot.cpython-*.py[co]
%{py3_sitescriptdir}/gprof2dot-%{version}-py*.egg-info
