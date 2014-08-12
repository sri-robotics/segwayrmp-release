Name:           ros-hydro-rmp-msgs
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS rmp_msgs package

Group:          Development/Libraries
License:        Private
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-std-msgs

%description
The rmp_msgs package defines rmp specific messages such as motor status, audio
command, ...

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Aug 12 2014 Thomas de Candia <thomas.decandia@sri.com> - 0.0.2-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Thomas de Candia <thomas.decandia@sri.com> - 0.0.1-0
- Autogenerated by Bloom

