%global module python-binary-memcached
%global srcname %{module}


Name:           %{module}
Version:        0.31.1
Release:        1%{?dist}
Summary:        Python module python-binary-memcached

License:        MIT
URL:            https://github.com/jaysonsantos/%{module}
Source:         https://github.com/jaysonsantos/%{module}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-m2r
BuildRequires:  python3-flake8
BuildRequires:  python3dist(mistune)
BuildRequires:  python3-pytest
BuildRequires:  python3-trustme
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-uhashring
BuildRequires:  memcached

%global _description %{expand:
A pure python module (thread safe) to access memcached via it’s binary with SASL auth support.}

%description %_description

%package -n python3-binary-memcached
Summary:        %{summary}
Requires:  memcached

%description -n python3-binary-memcached
%_description

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files bmemcached

%check
%pytest


%files -n python3-binary-memcached -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Nov 22 2022 Alfredo Moralejo <amoralej@redhat.com> - 0.31.1-1
- Initial build with version 0.31.1

