%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from net-ssh-2.1.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname net-ssh
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
Name: ruby-enterprise-rubygem-%{gemname}
Version: 2.1.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/net-ssh/net-ssh
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/THANKS.rdoc
%doc %{geminstdir}/CHANGELOG.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 2.1.4-1.hhg
- Rebuild for Ruby Enterprise Edition

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 2.1.4-1
- Initial package
