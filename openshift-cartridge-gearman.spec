%global cartridgedir %{_libexecdir}/openshift/cartridges/gearman

Summary:       Provides embedded Gearman support
Name:          openshift-cartridge-gearman
Version:       1.0.0
Release:       2%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://www.gearman.org
Source0:       %{name}-%{version}.tar.gz
Requires:      gearmand >= 1.1
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-cartridge-gearman = 1.1
BuildArch:     noarch

%description
Provides Gearman cartridge support to OpenShift.

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__rm -rf %{buildroot}%{cartridgedir}/rel-eng

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}/metadata
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE.txt

%changelog
* Mon Mar 02 2015 Builder <getup@getupcloud.com> 1.0.0-2
- fix spec

* Mon Mar 02 2015 Builder <getup@getupcloud.com> 1.0.0-1
- new package built with tito

