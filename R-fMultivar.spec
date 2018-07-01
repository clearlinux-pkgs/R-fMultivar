#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fMultivar
Version  : 3042.80
Release  : 1
URL      : https://cran.r-project.org/src/contrib/fMultivar_3042.80.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fMultivar_3042.80.tar.gz
Summary  : Rmetrics - Analysing and Modeling Multivariate Financial Return
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-cubature
Requires: R-fBasics
Requires: R-mvtnorm
Requires: R-sn
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-cubature
BuildRequires : R-fBasics
BuildRequires : R-mvtnorm
BuildRequires : R-sn
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : clr-R-helpers

%description
to manage, to investigate and to analyze bivariate and multivariate 
	data sets of financial returns.

%prep
%setup -q -c -n fMultivar

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530461261

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530461261
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fMultivar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fMultivar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fMultivar
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fMultivar|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fMultivar/DESCRIPTION
/usr/lib64/R/library/fMultivar/INDEX
/usr/lib64/R/library/fMultivar/Meta/Rd.rds
/usr/lib64/R/library/fMultivar/Meta/features.rds
/usr/lib64/R/library/fMultivar/Meta/hsearch.rds
/usr/lib64/R/library/fMultivar/Meta/links.rds
/usr/lib64/R/library/fMultivar/Meta/nsInfo.rds
/usr/lib64/R/library/fMultivar/Meta/package.rds
/usr/lib64/R/library/fMultivar/NAMESPACE
/usr/lib64/R/library/fMultivar/NEWS
/usr/lib64/R/library/fMultivar/R/fMultivar
/usr/lib64/R/library/fMultivar/R/fMultivar.rdb
/usr/lib64/R/library/fMultivar/R/fMultivar.rdx
/usr/lib64/R/library/fMultivar/help/AnIndex
/usr/lib64/R/library/fMultivar/help/aliases.rds
/usr/lib64/R/library/fMultivar/help/fMultivar.rdb
/usr/lib64/R/library/fMultivar/help/fMultivar.rdx
/usr/lib64/R/library/fMultivar/help/paths.rds
/usr/lib64/R/library/fMultivar/html/00Index.html
/usr/lib64/R/library/fMultivar/html/R.css
/usr/lib64/R/library/fMultivar/obsolete/R/utils-adapt.R
/usr/lib64/R/library/fMultivar/obsolete/man/utils-adapt.Rd
/usr/lib64/R/library/fMultivar/obsolete/src/adapt2.f
/usr/lib64/R/library/fMultivar/obsolete/src/adapt_callback.c
/usr/lib64/R/library/fMultivar/unitTests/Makefile
/usr/lib64/R/library/fMultivar/unitTests/runTests.R
/usr/lib64/R/library/fMultivar/unitTests/runit.BivariateBinning.R
/usr/lib64/R/library/fMultivar/unitTests/runit.BivariateDistributions.R
/usr/lib64/R/library/fMultivar/unitTests/runit.BivariateGridding.R
