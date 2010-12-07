%define	name	spip
%define	Name	SPIP
%define	version	2.0.10
%define	release	%mkrel 3
%define _requires_exceptions pear(SourceMap.class.php)


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	CMS tool for Internet
License:	GPL
Group:		System/Servers
URL:		http://www.spip.net/
Source0:	%{name}-v%{version}.zip
Source1:	%{name}.logrotate.bz2
Source2:	%{name}-apache.conf.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

# install files
install -d -m 755 %{buildroot}%{_var}/www/%{name}
cp -pR * %{buildroot}%{_var}/www/%{name}

# logrotate
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# apache configuration
install -d -m 755 %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
bzcat %{SOURCE2} > %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf

%clean
rm -rf %{buildroot}

%post
%create_ghostfile /var/log/httpd/spip.log apache apache 640
%if %mdkversion < 201010
%_post_webapp
%endif

%postun
%if %mdkversion < 201010
%_postun_webapp
%endif

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


