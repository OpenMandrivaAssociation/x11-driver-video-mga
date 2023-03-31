Summary:	X.org driver for Matrox Cards
Name:		x11-driver-video-mga
Epoch:		2
Version:	2.0.1
Release:	2
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.xz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-mga is the X.org driver for Matrox Cards.

%prep
%autosetup -n xf86-video-mga-%{version} -p1
autoreconf -fis

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.*

