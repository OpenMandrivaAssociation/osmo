Name:		osmo
Version:	0.2.8
Release:	%mkrel 1
Summary:	A handy personal organizer
License:	GPLv2+
Group:		Office
Url:		http://clayo.org/osmo
Source0:	http://downloads.sourceforge.net/osmo-pim/%{name}-%{version}.tar.gz
Patch0:		osmo-0.2.8-mdv-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	gtk+2-devel >= 2.10
BuildRequires:	gtkspell-devel >= 2.0.5
BuildRequires:	libical-devel >= 0.33
BuildRequires:	libtar-devel
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libgringotts-devel >= 1.2.1

%description
Osmo is a handy personal organizer, which includes calendar, tasks 
manager, address book and notes modules.

%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
%configure LIBICAL_CFLAGS=-I/usr/include/libical
%make

%install
rm -rf %{buildroot}
%makeinstall

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
%exclude %{_iconsdir}/hicolor/icon-theme.cache
%{_datadir}/sounds/%{name}
%{_mandir}/man1/%{name}.1*