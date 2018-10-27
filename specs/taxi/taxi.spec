%global appname     com.github.alecaddd.taxi

%global forgeurl    https://github.com/Alecaddd/taxi
%global tag         v0.0.1

Name:           taxi
Summary:        FTP Client that drives you anywhere
Version:        0.0.1
Release:        1%{?dist}
License:        LGPLv3+

%forgemeta

URL:            %{forgeurl}
Source0:        https://github.com/Alecaddd/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libsoup-2.4)

Requires:       hicolor-icon-theme


%description
Taxi is a native Linux FTP client built in Vala and Gtk originally
created by Kiran John Hampal. It allows you to connect to a remote
server with various Protocols (FTP, SFT, etc.), and offers an handy
double paned interface to quickly transfer files and folders between
your computer and the server.


%prep
%forgeautosetup -p1


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
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.0.1-1
- Initial package for fedora.

