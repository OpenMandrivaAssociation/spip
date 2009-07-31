%define	name	spip
%define	Name	SPIP
%define	version	2.0.8
%define	release	%mkrel 1
%define _requires_exceptions pear(SourceMap.class.php)


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	CMS tool for Internet
License:	GPL
Group:		System/Servers
Source0:	%{name}-v%{version}.zip
Source1:	%{name}.logrotate.bz2
Source2:	%{name}-apache.conf.bz2
URL:		http://www.spip.net/
BuildRequires:  apache-base >= 2.0.54-5mdk
Requires(pre):  mod_php >= 2.0.54-5mdk
Requires(pre):  apache >= 2.0.54-5mdk
Requires(pre):	rpm-helper
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
SPIP is a publishing system developed by the minirezo to manage the site
uZine. We provide it to anyone as a free software under GPL licence.
Therefore, you can use it freely for your own site, be it personnal,
co-operative, institutional or commercial.

To finish the installation, just go to http://localhost/spip/ecrire/

%prep
%setup -q -n %{name}
find . -name remove.txt -exec rm -f {} \;
find . -type f -exec chmod 644 {} \;
find . -name '*svn*' -exec rm -f {} \;

%build

%install
rm -rf $RPM_BUILD_ROOT

# install files
install -d -m 755 $RPM_BUILD_ROOT%{_var}/www/%{name}
cp -pR * $RPM_BUILD_ROOT%{_var}/www/%{name}

# logrotate
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}

# apache configuration
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/webapps.d
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%create_ghostfile /var/log/httpd/spip.log apache apache 640
%_post_webapp

%postun
%_postun_webapp

%files
%defattr(-,root,root)
%dir %{_var}/www/%{name}
%{_var}/www/%{name}/*.php
#%{_var}/www/%{name}/*.htc
%{_var}/www/%{name}/*.txt
%{_var}/www/%{name}/*.gif
%{_var}/www/%{name}/*.php
%{_var}/www/%{name}/config
%{_var}/www/%{name}/squelettes-dist
%{_var}/www/%{name}/ecrire/*
%{_var}/www/%{name}/local
%{_var}/www/%{name}/tmp
%{_var}/www/%{name}/prive
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf
%dir %attr(775,root,apache) %{_var}/www/%{name}/IMG
%dir %attr(775,root,apache) %{_var}/www/%{name}/ecrire
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}


