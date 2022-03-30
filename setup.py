import os
from glob import glob
from setuptools import find_packages
from setuptools import setup

package_name = 'teleop_joy'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kyuhyong You',
    maintainer_email='kyuhyong@gmail.com',
    description='Very simple xbox type joystick teleop controller',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_joy_node = teleop_joy.teleop_joy_node:main'
        ],
    },
)
