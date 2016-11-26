Summary:	X.org driver for Matrox Cards
Name:		x11-driver-video-mga
Epoch:		2
Version:	1.6.4.20161117
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mga-%{version}.tar.bz2
Patch0:		mga-1.4.5-no-hal-advertising.patch
Patch2:		mga-1.4.12-bigendian.patch
Patch3:		mga-1.6.3-shadowfb.patch
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-mga is the X.org driver for Matrox Cards.

%prep
%setup -qn xf86-video-mga-%{version}
%apply_patches
autoreconf -fis

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/mga_drv.so
%{_mandir}/man4/mga.*

