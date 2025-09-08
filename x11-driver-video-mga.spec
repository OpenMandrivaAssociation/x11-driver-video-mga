%define _disable_ld_no_undefined 1

Summary:	X.org driver for Matrox Cards
Name:		x11-driver-video-mga
Epoch:		2
Version:	2.1.0.1
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
# Insread deprecated freedesktop lets use activ maintained xlibre version
#Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.xz
Source0:  https://github.com/X11Libre/xf86-video-mga/archive/xlibre-xf86-video-mga-%{version}/xf86-video-mga-xlibre-xf86-video-mga-%{version}.tar.gz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-mga is the X.org driver for Matrox Cards.

%prep
%autosetup -n xf86-video-mga-xlibre-xf86-video-mga-%{version} -p1
autoreconf -fis

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.*

