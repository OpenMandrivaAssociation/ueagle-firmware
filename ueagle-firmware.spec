%define name ueagle-firmware
%define version 1.1
%define distname ueagle-data-%{version}
%define release %mkrel 2

Summary: Firmware and CMV files for Eagle-based modems
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://eagle-usb.org/ueagle-atm/non-free/%{distname}.tar.bz2
Source1: http://download.gna.org/ueagleatm/ikanos/ueagle4-data-1.0.tar.gz
# (tpg) stolen from http://svn.gna.org/viewcvs/ueagleatm/trunk/ueagle-utils/debug/#dirlist
# ueagle-utils are bit outdated and there are no reason to create separate pkg only for these two files
Source2: ueaglediag
Source3: ueaglestat
License: Public Domain/BSD
Group: System/Kernel and hardware
Url: http://eagle-usb.org/
BuildArch: noarch

%description
This package contains firmware and CMV files for Eagle-based modems.

%prep
%setup -q -n %{distname} -a 1

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware/ueagle-atm
install -m644 *.bin *.fw %{buildroot}/lib/firmware/ueagle-atm
pushd ueagle4-data-1.0
install -m644 *.bin* *.fw %{buildroot}/lib/firmware/ueagle-atm
popd

install -d %{buildroot}%{_bindir}
install -m755 %{SOURCE2} %{buildroot}%{_bindir}/ueaglediag
install -m755 %{SOURCE3} %{buildroot}%{_bindir}/ueaglestat

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /lib/firmware/ueagle-atm/
/lib/firmware/ueagle-atm/*.bin*
/lib/firmware/ueagle-atm/*.fw
%{_bindir}/ueagle*
