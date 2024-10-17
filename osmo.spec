Name:		osmo
Version:	0.2.10
Release:	%mkrel 3
Summary:	A handy personal organizer
License:	GPLv2+
Group:		Office
Url:		https://clayo.org/osmo
Source0:	http://downloads.sourceforge.net/osmo-pim/%{name}-%{version}.tar.gz
Patch0:		osmo-0.2.10-libnotify-0.7.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	gtk+2-devel >= 2.10
BuildRequires:	gtkspell-devel >= 2.0.5
BuildRequires:	libical-devel >= 0.33
BuildRequires:	libtar-devel
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libgringotts-devel >= 1.2.1
BuildRequires:	gtkhtml2-devel

%description
Osmo is a handy personal organizer, which includes calendar, tasks 
manager, address book and notes modules.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x LIBICAL_CFLAGS=-I/usr/include/libical
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README* TRANSLATORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_datadir}/sounds/%{name}
%{_mandir}/man1/%{name}.1*
