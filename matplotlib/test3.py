import pygal.maps.world
wm=pygal.maps.world.World()
wm.title='population of countries in north america'
wm.add('north america',{'ca':34126000,'us':309349000,'mx':113423000})
wm.render_to_file('na_populations.svg')
