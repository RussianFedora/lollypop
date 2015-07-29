Name: lollypop
Version: 0.9.42
Release: 1%{?dist}
Summary: Music player for GNOME

License: GPLv3+
URL: http://gnumdk.github.io/lollypop/
Source0: https://github.com/gnumdk/lollypop/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0: %{name}-fix-non-executable-script.patch
Patch1: %{name}-invalid-appdata-file.patch

BuildArch: noarch

BuildRequires: gobject-introspection-devel
BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: itstool

Requires: gstreamer1-plugins-base, gstreamer1
Requires: gobject-introspection
Requires: libnotify >= 0.7.6
Requires: python3-gobject
Requires: python3-cairo
Requires: python3-dbus
Requires: gdk-pixbuf2
Requires: pango
Requires: gtk3

%description
Lollypop is a new GNOME music playing application.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS TODO
%license COPYING 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.*.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/*/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-symbolic.svg
%{python3_sitelib}/%{name}

%changelog
* Wed Jul 29 2015 Maxim Orlov <murmansksity@gmail.com> - 0.9.42-1
- Initial package.
