%global appname com.github.bleakgrey.transporter

Name:           Transporter
Summary:        Simple file sharing app using Magic Wormhole
Version:        1.3.3
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/bleakgrey/%{name}
Source0:        https://github.com/bleakgrey/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# patch appdata file to remove U+200B (Zero-Width Space) characters;
# they break libappstream-glib / glib2 XML parsing
Patch0:         00-appdata-remove-u200b-chars.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       contractor
Requires:       hicolor-icon-theme
Requires:       magic-wormhole
Requires:       pulseaudio-utils
Requires:       sound-theme-freedesktop

%description
Share your files between computers, fast and safe.

Your devices are identified by using identical "wormhole codes":
In general, the sending machine generates and displays the code, which
must then be typed into the receiving machine. The "wormhole codes" are
easily memorized and pronounced, perfectly suitable for realization in
speech.

This application is based on and fully compatible with CLI-only
magic-wormhole.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/contractor/%{appname}.contract
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Dec 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.3-1
- Initial packaging.

