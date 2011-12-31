Name: x11-driver-video-mga
Epoch: 2
Version: 1.4.13
Release: 8
Summary: X.org driver for Matrox Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.bz2

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(gl)

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-mga is the X.org driver for Matrox Cards.

%prep
%setup -qn xf86-video-mga-%{version}

%build
autoreconf -fis
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.*

