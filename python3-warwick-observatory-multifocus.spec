Name:           python3-warwick-observatory-multifocus
Version:        20221016
Release:        0
License:        GPL3
Summary:        Common backend code for multi-channel focuser daemon
Url:            https://github.com/warwick-one-metre/multifocusd
BuildArch:      noarch

%description

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
