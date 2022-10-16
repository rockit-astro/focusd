Name:      observatory-multifocus-server
Version:   20221016
Release:   0
Url:       https://github.com/warwick-one-metre/multifocusd
Summary:   Multi-channel focuser control server.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-pyserial python3-warwick-observatory-common python3-warwick-observatory-multifocus

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/focusd/

%{__install} %{_sourcedir}/focusd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/focusd@.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/focusd
%defattr(0644,root,root,-)
%{_unitdir}/focusd@.service

%changelog
