import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and Sound America'

wm.add('North Am', ['ca', 'mx', 'us'])
wm.add('Central Am', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South Am', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy',
    'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
