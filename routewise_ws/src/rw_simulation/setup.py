from setuptools import setup

package_name = 'rw_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/gazebo_launch.py']),                              # Include the launch directory
        ('share/' + package_name + '/gazebo_maps', ['rw_simulation/gazebo_maps/initial_map.world']),     # Include the gazebo map
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='onur',
    maintainer_email='onurulusoys4@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
