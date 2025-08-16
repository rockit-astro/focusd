Name:      rockit-focuser-multichannel
Version:   %{_version}
Release:   1
Summary:   Focuser.
Url:       https://github.com/rockit-astro/focusd-multichannel
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/focusd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/focus %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/multichannel_focusd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/multichannel_focusd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/focus %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/clasp.json %{buildroot}%{_sysconfdir}/focusd/
%{__install} %{_sourcedir}/10-clasp-focuser.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/halfmetre.json %{buildroot}%{_sysconfdir}/focusd/
%{__install} %{_sourcedir}/10-halfmetre-focuser.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/portable.json %{buildroot}%{_sysconfdir}/focusd/
%{__install} %{_sourcedir}/10-portable-focuser.rules %{buildroot}%{_udevrulesdir}

%package server
Summary:  Focuser control server.
Group:    Unspecified
Requires: python3-rockit-focuser-multichannel
%description server

%package client
Summary:  Focuser control client.
Group:    Unspecified
Requires: python3-rockit-focuser-multichannel
%description client

%package data-clasp
Summary: Focuser data for CLASP telescope
Group:   Unspecified
%description data-clasp

%package data-halfmetre
Summary: Focuser data for the half metre telescope
Group:   Unspecified
%description data-halfmetre

%package data-portable
Summary: Focuser data for the portable telescope
Group:   Unspecified
%description data-portable

%files server
%defattr(0755,root,root,-)
%{_bindir}/multichannel_focusd
%defattr(0644,root,root,-)
%{_unitdir}/multichannel_focusd@.service

%files client
%defattr(0755,root,root,-)
%{_bindir}/focus
/etc/bash_completion.d/focus

%files data-clasp
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-clasp-focuser.rules
%{_sysconfdir}/focusd/clasp.json

%files data-halfmetre
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-halfmetre-focuser.rules
%{_sysconfdir}/focusd/halfmetre.json

%files data-portable
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-portable-focuser.rules
%{_sysconfdir}/focusd/portable.json

%changelog
