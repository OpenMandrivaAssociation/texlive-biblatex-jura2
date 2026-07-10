%global tl_name biblatex-jura2
%global tl_revision 64762

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Citation style for the German legal profession
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-jura2
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-jura2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-jura2.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers BibLaTeX support for citations in German legal texts.

