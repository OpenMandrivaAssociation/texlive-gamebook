Name:		texlive-gamebook
Version:	24714
Release:	2
Summary:	Typeset gamebooks and other interactive novels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gamebook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebook.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the means in order to lay-out gamebooks
with LaTeX. A simple gamebook example is included with the
package, and acts as a tutorial.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gamebook/gamebook.sty
%doc %{_texmfdistdir}/doc/latex/gamebook/README
%doc %{_texmfdistdir}/doc/latex/gamebook/gamebook-example.pdf
%doc %{_texmfdistdir}/doc/latex/gamebook/gamebook-example.tex
%doc %{_texmfdistdir}/doc/latex/gamebook/gamebook.pdf
%doc %{_texmfdistdir}/doc/latex/gamebook/lppl.txt
#- source
%doc %{_texmfdistdir}/source/latex/gamebook/gamebook.dtx
%doc %{_texmfdistdir}/source/latex/gamebook/gamebook.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
