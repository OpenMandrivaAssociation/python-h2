%define module	h2

Name:		python-%{module}
Version:	3.2.0
Release:	1
Summary:	HTTP/2 State-Machine based protocol implementation
Group:		Development/Python
License:	MIT
URL:		https://pypi.python.org/pypi/h2
Source0:	https://pypi.io/packages/source/h/h2/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

Requires: python3dist(hpack)
Requires: python3dist(hyperframe)

%description
This module contains a pure-Python implementation of a HTTP/2 protocol stack.
It’s written from the ground up to be embeddable in whatever program
you choose to use, ensuring that you can speak HTTP/2 regardless of
your programming paradigm.

%prep
%setup -q -n %{module}-%{version}
%autopatch -p1

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info/
