%global appname com.github.philip-scott.notes-up

Name:           Notes-up
Summary:        Markdown notes editor & manager
Version:        2.0.0
Release:        1%{?dist}
License:        GPLv2+ and BSD

URL:            https://github.com/Philip-Scott/Notes-up
Source0:        https://github.com/Philip-Scott/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.39.0

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       contractor
Requires:       hicolor-icon-theme

Provides:       bundled(highlight.js) = 9.10.0


%description
Notes Up is a notes manager written for elementary. With it, you'll be
able to write beautiful notes fast and easy using the markdown format.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang notes-up


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f notes-up.lang
%doc README.md
%license LICENSE
%license data/assets/highlightjs/highlight.LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/org.notes.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/notes-up/


%changelog
* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Update to version 2.0.0.

* Mon Feb 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.6.3-2
- Add missing contractor dependency.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.3-1
- Update to version 1.6.3.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.2-1
- Update to version 1.6.2.

* Mon Sep 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.1-1
- Update to version 1.6.1.

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.6.0-1
- Update to version 1.6.0.

* Sat Sep 08 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.2-1.20180819git532fa3b
- Initial package for fedora.

