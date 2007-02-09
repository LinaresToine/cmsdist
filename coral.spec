### RPM cms coral CORAL_1_6_3a-p1
## IMPORT configurations
Provides: /bin/zsh
Requires: coral-tool-conf

%define toolconf       ${CORAL_TOOL_CONF_ROOT}/configurations/tools-STANDALONE.conf
%define cvsprojuc      %(echo %n | sed -e "s|-debug||"| tr 'a-z' 'A-Z')
%define cvsprojlc      %(echo %cvsprojuc | tr 'A-Z' 'a-z')
%define cvsdir         %cvsprojlc
%define cvsserver      %cvsprojlc
%define cvsconfig      config
%define confversion    %cmsConfiguration
%define conflevel      %{nil}
%define prebuildtarget prebuild
%define buildtarget    release-build
%define bootstrapfile  %_builddir/%{cvsconfig}/%{cvsprojuc}_bootsrc
%define reqfile        %_builddir/%{cvsconfig}/%{cvsprojuc}_requirements

## IMPORT lcg-scram-build
## IMPORT scramv1-build
