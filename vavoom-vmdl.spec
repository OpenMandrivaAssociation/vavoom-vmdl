%define	oname	vavoom
%define	name	%{oname}-vmdl
%define	version	1.4.3
%define	release	%mkrel 1

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


