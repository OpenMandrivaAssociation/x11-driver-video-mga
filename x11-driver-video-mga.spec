Name: x11-driver-video-mga
Version: 1.4.13
Release: %mkrel 6
Epoch: 2
Summary: X.org driver for Matrox Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-mga is the X.org driver for Matrox Cards.

%prep
%setup -q -n xf86-video-mga-%{version}

%build
autoreconf -fis
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/mga_drv.la
%{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.*
