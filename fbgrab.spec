%define name	fbgrab
%define version 1.0
%define release %mkrel 10

Summary: Framebuffer screenshot program
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Graphics
Source: http://hem.bredband.net/gmogmo/fbgrab/%{name}-%{version}.tar.bz2
Patch: fbgrab-1.0-makefile.patch
Url: http://hem.bredband.net/gmogmo/fbgrab/
Buildroot: %{_tmppath}/fbgrab-root
BuildRequires: libpng-devel
BuildRequires: zlib-devel

%description 
FBGrab is a framebuffer screenshot program, capturing the linux frambuffer 
and converting it to a png-picture. FBGrab is delivered as is without any 
warranty and license is GPL version 2, see tar-ball for details.

%prep
%setup -q

%patch -p1 -z .splint

%build

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%files 
%defattr(-,root, root)
%doc INSTALL
%_bindir/fbgrab
%_mandir/man1/fbgrab.1*

%clean
rm -rf $RPM_BUILD_ROOT
