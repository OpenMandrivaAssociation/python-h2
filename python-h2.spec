%define module h2

Name:		python-h2
Version:	4.3.0
Release:	1
Summary:	HTTP/2 State-Machine based protocol implementation
Group:		Development/Python
License:	MIT
URL:		https://github.com/python-hyper/h2
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires: python%{pyver}dist(hpack)
Requires: python%{pyver}dist(hyperframe)

%description
This module contains a pure-Python implementation of a HTTP/2 protocol stack.
It’s written from the ground up to be embeddable in whatever program
you choose to use, ensuring that you can speak HTTP/2 regardless of
your programming paradigm.

%files
%doc README.rst CHANGELOG.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
