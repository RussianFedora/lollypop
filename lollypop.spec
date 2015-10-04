Name:          lollypop
Version:       0.9.52
Release:       1%{?dist}
Summary:       A music player for GNOME

License:       GPLv3+
URL:           http://gnumdk.github.io/lollypop-web/
Source0:       https://github.com/gnumdk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:     noarch

BuildRequires: intltool
BuildRequires: itstool
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: python3-devel
# check
BuildRequires: /usr/bin/appstream-util
BuildRequires: /usr/bin/desktop-file-validate

Requires:      gdk-pixbuf2
Requires:      gobject-introspection
Requires:      gstreamer1
Requires:      gstreamer1-plugins-base
Requires:      gtk3
Requires:      python3-cairo
Requires:      pango
Requires:      python3-gobject
Requires:      python3-dbus

%description
Lollypop is a new GNOME music playing application.

%prep
%setup -q

%build
%configure --disable-silent-rules
%make_build

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
