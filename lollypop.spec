%global gobject_introspection_version 1.35.9
%global gtk3_version 3.12

Name:          lollypop
Version:       0.9.81
Release:       1%{?dist}
Summary:       A music player for GNOME

License:       GPLv3+
URL:           http://gnumdk.github.io/lollypop-web/
Source0:       https://github.com/gnumdk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:     noarch

BuildRequires: intltool
BuildRequires: itstool
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: python3-devel
# check
BuildRequires: /usr/bin/appstream-util
BuildRequires: /usr/bin/desktop-file-validate

Requires:      gdk-pixbuf2
Requires:      gobject-introspection >= %{gobject_introspection_version}
Requires:      gstreamer1
Requires:      gstreamer1-plugins-base
Requires:      gtk3 >= %{gtk3_version}
Requires:      libnotify >= 0.7.6
Requires:      pango
Requires:      python3-cairo
Requires:      python3-gobject
Requires:      python3-dbus
# wikipedia, last.fm support
Requires:      python3-wikipedia >= 1.4.0
Requires:      python3-pylast >= 1.4.2

%description
Lollypop is a new GNOME music playing application.

%prep
%autosetup

%build
%configure
%make_build V=1

%install
%make_install

%find_lang %{name} --with-gnome

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
%doc AUTHORS TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-symbolic.svg
%{python3_sitelib}/%{name}

%changelog
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
