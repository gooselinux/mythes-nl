Name: mythes-nl
Summary: Dutch thesaurus
%define upstreamid 20090708
Version: 0.%{upstreamid}
Release: 6%{?dist}
Source: http://www.opentaal.org/opentaalbank/thesaurus/download/thes_nl_v2.zip
Group: Applications/Text
URL: http://www.opentaal.org/opentaalbank/thesaurus
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: BSD or CC-BY
BuildArch: noarch

%description
Dutch thesaurus.

%prep
%setup -q -c

%build
for i in README_th_nl_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_nl_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_nl_NL_v2.dat
cp -p th_nl_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_nl_NL_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s th_nl_NL_v2.dat "th_"$lang"_v2.dat"
        ln -s th_nl_NL_v2.idx "th_"$lang"_v2.idx"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_nl_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Wed Apr 07 2010 Caolan McNamara <caolanm@redhat.com> - 0.20090708-6
- bump for tooling

* Tue Apr 06 2010 Caolan McNamara <caolanm@redhat.com> - 0.20090708-5
- Resolves: rhbz#553234 fix license

* Thu Jan 07 2010 Caolan McNamara <caolanm@redhat.com> - 0.20090708-4
- Resolves: rhbz#553234 fix license

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090708-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-2
- tidy spec

* Wed Jul 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Fri Jun 12 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090608-2
- extend coverage

* Mon Jun 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Wed Mar 25 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090325-1
- initial version
