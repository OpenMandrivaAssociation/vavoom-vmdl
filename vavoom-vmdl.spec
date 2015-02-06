%define	oname	vavoom
%define	name	%{oname}-vmdl
%define	version	1.4.3
%define release	3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Summary:	VMDL files for %{oname}
Group:		Games/Arcade
License:	GPL
URL:		http://vavoom-engine.com/
Source0:	http://dl.sourceforge.net/vavoom/vmodels-doom-%{version}.zip
Source1:	http://dl.sourceforge.net/vavoom/vmodels-heretic-%{version}.zip
Source2:	http://dl.sourceforge.net/vavoom/vmodels-hexen-%{version}.zip
Source3:	http://dl.sourceforge.net/vavoom/vmodels-strife-%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	%{oname}

%description
3D model files to replace many of the game sprites.

%prep
%setup -q -c -b 1 -b 2 -b 3 -n %{name}-%{version}

%build
# Move the documentation files around to make it easier for packaging
for i in doom heretic hexen strife ; do
    mkdir $i
    mv basev/$i/*.txt $i
done

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/%{oname}
cp -ar basev %{buildroot}%{_gamesdatadir}/%{oname}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_gamesdatadir}/%{oname}/basev/doom
%{_gamesdatadir}/%{oname}/basev/strife
%{_gamesdatadir}/%{oname}/basev/heretic
%{_gamesdatadir}/%{oname}/basev/hexen
%doc doom heretic hexen strife




%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1:1.4.3-2mdv2010.0
+ Revision: 445655
- rebuild

* Tue Nov 11 2008 Zombie Ryushu <ryushu@mandriva.org> 1:1.4.3-1mdv2009.1
+ Revision: 302218
- Version bump.
- Version bump to 1.4.3 for Vavoom 1.29

* Sun Oct 26 2008 Stéphane Téletchéa <steletch@mandriva.org> 1:1.4.2-1mdv2009.1
+ Revision: 297442
- Update to latest release

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:1.3.1-4mdv2009.0
+ Revision: 261836
- rebuild
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1:1.3.1-1mdv2008.1
+ Revision: 128868
- kill re-definition of %%buildroot on Pixel's request


* Mon Jan 22 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.3.1-1mdv2007.0
+ Revision: 111952
- epoch to handle different versioning
- new release: 1.3.1
- Import vavoom-vmdl

* Thu Aug 10 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.20-2mdv2007.0
- fix file permissions

* Fri Aug 04 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.20-1mdv2007.0
- initial release baed on fedora package

* Sun Jun 04 2006 Wart <wart at kobold dot org> 1.20-1
- Initial Fedora Extras package

