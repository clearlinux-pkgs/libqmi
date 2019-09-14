#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libqmi
Version  : 1.22.6
Release  : 8
URL      : https://www.freedesktop.org/software/libqmi/libqmi-1.22.6.tar.xz
Source0  : https://www.freedesktop.org/software/libqmi/libqmi-1.22.6.tar.xz
Summary  : Library to communicate with QMI-powered modems
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libqmi-bin = %{version}-%{release}
Requires: libqmi-data = %{version}-%{release}
Requires: libqmi-lib = %{version}-%{release}
Requires: libqmi-libexec = %{version}-%{release}
Requires: libqmi-license = %{version}-%{release}
Requires: libqmi-man = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(mbim-glib)

%description
libqmi is a glib-based library for talking to WWAN modems and devices which
speak the Qualcomm MSM Interface (QMI) protocol.

%package bin
Summary: bin components for the libqmi package.
Group: Binaries
Requires: libqmi-data = %{version}-%{release}
Requires: libqmi-libexec = %{version}-%{release}
Requires: libqmi-license = %{version}-%{release}

%description bin
bin components for the libqmi package.


%package data
Summary: data components for the libqmi package.
Group: Data

%description data
data components for the libqmi package.


%package dev
Summary: dev components for the libqmi package.
Group: Development
Requires: libqmi-lib = %{version}-%{release}
Requires: libqmi-bin = %{version}-%{release}
Requires: libqmi-data = %{version}-%{release}
Provides: libqmi-devel = %{version}-%{release}
Requires: libqmi = %{version}-%{release}

%description dev
dev components for the libqmi package.


%package doc
Summary: doc components for the libqmi package.
Group: Documentation
Requires: libqmi-man = %{version}-%{release}

%description doc
doc components for the libqmi package.


%package lib
Summary: lib components for the libqmi package.
Group: Libraries
Requires: libqmi-data = %{version}-%{release}
Requires: libqmi-libexec = %{version}-%{release}
Requires: libqmi-license = %{version}-%{release}

%description lib
lib components for the libqmi package.


%package libexec
Summary: libexec components for the libqmi package.
Group: Default
Requires: libqmi-license = %{version}-%{release}

%description libexec
libexec components for the libqmi package.


%package license
Summary: license components for the libqmi package.
Group: Default

%description license
license components for the libqmi package.


%package man
Summary: man components for the libqmi package.
Group: Default

%description man
man components for the libqmi package.


%prep
%setup -q -n libqmi-1.22.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568272603
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1568272603
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libqmi
cp COPYING %{buildroot}/usr/share/package-licenses/libqmi/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libqmi/COPYING.LIB
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qmi-firmware-update
/usr/bin/qmi-network
/usr/bin/qmicli

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/qmicli

%files dev
%defattr(-,root,root,-)
/usr/include/libqmi-glib/libqmi-glib.h
/usr/include/libqmi-glib/qmi-client.h
/usr/include/libqmi-glib/qmi-compat.h
/usr/include/libqmi-glib/qmi-device.h
/usr/include/libqmi-glib/qmi-dms.h
/usr/include/libqmi-glib/qmi-enum-types.h
/usr/include/libqmi-glib/qmi-enums-dms.h
/usr/include/libqmi-glib/qmi-enums-loc.h
/usr/include/libqmi-glib/qmi-enums-nas.h
/usr/include/libqmi-glib/qmi-enums-oma.h
/usr/include/libqmi-glib/qmi-enums-pbm.h
/usr/include/libqmi-glib/qmi-enums-pdc.h
/usr/include/libqmi-glib/qmi-enums-pds.h
/usr/include/libqmi-glib/qmi-enums-private.h
/usr/include/libqmi-glib/qmi-enums-qos.h
/usr/include/libqmi-glib/qmi-enums-uim.h
/usr/include/libqmi-glib/qmi-enums-voice.h
/usr/include/libqmi-glib/qmi-enums-wda.h
/usr/include/libqmi-glib/qmi-enums-wds.h
/usr/include/libqmi-glib/qmi-enums-wms.h
/usr/include/libqmi-glib/qmi-enums.h
/usr/include/libqmi-glib/qmi-error-types.h
/usr/include/libqmi-glib/qmi-errors.h
/usr/include/libqmi-glib/qmi-flags64-dms.h
/usr/include/libqmi-glib/qmi-flags64-loc.h
/usr/include/libqmi-glib/qmi-flags64-nas.h
/usr/include/libqmi-glib/qmi-flags64-types.h
/usr/include/libqmi-glib/qmi-loc.h
/usr/include/libqmi-glib/qmi-message-context.h
/usr/include/libqmi-glib/qmi-message.h
/usr/include/libqmi-glib/qmi-nas.h
/usr/include/libqmi-glib/qmi-oma.h
/usr/include/libqmi-glib/qmi-pbm.h
/usr/include/libqmi-glib/qmi-pdc.h
/usr/include/libqmi-glib/qmi-pds.h
/usr/include/libqmi-glib/qmi-proxy.h
/usr/include/libqmi-glib/qmi-qos.h
/usr/include/libqmi-glib/qmi-uim.h
/usr/include/libqmi-glib/qmi-utils.h
/usr/include/libqmi-glib/qmi-version.h
/usr/include/libqmi-glib/qmi-voice.h
/usr/include/libqmi-glib/qmi-wda.h
/usr/include/libqmi-glib/qmi-wds.h
/usr/include/libqmi-glib/qmi-wms.h
/usr/lib64/libqmi-glib.so
/usr/lib64/pkgconfig/qmi-glib.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libqmi-glib/QmiClient.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientDms.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientLoc.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientNas.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientOma.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientPbm.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientPdc.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientPds.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientQos.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientUim.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientVoice.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientWda.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientWds.html
/usr/share/gtk-doc/html/libqmi-glib/QmiClientWms.html
/usr/share/gtk-doc/html/libqmi-glib/QmiDevice.html
/usr/share/gtk-doc/html/libqmi-glib/QmiMessageContext.html
/usr/share/gtk-doc/html/libqmi-glib/QmiProxy.html
/usr/share/gtk-doc/html/libqmi-glib/annotation-glossary.html
/usr/share/gtk-doc/html/libqmi-glib/api-index-full.html
/usr/share/gtk-doc/html/libqmi-glib/ch01.html
/usr/share/gtk-doc/html/libqmi-glib/ch02.html
/usr/share/gtk-doc/html/libqmi-glib/ch02s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch03.html
/usr/share/gtk-doc/html/libqmi-glib/ch03s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch04.html
/usr/share/gtk-doc/html/libqmi-glib/ch04s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch05.html
/usr/share/gtk-doc/html/libqmi-glib/ch05s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch06.html
/usr/share/gtk-doc/html/libqmi-glib/ch06s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch07.html
/usr/share/gtk-doc/html/libqmi-glib/ch07s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch08.html
/usr/share/gtk-doc/html/libqmi-glib/ch09.html
/usr/share/gtk-doc/html/libqmi-glib/ch09s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch10.html
/usr/share/gtk-doc/html/libqmi-glib/ch10s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch11.html
/usr/share/gtk-doc/html/libqmi-glib/ch12.html
/usr/share/gtk-doc/html/libqmi-glib/ch12s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch13.html
/usr/share/gtk-doc/html/libqmi-glib/ch13s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch14.html
/usr/share/gtk-doc/html/libqmi-glib/ch14s02.html
/usr/share/gtk-doc/html/libqmi-glib/ch15.html
/usr/share/gtk-doc/html/libqmi-glib/home.png
/usr/share/gtk-doc/html/libqmi-glib/index.html
/usr/share/gtk-doc/html/libqmi-glib/left-insensitive.png
/usr/share/gtk-doc/html/libqmi-glib/left.png
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-Common-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-Common-utilities.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Activate-Automatic-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Activate-Manual-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Delete-Stored-Image-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Dell-Change-Device-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Dell-Get-Firmware-Version-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Event-Report-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Activation-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Alt-Net-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Band-Capabilities-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Boot-Image-Download-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Capabilities-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Factory-SKU-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Firmware-Preference-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Hardware-Revision-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-IDs-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-MSISDN-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Manufacturer-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Model-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Operating-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-PRL-Version-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Power-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Revision-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Software-Version-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Stored-Image-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Supported-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-Time-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Get-User-Lock-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-HP-Change-Device-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-List-Stored-Images-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Read-ERI-File-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Read-User-Data-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Restore-Factory-Defaults-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Alt-Net-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Boot-Image-Download-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Event-Report-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-FCC-Authentication-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Firmware-ID-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Firmware-Preference-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Operating-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Service-Programming-Code-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-Time-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-User-Lock-Code-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Set-User-Lock-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Swi-Get-Current-Firmware-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Swi-Get-USB-Composition-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Swi-Set-USB-Composition-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Change-PIN-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Get-CK-Status-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Get-ICCID-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Get-IMSI-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Get-PIN-Status-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Get-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Set-CK-Protection-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Set-PIN-Protection-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Unblock-CK-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Unblock-PIN-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-UIM-Verify-PIN-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Validate-Service-Programming-Code-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-Write-User-Data-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-DMS-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-Deprecated-interface.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-Errors.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Delete-Assistance-Data-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Delete-Assistance-Data-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Engine-State-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Fix-Recurrence-Type-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-GNSS-Sv-Info-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Get-Operation-Mode-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Get-Operation-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Get-Predicted-Orbits-Data-Source-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Get-Predicted-Orbits-Data-Source-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Get-Server-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Get-Server-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Inject-Predicted-Orbits-Data-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Inject-Predicted-Orbits-Data-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Inject-Xtra-Data-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Inject-Xtra-Data-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-NMEA-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Position-Report-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Register-Events-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Set-Operation-Mode-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Set-Operation-Mode-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Set-Server-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Set-Server-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Start-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-Stop-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-LOC-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Attach-Detach-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Config-Signal-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Event-Report-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Force-Network-Search-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-CDMA-Position-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Cell-Location-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Home-Network-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-LTE-Cphy-CA-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Operator-Name-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-RF-Band-Information-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Serving-System-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Signal-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Signal-Strength-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Supported-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-System-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-System-Selection-Preference-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Technology-Preference-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Get-Tx-Rx-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Initiate-Network-Register-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Network-Scan-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Network-Time-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Operator-Name-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Register-Indications-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Serving-System-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Set-Event-Report-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Set-System-Selection-Preference-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Set-Technology-Preference-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-Signal-Info-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-System-Info-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-NAS-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Cancel-Session-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Event-Report-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Get-Feature-Setting-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Get-Session-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Send-Selection-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Set-Event-Report-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Set-Feature-Setting-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-Start-Session-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-OMA-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PBM-Get-All-Capabilities-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PBM-Get-Capabilities-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PBM-Indication-Register-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PBM-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Activate-Config-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Activate-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Config-Change-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Deactivate-Config-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Deactivate-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Delete-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Get-Config-Info-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Get-Config-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Get-Config-Limits-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Get-Default-Config-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Get-Selected-Config-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Get-Selected-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-List-Configs-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-List-Configs-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Load-Config-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Load-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Register-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Set-Selected-Config-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-Set-Selected-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDC-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Event-Report-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Get-AGPS-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Get-Auto-Tracking-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Get-Default-Tracking-Session-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Get-GPS-Service-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Set-AGPS-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Set-Auto-Tracking-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Set-Default-Tracking-Session-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Set-Event-Report-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-Set-GPS-Service-State-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-PDS-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QOS-Flow-Status-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QOS-Get-Flow-Status-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QOS-Get-Network-Status-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QOS-Network-Status-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QOS-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QOS-Swi-Read-Data-Stats-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QOS-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-QmiMessage.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Card-Status-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Change-PIN-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Get-Card-Status-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Get-File-Attributes-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Get-Supported-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Power-Off-SIM-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Power-On-SIM-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Read-Record-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Read-Transparent-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Register-Events-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Set-PIN-Protection-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Unblock-PIN-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-Verify-PIN-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-UIM-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-VOICE-All-Call-Status-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-VOICE-Answer-Call-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-VOICE-Dial-Call-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-VOICE-End-Call-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-VOICE-Get-Config-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-VOICE-Get-Supported-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-VOICE-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-Version-and-feature-checks.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDA-Get-Data-Format-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDA-Get-Supported-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDA-Set-Data-Format-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDA-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Bind-Mux-Data-Port-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Create-Profile-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Delete-Profile-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Event-Report-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Autoconnect-Settings-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Channel-Rates-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Current-Data-Bearer-Technology-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Current-Settings-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Data-Bearer-Technology-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Default-Profile-Num-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Default-Settings-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Dormancy-Status-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-PDN-Throttle-Info-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Packet-Service-Status-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Packet-Statistics-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Profile-List-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Profile-Settings-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Get-Supported-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Go-Active-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Go-Dormant-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Modify-Profile-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Packet-Service-Status-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Set-Autoconnect-Settings-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Set-Default-Profile-Num-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Set-Event-Report-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Set-IP-Family-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Start-Network-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Stop-Network-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-Swi-Create-Profile-Indexed-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WDS-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Delete-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Event-Report-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Get-Message-Protocol-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Get-Routes-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Get-Supported-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-List-Messages-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Modify-Tag-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Raw-Read-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Raw-Send-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Raw-Write-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Reset-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-SMSC-Address-indication.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Send-From-Memory-Storage-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Set-Event-Report-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-Set-Routes-request.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib-WMS-enumerations-and-flags.html
/usr/share/gtk-doc/html/libqmi-glib/libqmi-glib.devhelp2
/usr/share/gtk-doc/html/libqmi-glib/object-tree.html
/usr/share/gtk-doc/html/libqmi-glib/right-insensitive.png
/usr/share/gtk-doc/html/libqmi-glib/right.png
/usr/share/gtk-doc/html/libqmi-glib/style.css
/usr/share/gtk-doc/html/libqmi-glib/up-insensitive.png
/usr/share/gtk-doc/html/libqmi-glib/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqmi-glib.so.5
/usr/lib64/libqmi-glib.so.5.5.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/qmi-proxy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libqmi/COPYING
/usr/share/package-licenses/libqmi/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qmi-firmware-update.1
/usr/share/man/man1/qmi-network.1
/usr/share/man/man1/qmicli.1
