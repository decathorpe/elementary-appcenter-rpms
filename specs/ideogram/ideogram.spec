%global appname com.github.cassidyjames.ideogram

Name:           ideogram
Summary:        Insert emoji anywhere, even in non-native apps
Version:        1.1.3
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/cassidyjames/%{name}
Source0:        https://github.com/cassidyjames/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

Requires:       hicolor-icon-theme


%description
Quickly insert emoji anywhere you can paste text, including non-native
apps. Hit Super+E to open the emoji picker, choose the emoji you want, and
it's instantly pasted.

Change the shortcut in System Settings →Keyboard → Shortcuts → Custom.


%prep
%autosetup


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
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Tue Dec 04 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1.3-1
- Initial packaging.

