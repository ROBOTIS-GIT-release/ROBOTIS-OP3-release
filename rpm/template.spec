Name:           ros-kinetic-op3-action-module
Version:        0.1.0
Release:        0%{?dist}
Summary:        ROS op3_action_module package

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://wiki.ros.org/robotis_op3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-dynamixel-sdk
Requires:       ros-kinetic-robotis-device
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamixel-sdk
BuildRequires:  ros-kinetic-op3-action-module-msgs
BuildRequires:  ros-kinetic-robotis-controller-msgs
BuildRequires:  ros-kinetic-robotis-device
BuildRequires:  ros-kinetic-robotis-framework-common
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-std-msgs

%description
The op3_action_module package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Oct 27 2017 Pyo <pyo@robotis.com> - 0.1.0-0
- Autogenerated by Bloom

