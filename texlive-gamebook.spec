# revision 24714
# category Package
# catalog-ctan /macros/latex/contrib/gamebook
# catalog-date 2011-11-29 16:55:00 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-gamebook
Version:	1.0
Release:	1
Summary:	Typeset gamebooks and other interactive novels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gamebook
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebook.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebook.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the means in order to lay-out gamebooks
with LaTeX. A simple gamebook example is included with the
package, and acts as a tutorial.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
