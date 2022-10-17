# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global __strip /bin/true

%global __brp_mangle_shebangs /bin/true

Name: postgresql-jdbc
Epoch: 100
Version: 42.4.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Postgresql JDBC Driver
License: BSD-2-Clause
URL: https://github.com/pgjdbc/pgjdbc/tags
Source0: %{name}_%{version}.orig.tar.gz
Requires: java

%description
PostgreSQL JDBC Driver (PgJDBC for short) allows Java programs to
connect to a PostgreSQL database using standard, database independent
Java code. Is an open source JDBC driver written in Pure Java (Type 4),
and communicates in the PostgreSQL native network protocol.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_datadir}/java
install -Dpm755 -t %{buildroot}%{_datadir}/java postgresql-*.jar
pushd %{buildroot}%{_datadir}/java && \
    ln -fs postgresql-*.jar postgresql.jar && \
    popd

%check

%files
%license LICENSE
%dir %{_datadir}/java
%{_datadir}/java/*

%changelog
