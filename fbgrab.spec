Summary:	Framebuffer screenshot program
Name:		fbgrab
Version:	1.1
Release:	1
License:	GPL
Group:		Graphics
Source0:	http://fbgrab.monells.se/%{name}-%{version}.tar.gz
Patch0:		fbgrab-1.0-makefile.patch
Url: http://hem.bredband.net/gmogmo/fbgrab/
BuildRequires: libpng-devel
BuildRequires: zlib-devel

%description 
FBGrab is a framebuffer screenshot program, capturing the linux frambuffer 
and converting it to a png-picture. FBGrab is delivered as is without any 
warranty and license is GPL version 2, see tar-ball for details.

%prep
%setup -qn %{name}
%patch0 -p1 -z .splint

%build
%setup_compile_flags
%make

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1/
%makeinstall DESTDIR=%{buildroot}

%files 
%doc INSTALL
%_bindir/fbgrab
%_mandir/man1/fbgrab.1*
