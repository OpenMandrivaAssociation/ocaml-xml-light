%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Minimal XML parser & printer for OCaml
Name:		ocaml-xml-light
Version:	2.2
Release:	19
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://tech.motion-twin.com/xmllight.html
Source0:	http://tech.motion-twin.com/zip/xml-light.tar.bz2
Patch0:		%{name}-2.2-fix-build.patch
BuildRequires:	ocaml

%description
Xml-Light is a minimal XML parser & printer for OCaml. 
It provide functions to parse an XML document into an OCaml data structure, 
work with it, and print it back to an XML document. 
It support also DTD parsing and checking, and is entirely written in OCaml, 
hence it does not require additional C library.

%files
%doc README
%dir %{_libdir}/ocaml/xml-light
%{_libdir}/ocaml/xml-light/*.cmi
%{_libdir}/ocaml/xml-light/*.cma
%{_libdir}/ocaml/xml-light/META

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
This package contains the development files needed to build applications
using %{name}.

%files devel
%{_libdir}/ocaml/xml-light/*.a
%{_libdir}/ocaml/xml-light/*.cmx
%{_libdir}/ocaml/xml-light/*.cmxa
%{_libdir}/ocaml/xml-light/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n xml-light
%patch0 -p 1
chmod 644 README *.mli
perl -pi -e 's/\015$//' README

%build
make

%install
install -d %{buildroot}%{_libdir}/ocaml/xml-light
make install INSTALLDIR=%{buildroot}%{_libdir}/ocaml/xml-light

cat > %{buildroot}%{_libdir}/ocaml/xml-light/META <<EOF
version = "%{version}"
description = "Minimal XML parser & printer for OCaml"
archive(byte) = "xml-light.cma"
archive(native) = "xml-light.cmxa"
EOF


