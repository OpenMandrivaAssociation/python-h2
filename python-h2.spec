%define module	h2

Name:		python-%{module}
Version:	3.2.0
Release:	%mkrel 1
Summary:	HTTP/2 State-Machine based protocol implementation
Group:		Development/Python
License:	MIT
URL:		https://pypi.python.org/pypi/h2
Source0:	https://pypi.io/packages/source/h/h2/%{module}-%{version}.tar.gz
BuildArch:	noarch

%description
This module contains a pure-Python implementation of a HTTP/2 protocol stack.
It’s written from the ground up to be embeddable in whatever program
you choose to use, ensuring that you can speak HTTP/2 regardless of
your programming paradigm.

%package -n	python3-%{module}
Summary:	HTTP/2 State-Machine based protocol implementation
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This module contains a pure-Python implementation of a HTTP/2 protocol stack.
It’s written from the ground up to be embeddable in whatever program
you choose to use, ensuring that you can speak HTTP/2 regardless of
your programming paradigm.

This is the Python 3 version of the package.

%prep
%setup -q -n %{module}-%{version}
%autopatch -p1

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{python3_sitelib}/%{module}/
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info/
