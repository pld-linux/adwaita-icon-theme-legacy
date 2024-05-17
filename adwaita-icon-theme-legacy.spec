Summary:	Adwaita legacy fullcolor icons
Summary(pl.UTF-8):	Dawne pełnokolorowe ikony Adwaita
Name:		adwaita-icon-theme-legacy
Version:	46.2
Release:	1
License:	LGPL v3 or CC-BY-SA v3.0
Group:		Themes
Source0:	https://download.gnome.org/sources/adwaita-icon-theme-legacy/46/%{name}-%{version}.tar.xz
# Source0-md5:	9195eaeac4197d68a9271f1d5dd53452
URL:		https://www.gnome.org/
BuildRequires:	gtk-update-icon-cache
BuildRequires:	meson >= 0.64.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post):	gtk-update-icon-cache >= 3.14
Conflicts:	gnome-themes-standard < 3.14
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fullcolor icon theme providing fallback for legacy apps.

%description -l pl.UTF-8
Pełnokolorowy motyw ikon zapewniający rezerwę dla dawnych aplikacji.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# packaged as %doc or in common licenses
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/licenses

> $RPM_BUILD_ROOT%{_iconsdir}/AdwaitaLegacy/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache AdwaitaLegacy

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%dir %{_iconsdir}/AdwaitaLegacy
%{_iconsdir}/AdwaitaLegacy/index.theme
%{_iconsdir}/AdwaitaLegacy/[0-9]*x[0-9]*
%ghost %{_iconsdir}/AdwaitaLegacy/icon-theme.cache
%{_npkgconfigdir}/adwaita-icon-theme-legacy.pc
