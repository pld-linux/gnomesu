Summary:	GNOME SuperUser is a GTK frontend to su
Summary(pl):	GNOME SuperUser jest graficzn± nak³adk± na program su
Name:		gnomesu
Version:	0.3.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/xsu/%{name}-%{version}.tar.gz
# Source0-md5:	8ebcf248b4f8430c96d80379ec2acdd8
Patch0:		%{name}-desktop.patch
URL:		http://xsu.sourceforge.net/
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libzvt-devel >= 1.0
Requires:	/bin/su
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME SuperUser is a GTK frontend to su and as such an easy way to run
a program as root in the GNOME environment. It is based on xsu.

%description -l pl
GNOME SuperUser jest graficzn± nak³adk± na program su, bazuj±c± na
xsu. Aplikacja pozwala w prosty sposób uruchamiaæ programy z prawami
roota w ¶rodowisku GNOME.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/%{name}.1*
