Name:		python-json5
Version:	0.9.25
Release:	1
Summary:	A Python implementation of the JSON5 data format
Group:		Development/Python
License:	Apache 2.0
URL:		https://github.com/dpranke/pyjson5
Source0:	https://github.com/dpranke/pyjson5/archive/v%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildRequires:  python-pip
BuildRequires:  python-wheel

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

%prep
%autosetup -p1 -n pyjson5-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/pyjson5
%{python_sitelib}/json5
#{python_sitelib}/*.egg-info
