%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Minimal XML parser & printer for OCaml
Name:		ocaml-xml-light
Version:	2.4
Release:	1
License:	LGPLv2.1+
Group:		Development/Other
Url:		https://github.com/ncannasse/xml-light
Source0:	xml-light-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler

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
%{_libdir}/ocaml/xml-light/*.cmxs

%prep
%autosetup -n xml-light-%{version}
chmod 644 README *.mli || :

%build
%make_build all
%make_build opt

%install
install -d %{buildroot}%{_libdir}/ocaml/xml-light
%make_install INSTALLDIR=%{buildroot}%{_libdir}/ocaml/xml-light

cat > %{buildroot}%{_libdir}/ocaml/xml-light/META <<'METAEOF'
version = "2.4"
description = "Minimal XML parser & printer for OCaml"
archive(byte) = "xml-light.cma"
archive(native) = "xml-light.cmxa"
plugin(native) = "xml-light.cmxs"
METAEOF
