%global srcname finewalls
%global project xenlism

Name:           %{project}-%{srcname}
Version:        2018.05.02
Release:        1%{?dist}
Summary:        Minimalism and Simplicity wallpapers for desktop.

License:        GPLv3+
URL:            https://%{project}.github.io/
Source0:        https://github.com/%{project}/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  coreutils


%description
xenlism is Computer Graphic And Programming project to make something better.
xenlism is about minimalism and realism.
xenlism finewalls is wallpapers for desktop environment.

%prep
%setup -qn%{srcname}-%{version}
# W: hidden-file-or-dir, E: zero-length
find Xenlism-Finewalls -name '.*' -print -delete
find gnome-background-properties -name '.*' -print -delete

# W: spurious-executable-perm


%build
# nothing

%install
# copied from upstream install script
install -dm755 %{buildroot}%{_datadir}
install -dm755 %{buildroot}%{_datadir}/backgrounds/Xenlism-Finewalls
cp -pr Xenlism-Finewalls %{buildroot}%{_datadir}/backgrounds/
find %{buildroot}%{_datadir}/backgrounds/Xenlism-Finewalls -type d -exec chmod 755 '{}' \;
find %{buildroot}%{_datadir}/backgrounds/Xenlism-Finewalls -type f -exec chmod 644 '{}' \;
install -dm755 %{buildroot}%{_datadir}/gnome-background-properties
cp -pr gnome-background-properties/* %{buildroot}%{_datadir}/gnome-background-properties
find %{buildroot}%{_datadir}/gnome-background-properties -type d -exec chmod 755 '{}' \;
find %{buildroot}%{_datadir}/gnome-background-properties -type f -exec chmod 644 '{}' \;



%post


%postun


%posttrans



%files
%license LICENSE
%doc README.md
%{_datadir}/backgrounds/Xenlism-Finewalls/
%{_datadir}/gnome-background-properties/*.xml




%changelog
* Mon May 14 2018 Nattapong Pullkhow <ixenatt@gmail.com> - 2018.05.02
- Fix Bugs


* Sat May 05 2018 Nattapong Pullkhow <ixenatt@gmail.com> - 2018.05
- Initial



