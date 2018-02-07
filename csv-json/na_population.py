import pygal

wm = pygal.maps.world.World()
wm.title = 'North America'

wm.add('North Am', {
    'ca': 34126000,
    'us': 309349000,
    'mx': 113423000
})

wm.render_to_file('na_population.svg')
