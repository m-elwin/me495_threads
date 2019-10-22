# Python setup file used for installing a python catkin package.
# See http://docs.ros.org/melodic/api/catkin/html/user_guide/setup_dot_py.html
# For catkin to use this we have called python_catkin_setup() in CMakeLists.txt
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages = ['me495_threads'],
    scripts = ['scripts/gil_two_threads.py', 'scripts/race_cond.py'],
    package_dir={'' : 'src'}
)
   

setup(**d)
