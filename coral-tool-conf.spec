### RPM cms coral-tool-conf CMS_144a
# DO NOT MODIFY. This spec file is automatically generated by executing src/createConfSpecs.sh in the 
# main directory. Modify src/toolConfiguration.xsl if needed.

# We set a special variable TOOLCONF_VERSION which is then used by scram-build.file and scramv1-build.file to
# check out the correct toolbox. Notice that all the *-tool-conf.spec set the same variable so this is 
# relevant only for build time and not for runtime.
## INITENV SET TOOLCONF_VERSION %{v}
Source0: none

Requires: seal
Requires: oracle
Requires: oracle-env
Requires: p5-dbd-oracle

Requires: sqlite
Requires: mysql
Requires: frontier_client
Requires: expat
Requires: xerces-c
Requires: zlib
Requires: gcc

Requires: pcre
Requires: uuid
Requires: python
Requires: boost
Requires: cppunit
%prep
%build
(echo "ARCHITECTURE:%{cmsplatf}"
 echo "SCRAM_BASEPATH:%{instroot}/external"

echo "TOOL:seal:"
echo "  +SEAL_BASE:$SEAL_ROOT"

echo "TOOL:oracle:"
echo "  +ORACLE_BASE:$ORACLE_ROOT"
echo "  +PATH:$ORACLE_ROOT/bin"
echo "  +LIBDIR:$ORACLE_ROOT/lib"
echo "  +INCLUDE:$ORACLE_ROOT/include"
echo "  +ORACLE_ADMINDIR:$ORACLE_ENV_ROOT/etc"


echo "TOOL:sqlite:"
eval "echo \"  +SQLITE_BASE:\${SQLITE_ROOT}\""
eval "echo \"  +PATH:\${SQLITE_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${SQLITE_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${SQLITE_ROOT}/include\""

echo "TOOL:mysql:"
eval "echo \"  +MYSQL_BASE:\${MYSQL_ROOT}\""
eval "echo \"  +PATH:\${MYSQL_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${MYSQL_ROOT}/lib/mysql\""
eval "echo \"  +INCLUDE:\${MYSQL_ROOT}/include/mysql\""


echo "TOOL:frontier_client:"
eval "echo \"  +FRONTIER_CLIENT_BASE:\${FRONTIER_CLIENT_ROOT}\""
eval "echo \"  +PATH:\${FRONTIER_CLIENT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${FRONTIER_CLIENT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${FRONTIER_CLIENT_ROOT}/include\""


echo "TOOL:expat:"
eval "echo \"  +EXPAT_BASE:\${EXPAT_ROOT}\""
eval "echo \"  +PATH:\${EXPAT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${EXPAT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${EXPAT_ROOT}/include\""

echo "TOOL:xerces-c:"
eval "echo \"  +XERCESC_BASE:\${XERCES_C_ROOT}\""
eval "echo \"  +XERCES_C_BASE:\${XERCES_C_ROOT}\""
eval "echo \"  +PATH:\${XERCES_C_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${XERCES_C_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${XERCES_C_ROOT}/include\""


echo "TOOL:zlib:"
eval "echo \"  +ZLIB_BASE:\${ZLIB_ROOT}\""
eval "echo \"  +PATH:\${ZLIB_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${ZLIB_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${ZLIB_ROOT}/include\""

%if "%{?use_system_gcc:set}" == "set"
  echo "TOOL:cxxcompiler:"
       echo "  +GCC_BASE:/none"
       echo "  +CC:$(which gcc)"
       echo "  +CXX:$(which c++)"
       echo "  +PATH:/none"  # useless, toolbox says value=""
       echo "  +LD_LIBRARY_PATH:/none" # useless, toolbox says value=""
       echo "TOOL:g77gcc3:"
       echo "  +FC:$(which g77 | grep -v 'no g77')"
%endif
%if "%{?use_system_gcc:set}-%{?use_ccache:set}" == "-set"
echo "TOOL:cxxcompiler:"
       echo "  +GCC_BASE:$CCACHE_ROOT"
eval        "echo \"  +CC:$CCACHE_ROOT/bin/gcc\""
eval        "echo \"  +CXX:$CCACHE_ROOT/bin/c++\""
       echo "TOOL:g77gcc3:"
       echo "  +FC:$GCC_ROOT/bin/g77"
%endif
%if "%{?use_system_gcc:set}-%{?use_ccache:set}" == "-" 
echo "TOOL:cxxcompiler:"
       echo "  +GCC_BASE:$GCC_ROOT"
       echo "TOOL:g77gcc3:"
       echo "  +FC:$GCC_ROOT/bin/g77"
%endif


echo "TOOL:pcre:"
eval "echo \"  +PCRE_BASE:\${PCRE_ROOT}\""
eval "echo \"  +PATH:\${PCRE_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${PCRE_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${PCRE_ROOT}/include\""


echo "TOOL:uuid:"
eval "echo \"  +UUID_BASE:\${UUID_ROOT}\""
eval "echo \"  +PATH:\${UUID_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${UUID_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${UUID_ROOT}/include\""

PYTHON_MAJOR=$(echo $PYTHON_VERSION | sed 's/\.[0-9]*$//')
echo "TOOL:python:"
echo "  +PYTHON_BASE:$PYTHON_ROOT"
echo "  +LIBDIR:$PYTHON_ROOT/lib"
echo "  +INCLUDE:$PYTHON_ROOT/include/python$PYTHON_MAJOR"
echo "  +PATH:$PYTHON_ROOT/bin"


echo "TOOL:boost:"
eval "echo \"  +BOOST_BASE:\${BOOST_ROOT}\""
eval "echo \"  +PATH:\${BOOST_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${BOOST_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${BOOST_ROOT}/include\""


echo "TOOL:cppunit:"
eval "echo \"  +CPPUNIT_BASE:\${CPPUNIT_ROOT}\""
eval "echo \"  +PATH:\${CPPUNIT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${CPPUNIT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${CPPUNIT_ROOT}/include\""

) > tools.conf
%install
mkdir %i/configurations/
cp tools.conf %i/configurations/tools-STANDALONE.conf
%post
%{relocateConfig}configurations/tools-STANDALONE.conf
