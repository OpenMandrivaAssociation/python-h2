%define module	h2

Name:		python-%{module}
Version:	4.1.0
Release:	2
Summary:	HTTP/2 State-Machine based protocol implementation
Group:		Development/Python
License:	MIT
URL:		https://github.com/python-hyper/h2
Source0:	https://pypi.io/packages/source/h/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

Requires: python3dist(hpack)
Requires: python3dist(hyperframe)

BuildArch:	noarch

%files
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

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
