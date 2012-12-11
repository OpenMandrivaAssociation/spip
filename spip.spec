%define	Name	SPIP

%if %{_use_internal_dependency_generator}
%define __noautoreq 'pear(SourceMap.class.php)'
%else
%define _requires_exceptions pear(SourceMap.class.php)
%endif


Name:		spip
Version:	2.1.1
Release:	2
Summary:	CMS tool for Internet
License:	GPLv2+
Group:		System/Servers
URL:		http://www.spip.net/
Source0:	%{name}-v%{version}.zip
Source1:	%{name}.logrotate.bz2
Source2:	%{name}-apache.conf.bz2
BuildArch:	noarch

%description
SPIP is a publishing system developed by the minirezo to manage the site
uZine. We provide it to anyone as a free software under GPL licence.
Therefore, you can use it freely for your own site, be it personnal,
co-operative, institutional or commercial.

To finish the installation, just go to http://localhost/spip/ecrire/

%prep
%setup -q 
find . -name remove.txt -exec rm -f {} \;
find . -type f -exec chmod 644 {} \;
find . -name '*svn*' -exec rm -f {} \;

%build
:

%install
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


%files
%defattr(-,root,root)
%dir %{_var}/www/%{name}
%{_var}/www/%{name}/*.php
#%{_var}/www/%{name}/*.htc
%{_var}/www/%{name}/*.txt
%{_var}/www/%{name}/*.gif
%{_var}/www/%{name}/config
%{_var}/www/%{name}/squelettes-dist
%{_var}/www/%{name}/ecrire/*
%{_var}/www/%{name}/local
%{_var}/www/%{name}/tmp
%{_var}/www/%{name}/prive
%{_var}/www/%{name}/mutualisation/*
%{_var}/www/%{name}/extensions/*
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf
%dir %attr(775,root,apache) %{_var}/www/%{name}/IMG
%dir %attr(775,root,apache) %{_var}/www/%{name}/ecrire
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}




%changelog
* Mon May 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 2.1.1-1mdv2011.0
+ Revision: 677575
- clean spec
- new version 2.1.1
- fix %%prep
- update file list

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.10-3mdv2011.0
+ Revision: 614948
- the mass rebuild of 2010.1 packages

* Tue Jan 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.10-2mdv2010.1
+ Revision: 493886
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise

* Sun Dec 13 2009 Olivier Thauvin <nanardon@mandriva.org> 2.0.10-1mdv2010.1
+ Revision: 478141
- 2.0.10

* Sun Aug 09 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.9-1mdv2010.0
+ Revision: 412965
- Update to new version 2.0.9

* Fri Jul 31 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.8-1mdv2010.0
+ Revision: 405232
- Update to new version 2.0.8

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 2.0-1mdv2009.1
+ Revision: 332878
- New upstream release

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.9.2c-4mdv2009.0
+ Revision: 260950
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.9.2c-3mdv2009.0
+ Revision: 252951
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 13 2007 Anne Nicolas <ennael@mandriva.org> 1.9.2c-1mdv2008.1
+ Revision: 119561
- New version, fix security issues

* Tue Aug 14 2007 Anne Nicolas <ennael@mandriva.org> 1.9.2-2mdv2008.0
+ Revision: 63505
- Fix description typo (#30944)


* Tue Feb 27 2007 Anne Nicolas <anne.nicolas@mandriva.com> 1.9.2-1mdv2007.0
+ Revision: 126187
- New version
- Correct pear
- Import spip

* Thu Oct 12 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.9.1-2mdk
- new revision

* Mon Sep 11 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.9.1-1mdk
- new version : new tags and filters, bug fixes

* Sun Jul 02 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.9.0-3mk
- fix postinstall and delete order

* Sun Jul 02 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.9.0-2mk
- add apache configuration

* Sun Jul 02 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.9.0-1mk
- new version
- use /var/www as web root

* Sat Mar 18 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.8.3-1mdk
- new version

* Wed Feb 15 2006 Anne Nicolas <anne.nicolas@mandriva.com> 1.8.2-2mdk
- new version : bugs fix

* Sat Oct 22 2005 Anne Nicolas <anne.nicolas@mandriva.com> 1.8.2-1mdk
- new version
- clean spec

* Mon Apr 18 2005 ANne Nicolas <anne.nicolas@mandriva.com> 1.8-1mdk
- new version

* Fri Feb 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.7.2-2mdk
- spec file cleanups, remove the ADVX-build stuff

* Thu Jul 08 2004 Anne Nicolas <anne@mandrake.org> 1.7.2-1mdk
- new version

* Tue Apr 27 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.7.1-3mdk
- fix install (cpjc <cpjc@free.fr>)

* Wed Apr 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.7.1-2mdk
- fix order
- fix changelog
- user rpm-helper facility to create empty files

* Wed Apr 21 2004 Anne Nicolas <anne@lea-linux.org> 1.7.1-1mdk
- new release

