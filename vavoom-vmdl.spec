%define	oname	vavoom
%define	name	%{oname}-vmdl
%define	version	1.3.1
%define	release	%mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Epoch:		1
Summary:        VMDL files for %{oname}
Group:          Games/Arcade
License:	GPL
URL:		http://vavoom-engine.com/
Source0:	http://dl.sourceforge.net/vavoom/vmdl_doom_13-1.zip
Source1:	http://dl.sourceforge.net/vavoom/vmdl_heretic_13.zip
Source2:	http://dl.sourceforge.net/vavoom/vmdl_hexen_13-1.zip
Source3:	http://dl.sourceforge.net/vavoom/vmdl_strife_13.zip
BuildArch:      noarch
Requires:	%{oname}

%description
3D model files to replace many of the game sprites.

%prep
%setup -q -c -b 1 -b 2 -b 3 -n %{name}-%{version}

%build
# Move the documentation files around to make it easier for packaging
for i in doom heretic hexen strife ; do
    mkdir $i
    mv basev/$i/models/*.txt $i
done

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/%{oname}
cp -ar basev %{buildroot}%{_gamesdatadir}/%{oname}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_gamesdatadir}/%{oname}/basev/doom/models
%{_gamesdatadir}/%{oname}/basev/strife/models
%{_gamesdatadir}/%{oname}/basev/heretic/models
%{_gamesdatadir}/%{oname}/basev/hexen/models
%doc doom heretic hexen strife


