%global appname com.github.lainsce.aesop

Name:           aesop
Summary:        Simplest PDF viewer around
Version:        1.0.7
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/lainsce/%{name}
Source0:        https://github.com/lainsce/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(poppler-glib)

Requires:       hicolor-icon-theme


%description
The simplest PDF viewer around.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sat Oct 06 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.7-1
- Update to version 1.0.7.

* Tue Sep 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Update to version 1.0.6.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Initial package for fedora.


