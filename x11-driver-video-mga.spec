Name: x11-driver-video-mga
Version: 1.4.7
Release: %mkrel 3
Epoch: 1 
Summary: The X.org driver for Matrox Cards
Group: System/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-mga  xorg/drivers/xf86-video-mga
# cd xorg/drivers/xf86-video/mga
# git-archive --format=tar --prefix=xf86-video-mga-1.4.7/ master | bzip2 -9 > xf86-video-mga-1.4.7.tar.bz2
########################################################################
Source0: xf86-video-mga-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Matrox Cards

%prep
%setup -q -n xf86-video-mga-%{version}

%patch1 -p1

%build
autoreconf -ifs
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

