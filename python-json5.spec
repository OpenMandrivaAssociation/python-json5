%define module json5

Name:		python-json5
Version:	0.14.0
Release:	1
Summary:	A Python implementation of the JSON5 data format
Group:		Development/Python
License:	Apache 2.0
URL:		https://github.com/dpranke/pyjson5
Source0:	https://github.com/dpranke/pyjson5/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A Python implementation of the JSON5 data format.

JSON5 extends the JSON data interchange format to make it slightly more
usable as a configuration language:

JavaScript-style comments (both single and multi-line) are legal.
Object keys may be unquoted if they are legal ECMAScript identifiers
Objects and arrays may end with trailing commas.
Strings can be single-quoted, and multi-line string literals are
allowed.
There are a few other more minor extensions to JSON; see the above page
for the full details.

This project implements a reader and writer implementation for Python;
where possible, it mirrors the standard Python JSON API package for
ease of use.

This is an early release. It has been reasonably well-tested, but it is
SLOW. It can be 1000-6000x slower than the C-optimized JSON module, and
is 200x slower (or more) than the pure Python JSON module.

%files
%{_bindir}/py%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
