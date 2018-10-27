%global appname com.github.bartzaalberg.alias

Name:           alias
Summary:        Simplify your commands
Version:        0.1.2
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/bartzaalberg/alias
Source0:        https://github.com/bartzaalberg/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme


%description
Alias is a tool to manage your bash aliases.


%prep
%autosetup -p1


%build
mkdir build

pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

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
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Initial package for fedora.

