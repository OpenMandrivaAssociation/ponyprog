Name:		ponyprog
Version:	3.1.1
Release:	1
Summary:	Serial device programmer
# http://downloads.sourceforge.net/ponyprog/%origname-%version.tar.gz
Source0:	https://github.com/lancos/ponyprog/archive/v%{version}.tar.gz
Source1:	https://github.com/lancos/qhexedit2/archive/master.zip
License:	GPL
Group:		Development/Other
Url:		https://github.com/lancos/ponyprog/
BuildRequires:	cmake
BuildRequires:	cmake(LibFTDI1)

%description
PonyProg is a serial device programmer software with a user friendly GUI
framework available for Windows95, 98, 2000 & NT and Intel Linux. Its purpose
is reading and writing every serial device. At the moment it supports I2C Bus,
Microwire, SPI eeprom, the Atmel AVR and Microchip PIC micro.

%prep
%autosetup -p1 -a1
rm -rf qhexedit2/
mv qhexedit2* qhexedit2

%build
%cmake
%make_build

%install
%make_install -C build

%files
%{_bindir}/%{name}
%{_udevrulesdir}/90-ponyprog.rules
%{_datadir}/icons/ponyprog.png
%{_datadir}/doc/ponyprog/
%{_datadir}/applications/ponyprog.desktop
%{_datadir}/ponyprog/lang/*
