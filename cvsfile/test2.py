import pygal
wm = pygal.worldmap()
wm.title='North,Central,and South America'
wm.add('north amercia',['ca','mx','us'])
wm.add('central amercia',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('south america',['ar','bo','br','cl','co','ce','gf',
                        'gy','pe','py','sr','uy','ve'])
wm.render_to_file('amerias.svg')