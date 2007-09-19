%define name ueagle-firmware
%define version 1.1
%define distname ueagle-data-%{version}
%define release %mkrel 1

Summary: Firmware and CMV files for Eagle-based modems
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://eagle-usb.org/ueagle-atm/non-free/%{distname}.tar.bz2
License: Public Domain
Group: System/Kernel and hardware
Url: http://eagle-usb.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This package contains firmware and CMV files for Eagle-based modems.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/ueagle-atm
install -m644 *.bin *.fw $RPM_BUILD_ROOT/lib/firmware/ueagle-atm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /lib/firmware/ueagle-atm/
/lib/firmware/ueagle-atm/*.bin
/lib/firmware/ueagle-atm/*.fw
