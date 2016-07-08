%global gobject_introspection_version 1.35.9
%global gtk3_version 3.14

Name:           lollypop
Version:        0.9.112
Release:        1%{?dist}
Summary:        A music player for GNOME

License:        GPLv3+
URL:            http://gnumdk.github.io/lollypop-web/
Source0:        https://github.com/gnumdk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  intltool >= 0.26
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel

Requires:       gdk-pixbuf2
Requires:       gobject-introspection >= %{gobject_introspection_version}
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gtk3 >= %{gtk3_version}
Requires:       hicolor-icon-theme
#Requires:       kid3-common
Requires:       libnotify >= 0.7.6
Requires:       pango
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-pylast >= 1.4.2
Requires:       python3-wikipedia >= 1.4.0
Requires:       totem-pl-parser

%description
Lollypop is a new GNOME music playing application.

%prep
%autosetup

%build
%configure
%make_build V=1

%install
%make_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/help/*/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-symbolic.svg
%{python3_sitelib}/%{name}

%changelog
* Fri Jul 08 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.112-1
- Update to 0.9.112

* Tue Jul 05 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.111-1
- Update to 0.9.111
- Added R: hicolor-icon-theme

* Sun Jun 12 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.110-1
- Update to 0.9.110

* Fri Jun 10 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.109-1
- Update to 0.9.109

* Fri Jun 10 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.108-1
- Update to 0.9.108

* Wed May 18 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.107-1
- Update to 0.9.107

* Fri May 13 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.106-1
- Update to 0.9.106

* Wed May 11 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.105-1
- Update to 0.9.105

* Fri May 06 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.104-1
- Update to 0.9.104

* Wed May 04 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.103-1
- Update to 0.9.103

* Sun May 01 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.101-1
- Update to 0.9.101

* Fri Apr 29 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.100-1
- Update to 0.9.100

* Thu Apr 28 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.99-1
- Update to 0.9.99

* Wed Apr 20 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.98-1
- Update to 0.9.98

* Tue Apr 19 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.97-1
- Update to 0.9.97

* Mon Apr 18 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.96-1
- Update to 0.9.96

* Mon Apr 11 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.95-1
- Update to 0.9.95

* Wed Apr 06 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.94-1
- Update to 0.9.94

* Tue Apr 05 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.93-1
- Update to 0.9.93

* Mon Apr 04 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.92-1
- Update to 0.9.92

* Tue Mar 22 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.91-1
- Update to 0.9.91

* Mon Mar 21 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.90-1
- Update to 0.9.90
- Update gtk3 dep version
- Added R: totem-pl-parser

* Wed Feb 17 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.87-1
- Update to 0.9.87

* Tue Feb 16 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.86-1
- Update to 0.9.86

* Tue Feb 09 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.85-1
- Update to 0.9.85

* Mon Feb 08 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.84-1
- Update to 0.9.84

* Thu Feb 04 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.83-1
- Update to 0.9.83

* Wed Feb 03 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.82-1
- Update to 0.9.82

* Tue Feb 02 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.81-1
- Update to 0.9.81

* Mon Feb 01 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.80-1
- Update to 0.9.80

* Thu Jan 14 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.77-1
- Update to 0.9.77

* Mon Jan 11 2016 Maxim Orlov <murmansksity@gmail.com> - 0.9.76-1
- Update to 0.9.76

* Mon Dec 07 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.75-1
- Update to 0.9.75

* Fri Dec 04 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.74-1
- Update to 0.9.74

* Wed Dec 02 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.72-1
- Update to 0.9.72

* Tue Dec 01 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.71-1
- Update to 0.9.71

* Tue Dec 01 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.70-2
- Added R: python3-pylast

* Fri Nov 27 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.70-1
- Update to 0.9.70

* Tue Oct 27 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.62-1
- Update to 0.9.62

* Mon Oct 26 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.61-1
- Update to 0.9.61

* Tue Oct 20 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9-60-2
- fix E: non-executable-script

* Tue Oct 20 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9-60-1
- Update to 0.9.60

* Sun Oct 04 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.52-1
- Update to 0.9.52

* Fri Oct 02 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.51-1
- Update to 0.9.51

* Thu Oct 01 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.50-1
- Update to 0.9.50
- Validate AppData during check
- Cleanup spec

* Wed Jul 29 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.42-1
- Initial package.
