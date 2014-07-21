# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       maui-kickstarter

# >> macros
# << macros

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Summary:    Create kickstart files for Maui images
Version:    0.99.0
Release:    1
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        http://www.maui-project.org
Source0:    %{name}-%{version}.tar.xz
Source100:  maui-kickstarter.yaml
Requires:   python-yaml
Requires:   python-urlgrabber
Requires:   python-cheetah
Requires:   python-lxml
BuildRequires:  pkgconfig(python-2.7)
BuildRequires:  python-cheetah

%description
Create Configuration files to build Maui images.

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
make tmpls
# << build pre

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%{__python} setup.py install --root=%{buildroot} -O1

# >> install post
# << install post

%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/*
%{python_sitelib}/*
# << files
