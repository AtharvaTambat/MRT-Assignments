#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/atharva/gazebo_assignment/src/pysdf"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/atharva/gazebo_assignment/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/atharva/gazebo_assignment/install/lib/python2.7/dist-packages:/home/atharva/gazebo_assignment/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/atharva/gazebo_assignment/build" \
    "/usr/bin/python2" \
    "/home/atharva/gazebo_assignment/src/pysdf/setup.py" \
     \
    build --build-base "/home/atharva/gazebo_assignment/build/pysdf" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/atharva/gazebo_assignment/install" --install-scripts="/home/atharva/gazebo_assignment/install/bin"
