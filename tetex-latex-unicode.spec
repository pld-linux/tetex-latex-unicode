# TODO:
#  - package more files

%define	short_name	unicode
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Extended UTF-8 input encoding for LaTeX
Summary(pl):	Rozszerzone kodowanie wej¶ciowe UTF-8 dla LaTeXa
Name:		tetex-latex-%{short_name}
Version:	1.0.0
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://www.ctan.org/tex-archive/macros/latex/contrib/%{short_name}.zip
# Source0-md5:	d1391421f826743b59d1833620e0166f
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This bundle provides the ucs package, and utf8x.def, together with a
large number of support files.

The utf8x.def definition file for use with inputenc covers a wider
range of Unicode characters than does utf8.def in the LaTeX
distribution. The ucs package provides facilities for efficient use of
large sets of Unicode characters.

%description -l pl
Ten pakiet dostarcza pakietów ucs oraz utf8x.def, razem z du¿± liczb±
plików pomocniczych.

Plik definicji utf8x.def do u¿ywania z inputenc pokrywa szerszy zakres
znaków Unicode ni¿ utf8.def w dystrybucji LaTeXa. Pakiet ucs u³atwia
sprawne korzystanie z du¿ych zbiorów znaków Unicode.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install ucs.sty ucsencs.def utf8x.def $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
cp -a data $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc FAQ INSTALL README VERSION
%{_datadir}/texmf/tex/latex/%{short_name}
