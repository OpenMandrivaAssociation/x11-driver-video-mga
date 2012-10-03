Name:		x11-driver-video-mga
Epoch:		2
Version:	1.6.2
Release:	1
Summary:	X.org driver for Matrox Cards
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.bz2

BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(gl)

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts:	xorg-x11-server < 7.0

%description
x11-driver-video-mga is the X.org driver for Matrox Cards.

%prep
%setup -qn xf86-video-mga-%{version}
autoreconf -fis

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.*
