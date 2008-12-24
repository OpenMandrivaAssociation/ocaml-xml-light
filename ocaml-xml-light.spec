%define base_name	xml-light
%define name		ocaml-%{base_name}
%define version		2.2
%define release		%mkrel 16

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Minimal XML parser & printer for OCaml
URL:		http://tech.motion-twin.com/xmllight.html
Source: 	http://tech.motion-twin.com/zip/%{base_name}.tar.bz2
Patch:      %{name}-2.2-fix-build.patch
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Xml-Light is a minimal XML parser & printer for OCaml. 
It provide functions to parse an XML document into an OCaml data structure, 
work with it, and print it back to an XML document. 
It support also DTD parsing and checking, and is entirely written in OCaml, 
hence it does not require additional C library.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{base_name}
%patch -p 1
chmod 644 README *.mli
perl -pi -e 's/\015$//' README

%build
make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}/ocaml/xml-light
make install INSTALLDIR=%{buildroot}%{_libdir}/ocaml/xml-light

cat > %{buildroot}%{_libdir}/ocaml/xml-light/META <<EOF
version = "%{version}"
description = "Minimal XML parser & printer for OCaml"
archive(byte) = "xml-light.cma"
archive(native) = "xml-light.cmxa"
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{_libdir}/ocaml/xml-light
%{_libdir}/ocaml/xml-light/*.cmi
%{_libdir}/ocaml/xml-light/*.cma
%{_libdir}/ocaml/xml-light/META

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/xml-light/*.a
%{_libdir}/ocaml/xml-light/*.cmx
%{_libdir}/ocaml/xml-light/*.cmxa
%{_libdir}/ocaml/xml-light/*.mli
